class Obj:
    elem = None
    pos = {'x': 0, 'y': 0}
    img = None
    path = ""
    command = None
    args = None

    def __init__(self, elem, pos, img, path, command=None, *args):
        self.elem = elem
        self.pos = pos
        self.img = img
        self.path = path
        self.command = command
        self.args = args
