import cv2
from tkinter import filedialog

path = filedialog.askopenfilename()


userInput = int(input("COLOR  OPTIONS \n[1] Color \n[2] Grayscale \n[3] Unchange \n[0] Exit \nChoose Color: "))

if userInput == 1:
    f = 1
elif userInput == 2:
    f = 0
elif userInput == 3: 
    f = -1
elif userInput == 0:
    exit()
else: 
    f = 1

cv2.startWindowThread()

image = cv2.imread(path, f)

cv2.imshow("Window Name", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
