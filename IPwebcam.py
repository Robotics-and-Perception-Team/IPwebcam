import cv2
import numpy as np
import requests
url="http://192.168.35.38:8080//shot.jpg"
red_p=0
green_p=0
blue_p=0
while 1:
    img_resp= requests.get(url)
    img_arr= np.array(bytearray(img_resp.content),dtype=np.uint8)
    img= cv2.imdecode(img_arr,cv2.IMREAD_COLOR)
    img=cv2.resize(img,(640,480))
    hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(img, img, mask=red_mask)

    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(img, img, mask=blue_mask)
    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(img, img, mask=green_mask)

    for i in range(250,350):
        for j in range(150,250):
            if(red[i][j][0]<179 and red[i][j][1]<255 and red[i][j][2]<255 and red[i][j][0]>161and red[i][j][1]>155 and red[i][j][2]>84):
                #print("red")
                red_p+=1
    for i in range(250,350):
        for j in range(150,250):
            if(blue[i][j][0]<126 and blue[i][j][1]<255 and blue[i][j][2]<255 and blue[i][j][0]>94 and blue[i][j][1]>80 and blue[i][j][2]>2):
                #print("blue")
                blue_p+=1
    for i in range(250,350):
        for j in range(150,250):
            if(green[i][j][0]<102 and green[i][j][1]<255 and green[i][j][2]<255 and green[i][j][0]>25and green[i][j][1]>52 and green[i][j][2]>72):
                #print("green")
                green_p+=1
    if(red_p>blue_p and red_p>green_p):
        print("red")
    elif (blue_p > red_p and blue_p > green_p):
        print("blue")
    elif (green_p > red_p and green_p > blue_p):
        print("green")
    red_p=0
    blue_p=0
    green_p=0

    cv2.imshow("Frame", img)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)


    #cv2.imshow("androidcam",img)

    if cv2.waitKey(30)==27:
        break
cv2.destroyAllWindows()