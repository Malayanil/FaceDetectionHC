# Face Detection using Python

Welcome to the ReadMe file for the Face Detection using Python project. 

<b> Index: </b> 
<ol>
<li>Introduction</li>
<li>FAQs</li>
<li>Explanation of Code</li>
<li>Sample Outputs</li>
<li>Credits</li>
</ol>

<hr>

<b>1. Introduction</b>

<p>This project on Face Detection has been done with the implementation of Haar Cascade in Python scripts.
There are three scripts in this project.<br><b>'face_detect_static.py'</b> is the script for Face Detection on Image files as supplied by the User.<br><b>'face_detect_video.py'</b> is the script for Face Detection on Video files as supplied by the User.<br><b>'face_detect_webcam.py'</b> is the script for Face Detection from the Webcam of the host machine the script is executed on.
</p>
<br>

                                              ---End of Section One---
                                              

<b>2. FAQs</b>

<ul>
<li>What is Haar-like features ? What was used in this project ?</li><br>
<p>
Haar-like features are digital image features used in object recognition. They owe their name to their intuitive similarity with Haar wavelets and were used in the first real-time face detector. Historically, working with only image intensities (i.e., the RGB pixel values at each and every pixel of image) made the task of feature calculation computationally expensive. A publication by Papageorgiou et al. discussed working with an alternate feature set based on Haar wavelets instead of the usual image intensities. Viola and Jones adapted the idea of using Haar wavelets and developed the so-called Haar-like features. A Haar-like feature considers adjacent rectangular regions at a specific location in a detection window, sums up the pixel intensities in each region and calculates the difference between these sums. This difference is then used to categorize subsections of an image. 

For example, let us say we have an image database with human faces. It is a common observation that among all faces the region of the eyes is darker than the region of the cheeks. Therefore a common Haar feature for face detection is a set of two adjacent rectangles that lie above the eye and the cheek region. The position of these rectangles is defined relative to a detection window that acts like a bounding box to the target object (the face in this case). <br>~Wikipedia
<br><br>
A Haar Cascade is basically a classifier which is used to detect the object for which it has been trained for, from the source. The Haar Cascade is by superimposing the positive image over a set of negative images. The training is generally done on a server and on various stages. Better results are obtained by using high quality images and increasing the amount of stages for which the classifier is trained. One can also used predefined Haar Cascades which are available on <a href='https://github.com/'>GitHub.</a>

Haar Cascade for frontal face (default) detection was used in this project. It was downloaded from <a href='https://github.com/'>Github.</a> from this <a href='https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml'>link</a>. The OpenCV documentation for Face Detection using Haar Cascades is <a href='https://docs.opencv.org/3.4.1/d7/d8b/tutorial_py_face_detection.html'>here</a>.
</p>
<br>
<li>How is the performance of the script ? Why did we use Gray-Scale ?</li><br>
<p>
The performance of the script is strictly based upon the Hardware of the system on which it is run and the quality of files provided. For the webcam, the performance dependency on hardware is not much of a factor but for videos it is, as FFmpeg is decoding the video frame by frame as the script is run. 

We converted the input into Gray-Scale to simplify the job of the Haar Cascade algorithm. It would be able to work faster to determine edges and give out positive or negative results on images or frames.
</p>
<br>
<li>What are the requirements for running the scripts ?</li><br>
<p>
The following Python packages are required to run the scripts.<br>
a) <b>imutils</b> : A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV and both Python 2.7 and Python 3.<br>
b) <b>opencv2</b> : OpenCV (Open Source Computer Vision Library: http://opencv.org) is an open-source BSD-licensed library that includes several hundreds of computer vision algorithms.<br>
c) <b>ffmepg</b> : FFmpeg is a free software project, the product of which is a vast software suite of libraries and programs for handling video, audio, and other multimedia files and streams. At its core is the FFmpeg program itself, designed for command-line-based processing of video and audio files, widely used for format transcoding, basic editing (trimming and concatenation), video scaling, video post-production effects, and standards compliance (SMPTE, ITU).<br><br>
[Source: Internet]
</p>
<br>

                                              ---End of Section Two---
                                              
                                                    
 <b>3. Explanation of Code</b>
 
 <ol>
 <li>At first, we import the libraries needed for our Script.</li><br>
 							
                            import cv2
                            import sys
                            import imutils
                            
<ul>
<li>CV2 is the acronym for OpenCV2 (Open Computer Vision release 2). It is used to detect objects (faces) in the images.</li><br>
<li>"sys" module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.</li><br>
<li>"imutils" short for Image Utilities is a series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV and both Python 2.7 and Python 3.</li><br>
</ul><br>

                            cascPath = 'haarcascade_frontalface_default.xml'
                        
<ul>
<li>We load the Haar Cascade's default frontal face xml file into our program to detect frontal faces from Images, Videos or WebCams.</li><br>
</ul><br>

                            faceCascade = cv2.CascadeClassifier(cascPath)
                        
<ul>
<li>We create the Haar Cascade with the previously defined path with the 'CascadeClassifier()' function.</li><br>
</ul><br>

                            image = cv2.imread('img.jpg')
                            video_capture = cv2.VideoCapture(0)
                            video_capture = cv2.VideoCapture('vid.mp4')

<ul>
<li>We read the image, video or webcam input in which we have to detect the faces. We can also take these as input since we have used 'sys' import into our script.</li><br>
</ul><br>

For Images: <br>

                            # Convert to Gray-Scale
                            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                            # Detect Faces in the Image
                                      faces = faceCascade.detectMultiScale(
                                          gray,
                                          scaleFactor=1.1,
                                          minNeighbors=5,
                                          minSize=(25, 25)
                                      )

<ul>
<li>We convert the image input into gray-scale for ease of the interpreter to work faster and then detect the faces. The "faceCascade.detectMultiScale"'s parameters 'gray' specifies the gray-scale image where the objects are detected, scaleFactor specifies how much the image size is reduced at each image scale, 'minNeighbours' specifies how many neighbors each candidate rectangle should have to retain it, 'minSize' specifies the minimum possible object size and objects smaller than that are ignored. </li><br>
</ul><br>

For WebCam feed and Videos: <br>

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

                                  # Display the resulting Frame
                                  cv2.imshow('Video', frame)

                                  if cv2.waitKey(1) & 0xFF == ord('q'):
                                      break

                            # When everything is done, release the Capture
                            video_capture.release()
                            cv2.destroyAllWindows()

<ul>
<li>We use the 'while' loop to ensure that we get to visualize the output unless we opt to quit by pressing any defined keys (q). We resize the frame  and also convert to gray-scale to imporve the overall performance of the script. And finally we display the output to the screen by using the 'imshow()' function.</li><br>
</ul>

                            # Draw a rectangle around the Faces
                            for (x, y, w, h) in faces:
                                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

<ul>
<li>We draw rectangles around the faces that are detected using the 'rectangle()' function.
</li><br>

<li><b>NOTE:</b>In this project, the Haar Cascade used was the default one without any modifications. There are instances in the output where a non-face was detected as a face.</li><br>
</ul><br>

                                              ---End of Section Three---
                                              
 
<b>4. Sample Outputs</b>

![alt text](https://github.com/Malayanil/FaceDetectionHC/blob/master/outputs.png)

<ul>
  <li>The outputs obtained after executing the scripts have been given with pointed titles.</li><br>
</ul><br>

                                              ---End of Section Four---
                                              
                                              
<b>5. Credits</b>

<ul>
  <li>Image Credits: Mr. Ujan Banerjee</li>
  <li>WebCam Credits: Self</li>
  <li>Video Credits and all Copyrights goes to the Youtube Channel of JayZTwoCents. <a href='https://www.youtube.com/watch?v=b1qFrTo1O6c'>Here</a> is the link. </li><br>
</ul><br>
 
                                              ---End of Section Five---
 
