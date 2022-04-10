import imageio

def makegif(path,filename):    
   
   images = [f'res/{i}.png' for i in range(0,1440,30)]   
   frames = [imageio.imread(image) for image in images]
   imageio.mimsave(filename, frames, 'GIF', duration=0.1) 
    
if __name__ == "__main__":

    makegif("out","太极.gif")
    print("合成gif完毕.")


