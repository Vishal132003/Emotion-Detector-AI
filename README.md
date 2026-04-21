# Facial Emotion Detection using Deep Learning

## Overview

This project presents a **Facial Emotion Detection System** built using **Convolutional Neural Networks (CNN)** and deployed with **Streamlit**. The application analyzes facial images and predicts human emotions across multiple categories.

The system is trained on the **FER2013 dataset** and provides an intuitive web interface for real-time emotion prediction.

---

## Features

* Deep Learning based emotion detection
* Clean and interactive Streamlit UI
* Upload image for prediction
* Supports grayscale facial images
* Confidence score output
* Lightweight and easy to deploy

---

## Emotions Detected

The model predicts the following seven emotions:

* Angry
* Disgust
* Fear
* Happy
* Neutral
* Sad
* Surprise

---

## Dataset

**Dataset:** FER2013

* Training Images: 28,709
* Testing Images: 7,178
* Image Size: 48 × 48
* Format: Grayscale
* Classes: 7 Emotions

---

## Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Streamlit
* Matplotlib

---

## Model Architecture

The model consists of:

* Convolutional Layers
* MaxPooling Layers
* Dropout Layers
* Flatten Layer
* Dense Layers
* Softmax Output Layer

---

## Project Structure

```
Facial-Emotion-Detection/
│
├── app.py
├── emotion_model.h5
├── requirements.txt
├── README.md
└── dataset/
```

---

## Installation

### Clone Repository

```
git clone https://github.com/yourusername/facial-emotion-detection.git
```

### Navigate to Project Directory

```
cd facial-emotion-detection
```

### Install Dependencies

```
pip install -r requirements.txt
```

---

## Usage

Run the Streamlit application:

```
streamlit run app.py
```

Open your browser and upload a facial image to detect emotion.

---

## Model Performance

* Training Accuracy: ~50–55%
* Validation Accuracy: ~55–60%

*Note: Accuracy may vary depending on training configuration.*

---

## Future Enhancements

* Real-time webcam emotion detection
* Face detection using OpenCV
* Multi-face emotion detection
* Model optimization and accuracy improvement
* Cloud deployment

---

## Author

Your Name

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

* FER2013 Dataset
* TensorFlow & Keras
* Streamlit Community
