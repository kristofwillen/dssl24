import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Droneloader:

    def __init__(self, filename):
        self.path = "/code/dssl24/UAV/val"
        labelname = filename.split('.')[0] + '.txt'
        self.img = mpimg.imread(f"{self.path}/images/{filename}")
        with open(f"{self.path}/labels/{labelname}", 'r') as f:
            data = f.readlines()
            c, sx, sy, ex, ey = data[0].split(' ')

        self.width = self.img.shape[1]
        self.height = self.img.shape[0]

        self.sx = int(float(sx)*self.width)
        self.sy = int(float(sy)*self.height)
        self.ex = int(float(ex)*self.width)
        self.ey = int(float(ey)*self.height)


    def draw(self):
        plt.imshow(self.img)

    def drawbb(self):
        fig, ax = plt.subplots()
        ax.imshow(self.img)

        rect = patches.Rectangle((self.sx, self.sy), self.ex, self.ey, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

        plt.show()

    def rewrite_label_file(self):
        raise NotImplementedError



if __name__ == "__main__":
    t = Droneloader('chiang-mai-thailand-jan-23-260nw-446130538.jpg')
    t.drawbb()
