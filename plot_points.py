from svg_to_path import Reader

class svgToPath():
    
    def __init__(self, path):
        self.folder = ''
        self.filename = path.split('/')[-1]
        for i in path.split('/')[:-1]:
            self.folder += i + '/';

    def convert(self):
        self.reader = Reader(self.folder + self.filename, 0.01);
        self.reader.convertToPath()

    def writeToFile(self, path=''):
        if(path == ''):
            f = open(f"./paths/{self.filename.split('.')[0]}.txt", 'w')
            [f.writelines(str(i) + "\n") for i in self.reader.tracedPath]
            f.close()
        else:
            f = open(f"{path}", 'w')
            [f.writelines(str(i) + "\n") for i in self.reader.tracedPath]
            f.close()


class readFromPath():
    def __init__(self, file):
        self.pathCoords = []

        f = open(file, 'r')
        for i in range(sum(1 for j in open(file))):
            temp = f.readline()[1:-2].split(",")
            self.pathCoords.append([float(temp[0]), float(temp[1])])
        f.close()