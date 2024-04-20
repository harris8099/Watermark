import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# functions

# function to apply watermark
def watermark():
    if state == True:
        img = Image.open(current_file_loc)
        FONT = input_field.get().upper().strip()
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", int((img.size[1]//10)*(1/((len(FONT)*0.1)+1))))
        image_type = img.format.lower()
        distance = img.size[0] / len(FONT)
        for i in range(0, len(FONT)):
            draw.text((distance * i, (img.size[1] / img.size[0]) * distance * i), FONT[i], font=font,
                      fill=(130, 130, 130))
        file_name = "wm_" + current_file_loc.split("/")[-1]
        save_location = filedialog.asksaveasfilename(filetypes=[("jpg or png", f".{image_type}")], initialfile=file_name)
        img.save(save_location)


# function to open dir to select the file
current_file_loc = ""
def upload_loc():
    global current_file_loc, state
    current_file_loc = filedialog.askopenfilename(filetypes=[("jpg or png", ".jpeg .jpg .png")])
    label2.config(text=current_file_loc.split("/")[-1])
    if current_file_loc == "":
        return
    button1.pack(pady=10, padx=50, side=tk.LEFT, anchor='nw')
    label2.pack(pady=10, padx=50, side=tk.RIGHT, anchor='ne')
    state = True


# create the root window
root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('Watermark')
root.config(background="#CDFADB")
frame = tk.Frame(root, background="#CDFADB")
frame.pack()
second_frame = tk.Frame(root, background="#CDFADB")
second_frame.pack()
third_frame = tk.Frame(root, background="#CDFADB")
third_frame.pack()


# image
photo = tk.PhotoImage(file='assets/water mark.png')
canvas = tk.Canvas(frame, width=160, height=200)
canvas.create_image(80, 100, image=photo)
canvas.config(background="#CDFADB", highlightthickness=False)
canvas.pack(pady=10)

# Heading
label1 = ttk.Label(frame, text="Apply Watermark", background="#CDFADB")
label1.config(font=("Courier", 20))
label1.pack()


# upload button
upload_image = tk.PhotoImage(file="assets/upload.png")
button1 = tk.Button(frame, image=upload_image, highlightthickness=0, border=0, cursor="hand2", command=upload_loc)
button1.pack(pady=10)

# label for showing current file location
label2 = ttk.Label(frame, text="", background="#CDFADB")
label2.config(font=("Arial", 10))


# label for entering the text
label3 = ttk.Label(second_frame, text="ENTER THE TEXT", background="#CDFADB")
label3.config(font=("Arial", 10))
label3.pack(pady=10, padx=10, side=tk.LEFT, anchor='nw')

# watermark input field
input_field = ttk.Entry(second_frame, width=50)
input_field.pack(pady=10, padx=50, side=tk.RIGHT, anchor='ne')
input_field.insert(tk.END, string="Watermark")

# Submit button
state = False
load_image = tk.PhotoImage(file="assets/Submit.png")
button2 = tk.Button(third_frame, image=load_image, highlightthickness=0, border=0, cursor="hand2", command=watermark)
button2.pack()


root.mainloop()
