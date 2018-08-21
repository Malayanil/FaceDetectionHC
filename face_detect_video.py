import cv2
import sys
import imutils

# Load the Haar Cascade
cascPath = 'haarcascade_frontalface_default.xml'

# Create the Haar Cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the Video
video_capture = cv2.VideoCapture('vid.mp4')

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Resize the Frame to improve speed
    frame = imutils.resize(frame, width=450)

    # Convert to Gray-Scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(25, 25)
    )

    # Draw a rectangle around the Faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting Frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything is done, release the Capture
video_capture.release()
cv2.destroyAllWindows()
