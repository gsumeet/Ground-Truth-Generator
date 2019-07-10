import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog

root = Tk()
# Create empty lists
plist = []
clist = []

# Method to open images from File system
def openImage(event):
    root.filename =  filedialog.askopenfilename(initialdir = imgPath,title = "Select file",filetypes = (("tif files","*.tif"),("jpg files","*.jpg"),("all files","*.*")))
    editImage()

# Method to draw shape based on selection
def draw_shape(event,x,y,flags,param):
    global plist
    global clist
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x,y)
        clist = []
        cv2.circle(img,(x,y),1,(0,255,0),-1)
    if event == cv2.EVENT_LBUTTONUP:
        plist.append((x,y))
    if event == cv2.EVENT_MOUSEMOVE:
        clist.append((x,y))
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # print("List: ",plist)
        plist = np.array(plist)
        cv2.fillPoly(img, [plist],(0,255,0))
        # print("List: ",clist)
        clist = np.array(clist)
        cv2.fillPoly(img, [clist],(0,255,0))
        clist = []
        plist = []

# Method to create userinterface functions    
def editImage():
    global img
    img = cv2.imread(root.filename)
    clone = img.copy()
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    while(1):
        cv2.imshow('image',img)
        cv2.setMouseCallback('image',draw_shape)
        if cv2.waitKey(20) & 0xFF == ord("r"):
            img = clone.copy()
        if cv2.waitKey(20) & 0xFF == ord("s"):
            cv2.imwrite("testout.tif",img)
            break
        if cv2.waitKey(20) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()

heading = Label(root,text="Ground Truth Generator",bg='black',fg='white')
imgPathMsg = Label(root,text="Enter the path for image repository")
imgPath = Entry(root)
openimagebtn = Button(text="Open")
openimagebtn.bind("<Button-1>",openImage)

# userinterface formatting
heading.pack(fill=X)
imgPathMsg.pack()
imgPath.pack()
openimagebtn.pack(fill=Y)

root.mainloop()