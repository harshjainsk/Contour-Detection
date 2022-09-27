import cv2
import numpy as np


def empty(a):
    pass


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img, imgContour):
    """


    :param img: it is the input image
    :param imgContour: it will be our output image
    :return:
    """
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        areaMin = cv2.getTrackbarPos("Area", "PARAMETERS")
        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)  # True says that contour is closed
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))

            # Drawing Bounding Box
            x, y, width, height = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + width, y + height), (0, 255, 0), 5)

            cv2.putText(imgContour, "Points: " + str(len(approx)), (x + width + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX,
                        0.7, (0, 255, 0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + width + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX,
                        0.7, (0, 255, 0), 2)


cv2.namedWindow("PARAMETERS")
cv2.resizeWindow("PARAMETERS", 640, 240)
cv2.createTrackbar("Threshold1", "PARAMETERS", 0, 255, empty)
cv2.createTrackbar("Threshold2", "PARAMETERS", 255, 255, empty)
cv2.createTrackbar('Area', "PARAMETERS", 10, 200, empty)

frameWidth = 640
frameHeight = 400
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
# path = 'resources/shapes.jpg'
# img = cv2.imread(path)
# img = cv2.resize(img, (600, 400))

# 137 0
# 16 109

while True:

    ret, img = cap.read()

    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    # getting values from trackBar
    threshold1 = cv2.getTrackbarPos("Threshold1", "PARAMETERS")
    threshold2 = cv2.getTrackbarPos("Threshold2", "PARAMETERS")

    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    getContours(imgCanny, imgContour)

    imgStack = stackImages(0.8, ([img, imgGray, imgCanny],
                                 [imgContour, imgContour, imgContour]))
    cv2.imshow("img", imgStack)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
