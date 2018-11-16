from PIL import Image
import pytesseract
import os
#上面都是导包，只需要下面这一行就能实现图片文字识别
if __name__ == '__main__':
    imagepath ='../images/test_image.jpg'
    #print(os.path.exists(imagepath))
    text = pytesseract.image_to_string(Image.open(imagepath), lang='chi_sim')
    print(text)

