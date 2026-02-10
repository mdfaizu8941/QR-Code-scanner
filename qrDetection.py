import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow("QR Code Detection")

# Initialize QRCode detector
detector = cv2.QRCodeDetector()

scanned_qrcodes = set()

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Detect and decode
    data, bbox, _ = detector.detectAndDecode(frame)

    if bbox is not None and data:
        if data not in scanned_qrcodes:
            print(f"QR Code Detected: {data}")
            scanned_qrcodes.add(data)

        # Draw bounding box
        n = len(bbox[0])
        for i in range(n):
            pt1 = tuple(map(int, bbox[0][i]))
            pt2 = tuple(map(int, bbox[0][(i + 1) % n]))
            cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

    # Display
    cv2.imshow("QR Code Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
