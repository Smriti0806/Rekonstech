import cv2

# face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# open the image
img_path = r'C:\Users\usha rani\Pictures\Screenshots\onelove.jpg'
img = cv2.imread(img_path)

# Check if the image was loaded correctly
if img is None:
    raise FileNotFoundError(f"The image at path {img_path} could not be loaded.")

# face detection function
def detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.3, minNeighbors=3)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
     
    return face_img

# apply the face detection function
face_img = detect_face(img)

# display the result
cv2.imshow('Original Image', img)
cv2.imshow('Detected Faces', face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
