from gameturtle import splitgif

b = splitgif('aniam.gif')

print(b)
i = 0
for pic in b[0]:
    fi = "f/" + str(i) + ".png"
    pic.save(fi)
    i= i + 1 
