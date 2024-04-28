# Motion-Detection-and-Tracking-with-python-OpenCV

Motion detection is a fundamental technique in computer vision and image processing. It involves analyzing consecutive frames from a video to identify and track moving objects. This readme outlines the steps involved in implementing moving object detection using OpenCV, a popular library for computer vision tasks.


#Applications
Motion detection has various applications including:

Video surveillance
Activity recognition
Road condition monitoring
Airport safety
Marine border protection


#Steps Involved

1. Extract Background in Video Input:
Capture the video using OpenCV and select 30 random frames.
Calculate the median and average frames for outlier removal.

2. Processing a Frame:
Analyze a single frame separately, typically the first frame.
Convert the median and sample images to grayscale.

3. Background Removal:
Use Absolute Difference between the grayscale sample frame and the grayscale median frame to isolate moving objects and remove the background.

4. Blurring:
Apply Gaussian Blur to reduce noise and simplify edge detection.

5. Binarizing the Image - Thresholding:
Perform Threshold and OTSU Threshold to enhance the visibility of moving objects.

6. Contour and Boundary Boxes:
Create contours on the thresholded frame using cv2.RETR_EXTERNAL.
Generate bounding boxes for identified contours and overlay them on the sample frame.

7.Compiling Frames for Video Processing:
Declare an output video file.
Iterate through all frames of the input video, process each frame, and compile them into the output video.

# Output
To view the output video, please refer to the media file provided, where you can find the resulting video demonstrating the detected moving objects.


# How to Use

Ensure you have OpenCV installed. If not, install it using pip install opencv-python.
Download the provided code files.
Replace the input video path with your desired video file.
Run the code and observe the output video in the specified location.


# Dependencies
OpenCV: OpenCV is used for video capture, image processing, and visualization.


# Acknowledgments
This project was inspired by the need for efficient motion detection techniques and leverages the capabilities of OpenCV for practical implementation.
