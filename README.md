***

[![Documentation](https://img.shields.io/badge/Docs-Technical_Details-blue.svg)](docs/documentation.md)

# 🖼️ Watermark Application

A simple, lightweight Python tool that lets you add custom watermarks to your images with ease. Built using **Tkinter** for the graphical user interface (GUI) and **Pillow (PIL)** for image processing, it provides an intuitive interface where users can upload an image, type in a watermark, and save the securely branded picture. 💻✨

---

## 🎥 Demo
![Watermark app demo](assets/demo.gif)

## 📸 Preview
![Watermark app preview](https://github.com/user-attachments/assets/1174606c-f57b-4a84-818d-7c688ef5d28d)

---

## 🚀 Features
* **Interactive GUI:** A clean, minimal, and user-friendly interface built with Tkinter.
* **Custom Watermark Text:** Easily type and apply any text as your watermark.
* **Smart Scaling:** Dynamic font sizing that automatically adjusts based on the image's dimensions.
* **Live File Tracking:** Preview the selected file name before processing.
* **Flexible Export:** Save your watermarked images with custom file names and formats (JPG/PNG).

---

## 🛠️ Tech Stack
* **Python 3.x** 🐍
* **Tkinter** (Built-in GUI library)
* **Pillow (PIL)** (Image processing)

---

## ⚙️ Installation & Usage

1. **Clone this repository:**
   ```bash
   git clone https://github.com/harris8099/Watermark.git
   cd Watermark
   ```

2. **Install the required dependencies:**
   *(Note: `tkinter` comes pre-installed with Python, so you only need to install Pillow)*
   ```bash
   pip install Pillow
   ```

3. **Run the application:**
   ```bash
   python watermark_app.py
   ```

---

## 🛣️ Future Roadmap
We have big plans for this app! Upcoming features include:
- [ ] **Positioning Options:** Choose where the watermark goes (top-left, bottom-right, center, etc.).
- [ ] **Opacity Control:** Support for transparent/semi-translucent watermarks.
- [ ] **Batch Processing:** Watermark multiple images at once.
- [ ] **Font Customization:** Select specific font styles, sizes, and colors.
- [ ] **Drag-and-Drop:** Easily drop images directly into the app window.

---

## 🐛 Known Issues
* Watermark placement is currently diagonal across the center and may overlap depending on the text length.
* The font style is hardcoded to Arial. 
* Limited support for non-Latin characters in the watermark text.

---

## 🤝 Contributing
Contributions are always welcome! 

If you’d like to help tackle the roadmap features (like positioning, transparency, or batch processing) or fix known issues:
1. Fork the repo
2. Create a new branch (`git checkout -b feature/CoolNewFeature`)
3. Commit your changes (`git commit -m 'Add CoolNewFeature'`)
4. Push to the branch (`git push origin feature/CoolNewFeature`)
5. Submit a pull request!
