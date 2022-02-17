from re import template
from file_setting import file_setting


set = file_setting()

ori_img_route = 'D:/BlackHobby/blackhobby/4ML NEW'
img_save_route = 'D:/BlackHobby/blackhobby/4ML'
template_route = 'D:/BlackHobby/blackhobby/image.xlsx'
print_route = 'D:/BlackHobby/blackhobby/print'

# list = set.file_load(ori_img_route)
# set.img_change(list, ori_img_route, img_save_route)

# sample
img_list = set.file_load(img_save_route)


from openpyxl import load_workbook
from openpyxl.drawing.image import Image

wb = load_workbook(filename = template_route)
ws = wb.active

cell_list = [
    'B', 'D', 'F', 'H'
    ]

count=3
for cell in cell_list:
    count=3
    for num in range(8):
        
        cell_num = cell + str(num+count)
        # A2에 img_list[0] 저장
        img = Image(img_save_route + '/' + img_list[num+20])
        img.height = 98.6
        img.width = 176
        img.anchor = cell_num
        ws.add_image(img)
        count += 1

wb.save(filename = print_route+'/'+'print1.xlsx')


import pandas as pd

file = pd.read_excel('D:/BlackHobby_file/blackhobby/표_정리(6) new 2022.02.07.xlsx', sheet_name='TABLE CHECK')


