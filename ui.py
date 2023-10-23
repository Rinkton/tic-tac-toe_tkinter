from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from objClass import Obj

class UI:
    """
    Имеет общие параметры для всего пользовательского интерфейса.
    Имеет функции для создания UI-элементов
    ВАЖНО: Позиционирование осуществляется через ux, uy(unit x, unit y), а размеры
    через usx, usy(unit size x, unit size y), они являются единичными
    велечинами(0 <= n <= 1), которая внутри здешних функции домножается на geometry_x или geometry_y,
    т.о. мы располагаем элементы относительно размера пользовательского окна
    """

    geometry_x : int = 1280
    """Размеры пользовательского окна по x"""
    geometry_y : int = 720
    """Размеры пользовательского окна по y"""

    size_kx = 1
    size_ky = 1

    def __init__(self):
        self.size_kx = self.geometry_x / 1280
        self.size_ky = self.geometry_y / 720

    def get_root_geometry(self) -> str:
        """
        :return: root.geometry в виде "300x250" и подобных
        """
        s = f"{self.geometry_x}x{self.geometry_y}"
        return s

    def __get_photo_image_and_image(self, path):
        image = Image.open(path)
        image = image.resize((int(image.width * self.size_kx), int(image.height * self.size_ky)))
        photo_image = ImageTk.PhotoImage(image)
        return photo_image, image

    def __place_elem(self, elem, image, x, y):
        xpos = x * self.size_kx - (image.width / 2)
        ypos = y * self.size_ky - (image.height / 2)
        elem.place(x=xpos, y=ypos)
        return xpos, ypos

    def __null_func(self):
        """
        Эдакая реализация паттерна NullObject
        :return:
        """
        pass

    def create_image(self, path, x=0, y=0):
        photo_image, image = self.__get_photo_image_and_image(path)
        label = Label(image=photo_image)
        label.image = photo_image
        xpos, ypos = self.__place_elem(label, image, x, y)
        obj = Obj({'x': xpos, 'y': ypos}, image)
        return obj

    def create_button(self, path, x=0, y=0, func=__null_func):
        photo_image, image = self.__get_photo_image_and_image(path)
        button = Button(image=photo_image, command=func)
        button.image = photo_image
        xpos, ypos = self.__place_elem(button, image, x, y)
        obj = Obj({'x': xpos, 'y': ypos}, image)
        return obj

    def create_image_on(self, path, obj, ux=0, uy=0):
        """

        :param path:
        :param obj: objClass.py
        :param ux:
        :param uy:
        :return:
        """
        base_ux = int(obj.pos['x']) / self.geometry_x
        base_uy = int(obj.pos['y']) / self.geometry_y
        add_ux = ux * (obj.img.width / self.geometry_x)
        add_uy = uy * (obj.img.height / self.geometry_y)
        result_ux = base_ux + add_ux
        result_uy = base_uy + add_uy
        self.create_image(path, result_ux, result_uy)
