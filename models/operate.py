import os
import shutil
import re
from models import cropper

class operator:

    def __init__(self, PATH, LABEL_CLASS):
        self.path = PATH
        self.lclass = LABEL_CLASS
        self.class_dir = self.get_class_dir()
        self.buffer_dir = self.get_buffer_dir()
        self.save_dir = self.get_save_dir()
        self.curr_amount = self.get_amount(self.class_dir)
        self.new_amount = self.curr_amount + self.get_amount(self.buffer_dir, curr = False) - 1
        
    def get_buffer_dir(self):
        return (self.path + '\@buffer')

    def get_class_dir(self):
        return (self.path + '\\' + self.lclass)

    def get_save_dir(self):
        return (self.path + '\@saves')

    def get_amount(self, dir, curr = True):
        listdir = os.listdir(dir)
        if listdir:
            if curr:
                last_number = len(listdir) + 1
                return last_number
            else:
                return len(listdir)
        else:
            print('Директория @buffer пуста')
            return 0
        
    def move_files(self):
        os.chdir(self.buffer_dir)
        counter = self.curr_amount
        for file in os.listdir(self.buffer_dir):
            target_dir = self.class_dir + '\\{}_{}'.format(self.lclass, counter)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            file_dir = shutil.move(file, target_dir)
            print('Перемещение файла в папку ->', file, target_dir)
            file_dir_renamed = re.sub(r'([^\\]+).avi$', self.lclass + '_' + str(counter) + '.avi', file_dir)
            os.rename(file_dir, file_dir_renamed)
            print('Переименование файла ->', file_dir, file_dir_renamed)
            counter += 1

    def crop_videos(self):
        cropper.do_crop(self.lclass, self.path, self.class_dir, self.curr_amount, self.new_amount)

    def move_saves(self):
        listdir = os.listdir(self.save_dir)
        if listdir:
            for save in listdir:
                regex = r'({}_\d+)_'.format(self.lclass)
                folder_name = re.findall(regex, save)
                if folder_name:
                    print('Перемещение файла в папку ->', save, folder_name[0])
                    shutil.move(self.save_dir + '\\' + save, self.class_dir + '\\' + folder_name[0])
            

            
        
