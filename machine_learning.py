from equation import Equation
from to_image import draw

eqn = Equation(filename='test.txt')
buffer = eqn.get_buffer(100)
with open("output.txt", "w") as f:
    output = ""
    for x, y in buffer:
        output += f"{x} {y}\n"
    output = output[:-1]
    f.write(output)

draw()
