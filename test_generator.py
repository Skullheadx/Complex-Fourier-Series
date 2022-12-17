import random

def generate():
    output = ""
    for _ in range(random.randint(1,100)):
        output += f"{random.randint(1,100)} {random.randint(0,360)} {random.randint(0,50)}\n"

    return output[:-1]

for i in range(10):
    with open(f"tests/test{i+1}.txt","w") as f:
        f.write(generate())