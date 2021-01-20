'''
This is a Barcode/QR code reader program, It can read barcode from any image 
irrespective of Barcode/QR code region in the image.
It will return the output as a string.
'''

import cv2
from pyzbar.pyzbar import decode
import os

# img_path = 'E:/Projects/data/qr1.jpg'

def CodeReader(image):
    img = cv2.imread(image)
    # cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    try:     
        result = decode(img)
        for i in result:
            info = i.data.decode("utf-8")
            print("Information: ",info)
    except:
        print("Error: No Barcode/Qr code found. ")

PATH = 'E:/Projects/BarcodeScanner/data/'   # PATH to input image folder


for image_path in os.listdir(PATH):
    input_img = os.path.join(PATH, image_path)
    # print("filename: ",input_img)
    CodeReader(input_img)
