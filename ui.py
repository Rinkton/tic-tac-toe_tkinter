from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from objClass import Obj

class UI:
    """
    Имеет общие параметры для всего пользовательского интерфейса.
    Имеет функции для создания UI-элементов
    ВАЖНО: Позиционирование и размеры осуществляется через ux, uy(unit x, unit y), они являются единичными
    велечинами(0 <= n <= 1), которая внутри здешних функции домножается на geometry_x или geometry_y,
    т.о. мы располагаем элементы относительно размера пользовательского окна
    """

    geometry_x : int = 1280
    """Размеры пользовательского окна по x"""
    geometry_y : int = 720
    """Размеры пользовательского окна по y"""

    def get_root_geometry(self) -> str:
        """
        :return: root.geometry в виде "300x250" и подобных
        """
        s = f"{self.geometry_x}x{self.geometry_y}"
        return s

    def create_image(self, path, ux=0, uy=0):
        image = Image.open(path)
        photo_image = ImageTk.PhotoImage(image)
        label = Label(image=photo_image)
        label.image = photo_image
        xpos = ux*self.geometry_x - (image.width/2)
        ypos = uy*self.geometry_y - (image.height/2)
        label.place(x=xpos, y=ypos)
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
