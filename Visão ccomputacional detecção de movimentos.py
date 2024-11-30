import cv2
import time
from datetime import datetime

camera = cv2.VideoCapture(0)
ret, frame1 = camera.read()
ret, frame2 = camera.read()
movement_counter = 0


def save_frame_on_movement(frame):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"movement_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Movimento detectado! Imagem salva como: {filename}")


while camera.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    movement_detected = False

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        movement_detected = True

    if movement_detected:
        movement_counter += 1
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f"Movimento detectado às {current_time}. Total: {movement_counter}")
        save_frame_on_movement(frame1)

    cv2.imshow("Detecção de Movimento", frame1)

    frame1 = frame2
    ret, frame2 = camera.read()

    if cv2.waitKey(10) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
