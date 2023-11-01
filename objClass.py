class Obj:
    elem = None
    pos = {'x': 0, 'y': 0}
    img = None

    def __init__(self, elem, pos, img):
        self.elem = elem
        self.pos = pos
        self.img = img