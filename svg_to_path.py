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
        splits_str = (str(splits.group()).replace("d=\"", ""))
        splits_str = (splits_str.replace("\"", ""))
        self.path_str = splits_str.replace(",", " ")

    def convertToPath(self):
        self.__getFile()
        self.__getPath()
        
        self.path = self.path_str.split()

        tracedPath = []
        coord1 = [0, 0]
        coord2 = [0, 0]
        coord3 = [0, 0]
        last_control_point_q = [0, 0]
        last_control_point_c = [0, 0]
        command = 'M'

        i = 0;
        while(i < len(self.path)):
            if(not self.path[i].replace('.','',1).isdigit()):
                command = self.path[i]
                j_temp = 1;
            else:
                j_temp = 0;

            if(command == 'Z'):
                coord1 = [0, 0]
                coord2 = [0, 0]
                coord3 = [0, 0]

            if(command == 'M'):
                coord1[0] = float(self.path[i+(j_temp)])
                coord1[1] = float(self.path[i+(j_temp+1)])
                tracedPath.append([coord1[0], coord1[1]])
                i+=2;

            elif(command == 'm'):
                coord1[0] += float(self.path[i+(j_temp)])
                coord1[1] += float(self.path[i+(j_temp+1)])
                tracedPath.append([coord1[0], coord1[1]])
                i+=2;

            elif(command == 'Q' or command == 'q'):
                if(command == 'Q'):
                    coord2[0] = float(self.path[i+(j_temp)])
                    coord2[1] = float(self.path[i+(j_temp+1)])
                    coord3[0] = float(self.path[i+(j_temp+2)])
                    coord3[1] = float(self.path[i+(j_temp+3)])
                elif(command == 'q'):
                    coord2[0] = coord1[0] + float(self.path[i+(j_temp)])
                    coord2[1] = coord1[1] + float(self.path[i+(j_temp+1)])
                    coord3[0] = coord1[0] + float(self.path[i+(j_temp+2)])
                    coord3[1] = coord1[1] + float(self.path[i+(j_temp+3)])

                last_control_point_q = [coord2[0]-coord1[0], coord2[1]-coord1[1]];

                t = 0;
                while(t < 0.999):
                    t += self.resolution
                    x = ((1-t)*(((1-t)*coord1[0])+(t*coord2[0]))) + (t*(((1-t)*coord2[0])+(t*coord3[0])))
                    y = ((1-t)*(((1-t)*coord1[1])+(t*coord2[1]))) + (t*(((1-t)*coord2[1])+(t*coord3[1])))
                    tracedPath.append([x, y])

                coord1[0] = coord3[0]
                coord1[1] = coord3[1]

                i+=4;

            elif(command == 'T' or command == 't'):
                if(command == 'T'):
                    coord3[0] = float(self.path[i+(j_temp)])
                    coord3[1] = float(self.path[i+(j_temp+1)])
                elif(command == 't'):
                    coord3[0] = coord1[0] + float(self.path[i+(j_temp)])
                    coord3[1] = coord1[1] + float(self.path[i+(j_temp+1)])

                last_control_point_q[1] = last_control_point_q[1]*-1
                coord2[0] = last_control_point_q[0]+coord1[0]
                coord2[1] = last_control_point_q[1]+coord1[1]

                t = 0;
                while(t < 0.999):
                    t += self.resolution
                    x = ((1-t)*(((1-t)*coord1[0])+(t*coord2[0]))) + (t*(((1-t)*coord2[0])+(t*coord3[0])))
                    y = ((1-t)*(((1-t)*coord1[1])+(t*coord2[1]))) + (t*(((1-t)*coord2[1])+(t*coord3[1])))
                    tracedPath.append([x, y])

                coord1[0] = coord3[0]
                coord1[1] = coord3[1]

                i+=2;

            elif(command == 'L' or command == 'l'):
                if(command == 'L'):
                    coord2[0] = float(self.path[i+(j_temp)])
                    coord2[1] = float(self.path[i+(j_temp+1)])
                elif(command == 'l'):
                    coord2[0] = float(coord1[0]) + float(self.path[i+(j_temp)])
                    coord2[1] = float(coord1[1]) + float(self.path[i+(j_temp+1)])

                t = 0;
                while(t < 0.999):
                    t += self.resolution
                    x = (((1-t)*coord1[0]) + ((t)*coord2[0]))
                    y = (((1-t)*coord1[1]) + ((t)*coord2[1]))
                    tracedPath.append([x, y])

                coord1[0] = coord2[0]
                coord1[1] = coord2[1]
                i+=2;

            elif(command == 'H' or command == 'h' or command == 'V' or command == 'v'):
                if(command == 'H'):
                    coord2[0] = float(self.path[i+(j_temp)])
                    coord2[1] = coord1[1]
                elif(command == 'h'):
                    coord2[0] = coord1[0] + float(self.path[i+(j_temp)])
                    coord2[1] = coord1[1]
                elif(command == 'V'):
                    coord2[0] = coord1[0]
                    coord2[1] = float(self.path[i+(j_temp)])
                elif(command == 'v'):
                    coord2[0] = coord1[0]
                    coord2[1] = coord1[1] + float(self.path[i+(j_temp)])
                
                t = 0;
                while(t < 0.999):
                    t += self.resolution
                    x = (((1-t)*coord1[0]) + ((t)*coord2[0]))
                    y = (((1-t)*coord1[1]) + ((t)*coord2[1]))
                    tracedPath.append([x, y])

                coord1[0] = coord2[0]
                coord1[1] = coord2[1]
                i+=1;

            elif(command == 'C' or command == 'c'):
                coord4 = [0, 0]
                coord5 = [0, 0]
                coord6 = [0, 0]
                coord7 = [0, 0]

                if(command == 'C'):
                    coord4[0] = coord1[0]
                    coord4[1] = coord1[1]
                    coord5[0] = float(self.path[i+(j_temp)])
                    coord5[1] = float(self.path[i+(j_temp+1)])
                    coord6[0] = float(self.path[i+(j_temp+2)])
                    coord6[1] = float(self.path[i+(j_temp+3)])
                    coord7[0] = float(self.path[i+(j_temp+4)])
                    coord7[1] = float(self.path[i+(j_temp+5)])
                elif(command == 'c'):
                    coord4[0] = coord1[0]
                    coord4[1] = coord1[1]
                    coord5[0] = coord4[0] + float(self.path[i+(j_temp)])
                    coord5[1] = coord4[1] + float(self.path[i+(j_temp+1)])
                    coord6[0] = coord4[0] + float(self.path[i+(j_temp+2)])
                    coord6[1] = coord4[1] + float(self.path[i+(j_temp+3)])
                    coord7[0] = coord4[0] + float(self.path[i+(j_temp+4)])
                    coord7[1] = coord4[1] + float(self.path[i+(j_temp+5)])

                last_control_point_c = [coord6[0]-coord7[0], coord6[1]-coord7[1]]

                t = 0;
                while(t < 0.999):
                    t += self.resolution

                    coord1[0] = ((((1-t)*coord4[0])+(t*coord5[0])))
                    coord1[1] = ((((1-t)*coord4[1])+(t*coord5[1])))
                    coord2[0] = ((((1-t)*coord5[0])+(t*coord6[0])))
                    coord2[1] = ((((1-t)*coord5[1])+(t*coord6[1])))
                    coord3[0] = ((((1-t)*coord6[0])+(t*coord7[0])))
                    coord3[1] = ((((1-t)*coord6[1])+(t*coord7[1])))

                    x = ((1-t)*(((1-t)*coord1[0])+(t*coord2[0]))) + (t*(((1-t)*coord2[0])+(t*coord3[0])))
                    y = ((1-t)*(((1-t)*coord1[1])+(t*coord2[1]))) + (t*(((1-t)*coord2[1])+(t*coord3[1])))
                    tracedPath.append([x, y])

                coord1[0] = coord7[0]
                coord1[1] = coord7[1]

                i+=6;

            elif(command == 'S' or command == 's'):
                coord4 = [0, 0]
                coord5 = [0, 0]
                coord6 = [0, 0]
                coord7 = [0, 0]

                if(command == 'S'):
                    coord4[0] = coord1[0]
                    coord4[1] = coord1[1]
                    coord5[0] = coord4[0] + last_control_point_c[0]*-1
                    coord5[1] = coord4[1] + last_control_point_c[1]*-1
                    coord6[0] = float(self.path[i+(j_temp)])
                    coord6[1] = float(self.path[i+(j_temp+1)])
                    coord7[0] = float(self.path[i+(j_temp+2)])
                    coord7[1] = float(self.path[i+(j_temp+3)])
                elif(command == 's'):
                    coord4[0] = coord1[0]
                    coord4[1] = coord1[1]
                    coord5[0] = coord4[0] + last_control_point_c[0]*-1
                    coord5[1] = coord4[1] + last_control_point_c[1]*-1
                    coord6[0] = coord4[0] + float(self.path[i+(j_temp)])
                    coord6[1] = coord4[1] + float(self.path[i+(j_temp+1)])
                    coord7[0] = coord4[0] + float(self.path[i+(j_temp+2)])
                    coord7[1] = coord4[1] + float(self.path[i+(j_temp+3)])

                t = 0;
                while(t < 0.999):
                    t += self.resolution

                    coord1[0] = ((((1-t)*coord4[0])+(t*coord5[0])))
                    coord1[1] = ((((1-t)*coord4[1])+(t*coord5[1])))
                    coord2[0] = ((((1-t)*coord5[0])+(t*coord6[0])))
                    coord2[1] = ((((1-t)*coord5[1])+(t*coord6[1])))
                    coord3[0] = ((((1-t)*coord6[0])+(t*coord7[0])))
                    coord3[1] = ((((1-t)*coord6[1])+(t*coord7[1])))

                    x = ((1-t)*(((1-t)*coord1[0])+(t*coord2[0]))) + (t*(((1-t)*coord2[0])+(t*coord3[0])))
                    y = ((1-t)*(((1-t)*coord1[1])+(t*coord2[1]))) + (t*(((1-t)*coord2[1])+(t*coord3[1])))
                    tracedPath.append([x, y])

                coord1[0] = coord7[0]
                coord1[1] = coord7[1]

                i+=5;

            i+=j_temp;
        
            
        self.tracedPath = tracedPath