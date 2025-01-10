Abstract
========

As the world is getting more and more digitalized, the frequency of digital crimes such as online deception, 
social media fraud, and violation of the right to privacy has increased. **Biometric authentication** 
is one of the prominent ways to counter such mishappenings. Over the past few years, the enhancement 
in several biometric authentication technologies has proven its worth, and **facial recognition** is one of them.

This project focuses on designing a model for biometric authentication using facial recognition’s OpenCV 
algorithms in a Python environment. The proposed model has been designed using:

- A pre-trained face detection algorithm: **Haar Cascade Classifier**
- A facial recognizer algorithm: **LBPH (Local Binary Patterns Histogram)**

The Haar cascade classifier detects the user’s face and extracts unique facial features, while the LBPH 
face recognizer recognizes and identifies the user.

The model has been:

- **Trained** with the user’s image samples obtained from the webcam.
- **Tested** under various circumstances, with results showing:
  - **Accuracy**: 97%
  - **Precision**: 91.7%

Additionally, the model successfully identified an unknown user without being trained with their image, 
providing a robust solution to the common security issue of unauthorized access to data. Future development 
possibilities are discussed in the conclusion.
