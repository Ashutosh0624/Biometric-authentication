Introduction
============

1.1 Motive
----------

With the significant overlap in the enhancement of digital technologies across the globe, we can see 
the digitalization of the everyday needs of common people as well as administrative departments. 
For instance, bank accounts, passport services, medical records, security and surveillance, social 
media, etc., have become fully digitalized. Digitalization has largely impacted users positively; however, 
it has also created major concerns about countering fraud practices like unauthorized access to user 
information such as social media account information, passwords, and bank account credentials. 
This problem was addressed by implementing biometric techniques (Zhang Rui, 2019).

Biometric authentication is a method used to enhance the security features of applications by 
correctly identifying users and improving the efficiency of systems (National Cyber Security Centre, 2019). 
Although there are other legacy methods of authentication besides biometrics, these systems are 
often inefficient and lack robust security features such as strong password protection and real-time 
processing. Biometric techniques are considered the quickest, most secure, and best authentication 
methods available today because of their unique data sets (Phadke, 2013).

Facial recognition, a biometric authentication method, has gained unprecedented attention due to 
its universality in commercial, law enforcement, and administrative applications. The availability of 
high-quality cameras and optimized algorithms further solidifies facial recognition as a preferred 
biometric technique (Marley, 2019).

The project presented here stems from the need to address a critical digital security issue: fraud 
detection. The designed model uses facial recognition techniques to detect and recognize faces 
captured by a webcam. If the user is identified, the system unlocks; otherwise, it remains locked. 
This application offers solutions to unauthorized access, helps locate missing persons, and prevents 
internet scams.

1.2 Background
--------------

The first effort to develop a facial recognition system was made in the 1960s by Woodrow Wilson 
Bledsoe. His system measured and classified facial images, comparing unknown faces against known 
attribute points (Klosowski, 2020).

**Evolution of Computer Vision and Facial Recognition**:

- **2001**: The Viola-Jones framework for face detection was introduced. This framework works in real time.
- **2010**: Google released Goggles for image recognition, and Facebook integrated facial recognition.
- **2012**: Google Brain recognized images using deep learning.
- **2015**: TensorFlow was launched for efficient face recognition.
- **2018**: Amazon's Rekognition system was sold to police departments.
- **2019**: The Indian government planned to use facial recognition for law enforcement.

While the popularity of these technologies has grown, challenges such as privacy violations, deep fakes, 
bias, and inaccuracies have also emerged. Nonetheless, ongoing advancements in computer vision 
and facial recognition offer optimized solutions for security and data privacy concerns.

1.3 Goals and Objectives
------------------------

The primary goal of this project is to develop a biometric authentication application using facial 
recognition technology and analyze its performance under different conditions.

**Phase 1 Objectives**:

- Study computer vision concepts, image transformation techniques, and existing face detection 
  and facial recognition algorithms.
- Investigate and analyze a built-in facial recognition algorithm in OpenCV.

**Phase 2 Objectives**:

- Choose face detection and recognition algorithms based on Phase 1 research.
- Develop software to capture webcam frames, detect faces, and store the outputs.
- Train the model using the selected OpenCV algorithm.
- Test the model under different scenarios, including:
  - Varying training datasets
  - Distance from the webcam
  - Face angle variations
  - Lighting conditions
  - Face characteristic changes (e.g., spectacles, goggles)
  - Performance with unknown users
- Analyze the results and visualize performance using Matplotlib.

1.4 Potential Applications
--------------------------

Facial recognition applications can be deployed in various domains:

- **Smart Cards**: Enhance security for smart cards used for identification and payment.  
  Examples: Voter ID registrations, passport verification, and driving licenses.
- **Security and Surveillance**: Identify criminals by matching facial features with law enforcement databases.
- **Healthcare**: Protect patient medical records and sensitive information.
