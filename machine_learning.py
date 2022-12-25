from equation import Equation
from to_image import draw
from match import image_to_list, match

eqn = Equation(filename='test.txt')
buffer = eqn.get_buffer(100)

image = image_to_list("images/circle.png")

print(f"Image matches {match(image,buffer) * 100}%")

# write x,y coordinates to file for displaying
with open("output.txt", "w") as f:
    output = ""
    for x, y in buffer:
        output += f"{x} {y}\n"
    output = output[:-1]
    f.write(output)

draw()
