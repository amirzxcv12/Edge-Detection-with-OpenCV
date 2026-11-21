
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera could not be opened!")
    exit()

print("Edge Detection Started")
print("Press Q to exit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read frame!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    cv2.imshow("Original Camera", frame)
    cv2.imshow("Edge Detection", edges)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

