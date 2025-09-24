# Plant Disease Detection AI 🌿

A deep learning application built with Python and TensorFlow to identify plant diseases from leaf images. This project uses a Convolutional Neural Network (CNN) to achieve **96% prediction accuracy** and features an intuitive desktop GUI for easy use.



---

## 🚀 About The Project

Early detection of plant diseases is crucial for protecting crops and ensuring food security. This project aims to provide an accessible tool for farmers and botanists to quickly diagnose diseases by simply uploading a picture of a plant's leaf.

By leveraging the power of computer vision and deep learning, this application can classify over 04 different diseases, helping to facilitate timely and effective treatment.

---

## ✨ Key Features

* **High Accuracy:** Utilizes a custom-trained CNN model that achieves **96% accuracy** on the validation dataset.
* **Multiple Disease Classes:** Capable of identifying more than 10 different diseases across various plant species.
* **User-Friendly Interface:** Built with a clean and simple Graphical User Interface (GUI) using ttkbootstrap, making it easy for anyone to use.
* **Instant Diagnosis:** Provides real-time predictions from a local model, requiring no internet connection after setup.

---

## 🛠️ Tech Stack

* **Backend & Model:** Python
* **Deep Learning:** TensorFlow, Keras
* **Data Manipulation:** Scikit-learn, OpenCV, NumPy
* **GUI:** Tkinter, ttkbootstrap

---

## Dataset

The model was trained on a dataset of leaf images of 04 species namely,
1. Corn
2. Potato
3. Sugarcane
4. wheat.

You can find the dataset in the Repository itself.

---

## 📸 Screenshots

| Prediction Result |

![Prediction Result](./.3%20OUTPUT/Screenshot2.jpg)

![Prediction Result](./.3%20OUTPUT/Screenshot3.jpg)

---

## 🏁 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.8 or higher
* pip (Python package installer)

### Installation

1.  **Clone the repository.**
    ```sh
    git clone [https://github.com/your_username/plant-disease-detection.git](https://github.com/your_username/plant-disease-detection.git)
    cd plant-disease-detection
    ```

2.  **Create and activate a virtual environment (recommended).**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies.**
    ```sh
    pip install -r requirements.txt
    ```
    

## Usage Guide

1.  **Run the main application file.**
    ```sh
    python mainGUI.py
    ```
    
2.  **Using the App:**
    * Click the "Upload Image" button.
    * Select an image of a plant leaf from your computer.
    * The application will display the image and the predicted disease name with a confidence score.

---




---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
