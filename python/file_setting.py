from logging import raiseExceptions
from msilib.schema import Error
import os
from PIL import Image


class file_setting:
    
    def file_load(self, folder_route):
        file_list = os.listdir(folder_route)
        return file_list
    
    # folder_route는 원본 img가 있는 route
    def img_change(self, img_list, folder_route, img_save_route):
        for i in img_list:
            if i[-4:]=='.png':
                img = Image.open(folder_route+'/'+i)
                img = img.transpose(Image.ROTATE_270)
                img.save(img_save_route+'/'+i)
            
            else:
                pass