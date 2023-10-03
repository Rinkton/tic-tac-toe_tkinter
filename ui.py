from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#TODO: UI должно отлавливать изменение размеров экрана
class UI:
    """
    Имеет общие параметры для всего пользовательского интерфейса.
    Имеет функции для создания UI-элементов
    ВАЖНО: Позиционирование и размеры осуществляется через ux, uy(unit x, unit y), они являются единичными
    велечинами(0 <= n <= 1), которая внутри здешних функции домножается на geometry_x или geometry_y,
    т.о. мы располагаем элементы относительно размера пользовательского окна
    """

    geometry_x : int = 500
    """Размеры пользовательского окна по x"""
    geometry_y : int = 200
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
        label.place(x=ux*self.geometry_x, y=uy*self.geometry_y)