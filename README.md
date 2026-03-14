## Handwritten Equation Solver using DL with Web App

### 🎯 **Goal**

The main goal of this project is to develop a Deep Learning (DL) model that can accurately solve handwritten mathematical equations. This project utilizes Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs) to recognize and interpret handwritten characters and equations.

### 🧵 **Dataset**

The dataset used for training and testing the models can be accessed from the following sources:
- [Direct Download](https://cainvas-static.s3.amazonaws.com/media/user_data/Yuvnish17/data.zip)
- [Kaggle Dataset](https://www.kaggle.com/datasets/xainano/handwrittenmathsymbols/data) 


### 🧾 **Description**

The Handwritten Equation Solver project addresses the challenge of accurately interpreting and solving handwritten mathematical equations, which is a non-trivial task due to the inherent variability in handwriting. Traditional OCR systems often fail to effectively handle these variations, leading to errors in character recognition and equation interpretation.


### 🧮 **What I had done!**

- Data Preparation:

    - The dataset comprises images of handwritten mathematical symbols and equations. The dataset is sourced from Kaggle [Dataset](https://www.kaggle.com/datasets/xainano/handwrittenmathsymbols/data) and can also be downloaded directly from [here](https://cainvas-static.s3.amazonaws.com/media/user_data/Yuvnish17/data.zip)

    ![img](images/dataset.png)

    - Preprocessing steps include resizing images, normalizing pixel values, and augmenting data to improve model robustness.

    ![img](images/preprocessing.png)



- Character Recognition with CNNs:

    - Model Architecture: The CNN model is designed to capture spatial hierarchies and patterns in the input images. It consists of multiple convolutional layers followed by pooling layers and fully connected layers.

   
    - Training: The model is trained on individual character images to classify each character accurately. The CNN achieved an impressive accuracy of `96.97%` in recognizing handwritten characters.

    ![img4](images/cnn.png)

    
    - CNNs are highly effective in capturing local patterns and spatial features, making them ideal for character recognition tasks.

- Preprocessing for Equation Recognition

  Before feeding the images into the model for equation recognition, several preprocessing steps are performed to enhance the clarity and uniformity of the input data:

  1. Grayscale Conversion: The input image is converted to grayscale to simplify the processing.
  2. Thresholding: Binary thresholding is applied to convert the image to a binary format, making it easier to detect contours.
  3. Contour Detection: Contours of the characters are detected to identify individual symbols.
  4. Bounding Box Extraction: Bounding boxes are created around each detected contour to isolate individual characters.
  4. Padding and Resizing: Each character is padded and resized to a uniform size (e.g., 32x32 pixels) to match the input requirements of the CNN model.

  These preprocessing steps ensure that the input to the model is consistent, leading to more accurate character recognition and equation interpretation.

- Implementation

  The implementation involves integrating both CNN model to create a pipeline that processes input images, recognizes individual characters, and interprets the sequence to solve equations. The steps include:
  - Preprocessing: Input images are preprocessed to enhance clarity and uniformity.
  - Character Recognition: The CNN model identifies and classifies individual characters in the image.
  - Sequence Interpretation: The RNN model interprets the sequence of recognized characters to form and solve the equation.
  - Output: The final result is displayed, showing the interpreted equation and its solution.

-  Web application

    A Streamlit application has been developed to provide a user-friendly interface for solving hand written math equations using DL models. The application allows users to use their free hand to draw or write the math equation on a canvas and upload the drawing to the model. The interface includes features like stroke width adjustment, real-time updates, and a prediction button that processes the image and displays the equation and its solution.


   ![image](images/sample.png)


 
### 🚀 **Models Implemented**

- Convolutional Neural Netowrk (CNN)
- Recurrent Neural Netowrk (RNN)

### 📚 **Libraries Needed**

- TensorFlow
- Streamlit
- OpenCV
- Numpy
- Pandas
- Seaborn
- Sklearn
- Matplotlib


### ⚙️ **Usage**

1. **Exploring Notebook**: `Notebook.ipynb` cover data analysis, preprocessing, model training, and evaluation steps.
   -  Navigate to the `Notebook.ipynb`
   -  Run all the cells
2. **Streamlit App:** The `app.py` contains the source code for the Streamlit web application. To run the app locally, follow the instructions below:

    ```bash
    pip install -r requirements.txt
    streamlit run app.py
    ```

    
### 📈 **Performance of the Models based on the Accuracy Scores**

<div align="center">
<table>
  <tr>
    <th>Model</th>
    <th>Validation Accuracy</th>
  </tr>
  <tr>
    <td>CNN</td>
    <td>96.97%</td>
  </tr>
  <tr>
    <td>RNN</td>
    <td>74.18%</td>
  </tr>
</table>
</div>

![img1](images/graphs.png)


### 📢 **Conclusion**

In conclusion, the handwritten equation solver utilizing deep learning techniques, including Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs), has demonstrated promising accuracy levels. The CNN-based approach achieved an impressive accuracy of `96.97%`, while the RNN-based method achieved a respectable accuracy of `74.18%`.

The `CNN model` excelled in accurately recognizing and classifying individual handwritten characters within the equations. Its ability to effectively capture spatial hierarchies and local patterns in the input images contributed to its high accuracy. With its deep layers and convolutional operations, the CNN was capable of learning complex features directly from the pixel values, enabling robust classification of handwritten characters.
