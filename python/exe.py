from file_setting import file_setting


set = file_setting()

img_route = 'D:/BlackHobby/blackhobby/4ML NEW'
img_save_route = 'D:/BlackHobby/blackhobby/4ML'
list = set.file_load(img_route)

set.img_change(list, img_route, img_save_route)
