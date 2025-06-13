class Hand:
    def __init__(self, servos):
        self.pinky = servos[0]
        self.ring = servos[1]
        self.middle = servos[2]
        self.index = servos[3]
        self.thumb = servos[4]

