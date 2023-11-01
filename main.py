from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ui import UI

if __name__ == '__main__':
    # Мб каждую клетку отдельно и 3 спрайта с пустым, иксом и ноликом
    root = Tk()
    root.title("Приложение на Tkinter")
    root.resizable(False, False)

    def quit():
        global root
        root.quit()

    ui = UI()
    geometry_s = ui.get_root_geometry()
    root.geometry(geometry_s)

    ui.create_image("imgs/bg.png", 640, 360)

    """
    for y in range(0, 180*3, 180):
        for x in range(0, 180 * 3, 180):
            ui.create_image("imgs/cell.png", 505 - 37.5 + x, 220 + y)
    """

    but = ui.create_button("imgs/person_choice.png", 467.5, 220)
    pic = ui.create_image("imgs/vs.png", 467.5 + 180, 220)
    ui.create_button("imgs/computer_choice.png", 467.5 + 180*2, 220)
    ui.create_button("imgs/play.png", 467.5 + 180, 220 + 180)
    ui.create_button("imgs/exit.png", 467.5 + 180, 220 + 180*2, quit)

    root.mainloop()
