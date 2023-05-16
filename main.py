#welcome to the FileExplorer

#importing modules
from collections.abc import Iterable
from typing import Any
import pygame
import threading
import multiprocessing
import os
import time


class pages :

    pages_list = []


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
                document = folder(files)
                document.image = pygame.image.load('H:\\AP projects\\FileExplorer\\icons\\foldericon.png')
                document.rect = document.image.get_rect(topleft = (120,pixel_distance))
                document.rect.left = 75
                document.name_id = pygame.font.SysFont("Arial", 10).render(document._name,True,'black'),(120,pixel_distance + 2 )

            else :
                document = file(files)
                document.image = pygame.image.load('H:\\AP projects\\FileExplorer\\icons\\documenticon.png')
                document.rect = document.image.get_rect(topleft = (120,pixel_distance))
                document.rect.left  = 75
                document.name_id = pygame.font.SysFont("Arial", 10).render(document._name,True,'black'),(120,pixel_distance + 2)




            #dir_list.append(document)
            directories_sprite_list.add(document)
            pixel_distance += 21.7

        self.directories = directories_sprite_list
        


#files initialization -----------------------------------------------------------------------------------------------
class directory :
    timer = 0
    timer_counter = 1
    def __init__(self, name) :
        
        self._name = name
        self._path = name
    
    @property
    def _path(self) :
        return self.path
    
    @_path.setter
    def _path(self,name) :
        self.path = os.path.join(os.getcwd(),name)



class file(directory,pygame.sprite.Sprite) :
    def __init__(self,name) :
        
        
        super().__init__(name) 
        pygame.sprite.Sprite.__init__(self)

        self._file_type = self._path
        self.image = None
        
        
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
        if directory.timer > directory.timer_counter :
            if self.rect.collidepoint(mouse_pos) == True :
                commitsonfiles(self,pygame.image.load('H:\AP projects\FileExplorer\icons\\documenticon(selected).png'))

        directory.timer += 1



    @staticmethod
    def reverse_index_finder(address) :
        reversed_address = "".join(reversed(address))
        index= reversed_address.find('.')
        return index


class folder(directory,pygame.sprite.Sprite) :
    def __init__(self,name) :
        super().__init__(name)
        pygame.sprite.Sprite.__init__(self)

        self.image = None
        

    def update(self) :
        if directory.timer > directory.timer_counter :
            if self.rect.collidepoint(mouse_pos) == True :
                commitsonfiles(self,pygame.image.load('H:\AP projects\FileExplorer\icons\\foldericon(selected).png'))
        directory.timer += 1



def outer_2() :
    last_direc = None
    last_image = None
    timer  = 0
    def commitsonfiles(direc,image) :
        nonlocal last_image,last_direc ,timer
        if event.type == pygame.MOUSEBUTTONDOWN :
            directory.timer = 0
            if last_direc != None :
                last_direc.image = last_image      
            if last_direc == direc :
                if os.path.isdir(direc._path) :
                    back_button.history.append(os.getcwd())
                    try :
                        os.chdir(direc._path)
                    except PermissionError :
                        print("not allowed to go to this file")
                    lst = os.listdir(os.getcwd())
                    directory_list(lst)
                    page_changer(None)
                else :
                    os.system('"%s"' % direc._path)

            last_direc = direc
            last_image = direc.image
            direc.image = image
        
    return commitsonfiles

commitsonfiles = outer_2()

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
        self.image = pygame.image.load("H:\\AP projects\\FileExplorer\\laodings\\loading00.png")
        self._frames = "H:\\AP projects\\FileExplorer\\laodings"
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
            frames_png.append(pygame.image.load('H:\\AP projects\\FileExplorer\\laodings\\' + png))

        self.frames = frames_png


    def update(self) :
        if self.frame_index > 68 :
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
                    lst = os.listdir(os.getcwd())
                    directory_list(lst)
                    page_changer(None)
                    self.timer = 0


            else :
                self.image = self.active_button

        else :
            self.image = self.unactive_button


        self.timer += 1



class forward_button(forward_back_button) :
    history = []
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load('H:\AP projects\FileExplorer\icons\\backbuttonicon\\backbuttoniconrightnowork.png')
        self.unactive_button = pygame.image.load('H:\AP projects\FileExplorer\icons\\backbuttonicon\\backbuttoniconrightnowork.png')
        self.active_button = pygame.image.load('H:\AP projects\FileExplorer\icons\\backbuttonicon\\backbuttonicon.png')
        self.collision_with_active_button = pygame.image.load('H:\AP projects\FileExplorer\icons\\backbuttonicon\\backbuttoniconrightcollision.png')
        self.rect = self.image.get_rect(topleft = (60,20))



class back_button(forward_back_button) :
    history = []
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load('H:\AP projects\FileExplorer\icons\\backbuttonicon\\backbuttoniconleftnowork.png')
        self.unactive_button = pygame.image.load('H:\AP projects\FileExplorer\icons\\backbuttonicon\\backbuttoniconleftnowork.png')
        self.active_button = pygame.image.load('H:\AP projects\FileExplorer\icons\\backbuttonicon\\backbuttoniconleft.png')
        self.collision_with_active_button = pygame.image.load('H:\AP projects\FileExplorer\icons\\backbuttonicon\\backbuttoniconcollisionleft.png')
        self.rect = self.image.get_rect(topleft = (20,20))

def outer() :


    def directory_list(dirlist) :
        pages.pages_list = []

        pages_ = [dirlist[i:i + 13] for i in range(0, len(dirlist), 13)]

        for page in pages_ :
            pages.pages_list.append(pages(page))
    

    return directory_list


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


os.chdir('H:\\')        



pygame.init()




screen = pygame.display.set_mode((600,400))
screen.fill('white')
pygame.display.set_caption('FileExplorer')
clock = pygame.time.Clock()


#dirlist = os.listdir(os.getcwd())
dirlist = os.listdir(os.getcwd())
directory_list(dirlist)
mouse_pos = pygame.mouse.get_pos()
page_index = 0

display_dir()


left_page_button = pagebuttons(pos_x=310 ,pos_y=370 ,link='H:\AP projects\FileExplorer\icons\wiggelingbutton(left)animation')
right_page_button = pagebuttons(pos_x=340,pos_y=370,link= 'H:\AP projects\FileExplorer\icons\wigglebutton(right)')
buttons_group  = pygame.sprite.Group()
buttons_group.add(left_page_button)
buttons_group.add(right_page_button)

laoding = loading_icon()
loading_group = pygame.sprite.Group()
loading_group.add(loading_icon())


_forward = forward_button()
_back = back_button()
_forward.instance = _back
_back.instance = _forward
forward_back_button_group = pygame.sprite.Group()
forward_back_button_group.add(_forward)
forward_back_button_group.add(_back)

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()

    mouse_pos = pygame.mouse.get_pos()
    display_dir()
    

    
    clock.tick(60)
    buttons_group.draw(screen)
    buttons_group.update()    

    forward_back_button_group.draw(screen)
    forward_back_button_group.update()

    pygame.display.flip()
    pygame.display.update()
    screen.fill(color='white')
