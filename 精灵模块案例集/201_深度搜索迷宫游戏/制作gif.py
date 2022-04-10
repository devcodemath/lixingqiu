from PIL import Image
from gameturtle import makegif

frames = [f"frames/{i}.png" for i in range(62)]
frames = [Image.open(im) for im in frames]

gif = makegif(frames,'bug走迷宫.gif')
