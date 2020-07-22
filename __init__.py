import os

current_dir = os.getcwd()

if not os.path.exists(current_dir + '\\' + '@buffer'):
    os.makedirs(current_dir + '\\' + '@buffer')
    print('Папка @buffer создана')

if not os.path.exists(current_dir + '\\' + '@saves'):
    os.makedirs(current_dir + '\\' + '@saves')
    print('Папка @saves создана')

print('Программа-ассистент для разметки изображений запущена!')

