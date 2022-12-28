from svg_to_path import Reader


folder = './svgs/'
filename = 'test3.svg'
reader = Reader(folder + filename, 0.01);

reader.convertToPath()

f = open(f"./paths/{filename.split('.')[0]}.txt", 'w')
[f.writelines(str(i) + "\n") for i in reader.tracedPath]
f.close()

# import matplotlib.pyplot as plt
# x, y = zip(*reader.tracedPath)
# plt.scatter(x, y)
# plt.show()
