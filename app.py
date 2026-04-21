import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

# Load Model
model = load_model("emotion_model.h5")

# Emotion labels
emotion_labels = [
    'Angry',
    'Disgust',
    'Fear',
    'Happy',
    'Neutral',
    'Sad',
    'Surprise'
]

# Page config
st.set_page_config(
    page_title="Emotion Detection",
    page_icon="😊",
    layout="centered"
)

# Title
st.title("😊 Facial Emotion Detection")
st.write("Upload image to detect emotion")

# Upload file
uploaded_file = st.file_uploader(
    "Upload Face Image",
    type=["jpg","png","jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    resized = cv2.resize(gray, (48,48))

    normalized = resized / 255.0

    reshaped = np.reshape(normalized, (1,48,48,1))

    # Prediction
    prediction = model.predict(reshaped)

    label = emotion_labels[np.argmax(prediction)]

    confidence = np.max(prediction)

    st.success(f"Emotion: {label}")
    st.info(f"Confidence: {confidence:.2f}")
