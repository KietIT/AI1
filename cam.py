import cv2
import pyttsx3

AI_mouth = pyttsx3.init()
cam = cv2.VideoCapture(0)

cv2.namedWindow("Camera")

img_counter = 0

rate = AI_mouth.getProperty('rate')
AI_mouth.setProperty('rate', 175)
voices = AI_mouth.getProperty('voices')
AI_mouth.setProperty('voice', voices[1].id)

while True:
    ret, frame = cam.read()
    cv2.imshow("Camera", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "picture {}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1


cv2.destroyAllWindows()
AI = "Good morning, Kiệt. How can I help you?"
print("AI:" + AI)	
AI_mouth = pyttsx3.init()
AI_mouth.say(AI)
AI_mouth.runAndWait()