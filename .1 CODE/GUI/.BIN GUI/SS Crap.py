import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
from tensorflow.keras.preprocessing import image
from pathlib import Path

# Load the pre-trained InceptionV3 model from TensorFlow Hub
model_url = "https://tfhub.dev/google/tf2-preview/inception_v3/classification/4" # hme apna model daalna hoga yaha pr
#url ki bjae location daalni hogi model ki
model = tf.keras.Sequential([hub.KerasLayer(model_url, input_shape=(299, 299, 3))])

# Function to predict the plant species
def predict_species(image_path):
    img = image.load_img(image_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = tf.image.resize(img_array, (299, 299)) / 255.0  # Normalize pixel values
    img_array = tf.expand_dims(img_array, 0)  # Add batch dimension

    predictions = model.predict(img_array)
    predicted_label = np.argmax(predictions[0])
    return predicted_label

# Function to organize images into folders based on predicted species
def organize_images(source_folder, destination_folder):
    source_path = Path(source_folder)
    dest_path = Path(destination_folder)

    # Create destination folders if they don't exist
    dest_path.mkdir(parents=True, exist_ok=True)

    # Iterate through the images in the source folder (assuming they are JPEGs)
    for image_file in source_path.glob("*.jpg"):
        # Predict the species
        predicted_label = predict_species(str(image_file))

        # Create a folder for the species if it doesn't exist
        species_folder = dest_path / f"species_{predicted_label}"
        species_folder.mkdir(parents=True, exist_ok=True)

        # Move the image to the corresponding species folder
        destination_file = species_folder / image_file.name
        image_file.rename(destination_file)

        print(f"Image: {image_file.name} -> Species: {predicted_label}")

# Example usage
source_folder = r"V:\Plant_Species_Identifier\Test" # yaha pr source folder ki location dalegi jisse compare krke answer dega
destination_folder = r"V:\Plant_Species_Identifier\DUMP" # yaha pr destination folder ki location h jisme images ki dumping hogi segregation krke
#photo = r"C:\Users\SARTHAK AGGARWAL\Downloads\healthy_leaf0040.jpg" # yeh testcase photo h, loop chalake dekhna pdega test cases ki photos ko
#predict_species(photo)
organize_images(source_folder, destination_folder)


'''
run krne pr yeh warnings aa rhi thi:
2024-01-23 21:00:31.008463: I tensorflow/core/util/port.cc:113] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
WARNING:tensorflow:From C:\Program Files\Python311\Lib\site-packages\keras\src\losses.py:2976: The name tf.losses.sparse_softmax_cross_entropy is deprecated. Please use tf.compat.v1.losses.sparse_softmax_cross_entropy instead.

WARNING:tensorflow:From C:\Program Files\Python311\Lib\site-packages\tensorflow_hub\resolver.py:120: The name tf.gfile.MakeDirs is deprecated. Please use tf.io.gfile.makedirs instead.

WARNING:tensorflow:From C:\Program Files\Python311\Lib\site-packages\tensorflow_hub\resolver.py:120: The name tf.gfile.MakeDirs is deprecated. Please use tf.io.gfile.makedirs instead.

WARNING:tensorflow:From C:\Program Files\Python311\Lib\site-packages\tensorflow_hub\module_v2.py:126: The name tf.saved_model.load_v2 is deprecated. Please use tf.compat.v2.saved_model.load instead.

WARNING:tensorflow:From C:\Program Files\Python311\Lib\site-packages\tensorflow_hub\module_v2.py:126: The name tf.saved_model.load_v2 is deprecated. Please use tf.compat.v2.saved_model.load instead.

2024-01-23 21:00:38.139730: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: SSE SSE2 SSE3 SSE4.1 SSE4.2 AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
WARNING:tensorflow:From C:\Program Files\Python311\Lib\site-packages\keras\src\backend.py:873: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

WARNING:tensorflow:From C:\Program Files\Python311\Lib\site-packages\keras\src\backend.py:873: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.
'''

'''
ouptput aisa aa rha tha:
1/1 [==============================] - 2s 2s/step
'''
