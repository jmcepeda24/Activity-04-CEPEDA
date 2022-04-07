import cv2
from tkinter import filedialog

path = filedialog.askopenfilename()

print("Select image flag")
print("1. Color")
print("2. Grayscale")
print("3. Unchange")
print("0. Exit")

userInput = int(input("Select to change color: "))

if userInput == 1:
    flag = 1
elif userInput == 2:
    flag = 0
elif userInput == 3: 
    flag = -1
elif userInput == 0:
    exit()
else: 
    flag = 1

cv2.startWindowThread()

image = cv2.imread(path, flag)

cv2.imshow("Window Name", image)
cv2.waitKey(0)
cv2.destroyAllWindows()