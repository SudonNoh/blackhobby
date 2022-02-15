import os
from PIL import Image
import pandas as pd

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
    
    
class excel_control:
    
    def key_load(self, file_name, sheet_name):
        
        file = pd.read_excel(file_name, sheet_name=sheet_name)
        data = file.drop(file.index[0:6])
        key = data[[data.columns[3]]].dropna(axis=0)
        key_list = [j for i in key.values.tolist() for j in i]
        
        return key_list