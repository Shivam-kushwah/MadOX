import tkinter as tk
from PIL import Image, ImageTk

def button1_click():
    print("Button 1 clicked")

def button2_click():
    print("Button 2 clicked")

def button3_click():
    print("Button 3 clicked")

# Create the main window
root = tk.Tk()
root.title("GUI Window")
root.geometry("960x720")  # Assuming 720p resolution

# Load and display the background image
background_image = Image.open("background_image.jpg")  # Replace with your image file path
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Create three buttons on the left side
button1 = tk.Button(root, text="Button 1", command=button1_click)
button1.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.2)

button2 = tk.Button(root, text="Button 2", command=button2_click)
button2.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.2)

button3 = tk.Button(root, text="Button 3", command=button3_click)
button3.place(relx=0.1, rely=0.8, relwidth=0.2, relheight=0.2)

root.mainloop()
