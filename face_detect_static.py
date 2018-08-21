import cv2
import sys

# Get user supplied values
imagePath = sys.argv[0]

# Load the Haar Cascade 
cascPath = 'haarcascade_frontalface_default.xml'

# Create the Haar Cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the Image
image = cv2.imread('img.jpg')

# Convert to Gray-Scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect Faces in the Image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(25, 25)
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the Faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Faces found', image)
cv2.waitKey(0)

