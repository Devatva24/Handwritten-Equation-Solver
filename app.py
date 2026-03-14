import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import cv2
from predict import predict

# Page configuration
st.set_page_config(page_title="Handwritten Equation Solver", layout="centered")

st.title("✍️ Handwritten Equation Solver")
st.write("Draw a mathematical equation and click **Predict**")

# Sidebar controls
st.sidebar.header("Canvas Settings")
stroke_width = st.sidebar.slider("Stroke Width", 3, 15, 5)

# Canvas
canvas_result = st_canvas(
    stroke_width=stroke_width,
    stroke_color="black",
    background_color="white",
    height=300,
    width=600,
    drawing_mode="freedraw",
    key="canvas",
)

# Predict button
if st.button("Predict Equation"):
    
    if canvas_result.image_data is not None:

        path = "temp.png"
        cv2.imwrite(path, canvas_result.image_data)

        equation, result = predict(path)

        st.markdown("### 🧮 Detected Equation")
        st.success(equation)

        st.markdown("### ✅ Result")
        st.info(result)

    else:
        st.warning("Please draw an equation first.")