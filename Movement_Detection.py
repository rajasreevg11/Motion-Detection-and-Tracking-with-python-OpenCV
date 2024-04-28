import cv2 #for image
import time #for delay
import imutils #for resize

camera = cv2.VideoCapture(0) #camera id
time.sleep(1)

first_Frame=None
area = 500

while True:
    _,img = camera.read() #read frame from camera
    text = "Normal image" 
    img = imutils.resize(img, width=500) #resize
    
    gray_Img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #color 2 Gray scale image
    
    gaussian_Img = cv2.GaussianBlur(gray_Img, (21, 21), 0) #smoothened
    
    if first_Frame is None:
            first_Frame = gaussian_Img #capturing 1st frame on 1st iteration
            continue

    img_Diff = cv2.absdiff(first_Frame, gaussian_Img) #absolute diff b/w 1st nd current frame
    
    thresh_Img = cv2.threshold(img_Diff, 25, 255, cv2.THRESH_BINARY)[1] #binary
    
    thresh_Img = cv2.dilate(thresh_Img, None, iterations=2)
    
    contours = cv2.findContours(thresh_Img.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
    
    contours = imutils.grab_contours(contours)
    for c in contours:
            if cv2.contourArea(c) < area:
                    continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Moving Object detected"
    print(text)
    cv2.putText(img, text, (10, 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("cameraFeed",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()