# Computer-Vision

#### In this repository we will be looking into a lot of CV techniques, using python library openCV, as well as implementation from scratch.

------

## INDEX:

### 1) [Tutorial1](https://github.com/XXDIL/Computer-Vision/tree/main/tut1)

> 1. Read and write the dimensions of an image.

> 2. Perform following operations on an image:<br/>
  a) RGB to Grayscale.<br/>
  b) Find index of pixels having value equal to 6.<br/>
  c) Identify and display the value of darkest pixel in both the images.<br/>
  d) Modify the above image by replacing the square (31x31) around darkest pixel with the white pixels.<br/>
  e) Make a gray square with pixel value 100 at the center of this image.<br/>
  

> 3. Compute the average pixel value for each channel R, G and B then subtract the average value per
channel for the above image (used in q1).

> 4. Perform basic transformation on an image: Apply padding in case of loss of data.<br/>
  a) Rotation 30 degree<br/>
  b) Scaling by factor 2<br/>
  c) Shifting (0,0) to (10, 10)<br/>
  d) Filtering to detect edges.<br/>

### 2) [Interpolation](https://github.com/XXDIL/Computer-Vision/tree/main/tut2)

> A basic Nearest Neighbor Interpolation done on a 3D Image(RGB)

### 3) [B-spline](https://github.com/XXDIL/Computer-Vision/tree/main/B-spline)

> Numerical : <br/>
  Find the value of f(2.5) using:<br/>
  >> a) 0-degree B-spline function<br/>
  >> b) 1-degree B-spline function<br/>
  >> c) 2-degree B-spline function<br/>
  
  > given -> f(0) = 2, f(1) = 3, f(2) = 4, f(3) = 2, f(4) = 5.

> Practical : 
   Given in the pdf attached in the B-spline folder.

### 4) [RGB2Grayscale](https://github.com/XXDIL/Computer-Vision/tree/main/Grayscale)

> Conversion from RGB tp Grayscale using 3 formulas

### 5) [Canny-Edge-Detection](https://github.com/XXDIL/Computer-Vision/tree/main/Canny)

> Explain the 5 steps on canny edge detection:<br/>
  >> 1) Noise reduction<br/>
  >> 2) Gradient calculation<br/>
  >> 3) Non-maximum suppression<br/>
  >> 4) Double threshold<br/>
  >> 5) Edge Tracking by Hysteresis

### 6) [Video Summarization](https://github.com/XXDIL/Computer-Vision/tree/main/Video-Summary)

> There are many algorithms that exists for video summarization. You are not restricted here to use any specific one (means free to use keyframe extraction, uniform sampling, image histogram, SIFT etc).

> What you are required to do is:<br/>
  a) Take any video of not more than 1 min and give the result video as per the important keyframes required.<br/>
  b) Files to be uploaded should include program file(.ipynb) video to summarize and summarized video.<br/>
  c) All files should be zipped and name with your roll no.<br/>
  d) If any other information is required to execute the code, in that case, include readme file as well.

### 7) [Camera Calibration](https://github.com/XXDIL/Computer-Vision/tree/main/Camera-Calibration)

> Here we learn about the basics of different corodinate systems and an insight in Homogeneous coordinates.

### 8) [Corner Detection](https://github.com/XXDIL/Computer-Vision/tree/main/Harris)

> Implementing the Harris Corner Detection ALgorithm from scratch. [Harris](https://en.wikipedia.org/wiki/Harris_Corner_Detector)
