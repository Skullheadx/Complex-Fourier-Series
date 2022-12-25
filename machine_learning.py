from equation import Equation
from to_image import draw
from match import image_to_list

eqn = Equation(filename='test.txt')
buffer = eqn.get_buffer(100)

image = image_to_list("images/circle.png")

# write x,y coordinates to file for displaying
with open("output.txt", "w") as f:
    output = ""
    for x, y in buffer:
        print(x,y)
        output += f"{x} {y}\n"
    output = output[:-1]
    f.write(output)

draw()
