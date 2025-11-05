import serial
import pyautogui
import time
import cv2

arduino = serial.Serial('COM5', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0)

print("🎮 Hybrid Battlefield 2 Controller Ready!")

while True:
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip()
        if data == "BTN1":
            pyautogui.press('space')
        elif data == "BTN2":
            pyautogui.click()
        elif data == "BTN3":
            pyautogui.press('r')
        elif data == "BTN4":
            pyautogui.press('ctrl')
        elif data == "BTN5":
            pyautogui.press('q')  # optional extra action

    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red1 = (0, 120, 70)
    upper_red1 = (10, 255, 255)
    lower_red2 = (170, 120, 70)
    upper_red2 = (180, 255, 255)

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest) > 1000:
            pyautogui.press('g')
            cv2.drawContours(frame, [largest], -1, (0, 255, 0), 3)

    cv2.imshow("Controller Vision", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
