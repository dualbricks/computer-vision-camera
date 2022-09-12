import cv2 as cv
faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade= cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")


def detectface(frame):
    frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray)
    for(x,y,w,h) in faces:
        frame = cv.rectangle(img,(x,y),(x+w,y+h),(255,100,100),3)
        frameCircle = frameGray[y:y+h,x:x+w]
        eyes = eyeCascade.detectMultiScale(frameCircle)
        for(x1,y1,w1,h1) in eyes:
            eye_center = (x+x1+w1//2,y+y1+h1//2)
            radius = int(round((w1+h1)*0.25))
            frame = cv.circle(frame,eye_center,radius,(74,120,90),4)
    cv.imshow("Webcam",frame)


if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        success, img =cap.read()
        detectface(img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break



