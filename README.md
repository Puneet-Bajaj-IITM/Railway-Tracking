### Face Recognition System Overview

This face recognition system is designed to identify users for fare calculation in a transport system, such as a train network. The key components include a **Next.js** frontend, a **Python** backend utilizing machine learning for face recognition, and **Firebase** for storing user data and transaction details.

#### System Workflow

1. **User Registration**: During the signup process, users capture an image of their face using the frontend. This image is then sent to the backend, where it is saved in the face recognition database.

2. **User Entry**: When a user boards the train, a new face image is captured and sent to the backend. The backend uses a face recognition model to match the face with the stored record from the signup phase.

3. **User Exit**: Upon leaving the train, another face image is captured. The backend compares the new image with the initial entry image to recognize the user and calculate the time spent on the train.

4. **Fare Calculation**: Based on the time spent, the backend calculates the fare. The fare is then deducted from the user's balance in Firebase. If the user has insufficient funds, they are notified that they cannot continue.

5. **Profile Overview**: Users can view fare deductions and transaction history in their profile section on the frontend.

#### Backend Architecture and Face Recognition

- The face recognition system is based on the **FaceNet model** by Florian Schroff, Dmitry Kalenichenko, and James Philbin (2015), which transforms face images into 128-dimensional vectors. These vectors are used to compare different face images and identify individuals based on similarity.

- The core functionality relies on a **triplet loss function** to optimize the model. This function helps push the encodings of similar faces closer together while pushing the encodings of different faces further apart. The model was pretrained and can be loaded using TensorFlow and Keras.

#### Running the System

To set up and run the system, follow these steps:

1. **Backend Setup**:
   - Create a new Conda environment:
     ```bash
     conda create -n face-reco python=3.7.6
     conda activate face-reco
     ```
   - Install the required Python packages:
     ```bash
     pip install tensorflow numpy matplotlib pillow h5py opencv-python flask flask-cors
     ```
   - Run the Python backend:
     ```bash
     python app.py
     ```

2. **Frontend Setup**:
   - Navigate to the frontend directory:
     ```bash
     cd frontend
     ```
   - Install dependencies and run the development server:
     ```bash
     npm install
     npm run dev
     ```

3. **Configuration**:
   - Edit the `.env` file in the frontend to adjust settings such as the fare price and backend URL.

#### References

1. Florian Schroff, Dmitry Kalenichenko, James Philbin (2015). [FaceNet: A Unified Embedding for Face Recognition and Clustering](https://arxiv.org/pdf/1503.03832.pdf)
2. Yaniv Taigman, Ming Yang, Marc'Aurelio Ranzato, Lior Wolf (2014). [DeepFace: Closing the gap to human-level performance in face verification](https://research.fb.com/wp-content/uploads/2016/11/deepface-closing-the-gap-to-human-level-performance-in-face-verification.pdf)
3. Official FaceNet GitHub repository: [FaceNet](https://github.com/davidsandberg/facenet)
4. Jason Brownlee, How to Develop a Face Recognition System Using FaceNet in Keras and an SVM Classifier: [Machine Learning Mastery](https://machinelearningmastery.com/how-to-develop-a-face-recognition-system-using-facenet-in-keras-and-an-svm-classifier/)
5. Keras FaceNet conversion: [GitHub](https://github.com/nyoki-mtl/keras-facenet/blob/master/notebook/tf_to_keras.ipynb)

By following these instructions, the system will be set up to perform face recognition and fare calculation based on user entry and exit from a train.
