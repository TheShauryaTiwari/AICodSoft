import cv2
import dlib

# Load the pre-trained face detection model
face_detector = dlib.get_frontal_face_detector()

# Load the pre-trained face recognition model
face_recognizer = dlib.face_recognition_model_v1("shape_predictor_68_face_landmarks.dat")

def recognize_face(embedding, known_embeddings, threshold=0.6):
    min_distance = threshold
    recognized_face = None

    for name, known_embedding in known_embeddings.items():
        distance = dlib.vector_distance(embedding, known_embedding)
        if distance < min_distance:
            min_distance = distance
            recognized_face = name
    
    return recognized_face

def main():
    # Load known face embeddings (you need to have a dataset with known face embeddings)
    known_embeddings = {
        "Person1": [0.1, 0.2, ..., 0.9],
        "Person2": [0.3, 0.4, ..., 0.7]
    }

    cap = cv2.VideoCapture(0)  # 0 for webcam

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector(gray)

        for face in faces:
            landmarks = face_recognizer(frame, face)
            embedding = face_recognizer.compute_face_descriptor(frame, landmarks)
            recognized_name = recognize_face(embedding, known_embeddings)

            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, recognized_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
