colors = ["black", "white"]
sizes = ["S", "M", "L"]
# 先以颜色排列,在以尺码排列
tshirts = ((color, size) for color in colors for size in sizes)
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))

# 先以尺码排列,在以颜色排列
tshirts1 = [(color, size) for size in sizes for color in colors]
print(tshirts1)
