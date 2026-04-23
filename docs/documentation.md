# 🖼️ Technical Documentation: Watermark Application

This document outlines the core architecture, logic, and image processing pipeline for the Python-based Watermark Application (`watermark_app.py`).

---

## 🏗️ Architecture Overview

The application is a lightweight desktop utility that combines a graphical user interface with an image processing backend. It is structured around two main pillars:
1.  **GUI Framework:** `tkinter` handles the application window, layout frames, user inputs, and native file dialogs.
2.  **Image Processing:** `Pillow` (PIL) manages opening the image files, rendering the TrueType font, and drawing the text directly onto the image matrix before saving.

---

## ⚙️ Dependencies

* `tkinter`: The standard Python interface to the Tcl/Tk GUI toolkit. Used for the root window, frames, labels, buttons, and entry fields.
* `tkinter.filedialog`: Used to trigger the native OS file explorer for uploading and saving images.
* `PIL` (Pillow):
    * `Image`: Opens, formats, and saves the image file.
    * `ImageDraw`: Provides simple 2D graphics capabilities to draw text onto the `Image` object.
    * `ImageFont`: Loads the local TrueType font (`arial.ttf`) and dynamically sizes it.

---

## 🧠 Core Functions

The script utilizes a functional programming approach for its logic, relying on global state variables (`state`, `current_file_loc`) to pass data between the GUI and the processing engine. 

### Function Signatures & Type Usage
Because this script acts as a Tkinter GUI application, the functions are designed specifically to be used as **Event Callbacks** (passed to the `command` parameter of Tkinter buttons). 
* Neither function accepts arguments `()` because Tkinter button commands do not pass arguments by default.
* Both functions implicitly return `None`.

### 1. File Upload (`upload_loc`)
* **Signature:** `def upload_loc() -> None:`
* **Usage:** Assigned to `button1` (`command=upload_loc`). Triggered when the user clicks the "Upload" button.
* **Action:** Opens an `askopenfilename` dialog filtered for `.jpeg`, `.jpg`, and `.png` formats.
* **State Management:** Sets the global `current_file_loc` variable to the chosen file path. If a file is successfully selected, it toggles the global `state` variable to `True` (enabling the watermark function).
* **UI Update:** Extracts the raw file name from the path using `.split("/")[-1]`, updates `label2` to display it to the user, and dynamically repackages the layout to show the filename next to the upload button.

### 2. Image Processing (`watermark`)
* **Signature:** `def watermark() -> None:`
* **Usage:** Assigned to `button2` (`command=watermark`). Triggered when the user clicks the "Submit" button.
* **Action:** This is the core rendering engine. It only executes if `state == True` (meaning a file has been uploaded).
* **Text Extraction:** Grabs the string from `input_field`, strips trailing whitespace, and forces it to uppercase.
* **Dynamic Font Sizing:** Uses a custom mathematical formula to ensure the font size scales proportionally with the image dimensions and text length:
    * `font_size = int((img.size[1]//10) * (1/((len(FONT)*0.1)+1)))`
    * This prevents long text strings from overflowing the image bounds.
* **Diagonal Placement:** Instead of printing the word as a single string, the script iterates through each character (`FONT[i]`). It calculates an X/Y offset (`distance`) based on the image's aspect ratio, drawing each character diagonally from the top-left toward the bottom-right.
    * *Color:* Fixed to RGB `(130, 130, 130)` (Gray).
* **Export:** Generates a default save name by prepending `"wm_"` to the original filename. Opens an `asksaveasfilename` dialog, allowing the user to select the final directory and extension type before executing `img.save()`.

---

## 🎨 GUI Layout & Structure

The user interface is broken down into three distinct vertical frames stacked within a `500x500` non-resizable root window.

* **Window Settings:** Fixed dimensions (`500x500`), disabled resizing, and a global background color of `#CDFADB` (Mint Green).
* **Frame 1 (Top):**
    * Contains the aesthetic application logo (`assets/water mark.png`) drawn on a `Canvas`.
    * Displays the main "Apply Watermark" heading.
    * Houses the custom "Upload" image button and the dynamic filename label.
* **Frame 2 (Middle):**
    * Contains the "ENTER THE TEXT" label.
    * Houses the `ttk.Entry` input field, pre-populated with the default string `"Watermark"`.
* **Frame 3 (Bottom):**
    * Contains the custom "Submit" image button that triggers the final `watermark()` processing function.

---

## 💡 Notes for Future Development
* **Global Variables:** The reliance on global variables (`state` and `current_file_loc`) could be refactored into a Class-based Object-Oriented structure (`class WatermarkApp:`) for better state encapsulation.
* **Font Dependency:** The script currently relies on `arial.ttf` being available in the system's font path or the local directory.
* **Text Overlap:** Because the diagonal character placement relies on a hardcoded step distance, extremely narrow images or extremely long text strings may result in characters being rendered off-canvas or overlapping.
