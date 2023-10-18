from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ui import UI

if __name__ == '__main__':
    # Мб каждую клетку отдельно и 3 спрайта с пустым, иксом и ноликом
    root = Tk()
    root.title("Приложение на Tkinter")
    root.resizable(False, False)

    ui = UI()
    geometry_s = ui.get_root_geometry()
    root.geometry(geometry_s)

    ui.create_image("imgs/bg.png", 0.5, 0.5)
    basa = ui.create_image("imgs/basa.png", 0.5, 0.5)
    ui.create_image_on("imgs/x.png", basa, 0, 0)

    root.mainloop()
