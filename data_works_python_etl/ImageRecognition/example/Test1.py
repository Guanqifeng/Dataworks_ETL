from pyocr import pyocr
from PIL import Image
import os
if __name__ == '__main__':
    # coding=utf-8
    __author__ = 'syq'

    # https://github.com/tesseract-ocr
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    tools = pyocr.get_available_tools()[:]
    if len(tools) == 0:
        print("No OCR tool found")
    print("Using '%s'" % (tools[0].get_name()))
    print(tools[0].image_to_string(Image.open('../images/123.png'), lang='eng'))
    print(tools[0].image_to_string(Image.open('../images/123.png'), lang='chi_sim'))
    # print tools[0].image_to_string(Image.open('D:\\3535.png'),lang='chi_sim')
# from PIL import Image
# import pytesseract
# import os
# #上面都是导包，只需要下面这一行就能实现图片文字识别
# if __name__ == '__main__':
#     imagepath ='../images/test2.png'
#     #print(os.path.exists(imagepath))
#     text = pytesseract.image_to_string(Image.open(imagepath), lang='eng')
#     print(text)

