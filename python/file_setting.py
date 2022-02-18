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
    
    def __init__(self):
        self.fs = file_setting()
    
    def key_load(self, file_name, sheet_name):
        
        file = pd.read_excel(file_name, sheet_name=sheet_name)
        data = file.drop(file.index[0:6])
        key = data[[data.columns[3]]].dropna(axis=0)
        key_list = [str(j).zfill(4) for i in key.values.tolist() for j in i]
        
        return key_list
    
    def check_list(self, url, sheet_name, folder_name):
        key_list = self.key_load(url, sheet_name)
        folder_route = os.getcwd().replace("\\", "/")+'/'+folder_name
        
        # error 발생 코드
        error = 0
        # 최종 img가 담기는 list
        img_list = []
        if os.path.isdir(folder_route):
            for i in key_list:
                temp_list = []
                for j in self.fs.file_load(folder_route):
                    if i == j[:4]:
                        temp_list.append(j)
                # 해당하는 번호의 img 가 없으면 Error 발생
                if not temp_list:
                    error = 2
                    error_text = i
                    return error, error_text
                else:
                    for n in temp_list:
                        img_list.append(n)
            return error, img_list
        else:
            error = 1
            error_text = folder_route
            return error, error_text