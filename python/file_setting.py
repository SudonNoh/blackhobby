import os
from PIL import Image
import pandas as pd

class file_setting:
    
    def file_load(self, folder_route):
        file_list = os.listdir(folder_route)
        return file_list
    
    # folder_route는 원본 img가 있는 route
    # 차라리 for문을 밖에서 돌리는 방법을 생각하는게 낫다.
    def img_change(self, image_route, img_save_route):
        if image_route[-4:]=='.png':
            img = Image.open(image_route)
            img = img.transpose(Image.ROTATE_270)
            file_route = image_route.split('/')
            cr = os.getcwd().replace("\\", "/")
            try:
                img.save(cr + '/' + img_save_route + '/' + file_route[-1])
            except FileNotFoundError:
                os.makedirs(cr + '/' + img_save_route)
                img.save(cr + '/' + img_save_route + '/' + file_route[-1])
        else:
            pass
    
    
class excel_control:
    
    def key_load(self, file_name, sheet_name):
        
        file = pd.read_excel(file_name, sheet_name=sheet_name)
        data = file.drop(file.index[0:6])
        key = data[[data.columns[3]]].dropna(axis=0)
        key_list = [j for i in key.values.tolist() for j in i]
        
        return key_list