Conclusion and Future Work
==========================

6.1 Conclusions
---------------

Biometric authentication plays a significant role in today’s digital landscape, especially in ensuring security and protecting users' data privacy. Facial recognition has emerged as a paramount technique in this context.

This project aimed to design a facial recognition model for biometric authentication and evaluate its performance under various circumstances. The model was developed using:

- **Face Detection Algorithm**: Pretrained Haar Cascade Classifier.
- **Facial Recognition Algorithm**: LBPH (Local Binary Pattern Histogram).

The model was trained with image data samples of the user’s detected face and tested under different scenarios and test cases, primarily focusing on a single user. The overall performance was satisfactory, achieving accuracy and precision above 90% for a single user.

However, the model’s performance for recognizing unknown users showed limitations, with significantly lower accuracy and precision. This highlights the potential for further development in improving its robustness and security features.

This project provided a comprehensive understanding of:

- **Artificial Intelligence and Computer Vision**: Fundamentals and their applications.
- **OpenCV Libraries**: Methods implemented in Python for real-time applications.
- **Project Management Skills**: Time management, research, execution, and documentation.


6.2 Future Work
---------------

The model offers significant scope for improvement. Key areas for future enhancements include:

6.2.1 Multi-user Identification and Privacy Concerns
----------------------------------------------------

Currently, the model identifies a single user. It can be upgraded to identify multiple users by training it with images of all concerned users. However, the accuracy for unknown users without prior training was low, raising potential security concerns (as discussed in section 5.2 Challenges).

To address these challenges:

- **Develop a Custom Haar Cascade Classifier**:
  - Replace the pretrained Haar Cascade Classifier with a custom one designed using deep learning algorithms.
  - Train the classifier to detect specific user faces during the data collection phase.
  - Restrict the model to identify only authorized users and reject unknown users, enhancing security for single-user applications (e.g., phone unlock systems).

- **Privacy and Confidentiality**:
  - Address challenges such as privacy violations and data confidentiality through enhanced security protocols, ensuring compliance with ethical and legal standards (Technologies, 2020).


6.2.2 Potential Embedded Applications
-------------------------------------

This project was implemented as software on the host machine (Dell G3) in a Python environment using Jupyter Notebook. However, facial recognition technology's versatility allows it to be integrated into real-time embedded systems.

Future possibilities include:

- **Cross-platform Deployment**:
  - Leverage OpenCV’s compatibility with C/C++ to deploy the model on various platforms and embedded systems.
  - Implement the model in goal-oriented applications requiring facial recognition as a core or intermediary feature.

- **Examples of Embedded Applications**:
  - Smart security systems.
  - IoT devices using facial authentication.
  - Automotive systems for driver monitoring and safety.

This project demonstrates the potential to serve as a standalone application or as part of a larger embedded system, making it adaptable for various real-world applications.
