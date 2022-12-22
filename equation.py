from utils import to_components, to_polar

with open("tests/test4.txt", "r") as f:
    contents = f.read().split('\n')
    mode = contents[0]
    contents = contents[1:]
contents = [tuple(map(int, i.split(" "))) for i in contents]
if mode == "components":
    for i, val in enumerate(contents):
        x, y = to_polar(val[0], val[1])
        contents[i] = (x, y, val[2])
print(contents)
