import pandas as pd
import os
from PIL import Image


file = pd.read_excel('C:/Users/SD NOH/Desktop/표_정리(6) new 2022.02.07.xlsx', sheet_name='TABLE')
data = file.drop(file.index[0:6])
key = data[[data.columns[1], data.columns[2]]].dropna(axis=0)
key.columns= ["옵션정보", "KEY"]
key["옵션정보"] = key["옵션정보"].str.replace(pat=r'[^\w]', repl=r'', regex=True)
key_list = key.values.tolist()
key_4ml = [i for i in key_list if '4' in i[0]] 

files = os.listdir('D:/BlackHobby_file/blackhobby/원본_4ml')
file_name = [i.replace(" ", "") for i in files]
file_name2 = [i.replace("4ml.png", "") for i in file_name]
file_name3 = [i.replace("4ML.png", "") for i in file_name2]
file_name4 = [i.replace("4.png", "") for i in file_name3]
file_name5 = [i.replace(".png", "") for i in file_name4]
file_name5.pop(0)



# 이미지 변경 및 이름 변경 후 저장
# 원본 4ml 리스트
load = 'D:/BlackHobby_file/blackhobby/원본_4ml'
save_load = 'D:/BlackHobby_file/blackhobby/4ml'
file_in_folder = os.listdir(load)

count = 1
for i in file_in_folder:
    if i[-4:] == '.png':
        img = Image.open(load + '/' + i)
        img = img.transpose(Image.ROTATE_270)
        img.save(save_load + '/' + str(count).zfill(4) + '. ' + i)
        count += 1
    else:
        pass
    
    
# 원본 30ml 리스트
load = 'D:/BlackHobby_file/blackhobby/원본_30ml'
save_load = 'D:/BlackHobby_file/blackhobby/30ml'
file_in_folder = os.listdir(load)

for i in file_in_folder:
    if i[-4:] == '.png':
        img = Image.open(load + '/' + i)
        img = img.transpose(Image.ROTATE_270)
        
        if '뒷면' in i:
            img.save(save_load + '/' + str(count).zfill(4) + '. ' + i)
        else:
            img.save(save_load + '/' + str(count).zfill(4) + '. ' + i)
            count += 1
    else:
        pass
    
    
file_load = 'D:/BlackHobby_file/blackhobby/4ml'