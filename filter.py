import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

video = cv2.VideoCapture(0)
image = cv2.imread("me.jpeg")

while True:
    ret, img = video.read()
    print(frame)
    image = cv2.resize(frame, (640, 480))
    frame = cv2.cvtColor(image, (640, 480))

    l_black = np.array([30, 30, 0])
    u_black = np.array([104, 153, 70])

    mask_1 = cv2.inRange(frame, l_black, u_black)    
    res_1 = cv2.bitwise_and(frame, frame, mask=mask_1)

    f = frame - res_1
    f = np.where(f==0, image, f)

    cv2.imshow("mask", f)
    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
     

video.release()
cv2.destroyAllWindows()