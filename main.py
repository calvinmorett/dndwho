import pytesseract
from pytesseract import Output
from PIL import Image, ImageEnhance
import cv2
import dxcam

# opencv config
myconfig = r"--psm 11 --oem 1"

input_file = Image.open('da.png')
output_file = ImageEnhance.Sharpness(input_file).enhance(2.9)
saved = 'saved.png'
output_file.save(saved)

img = cv2.imread(saved)
height, width, _ = img.shape

data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
print(data['text'])

amount_boxes = len(data['text'])  
for i in range(amount_boxes):
    if float(data['conf'][i]) > 60:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x,y), (x+width, y+height), (255,0,255), 1)
        img = cv2.putText(img, data['text'][i], (x, y+height+10), cv2.FONT_HERSHEY_PLAIN, 0.7, (255,255,0), 1, cv2.LINE_4)
        
cv2.imshow("img", img)
cv2.waitKey(0)