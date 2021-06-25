import cv2
import numpy as np
from pynput.mouse import Button, Controller

#init
###CAN BE MODIFIED###
faceCascade = cv2.CascadeClassifier('D:/Coding/Python 3/Cursor Face Tracking/classifier/haarcascade_frontalface_default.xml')
###CAN BE MODIFIED###
font = cv2.FONT_HERSHEY_SIMPLEX
mouse = Controller()

def detectFace(img, cascade):
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detect the coords of faces in the gray image
    coords = cascade.detectMultiScale(
        grayImg,
        scaleFactor = 1.3,
        minNeighbors = 5,
        # minSize = (30, 30)
    )
    if len(coords) > 1:
        biggest = (0, 0, 0, 0)
        for i in coords:
            if i[3] > biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
    elif len(coords) == 1:
        biggest = coords
    else:
        return None, None, None
    frame = None
    midx = None
    midy = None
    for (x, y, w, h) in biggest:
        frame = img[y:y + h, x:x + w]
        midx = x + (((x + w) - x) / 2)
        midy = y + (((y + h) - y) / 2)
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) #Draw a rectangle around the faces
    
    return frame, midx, midy

def middleFaceFrame(img, posx, posy):
    x1 = int(posx - 3)
    y1 = int(posy - 3)
    x2 = int(posx + 3)
    y2 = int(posy + 3)

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

def middleScreenCoords(img, posx, posy):
    x1 = int(posx - 16)
    y1 = int(posy - 7)
    x2 = int(posx + 16)
    y2 = int(posy + 7)
    
    # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    return x1, x2, y1, y2

def nothing(x):
    pass

def main():
    #assign the captured video from webcam into cam
    ###CAN BE MODIFIED###
    cam = cv2.VideoCapture(0)
    #changing the resolution of the video from the webcam
    #the resolution must be 16:9
    camSizeX = 960
    camSizeY = 540
    ###CAN BE MODIFIED###
    cam.set(3, camSizeX)
    cam.set(4, camSizeY)

    while True:
        _, img = cam.read() #assigning the video into an image per frame
        

        #find the middle/nose of the faceFrame
        frame, midx, midy = detectFace(img, faceCascade)

        if frame is not None and midx is not None and midy is not None:
            middleFaceFrame(img, midx, midy) #to show the middle of the face frame

            #moving the cursor based on the movement of the face
            #DIRECTLY MOVE THE CURSOR COORDS THE SAME AS THE COORDS FOR THE FACE FRAME
            ########1111111111111111111111111########
            #########################################
            #######THERES GOTTA BE A BETTER WAY######
            #########################################
            # moveX = 30
            # moveY = 30

            # mousePos = mouse.position
            # mouseX = mousePos[0]
            # mouseY = mousePos[1]

            # if midx > lastx and midy > lasty:
            #     mouse.position = (mouseX + moveX, mouseY + moveY)
            # elif midx > lastx and midy < lasty:
            #     moveY *= -1
            #     mouse.position = (mouseX + moveX, mouseY + moveY)
            # elif midx < lastx and midy > lasty:
            #     moveX *= -1
            #     mouse.position = (mouseX + moveX, mouseY + moveY)
            # elif midx < lastx and midy < lasty:
            #     moveX *= -1; moveY *= -1;
            #     mouse.position = (mouseX + moveX, mouseY + moveY)
            # elif midx > lastx and midy == lasty:
            #     mouse.position = (mouseX + moveX, mouseY)
            # elif midx < lastx and midy == lasty:
            #     moveX *= -1
            #     mouse.position = (mouseX + moveX, mouseY)
            # elif midy > lasty and midx == lastx:
            #     mouse.position = (mouseX, mouseY + moveY)
            # elif midy < lasty and midx == lastx:
            #     moveY *= -1
            #     mouse.position = (mouseX, mouseY + moveY)
            # elif midx == lastx and midy == lasty:
            #     mouse.position = (mouseX, mouseY)
            # else:
            #     print ("Error in coords movement")
                
            # lastx = midx; lasty = midy;
            #########################################
            #######THERES GOTTA BE A BETTER WAY######
            #########################################


            #moving the cursor based on the movement of the face
            #MOVE THE CURSOR COORDS BASED FROM THE CENTER COORDS OF THE FACE FRAME
            ########2222222222222222222222222########
            #########################################
            #######MAYBE THIS IS THE BETTER WAY######
            #########################################
            # midOfScreenX = camSizeX / 2
            # midOfScreenY = camSizeY / 2
            # moveX = 30
            # moveY = 30

            # mousePos = mouse.position
            # mouseX = mousePos[0]
            # mouseY = mousePos[1]

            # if midx == midOfScreenX and midy == midOfScreenY:
            #     mouse.position = (mouseX, mouseY)
            # elif midx > midOfScreenX and midy == midOfScreenY:
            #     mouse.position = (mouseX + moveX, mouseY)
            # elif midx < midOfScreenX and midy == midOfScreenY:
            #     moveX *= -1
            #     mouse.position = (mouseX + moveX, mouseY)
            # elif midx == midOfScreenX and midy > midOfScreenY:
            #     mouse.position = (mouseX, mouseY + moveY)
            # elif midx == midOfScreenX and midy < midOfScreenY:
            #     moveY *= -1
            #     mouse.position = (mouseX, mouseY + moveY)
            # elif midx > midOfScreenX and midy > midOfScreenY:
            #     mouse.position = (mouseX + moveX, mouseY + moveY)
            # elif midx > midOfScreenX and midy < midOfScreenY:
            #     moveY *= -1
            #     mouse.position = (mouseX + moveX, mouseY + moveY)
            # elif midx < midOfScreenX and midy > midOfScreenY:
            #     moveX *= -1
            #     mouse.position = (mouseX + moveX, mouseY + moveY)
            # elif midx < midOfScreenX and midy < midOfScreenY:
            #     moveX *= -1
            #     moveY *= -1
            #     mouse.position = (mouseX + moveX, mouseY + moveY)
            # else:
            #     print ("Error in coords movement")
            #########################################
            #######MAYBE THIS IS THE BETTER WAY######
            #########################################


            #moving the cursor based on the movement of the face
            #MOVE THE CURSOR COORDS BASED FROM THE X AND Y OF THE FACE FRAME
            #MAKES AN X AND Y GRAPH IN THE FACE FRAME
            ########3333333333333333333333333#########
            ################(IMPROVED)################
            ##########THIS IS THE BETTER WAY##########
            ##########################################
            ###CAN BE MODIFIED###
            midOfScreenX = camSizeX / 2
            midOfScreenY = camSizeY / 2
            ###CAN BE MODIFIED###

            x1, x2, y1, y2 = middleScreenCoords(img, midOfScreenX, midOfScreenY)
            ###CAN BE MODIFIED###
            moveX = 30
            moveY = 30
            ###CAN BE MODIFIED###
            
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 1)

            mousePos = mouse.position
            mouseX = mousePos[0]
            mouseY = mousePos[1]
            if (midx > x2) and (midy < y1):
                #top right
                moveY *= -1
                mouse.position = (mouseX + moveX, mouseY + moveY)
                # mouse.move(mouseX + moveX, mouseY + moveY)
            elif (midx < x1) and (midy < y1):
                #top left
                moveX *= -1
                moveY *= -1
                mouse.position = (mouseX + moveX, mouseY + moveY)
                # mouse.move(mouseX + moveX, mouseY + moveY)
            elif (midx < x1) and (midy > y2):
                #bottom left
                moveX *= -1
                mouse.position = (mouseX + moveX, mouseY + moveY)
                # mouse.move(mouseX + moveX, mouseY + moveY)
            elif (midx > x2) and (midy > y2):
                #bottom right
                mouse.position = (mouseX + moveX, mouseY + moveY)
                # mouse.move(mouseX + moveX, mouseY + moveY)
            elif (midx > x1 and midx < x2) and (midy > y1 and midy < y2):
                #middle
                mouse.position = (mouseX, mouseY)
                # mouse.move(mouseX, mouseY)
            elif (midx > x1 and midy < x2) and (midy < y1):
                #middle top
                moveY *= -1
                mouse.position = (mouseX, mouseY + moveY)
                # mouse.move(mouseX, mouseY + moveY)
            elif (midx > x1 and midx < x2) and (midy > y2):
                #middle bottom
                mouse.position = (mouseX, mouseY + moveY)
                # mouse.move(mouseX, mouseY + moveY)
            elif (midx < x1) and (midy > y1 and midy < y2):
                #middle left
                moveX *= -1
                mouse.position = (mouseX + moveX, mouseY)
                # mouse.move(mouseX + moveX, mouseY)
            elif (midx > x2) and (midy > y1 and midy < y2):
                #middle right
                mouse.position = (mouseX + moveX, mouseY)
                # mouse.move(mouseX + moveX, mouseY) 
            elif midx == x1:
                pass
            elif midx == x2:
                pass
            elif midy == y1:
                pass
            elif midy == y2:
                pass
            else:
                print ("Error in coords movement")
            ##########################################
            #######MAYBE THIS IS THE BETTER WAY#######
            ##########################################


        cv2.putText(img, 'Press Q on this window to close', (10, 50), font, 0.5, (0, 255, 0), 1)
        cv2.putText(img, 'Press P on this window to stop tracking', (10, 30), font, 0.5, (0, 255, 0), 1)
        cv2.imshow('tracking', img)

        keyPressed = cv2.waitKey(1) & 0xff
        #press P to pause tracking
        while keyPressed == ord('p'):
            if cv2.waitKey(1) & 0xff == ord('p'):
                break
        #press Q to quit the program
        if keyPressed == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

main()
