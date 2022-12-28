import re

class Reader:
    def __init__(self, file, resolution=0.01):
        self.filename = file
        self.tracedPath = []
        self.resolution = resolution

    def __getFile(self):
        f = open(self.filename)
        self.file_info = f.readlines()
        f.close()

    def __getPath(self):
        # for i in range(len(self.file_info)):
            # splits.append(self.file_info[i].split("<path"))
        temp = re.findall("<path.*\" ", self.file_info[0])
        splits = re.search("d=.*", temp[0])
        splits_str = (str(splits.group()).split(" ", maxsplit=1))[1]
        splits_str = (splits_str.split("\"", maxsplit=1))[0]
        self.path_str = splits_str

    def convertToPath(self):
        self.__getFile()
        self.__getPath()
        
        self.path = self.path_str.split()

        tracedPath = []
        coord1 = [0, 0]
        coord2 = [0, 0]
        coord3 = [0, 0]
        command = 'M'

        i = 0;
        while(i < len(self.path)):
            if(not self.path[i].replace('.','',1).isdigit()):
                command = self.path[i]
                j_temp = 1;
            else:
                j_temp = 0;

            # if(command == 'Z'):
            #     break;

            if(command == 'M'):
                coord1[0] = float(self.path[i+(j_temp)])
                coord1[1] = float(self.path[i+(j_temp*2)])
                tracedPath.append([coord1[0], coord1[1]])
                i+=2;

            elif(command == 'Q'):
                coord2[0] = float(self.path[i+(j_temp)])
                coord2[1] = float(self.path[i+(j_temp*2)])
                coord3[0] = float(self.path[i+(j_temp*3)])
                coord3[1] = float(self.path[i+(j_temp*4)])

                t = 0;
                while(t < 0.999):
                    t += self.resolution
                    x = ((1-t)*(((1-t)*coord1[0])+(t*coord2[0]))) + (t*(((1-t)*coord2[0])+(t*coord3[0])))
                    y = ((1-t)*(((1-t)*coord1[1])+(t*coord2[1]))) + (t*(((1-t)*coord2[1])+(t*coord3[1])))
                    tracedPath.append([x, y])

                coord1[0] = coord3[0]
                coord1[1] = coord3[1]

                i+=4;

            elif(command == 'L'):
                coord2[0] = float(self.path[i+(j_temp)])
                coord2[1] = float(self.path[i+(j_temp*2)])

                t = 0;
                while(t < 0.999):
                    t += self.resolution
                    x = (((1-t)*coord1[0]) + ((t)*coord2[0]))
                    y = (((1-t)*coord1[1]) + ((t)*coord2[1]))
                    tracedPath.append([x, y])

                coord1[0] = coord2[0]
                coord1[1] = coord2[1]
                i+=2;

            i+=1;
        
            
        self.tracedPath = tracedPath