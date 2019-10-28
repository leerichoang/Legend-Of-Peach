

class Controller:
    """ Controller managers the players keyboard and mouse inputs """
    def __init__(self, hub):
        self.move_left = False
        self.move_right = False
        self.jump = False
        self.up = False

        self.developer_mode = True

        self.toggle_grid = False