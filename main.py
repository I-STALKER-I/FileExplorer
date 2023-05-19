#welcome to the FileExplorer

#importing modules
from typing import Any
import pygame
import threading
import multiprocessing
from multiprocessing import Barrier
import os
import time
from multiprocessing.context import Process

class pages :

    pages_list = []
    hidden = True


    def __init__(self,directories) :
        self._directories = directories




    @property
    def _directories(self) :
        return self.directories
    

    @_directories.setter
    def _directories(self,directory) :
        directories_sprite_list = pygame.sprite.Group()
        pixel_distance = 60
        for files in directory :
            if os.path.isdir(files) :
                document = folder(files,pixel_distance)


            else :
                document = file(files,pixel_distance)




            #dir_list.append(document)
            if self.hidden == True :
                try:
                    if document._name[0] !='.' and document._name[0] != '$' and '.ini' not in document._file_type:
                        directories_sprite_list.add(document)
                        pixel_distance += 21.7
                except IndexError :
                    directories_sprite_list.add(document)
                    pixel_distance += 21.7

            else :
                    directories_sprite_list.add(document)
                    pixel_distance += 21.7

        self.directories = directories_sprite_list

        if len(shared_memory.memory_cut) > 0 :
            for dir in self.directories :
                if dir in shared_memory.memory_cut :
                    dir.image = dir.cut_icon
        


#files initialization -----------------------------------------------------------------------------------------------
class directory :
    timer = 0
    timer_counter = 1
    selected_files_folders = []
    def __init__(self, name) :
        
        self._name = name
        self._path = name
        self.Lock = False

    @property
    def _path(self) :
        return self.path
    
    @_path.setter
    def _path(self,name) :
        self.path = os.path.join(os.getcwd(),name)



class file(directory,pygame.sprite.Sprite) :
    def __init__(self,name,pixel_distance) :
        
        
        super().__init__(name) 
        pygame.sprite.Sprite.__init__(self)
        self.cut_icon = pygame.image.load(f'{source}\icons\\documenticon_cut.png')
        self._file_type = self._path
        self.image = pygame.image.load(f'{source}\\icons\\documenticon.png')
        self.rect = self.image.get_rect(topleft = (120,pixel_distance))
        self.rect.left  = 75
        self.name_id = pygame.font.SysFont("Arial", 10).render(self._name,True,'black'),(120,pixel_distance + 2)
        self.unactive_icon = self.image
        self.active_icon = pygame.image.load(f'{source}\icons\\documenticon(selected).png')


    @property
    def image(self) :
        return self._image
    
    @image.setter
    def image(self,value) :
        self._image = value
        if value == self.cut_icon :
            self.Lock = True
        else :
            self.Lock = False
        
        
    @property
    def _name(self):
        return self.name

    @_name.setter
    def _name(self,address) :
        """in here we wnat to find the last dot so we can get our file type if we use find() it wont have a problem if there is no dot in the
        naming of files but if a dot pops out we have to find the last dot so ve reverse our string the find the dot """
        self.name = address[:-self.reverse_index_finder(address) - 1]


    @property
    def _file_type(self) :
        return self.file_type
    
    @_file_type.setter
    def _file_type(self,address) :
        self.file_type = address[-self.reverse_index_finder(address) - 1:]


    def update(self) :
        if self.Lock == False :
            if directory.timer > directory.timer_counter :
                if self.rect.collidepoint(mouse_pos) == True :
                    commitsonfiles(self,pygame.image.load(f'{source}\icons\\documenticon(selected).png'))

            directory.timer += 1


    @staticmethod
    def reverse_index_finder(address) :
        reversed_address = "".join(reversed(address))
        index = reversed_address.find('.')
        return index
    
    def __eq__(self,value) :
        try :
            if self._path == value._path :
                return True
            return False
        except Exception :
            return False
        
    def __hash__(self) :
        return id(self)


class folder(directory,pygame.sprite.Sprite) :
    def __init__(self,name,pixel_distance) :
        super().__init__(name)
        pygame.sprite.Sprite.__init__(self)
        self.cut_icon = pygame.image.load(f'{source}\icons\\foldericon_cut.png')
        self._file_type = "None"
        self.image = None
        self.image = pygame.image.load(f'{source}\\icons\\foldericon.png')
        self.rect = self.image.get_rect(topleft = (120,pixel_distance))
        self.rect.left = 75
        self.name_id = pygame.font.SysFont("Arial", 10).render(self._name,True,'black'),(120,pixel_distance + 2 )
        self.unactive_icon = self.image
        self.active_icon = pygame.image.load(f'{source}\icons\\foldericon(selected).png')
        

    @property
    def image(self) :
        return self._image
    
    @image.setter
    def image(self,value) :
        self._image = value
        if value == self.cut_icon :
            self.Lock = True
        else :
            self.Lock = False
        

    def update(self) :
        if self.Lock == False :
            if directory.timer > directory.timer_counter :
                if self.rect.collidepoint(mouse_pos) == True :
                    commitsonfiles(self,pygame.image.load(f'{source}\icons\\foldericon(selected).png'))
            directory.timer += 1

    def __eq__(self,value) :
        try :
            if self._path == value._path :
                return True
            return False
        except Exception :
            return False

    def __hash__(self) :
        return id(self)



def outer_2() :
    last_direc = None
    timer  = 0
    def commitsonfiles(direc,image) :
        nonlocal last_direc ,timer

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            directory.timer = 0
            if last_direc != None :
                if last_direc.image != last_direc.cut_icon :
                    last_direc.image = last_direc.unactive_icon     
            if last_direc == direc :
                if os.path.isdir(direc._path) :
                    back_button.history.append(os.getcwd())
                    try :
                        directory.selected_files_folders = []
                        os.chdir(direc._path)
                        loader('folder')
                    except PermissionError :
                        print("not allowed to go to this file")

                else :
                    loader('file',direc._path)
            else :

                last_direc = direc
                deselect(direc)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 :
            multiple_files_selection(direc)
            directory.timer = 0

        
    return commitsonfiles

commitsonfiles = outer_2()


def deselect(direc) :
    for file in directory.selected_files_folders :
        file.image = file.unactive_icon

    directory.selected_files_folders = []
    directory.selected_files_folders.append(direc)



    direc.image = direc.active_icon


def multiple_files_selection(direc) :
    if direc in direc.selected_files_folders :
        direc.selected_files_folders.remove(direc)
        direc.image = direc.unactive_icon
    else :
        direc.selected_files_folders.append(direc)
        direc.image = direc.active_icon


#left and right page buttons ------------------------------------------------------------------------

def page_changer(variable) :
    global page_index 
    if variable == "right" :
        if page_index == len(pages.pages_list) - 1:
            return False
        
        page_index += 1

    elif variable == "left" :
        if page_index == 0 :
            return False
        
        page_index -= 1

    else :
        page_index = 0






class pagebuttons(pygame.sprite.Sprite) :
    def __init__(self ,link,pos_x,pos_y) :
        super().__init__()
        self._name = link
        self._link = link
        self._frames = link
        self.image = None
        self.counter = 1
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self._button_rect = self.rect
        self.rect = [pos_x ,pos_y]

    @property
    def _name(self) :
        return self.name
    
    @_name.setter
    def _name(self,value) :
        if value[-1] == 'n' :
            self.name = 'left'
        else :
            self.name = 'right' 

    @property
    def _frames(self) :
        return self.frames
    
    @_frames.setter
    def _frames(self,link) :
        frames = os.listdir(link)
        self.frames = self.motion_maker(frames)

    @property
    def image(self) :
        return self._image
    
   
    @image.setter
    def image(self,value) :
        if value == None : 
            self._image = self.frames[0]
        else :
            self._image = value

    def motion_maker(self,lst) :
        frames_list = []
        for frame in lst :
            frames_list.append(pygame.image.load(self._link + '\\' + frame).convert_alpha())

        return frames_list
    

    def update(self) :
        if self._button_rect.collidepoint(mouse_pos) == True :
            if self.counter >= len(self.frames) :
                self.counter = 0
 
            if event.type == pygame.MOUSEBUTTONDOWN :
                page_changer(self._name)
                time.sleep(0.2)
                

            self.image = self.frames[self.counter]
            self.counter += 1

        else :
            self.image = self.frames[0]
            self.counter = 0


#loading screen ---------------------------------------------------------------------------------------------------------
class loading_icon(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load(f"{source}\\laodings\\loading00.png")
        self._frames = f"{source}\\laodings"
        self.frame_index = 0
        self.rect = self.image.get_rect()


    @property
    def _frames(self) :
        return self.frames
    
    @_frames.setter
    def _frames(self,link) :
        frames_png = []
        pngs = os.listdir(link)
        for png in pngs :
            frames_png.append(pygame.image.load(f'{source}\\laodings\\' + png))

        self.frames = frames_png


    def update(self) :
        if self.frame_index > 19 :
            self.frame_index = 0

        self.image =  self._frames[self.frame_index]
        self.frame_index += 1


#forward back butoon -------------------------------------------------------------------------------------------------------
class forward_back_button(pygame.sprite.Sprite) :

    def __init__(self) :
        super().__init__()
        self.timer = 0


    def update(self, *args: Any, **kwargs: Any) :

        if len(self.history) > 0 :
            self.image = self.active_button

            if self.rect.collidepoint(mouse_pos) == True :
                self.image = self.collision_with_active_button
                if event.type == pygame.MOUSEBUTTONDOWN and self.timer > 13 :
                    self.instance.history.append(os.getcwd())
                    os.chdir(self.history[len(self.history)- 1])
                    self.history.pop(len(self.history) - 1)
                    loader('folder')
                    self.timer = 0


            else :
                self.image = self.active_button

        else :
            self.image = self.unactive_button


        self.timer += 1


#back and forward button -----------------------------------------------------
class forward_button(forward_back_button) :
    history = []
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load(f'{source}\icons\\backbuttonicon\\backbuttoniconrightnowork.png')
        self.unactive_button = pygame.image.load(f'{source}\icons\\backbuttonicon\\backbuttoniconrightnowork.png')
        self.active_button = pygame.image.load(f'{source}\icons\\backbuttonicon\\backbuttonicon.png')
        self.collision_with_active_button = pygame.image.load(f'{source}\icons\\backbuttonicon\\backbuttoniconrightcollision.png')
        self.rect = self.image.get_rect(topleft = (60,20))



class back_button(forward_back_button) :
    history = []
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load(f'{source}\icons\\backbuttonicon\\backbuttoniconleftnowork.png')
        self.unactive_button = pygame.image.load(f'{source}\icons\\backbuttonicon\\backbuttoniconleftnowork.png')
        self.active_button = pygame.image.load(f'{source}\icons\\backbuttonicon\\backbuttoniconleft.png')
        self.collision_with_active_button = pygame.image.load(f'{source}\icons\\backbuttonicon\\backbuttoniconcollisionleft.png')
        self.rect = self.image.get_rect(topleft = (20,20))

def outer() :


    def directory_list(dirlist) :
        pages.pages_list = []

        pages_ = [dirlist[i:i + 13] for i in range(0, len(dirlist), 13)]

        for page in pages_ :
            pages.pages_list.append(pages(page))
    

        

    return directory_list

#hidden files and folders shower ================================================
class hidden_button(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load(f'{source}\icons\\featureicons\hidden_files_icon(unactive).png')
        self.flag = True
        self.next_image = pygame.image.load(f'{source}\icons\\featureicons\hidden_files_icon(active).png')
        self.rect = self.image.get_rect(topleft = (120,25))
        self.timer = 0


    def update(self) :
        if self.rect.collidepoint(mouse_pos) :
            if self.timer > 13 :
                
                if event.type == pygame.MOUSEBUTTONDOWN :
                    next_image = self.image
                    self.image =  self.next_image
                    self.next_image = next_image
                    self.timer = 0
                    if self.flag == True :
                        pages.hidden = False
                        loader('folder')
                        self.flag = False
                    else :
                        pages.hidden = True
                        loader('folder')
                        self.flag = True
                    

        self.timer += 1



directory_list = outer()

def display_dir() :
    global page_index

    directory_screen = pygame.Surface((518,291))
    directory_screen.fill('#F2F2F2')
    screen.blit(directory_screen,(69 ,61))
    try :
        directory.timer_counter = len(pages.pages_list[page_index]._directories) * 13
        pages.pages_list[page_index]._directories.update()

    except IndexError :
        pass
    
    try :
        pages.pages_list[page_index]._directories.draw(screen)
        for document in pages.pages_list[page_index]._directories :

            screen.blit(document.name_id[0],document.name_id[1])
    except IndexError :
        pass


def folder_loader() :
    lst = os.listdir(os.getcwd())
    directory_list(lst)
    page_changer(None)


    return 0

def file_loader(path) :

    os.system('"%s"' % path)

def search_loader(lst) :
    directory_list(lst)
    page_changer(None)



def loader(flag,*args) :
    if flag == 'folder' :
        thread = threading.Thread(target = folder_loader)
    elif flag == 'file' :
        thread = threading.Thread(target=file_loader,args = (args))
    else :
        thread = threading.Thread(target=search_loader,args = (args))

    thread.start()

    while True :
        
        if thread.is_alive() == False :
            screen.fill('white')
            break
        

        loading_group.draw(screen)
        loading_group.update()
        pygame.display.flip()
        pygame.display.update()
        screen.fill('white')
        
        clock.tick(60)
        

    return 0


#new file maker ------------------------------------------------------------------------------

def typing() :
    while True :

        if new_file.flag == True :
            new_file.flag = False
            break

        try :
            folder_typing_group.draw(screen)
            folder_typing_group.update()
            
        except Exception :
            pass

        clock.tick(60)



class new_file(pygame.sprite.Sprite) :
    flag = False
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load(f'{source}\icons\\newfolder.png')
        self.active_image = pygame.image.load(f'{source}\icons\\newfolder(active).png')
        self.unactive_image = pygame.image.load(f'{source}\icons\\newfolder.png')
        self.rect = self.image.get_rect(topleft = (170,20))
        self.timer = 0
        self.thread = None

    def update(self) :
        if self.rect.collidepoint(mouse_pos) :
            self.image = self.active_image
            if self.timer > 13 :
                if event.type == pygame.MOUSEBUTTONDOWN  :
                    if self.thread == None :
                        self.timer = 0

                        self.thread = threading.Thread(target = typing)
                        self.thread.start()
                    
        else :
            self.image = self.unactive_image

        if self.timer < 14 :
            self.timer += 1
        
        if self.thread != None :
            if self.thread.is_alive() == False :
                self.thread = None



class folder_typing_gui(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load(f'{source}\icons\\filenameinput.png')
        self.non_active_icon = pygame.image.load(f'{source}\icons\\filenameinput.png')
        self.active_icon = pygame.image.load(f'{source}\icons\\filenameinput(active).png')
        self.rect = self.image.get_rect(topleft = (220,15))
        self.flag = False
        self.txt = ''
        self.timer = 0

    def update(self) :

        screen.blit(pygame.font.SysFont("Arial", 10).render(self.txt,True,'black'),(225,20))
        if event.type == pygame.MOUSEBUTTONDOWN :
            if self.rect.collidepoint(mouse_pos) :
                self.image =  self.active_icon
                self.flag = True
            else :
                self.image = self.non_active_icon
                self.flag = False
                self.txt = ''
        
        if self.flag == True :
            if self.timer > 8 :
                if event.type == 771 :
                    if len(self.txt) <= 33 :
                        self.txt += event.text
                    self.timer = 0

                elif event.key == pygame.K_BACKSPACE and event.type == pygame.KEYDOWN :
                    self.txt = self.txt[:-1]
                    self.timer = 0

                elif event.key == pygame.K_RETURN :
                    new_file.flag = True
                    os.system(f"mkdir {self.txt}")
                    loader('folder')
                    self.timer = 0

            if self.timer < 14 :
                self.timer += 1

                    





class fodler_typing_gui_exit(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__() 
        self.image = pygame.image.load(f'{source}\icons\\filenameinputexitbutton.png')
        self.non_active_image = pygame.image.load(f'{source}\icons\\filenameinputexitbutton.png')
        self.active_image = pygame.image.load(f'{source}\icons\\filenameinputexitbutton(acitve).png')
        self.rect = self.image.get_rect(topleft = (390,13))

    def update(self) :
        if self.rect.collidepoint(mouse_pos) :
            self.image = self.active_image
            if event.type == pygame.MOUSEBUTTONDOWN :
                new_file.flag = True

        else :
            self.image = self.non_active_image


#Recyclebin
class recyclebin(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load(f"{source}\icons\\recyclebin.png")
        self.rect = self.image.get_rect(topleft = (80,360))
        self.unactive_icon = self.image
        self.active_icon = pygame.image.load(f"{source}\icons\\recyclebin(active).png")
        self.timer = 0

    def update(self) :
        if len(directory.selected_files_folders) > 0 :
            if self.rect.collidepoint(mouse_pos) :
                self.image = self.active_icon
                if event.type == pygame.MOUSEBUTTONDOWN and self.timer > 13 :
                    """removing files was risky and it could harm the drives so instead im moving the files to a folder named recyclebin"""
                    for file in directory.selected_files_folders :
                        os.system(f'move "{file._path}" "{source}"\\recyclebin') 

                    loader('folder')
                    directory.selected_files_folders = []
            else :
                self.image = self.unactive_icon
        else :
            self.image = self.unactive_icon
        
        if self.timer < 14 :
            self.timer += 1
            
#cut copy paste ---------------------------------------------------------------------------------------[]
class shared_memory(pygame.sprite.Sprite) :
    memory_cut = []
    memory_copy = []

    def __init__(self) :
        super().__init__()
        self.timer = 0


    def update(self) :
        if len(directory.selected_files_folders) > 0 and self.rect.collidepoint(mouse_pos) :
            self.image = self.active_icon
            if self.timer > 13 :
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                    if self.__name__ == 'cut' :
                        self.cut()
                    elif self.__name__ == 'copy' :
                        self.copy()

                    self.timer = 0
        else :
            self.image = self.unactive_icon
            

        if self.timer < 14 :
            self.timer += 1


class cut(shared_memory) :
    def __init__(self) :
        
        super().__init__() 
        self.image = pygame.image.load(f'{source}\icons\cutcopypaste\cut(unactive).png')
        self.unactive_icon = self.image
        self.active_icon = pygame.image.load(f"{source}\icons\cutcopypaste\cut(active).png")
        self.rect = self.image.get_rect(topleft = (120,360))
        self.__name__ = cut.__name__

    def cut(self) :
        
        if len(shared_memory.memory_cut) > 0 :
            thread = threading.Thread(target = cutted_file_folder_to_unactive,args=(shared_memory.memory_cut,))
            thread.start()

        shared_memory.memory_cut = [*directory.selected_files_folders]
        for file in directory.selected_files_folders :
            file.image = file.cut_icon


        directory.selected_files_folders = []

def cutted_file_folder_to_unactive(memory) :
    counter = 0
    for page in pages.pages_list :
        if counter == len(memory) :
            break
        for file in memory :
            for files in page._directories :
                if file == files :
                    files.image = files.unactive_icon
                    counter += 1
                    break



class copy(shared_memory) :
    def __init__(self) :
        super().__init__() 
        self.image = pygame.image.load(f'{source}\icons\cutcopypaste\copy(unactive).png')
        self.unactive_icon = self.image
        self.active_icon = pygame.image.load(f"{source}\icons\cutcopypaste\copy(active).png")
        self.rect = self.image.get_rect(topleft = (160,360))
        self.__name__ = copy.__name__

    def copy(self) :
        shared_memory.memory_copy = [*directory.selected_files_folders]
        directory.selected_files_folders = []



class paste(shared_memory) :
    def __init__(self) :
        super().__init__() 
        self.image = pygame.image.load(f'{source}\icons\cutcopypaste\past(unactive).png')
        self.unactive_icon = self.image
        self.active_icon = pygame.image.load(f"{source}\icons\cutcopypaste\past(active).png")
        self.rect = self.image.get_rect(topleft = (200,360))
        self.__name__ = paste.__name__


    def paste(self) :
        if len(shared_memory.memory_cut) == 0 and len(shared_memory.memory_copy) == 0 :
            thread = threading.Thread(target = paste.empty_shared_memory)
            thread.start()

        else :
            if len(shared_memory.memory_cut) > 0 :
                thread = threading.Thread(target= self.cut_paste)
                thread.start()
                thread.join()
                


            elif len(shared_memory.memory_copy) > 0 :
                thread = threading.Thread(target=self.copy_paste)
                thread.start()
                thread.join()

    def update(self):
        if self.rect.collidepoint(mouse_pos) and (len(shared_memory.memory_copy) > 0 or len(shared_memory.memory_cut) > 0) :
            self.image = self.active_icon
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.timer > 13:
                self.paste()
        else :
            self.image = self.unactive_icon

        if self.timer < 14 :
            self.timer += 1


    @staticmethod
    def cut_paste() :
        for file in shared_memory.memory_cut :
            os.system(f'move "{file._path}" {os.getcwd()}')
            file.image = file.unactive_icon

        shared_memory.memory_cut = []
        loader("folder")

    @staticmethod
    def copy_paste() :
        for file in shared_memory.memory_copy :
            os.system(f'copy "{file._path}" {os.getcwd()}')


        shared_memory.memory_copy = []
        loader("folder")



    @staticmethod
    def empty_shared_memory() :
        for i in range(200) :
            screen.blit(pygame.font.SysFont("Arial", 10).render('nothing to paste',True,'black'),(230,360))
            clock.tick(60)

class rename(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load(f"{source}\icons\Rename(unactive).png")
        self.rect = self.image.get_rect(topleft = (240,356))
        self.active_icon = pygame.image.load(f'{source}\icons\Rename(active).png')
        self.unactive_icon = self.image
        self.thread = None

        self.timer = 0
        self.flag = False
    

    def update(self) :
        if self.flag == False :
            if self.rect.collidepoint(mouse_pos) and len(directory.selected_files_folders) > 0:
                self.image = self.active_icon
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.timer > 13 :
                    self.timer = 0
                    if len(directory.selected_files_folders) > 1 :
                        thread = threading.Thread(target = self.to_many_selected)
                        thread.start()
                
                    elif len(directory.selected_files_folders) == 1 :
                        if self.thread == None or self.thread.is_alive() == False :
                            self.thread = threading.Thread(target = self.renaiming,args=(directory.selected_files_folders[0],))
                            self.thread.start() 
                            directory.selected_files_folders = []

            else :
                self.image = self.unactive_icon

        if self.timer <= 14 :
            self.timer += 1

        
    @staticmethod
    def to_many_selected() :
        for i in range(200) :
            screen.blit(pygame.font.SysFont("Arial", 10).render('cannot rename multiple files',True,'black'),(250,360))
            clock.tick(60)

    @staticmethod
    def renaiming(direc) :
        rect_renaming.rect = rect_renaming.image.get_rect(topleft = (direc.name_id[1][0] - 1,direc.name_id[1][1] - 3))
        while True :
            if renaming_rect.flag == False :
                renaming_rect.flag = True
                break


            rect_group.draw(screen)
            rect_group.update(direc.name_id[1],direc)
            clock.tick(60)
        
                

class renaming_rect(pygame.sprite.Sprite) :
    flag = True
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load(f"{source}\icons\\rename.png")
        self.rect = self.image.get_rect()
        self.timer = 0
        self.text = ''
        self.first_text = True

    def update(self,location,direc) :
        screen.blit(pygame.font.SysFont("Arial", 10).render(self.text,True,'black'),(location[0] + 3,location[1]))
        if self.timer > 13 :
            if event.type == pygame.MOUSEBUTTONDOWN :
                renaming_rect.flag = False
                self.timer = 0


            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE :
                self.text = self.text[:-1]
                self.timer = 0


            elif event.type == pygame.TEXTINPUT :
                    
                    
                self.text += event.text 
                self.timer = 0

            elif event.type == pygame.KEYDOWN and event.key == 13 :
                self.timer = 0
                renaming_rect.flag = False
                direc.name_id = pygame.font.SysFont("Arial", 10).render(self.text,True,'black'),direc.name_id[1]
                try :
                    old_name = direc._name + direc.file_type
            
                    direc._name = self.text + direc.file_type
                    direc._path = self.text + direc.file_type

                    new_name = self.text + direc.file_type
                except AttributeError :
                    old_name = direc._name

                    direc._name = self.text
                    direc._path = self.text

                    new_name = self.text
                os.system(f'ren "{old_name}" "{new_name}"')
                


                
        
        if self.timer <= 13 :
            self.timer += 1

        
class ext(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image =  pygame.image.load(f"{source}\icons\ext(unactive).png")
        self.rect = self.image.get_rect(topleft = (500,20))
        self.active_icon = pygame.image.load(f'{source}\icons\ext(active).png')
        self.unactive_icon = self.image
        self.flag = False
        self.timer = 0

    def update(self) :
        if self.rect.collidepoint(mouse_pos) :
            if self.timer > 13 : 
                if event.type == pygame.MOUSEBUTTONDOWN :
                    self.timer = 0

                    self.flag =  not self.flag


                    if self.flag == True :
                        thread = threading.Thread(target = self.ext_show) 
                        thread.start()

                    else :
                        thread = threading.Thread(target=self.ext_unshow)
                        thread.start()
                
            self.image = self.active_icon

        
        else :
            if self.flag == False :

                self.image = self.unactive_icon





        if self.timer <= 14 :
            self.timer += 1


    @staticmethod
    def ext_show() :
        for page in pages.pages_list :
            for doc in page._directories :
                try :
                    doc.name_id = pygame.font.SysFont("Arial", 10).render(doc._name + doc.file_type,True,'black'),doc.name_id[1]

                except AttributeError :
                    pass
    @staticmethod
    def ext_unshow() :
        for page in pages.pages_list :
            for doc in page._directories :
                try :
                    doc.name_id = pygame.font.SysFont("Arial", 10).render(doc._name,True,'black'),doc.name_id[1]
                except AttributeError :
                    pass


# search -------------------------------------------------------------------------
class search(pygame.sprite.Sprite) :
    matches = []
    child_threads = []
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load(f'{source}\icons\search(unactive).png')
        self.rect = self.image.get_rect(topright = (585,370))
        self.timer = 0 
        self.flag = False
        self.text = "search here"
        self.mutex = threading.Lock()

    def update(self) :
        screen.blit(pygame.font.SysFont("Arial", 10).render(self.text,True,'black'),(430,375))


        if self.flag == False :
            self.text = "search here(max 31 digit & word)"
            if self.rect.collidepoint(mouse_pos) :
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.timer > 13:
                    self.flag = True
                    self.text = ''
                    self.timer = 0
                    

        else :
            if search_button.flag == True :
                if len(self.text) > 0 :
                    _search_button.image = _search_button.active_icon
                else :
                    _search_button.image = _search_button.unactive_icon

                if self.timer > 13 :
                    if event.type == pygame.TEXTINPUT and len(self.text) < 31:
                        self.text += event.text
                        self.timer = 0

                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE :
                        self.text = self.text[:-1]
                        self.timer = 0
            
                    elif event.type == pygame.KEYDOWN and event.key == 13 :
                        if len(self.text) == 0 :
                            _search_button.image = _search_button.unactive_icon
                            self.flag = False
                            self.timer = 0

                        else :
                            search.matches = []
                            search.child_threads = []
                            _search_button.image = _search_button.unactive_icon
                            self.flag = False
                            self.timer = 0 
                            thread = threading.Thread(target = self.searching ,args = (os.getcwd(),self.text))
                            thread.start()

                            while thread.is_alive() :
                                for events in pygame.event.get() :
                                    if events.type == pygame.QUIT :
                                        pygame.quit()
                                        exit()

                                loading_group.draw(screen)
                                loading_group.update()
                                pygame.display.flip()
                                pygame.display.update()
                                screen.fill('white')
                                clock.tick(60)

                            loader("search",search.matches)
                            

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                    if self.rect.collidepoint(mouse_pos) == False :
                        self.flag = False 

            else :
                search_button.flag = True
                self.flag = False

        if self.timer <= 13 :
            self.timer += 1

    def searching(self,root,filename) :
        
        #print('Searching in:', root)
        
        try :
            for file in os.listdir(root):
                full_path = os.path.join(root, file)  # concatenates root with file
                if filename in file:
                    self.mutex.acquire()  # mutex
                    search.matches.append(full_path)
                    self.mutex.release()  # mutex
                if os.path.isdir(full_path):
                    t = threading.Thread(target=self.searching, args=(full_path, filename))
                    t.start()
                    search.child_threads.append(t)
        except Exception :
            pass
            for thread in search.child_threads:
                thread.join()






                
class search_button(pygame.sprite.Sprite) :
    flag = True
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load(f"{source}\icons\search_button(unactive).png")
        self.rect = self.image.get_rect(topright = (585,370))
        self.active_icon = pygame.image.load(f"{source}\icons\search_button(active).png")
        self.unactive_icon = self.image
        self.timer = 0
    def update(self) :
        if self.timer > 13 :
            if self.rect.collidepoint(mouse_pos) :
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                    search_button.flag = False
                    self.image = self.unactive_icon

        
        if self.timer <= 13 :
            self.timer += 1


source = os.getcwd()

class quickaccess(pygame.sprite.Sprite) :
    distance = 80
    def __init__(self,name,path) :
        super().__init__()
        self.timer = 0
        self.name = name
        self.path = path
        self.image = pygame.image.load(f"{source}\icons\disk.png")
        self.unactive_icon = pygame.image.load(f"{source}\icons\disk.png")
        self.active_icon = pygame.image.load(f"{source}\icons\disk(active).png")
        self.rect = self.image.get_rect(topleft = (5,quickaccess.distance))
        self.name_show = pygame.font.SysFont("Arial", 15).render(self.name,True,'black'),(40,quickaccess.distance - 5)
        quickaccess.distance += 20

    def update(self) :
        print(self.timer)
        screen.blit(self.name_show[0],self.name_show[1])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.timer >= 13 :
            if self.rect.collidepoint(mouse_pos) :
                self.image = self.active_icon
                os.chdir(self.path)
                loader("folder")
                self.timer = 0
            
            else :
                self.image = self.unactive_icon



        if self.timer <= 14 :
            self.timer += 1


quickaccess_group = pygame.sprite.Group()

def quickaccess_check() :
    if os.path.isdir("C:") :
        quickaccess_group.add(quickaccess("C","C:"))
        
    
    if os.path.isdir("D:") :
        quickaccess_group.add(quickaccess("D","D:"))

    if os.path.isdir("H:") :
        quickaccess_group.add(quickaccess("H","H:"))




def main() :
    global screen ,mouse_pos ,event ,page_index ,loading_group,clock ,folder_typing_group ,rect_group ,rect_renaming ,_search_button
    pygame.init()




    screen = pygame.display.set_mode((600,400))
    screen.fill('white')
    pygame.display.set_caption('FileExplorer')
    clock = pygame.time.Clock()


    dirlist = os.listdir(os.getcwd())
    directory_list(dirlist)
    mouse_pos = pygame.mouse.get_pos()
    page_index = 0

    display_dir()


    left_page_button = pagebuttons(pos_x=310 ,pos_y=370 ,link=f'{source}\icons\wiggelingbutton(left)animation')
    right_page_button = pagebuttons(pos_x=340,pos_y=370,link= f'{source}\icons\wigglebutton(right)')
    buttons_group  = pygame.sprite.Group()
    buttons_group.add(left_page_button)
    buttons_group.add(right_page_button)

    loading_group = pygame.sprite.Group()
    loading_group.add(loading_icon())


    _forward = forward_button()
    _back = back_button()
    _forward.instance = _back
    _back.instance = _forward
    forward_back_button_group = pygame.sprite.Group()
    forward_back_button_group.add(_forward)
    forward_back_button_group.add(_back)


    hidden = hidden_button()
    Rename = rename()
    ext_ = ext()
    _search = search()
    _search_button = search_button()
    
    feature_group = pygame.sprite.Group()
    feature_group.add(hidden,Rename,ext_,_search,_search_button)


    rect_renaming = renaming_rect()
    rect_group = pygame.sprite.Group()
    rect_group.add(rect_renaming)


    new_file_make = new_file()
    new_file_group = pygame.sprite.Group()
    new_file_group.add(new_file_make)

    folder_typing = folder_typing_gui()
    folder_typing_exit = fodler_typing_gui_exit()
    folder_typing_group = pygame.sprite.Group()
    folder_typing_group.add(folder_typing)
    folder_typing_group.add(folder_typing_exit)


    recycle_bin = recyclebin()
    cut_mov = cut()
    copy_mov = copy()
    paste_mov = paste()
    movement_group = pygame.sprite.Group()
    movement_group.add(recycle_bin,cut_mov,copy_mov,paste_mov)


    quickaccess_check()

    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()



        mouse_pos = pygame.mouse.get_pos()
        display_dir()

        clock.tick(60)

        screen.blit(pygame.font.SysFont("Arial", 15).render(os.getcwd(),True,'black'),(225,43))

        buttons_group.draw(screen)
        buttons_group.update()    

        forward_back_button_group.draw(screen)
        forward_back_button_group.update()

        feature_group.draw(screen)
        feature_group.update()


        new_file_group.draw(screen)
        new_file_group.update()

        movement_group.draw(screen)
        movement_group.update()

        quickaccess_group.draw(screen)
        quickaccess_group.update()

        pygame.display.flip()
        pygame.display.update()
        screen.fill(color='white')





        
if __name__ == '__main__' :
    main()