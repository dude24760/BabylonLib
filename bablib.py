import random
from PIL import Image
import itertools

mode = "1"
res = (100, 100)

def rand():
    return random.randint(0, 1)

def create_image(a):
    img = Image.new("1", res)
    pixels = img.load()
    p = next(a)
    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            pixels[x,y] = (p[x][y])
    return img

def generate_image(n):
    for i in range(1<<n):
        s=bin(i)[2:]
        s='0'*(n-len(s))+s
        f = list(map(int,list(s)))
        f = [f[i:i+100] for i in range(0, len(f), 100)]
        yield f
def permute(original):
    a = list(original)
    first_swap = True
    perms = []
    pointer = len(a) - 1
    while a != original or first_swap:
        if pointer == 0:
            tmp = a[pointer]
            a[pointer] = a[len(a)-1]
            a[len(a)-1] = tmp
            b = list(a)
            perms.append(b)
            pointer = len(a) - 1
        else:
            tmp = a[pointer]
            a[pointer] = a[pointer-1]
            a[pointer-1] = tmp
            b = list(a)
            perms.append(b)
            pointer -= 1
        first_swap = False
    a = a[:-1]
    return perms

a = generate_image(10000)

img = create_image(a)
img.show()
input()
img = create_image(a)
img.show()
