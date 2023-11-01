from tkinter import *
from ui import UI
from game import Game


def play():
    global root, first_player, second_player
    game = Game(root, first_player.path == "imgs/person_choice.png", second_player.path == "imgs/person_choice.png")
    game.main()

def quit():
    global root
    root.quit()

def change_player(player):
    if player.path == "imgs/person_choice.png":
        player = ui.change_button(player, "imgs/computer_choice.png")
    else:
        player = ui.change_button(player, "imgs/person_choice.png")
    return player

def change_first():
    global first_player
    first_player = change_player(first_player)

def change_second():
    global second_player
    second_player = change_player(second_player)


if __name__ == '__main__':
    root = Tk()
    root.title("Приложение на Tkinter")
    root.resizable(False, False)

    ui = UI()
    geometry_s = ui.get_root_geometry()
    root.geometry(geometry_s)

    ui.create_image("imgs/bg.png", 640, 360)

    """
    for y in range(0, 180*3, 180):
        for x in range(0, 180 * 3, 180):
            ui.create_image("imgs/cell.png", 505 - 37.5 + x, 220 + y)
    """

    first_player = ui.create_button("imgs/person_choice.png", 467.5, 220, change_first)
    ui.create_image("imgs/vs.png", 467.5 + 180, 220)
    second_player = ui.create_button("imgs/computer_choice.png", 467.5 + 180*2, 220, change_second)
    ui.create_button("imgs/play.png", 467.5 + 180, 220 + 180, play)
    ui.create_button("imgs/exit.png", 467.5 + 180, 220 + 180*2, quit)

    root.mainloop()
