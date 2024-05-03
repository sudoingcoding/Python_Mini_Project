import cv2, glob

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
all_images = glob.glob("*.jpg")
print("Printing image lists:")
for image in all_images:
    print(image)
im=input("Enter image name with .jpg format:\n")
txt = im[:-4]
imp_img = cv2.VideoCapture(im)

res,img =imp_img.read() #res return T/F & img returns the image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #img is converted into graysacle image

faces = detect.detectMultiScale(gray,1.3,5) #input is our grayscaled image,resize 1.3,neigbouring code 5

for (x,y,w,h) in faces: # takes each coordinates from faces and draw a square
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) #pass img ,(x,y) coordinates,(x+w,y+h) righhandside topmost coordinates,(255,255,0) color of the square,2 width

cv2.imshow(txt,img) #title of the window is "Elon Image" with (img)
cv2.waitKey(0) #I will close the window whenever I want
imp_img.release() #I captured the imported image, now I released that
cv2.destroyAllWindows() #close all the window