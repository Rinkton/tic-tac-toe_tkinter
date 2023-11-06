from tkinter import *
from ui import UI
from field import Field
import win_checker


class Game:

    frame = None
    ui = None
    root = None
    first_is_person = False
    second_is_person = False
    is_the_first_player_move = True
    field = None

    def __init__(self, root, first_is_person, second_is_person):
        self.root = root
        self.first_is_person = first_is_person
        self.second_is_person = second_is_person
        self.field = Field()

    def back_to_menu(self):
        self.frame.pack_forget()
        self.frame.destroy()

    def put(self, x, y):
        obj = self.field.cells[y][x]
        if self.its_putted(obj):
            return
        obj = self.ui.change_button(obj, "imgs/x.png" if self.is_the_first_player_move else "imgs/o.png")
        self.field.cells[y][x] = obj
        self.is_the_first_player_move = not self.is_the_first_player_move
        winner = win_checker.who_won(self.field)
        if winner != None:
            if winner == "first":
                self.ui.create_image("imgs/x-win.png", 467.5 + 180, 65)
            elif winner == "second":
                self.ui.create_image("imgs/o-win.png", 467.5 + 180, 65)
        # Останови все взаимодействия, чтобы пользователь перешёл обратно... а потом надо всё тут будет обнулить, чтобы ещё играть можно было

    def its_putted(self, obj):
        return obj.path == "imgs/x.png" or obj.path == "imgs/o.png"

    def on_cell_button_enter(self, event):
        obj, x, y = self.field.find_obj_by_widget(event.widget)
        if self.its_putted(obj):
            return
        obj = self.ui.change_button(obj, "imgs/x-to-put.png" if self.is_the_first_player_move else "imgs/o-to-put.png")
        self.field.cells[y][x] = obj
        for row in self.field.cells:
            for cell in row:
                if cell != self.field.cells[y][x]:
                    cell.elem.event_generate("<Leave>")
        obj.elem.bind('<Leave>', self.on_cell_button_leave)

    def on_cell_button_leave(self, event):
        obj, x, y = self.field.find_obj_by_widget(event.widget)
        if self.its_putted(obj):
            return
        obj = self.ui.change_button(obj, "imgs/cell.png")
        self.field.cells[y][x] = obj
        obj.elem.bind('<Enter>', self.on_cell_button_enter)

    def main(self):
        self.frame = Frame()
        self.frame.place(x=0, y=0)
        self.frame.pack(fill='both', expand=1)
        self.ui = UI(self.frame)

        self.ui.create_image("imgs/bg.png", 640, 360)
        for y in range(3):
            for x in range(3):
                cell_button = self.ui.create_button(
                    "imgs/cell.png", 467.5 + 180 * x, 220 + 180 * y, self.put, x, y)
                self.field.cells[y][x] = cell_button
                cell_button.elem.bind('<Enter>', self.on_cell_button_enter)
        self.ui.create_button("imgs/back.png", 90, 90, self.back_to_menu)

        self.root.mainloop()