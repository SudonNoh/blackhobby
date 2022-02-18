import os
from PIL import Image
import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from datetime import date


class file_setting:
    
    def __init__(self):
        
        self.route = os.getcwd().replace("\\", "/")
    
    def file_load(self, folder_name):
        file_list = os.listdir(self.route + "/" + folder_name)
        return file_list
    
    # folder_route는 원본 img가 있는 route
    # 차라리 for문을 밖에서 돌리는 방법을 생각하는게 낫다.
    def img_change(self, image_route, folder_name):
        if image_route[-4:]=='.png':
            img = Image.open(image_route)
            img = img.transpose(Image.ROTATE_270)
            file_route = image_route.split('/')
            cr = os.getcwd().replace("\\", "/")
            try:
                img.save(self.route + '/' + folder_name + '/' + file_route[-1])
            except FileNotFoundError:
                os.makedirs(self.route + '/' + folder_name)
                img.save(self.route + '/' + folder_name + '/' + file_route[-1])
        else:
            pass
    
    
class excel_control:
    
    def __init__(self):
        self.fs = file_setting()
        # D:/BlackHobby
        self.route = os.getcwd().replace("\\", "/")
    
    def key_load(self, file_name, sheet_name):
        
        file = pd.read_excel(file_name, sheet_name=sheet_name)
        data = file.drop(file.index[0:6])
        key = data[[data.columns[3]]].dropna(axis=0)
        key_list = [str(j).zfill(4) for i in key.values.tolist() for j in i]
        
        return key_list
    
    def check_list(self, url, sheet_name, folder_name):
        key_list = self.key_load(url, sheet_name)
        print("route : ", self.route)
        
        # error 발생 코드
        error = 0
        # 최종 img가 담기는 list
        img_list = []
        if os.path.isdir(folder_name):
            for i in key_list:
                temp_list = []
                for j in self.fs.file_load(folder_name):
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
            error_text = folder_name
            return error, error_text
        
    def make_excel(self, img_list, img_folder_name, save_folder_name, height, width):
        # img_folder_name : image들이 들어있는 folder의 이름
        # add_ok에서 self.route+'/'
        # save_folder_name : excel 파일들이 저장될 폴더 이름
        loof_num = len(img_list)//32+1
        cell_list = [
            "B", "D", "F", "H"
            ]
        today = date.today().strftime('%y%m%d')
        
        for n in range(loof_num):
            # 엑셀 파일 하나에 들어갈 image list 분리
            if len(img_list)-(32*n+32-1) < 0:
                adj_img = img_list[32*n:]
            else:
                adj_img = img_list[32*n:32*n+32-1]

            wb = load_workbook(filename= self.route + '/' + 'image.xlsx')
            ws = wb.active

            count_img = 0
            for cell in cell_list:
                count=3
                for num in range(8):
                    cell = cell + str(num+count)
                    img = Image(self.route + '/' + img_folder_name + '/' + adj_img[count_img])
                    img.height = height
                    img.width = width
                    img.anchor = cell
                    ws.add_image(img)
                    count += 1
                    count_img += 1
                    
            wb.save(filename = self.route+'/'+save_folder_name+'/'+'file_'+str(n).zfill(2)+"_"+today)

