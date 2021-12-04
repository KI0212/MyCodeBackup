import cv2 as cv


# * Reading Images * #

img = cv.imread("Photos/cat_large.jpg")

cv.imshow('Cat', img)

def changeRes(widht, height):
    # * Works on live video * #

    capture.set(3, widht)
    capture.set(4, height)

def rescaleFrame(frame, scale=0.75):
    # * Image, video and live video * #

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions= (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('Video REsized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()


cv.waitKey(0)