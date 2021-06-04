import cv2 as cv

url = 'http://192.168.0.104:8080/video'

cap = cv.VideoCapture(url)
ret = True
f = 0
i = 0

image_output = "desktop/images"

while ret:
    if f == 0:
        print("Press 's' to Scan the Image")
        print("Press 'q' to Quit")
        f = f + 1

    ret, frame = cap.read()
    cv.imshow("Camera", frame)

    k = cv.waitKey(1)

    if k == ord('s'):
        cv.destroyWindow("Camera")
        cv.imshow("Scanned Photo", frame)

        print("Press 'u' If It's Unreadable")
        print("Press 'b' to Convert it to B&W")
        print("Press 'e' for Edge Detection")
        print("Press 'o' for object Detection")
        k1 = cv.waitKey(0)

        if k1 == ord('u'):
            cv.destroyWindow("Scanned Photo")

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 155, 1)
            cv.imwrite(f"{image_output}/image_thresold{i}.jpg", threshold)
            i = i + 1

            print("Press 's' to Scan More Document")
            print("Press 'q' to Quit")
            continue

        elif k1 == ord('b'):
            cv.destroyWindow("Scanned Photo")

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imwrite(f"{image_output}/image_b&w{i}.jpg", gray)
            i = i + 1

            print("Press 's' to Scan More Document")
            print("Press 'q' to Quit")
            continue

        elif k1 == ord('e'):
            cv.destroyWindow("Scanned Photo")

            canny = cv.Canny(frame, 200, 220)
            cv.imwrite(f"{image_output}/image_edge{i}.jpg", canny)
            i = i + 1

            print("Press 's' to Scan More Document")
            print("Press 'q' to Quit")
            continue

        elif k1 == ord('o'):
            cv.destroyWindow("Scanned Photo")

            grayscaled = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
            cannied_img = cv.Canny(frame, 100, 200)
            gaussian_blurred = cv.GaussianBlur(cannied_img, (5, 5), 0, 0)
            countours, hierarchy = cv.findContours(gaussian_blurred, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
            cv.drawContours(frame, countours, -1, (0, 255, 0), 5)
            cv.imwrite(f"{image_output}/image_object{i}.jpg", frame)
            i = i + 1

            print("Press 's' to Scan More Document")
            print("Press 'q' to Quit")
            continue

    elif k == ord('q'):
        ret = False
        break

cv.destroyAllWindows()
