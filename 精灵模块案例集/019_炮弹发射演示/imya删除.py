from sprites import Sprite

while True:
    sps = [Sprite() for i in range(50)]
    [x.randompos() for x in sps]
    [x.remove() for x in sps]

