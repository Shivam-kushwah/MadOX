import tkinter as tk
from PIL import Image, ImageTk

def health_report_click():
    print("Health Report button clicked")

def user_validation_click():
    print("User Validation button clicked")

def health_map_click():
    print("Health Map button clicked")

# Create the main window
root = tk.Tk()
root.title("GUI Window")
root.geometry("960x720")  # Assuming 720p resolution

# Load and display the background image
background_image = Image.open("background_image.jpg")  # Replace with your image file path
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Create three buttons in the middle of the vertical axis
button_height = int(root.winfo_reqheight() * 0.2)  # 20% of the window height

button1 = tk.Button(root, text="Health Report", command=health_report_click, fg="white")
button1.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=button_height)

button2 = tk.Button(root, text="User Validation", command=user_validation_click, fg="white")
button2.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=button_height)

button3 = tk.Button(root, text="Health Map", command=health_map_click, fg="white")
button3.place(relx=0.1, rely=0.8, relwidth=0.2, relheight=button_height)

root.mainloop()
