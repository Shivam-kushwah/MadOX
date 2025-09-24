import os
import cv2
import tkinter as tk
from tkinter import Canvas, Scrollbar, Label, Frame
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('plant_disease_model.h5')  # Update with your model file path

# Define the class mapping dictionary
class_mapping = {
    0: ('Generic', 'Healthy'),
    1: ('Generic', 'Powdery'),
    2: ('Generic', 'Rusty'),
    3: ('CORN', 'Rust'),
    4: ('CORN', 'Gray Spot'),
    5: ('CORN', 'Healthy'),
    6: ('CORN', 'Leaf Blight'),
    7: ('Potato', 'Early Blight'),
    8: ('Potato', 'Healthy'),
    9: ('Potato', 'Late Blight'),
    10: ('SugarCane', 'Bacterial Blight'),
    11: ('SugarCane', 'Healthy'),
    12: ('SugarCane', 'Red Rot'),
    13: ('Wheat', 'Brown Rust'),
    14: ('Wheat', 'Healthy'),
    15: ('Wheat', 'Yellow Rust'),
}

# Specify the folder containing images for classification
input_folder = "V:\Radon\Rusty"

# Create a tkinter window
root = tk.Tk()
root.title("Image Viewer")

# Set the main window size
main_window_width = 980
main_window_height = 720
root.geometry(f"{main_window_width}x{main_window_height}")

# Create a canvas with a scrollbar
canvas = Canvas(root, width=main_window_width, height=main_window_height)
scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)
scroll_y.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.configure(yscrollcommand=scroll_y.set)

# Create a frame inside the canvas to hold the images and labels
frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Function to update the canvas with images and labels
def update_images():
    for i, image_file in enumerate(image_files):
        # Read and preprocess the image
        image_path = os.path.join(input_folder, image_file)
        img = cv2.imread(image_path)
        img = cv2.resize(img, (256, 256))  # Ensure the image size matches the model input size
        img_display = img.copy()
        img = img / 255.0  # Normalize pixel values

        # Expand dimensions to match the model input shape
        img = np.expand_dims(img, axis=0)

        # Make prediction
        prediction = model.predict(img)
        predicted_class = np.argmax(prediction)

        # Use the class_mapping dictionary to get species and disease names
        species, disease = class_mapping[predicted_class]

        # Display the image with predicted class information
        img_rgb = cv2.cvtColor(img_display, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)

        label_heading = Label(frame, text=f"Species: {species}, Disease: {disease}")
        label_heading.grid(row=i * 2, column=0, sticky="w")
        
        label_image = Label(frame, image=img_tk)
        label_image.grid(row=i * 2 + 1, column=0, sticky="w")

        label_image.img_tk = img_tk  # Save reference to prevent image from being garbage collected

# Update the canvas with images and labels
update_images()

# Configure canvas scrolling
frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

root.mainloop()
