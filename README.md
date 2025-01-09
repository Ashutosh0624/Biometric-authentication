# Biometric Authentication Using Facial Recognition

This project implements a biometric authentication system using facial recognition technology. The system leverages OpenCV's Haar Cascade Classifier for face detection and the LBPH (Local Binary Patterns Histogram) algorithm for facial recognition. The primary goal is to create a secure and efficient authentication method that can be used in various applications.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Results](#results)
8. [Challenges and Future Work](#challenges-and-future-work)

---

## Overview

The project focuses on:
- Detecting human faces using Haar Cascade Classifier.
- Recognizing faces using the LBPH algorithm.
- Evaluating the performance under various conditions, including lighting variations, face angles, and unknown users.

**Accuracy**: 97%  
**Precision**: 91.7%

---

## Features

- **Face Detection**: Uses Haar Cascade Classifier for robust and fast face detection.
- **Facial Recognition**: Implements LBPH for recognizing faces with high accuracy.
- **Customizable Threshold**: Confidence percentage can be adjusted for specific applications.
- **Performance Evaluation**: Evaluates under diverse test cases including lighting conditions, distances, and face angles.

---

## Requirements

- **Python 3.8+**
- **Libraries**:
  - OpenCV
  - NumPy
  - Matplotlib
  - Sphinx (for documentation)
- **Hardware**:
  - Webcam-enabled system

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Biometric-authentication.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Biometric-authentication
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Build documentation (optional):
   ```bash
   cd source
   make html
   ```

---

## Usage

1. **Run the Application**:
   ```bash
   python main.py
   ```
2. Follow on-screen instructions to capture and store face samples, train the model, and perform recognition.

---

## Project Structure

```
Biometric-authentication/
├── build/                   # Built documentation files
├── source/                  # Sphinx documentation files
├── main.py                  # Main application script
├── requirements.txt         # Required Python packages
├── README.md                # Project readme
└── data/                    # Folder for storing training images and models
```

---

## Results

Performance results under test conditions:

| Test Case                     | Result                                    |
|-------------------------------|-------------------------------------------|
| Varying Training Data         | Confidence improved with increased data. |
| Distance from Webcam          | Reliable up to 240 cm.                   |
| Face Angle Variation          | Accurate up to ±20° tilt.                |
| Lighting Conditions           | Optimal in focused lighting conditions.  |
| Unknown User Recognition      | Precision of 40%.                        |

---

## Challenges and Future Work

### Challenges
- **Hardware Limitations**: Limited flexibility in webcam positioning and calibration.
- **Lighting Variations**: Performance affected by extreme lighting conditions.
- **Unknown User Accuracy**: Lower precision for users not in the training set.

### Future Work
- Develop a custom Haar Cascade Classifier to improve detection.
- Enhance the model to support multiple users.
- Deploy the system as a web or mobile application.

---

**Author**: [Your Name]  
**License**: MIT  
**Repository**: [GitHub Link](https://github.com/<your-username>/Biometric-authentication)
