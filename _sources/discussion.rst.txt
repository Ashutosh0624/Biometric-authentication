Discussion
==========

5.1 Performance Evaluation
---------------------------

The model’s performance evaluation was based on its response to the six test cases discussed in the Results section. The important outcomes observed from each test case are described below.

5.1.1 Outcome of Varying the Training Data
------------------------------------------

It was observed that increasing the training data in each iteration improved the model's prediction ability (confidence %). 
- **Minimum Training Data**: 20 images, Confidence: 89.3%
- **Maximum Training Data**: 1000 images, Confidence: 92.33%

The model performed exceptionally well, detecting the user confidently even with minimal training data. However, the highest prediction confidence (92.33%) may not suffice for high-security applications, such as military or defense zones requiring near-100% confidence. 

The rectangular bounding box dimensions during face detection may have contributed to this saturation in confidence. Smaller bounding boxes could introduce noise and reduce the effectiveness of the trained features.

5.1.2 Outcome of Varying the Distance
-------------------------------------

During testing, the model was trained with static images where the user was positioned at a fixed location. When tested with varying distances, the model successfully identified the user with confidence percentages above 90%, even as the user moved closer to or farther from the webcam.

This test demonstrated the model's efficiency in identifying users in motion or with slight movements. However, confidence percentages were influenced by factors such as:
- **Face Orientation**: The face had to be directed toward the camera.
- **Lighting**: Better performance was observed in daylight or with proper illumination.

5.1.3 Outcome of Face Tilt Variation
------------------------------------

The model recognized faces successfully with up to 20-degree tilts to the left or right. Beyond this angle, prediction accuracy decreased significantly due to the inability to detect certain face features not aligned with the training dataset.

5.1.4 Outcome of Different Lighting Conditions
----------------------------------------------

Face detection efficiency improved when light was focused on the user's face. However:
- When light intensity on the face and surroundings was similar, performance declined.
- Higher light intensities (e.g., 210 Lux) yielded results comparable to those in ideal conditions.

This test case highlighted that face detection depends more on face clarity than overall lighting intensity.

5.1.5 Outcome of Varying Face Characteristics
---------------------------------------------

Testing involved variations in face characteristics (e.g., glasses, goggles) under low-light conditions. Results showed:
- Performance was better with goggles than with transparent glasses due to reduced light reflections.
- The model performed optimally when the user’s face was 90–120 cm from the webcam.

5.1.6 Outcome of Testing with Unknown Users
-------------------------------------------

For unknown users, the model's precision was poor as it lacked training with those images. Precision improved significantly when trained with user-specific data.

5.1.7 Accuracy and Precision Evaluation
---------------------------------------

Accuracy and precision were calculated based on 100 samples:
- **True Positive (TP)**: 31
- **True Negative (TN)**: 65
- **False Positive (FP)**: 3
- **False Negative (FN)**: 0

**Precision**: 

.. math::

   \text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} = 91.7\%

**Accuracy**: 

.. math::

   \text{Accuracy} = \frac{\text{Total Correctly Identified Samples}}{\text{Total Samples}} = 97\%


These results suggest the model is efficient for its intended purpose, though improvements are needed for high-security applications.

Table 9: Tabulated data for accuracy and precision measurements

Table 9: Tabulated data for accuracy and precision measurements

+------------+---------------+--------------+----+----+----+----+
| Sample No. | Face          | Confidence % | TP | TN | FP | FN |
+============+===============+==============+====+====+====+====+
| 1          | Yes           | 92           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 2          | Yes           | 92           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 3          | Yes           | 92           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 4          | Yes           | 92           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 5          | Yes           | 92           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 6          | Yes           | 92           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 7          | Yes           | 92           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 8          | Yes           | 92           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 9          | Yes           | 92           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 10         | Yes           | 91           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 11         | Yes           | 88           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 12         | Yes           | 89           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 13         | Yes           | 89           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 14         | No (Blurry)   | 70           | 0  | 0  | 1  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 15         | No (Blurry)   | 70           | 0  | 0  | 1  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 16         | Yes           | 87           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 17         | Yes           | 87           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 18         | Yes           | 88           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 19         | Yes           | 90           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 20         | Yes           | 90           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 21         | Yes           | 91           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 22         | Yes           | 91           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 23         | Yes           | 91           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 24         | Yes           | 90           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 25         | Yes           | 91           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 26         | Yes           | 91           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 27         | Yes           | 90           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 28         | Yes           | 90           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 29         | Yes           | 91           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 30         | Yes           | 91           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 31         | Yes           | 91           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 32         | Yes           | 91           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 33         | Yes           | 90           | 1  | 0  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 34         | No (Blurry)   | 70           | 0  | 0  | 1  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 35         | No            | N.A          | 0  | 1  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+
| 100        | No            | N.A          | 0  | 1  | 0  | 0  |
+------------+---------------+--------------+----+----+----+----+


5.2 Challenges Faced
--------------------

During the implementation phase of the project, the following challenges were encountered:

1. **Hardware Setup Limitations**:
   - The project was implemented using the webcam preinstalled on the host machine (Laptop - Dell G3). Experimenting with webcam properties was very limited.
   - The webcam was fixed at the top-central point of the screen, making it difficult to evaluate the model’s efficiency under different circumstances such as:
   - Face angle orientation.
   - Distance of the detected face.
   - Additionally, the webcam lacked calibration flexibility, which could have improved the model's accuracy significantly.

2. **Varying Weather Conditions/Light Intensities**:
   - Testing the model and the face recognition algorithm under different light intensities was necessary for performance evaluation.
   - Testing during night hours was less challenging due to mild variations in light intensity.
   - Frequent weather changes during daytime made it difficult to perform testing under specific lighting conditions.

3. **Software Challenge**:
   - The Haar cascade classifier, a pretrained library, was used for face detection in the first phase of the project. This library, while helpful due to its vast dataset of faces with varying pixel values, posed a challenge during testing.
   - When testing the model for an unknown user (without prior training on the user’s image samples), the model recognized the user with very low accuracy and precision. This could be a potential security concern.
   - A solution to this challenge could involve building a new Haar cascade classifier tailored to the project's requirements instead of relying on the pretrained library.


5.2.1 Hardware Limitations
--------------------------

The pre-installed webcam on the host machine (Dell G3) had limited flexibility:
- The fixed position of the webcam restricted tests for face angle variations.
- Lack of calibration options impacted accuracy in different test scenarios.

5.2.2 Lighting and Weather Variations
-------------------------------------

Testing during the day was challenging due to frequent changes in lighting caused by weather. However, testing at night yielded more consistent results.

5.2.3 Pretrained Haar Cascade Classifier
----------------------------------------

Using a pretrained Haar cascade classifier was beneficial but posed challenges:
- The model achieved low accuracy and precision for unknown users not included in the training dataset.
- This limitation could be addressed by training a custom Haar cascade classifier tailored to the application.

