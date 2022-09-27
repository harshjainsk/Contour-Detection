# Shape-Detection-Using-Contours
<br>

This project was built to understand how we can calculate area using contours.

## Demo

<div align="center"> 
<img width="90%" height="80%" src="https://github.com/harshjainsk/Shape-Detection-Using-Contours/blob/main/resources/Real-time-Contour-Detection-Using-Webcam.gif" hspace="10">
</div><br>

> ## An example of Real-time Contour Detection using webcam

<hr>

<div align="center"> 
<img width="90%" height="80%" src="https://github.com/harshjainsk/Shape-Detection-Using-Contours/blob/main/resources/Real-time-Contour-Detection-On-Image.gif" hspace="10">
</div><br/>

> ## An example of Real-time Colour Detection on a image stored in local memory

## About the project

When a image is captured by webcam or is loaded from local memory:
- It is stored in BGR(Blue, Green, Red) format.
- Converted to `grayscale` using opencv's inbuilt function `COLOR_BGR2GRAY`
- Edges are detected using `Canny Edge Detection`
- The threshold values for edge detection are passed from the <a href="https://github.com/harshjainsk/Shape-Detection-Using-Contours/blob/a655a1fe3afab7ce85963bbe5fff3b19417c60f0/main.py#L74">Trackbar</a>
- Contour points are calculated using <a href="https://github.com/harshjainsk/Shape-Detection-Using-Contours/blob/a655a1fe3afab7ce85963bbe5fff3b19417c60f0/main.py#L42">getContours</a> function
- Results are stacked and combined using <a href="https://github.com/harshjainsk/Shape-Detection-Using-Contours/blob/a655a1fe3afab7ce85963bbe5fff3b19417c60f0/main.py#L9">stackImages</a> function
