from tqdm import tqdm
from PIL import Image
import numpy as np
import json

im = Image.open("./images/randomimage.jpg")
width, height = im.size
print(im.size)
arr = np.array(im)

R = arr[:, :, 0]
G = arr[:, :, 1]
B = arr[:, :, 2]

colors = {'data': []}
sorted_colors = {'data': []}


def has_color(list, value):
    for item in list:
        if item["rgb"] == value:
            return True
    return False


def add_color_count(list, value):
    for item in list:
        if item["rgb"] == value:
            item["count"] += 1


print("Gathering colors")
for i in tqdm(range(0, height)):
    for j in range(0, width):
        red = R[i][j]
        green = G[i][j]
        blue = B[i][j]

        # Cast because we cannot convert to JSON with numpy.uint8 type
        color = (int(red), int(green), int(blue))

        if has_color(colors['data'], color):
            add_color_count(colors['data'], color)
        else:
            colors['data'].append({"rgb": color, "count": 1})

sorted_list = sorted(colors['data'], key=lambda x: x["count"], reverse=True)
sorted_colors['data'] = sorted_list

json_object = json.dumps(sorted_colors, indent=4)
with open("randomimage.json", "w") as outfile:
    outfile.write(json_object)


# print(len(sorted_colors_by_count))

# filtered_sorted = sorted_colors_by_count[:]
# filtered_sorted = filtered_sorted.remove(lambda x: x.count == 1)


# def color_is_different(arr, color, diff_range):
#     for item in arr:
#         if item['rgb'] != color['rgb']:
#             rdiff = item['rgb'][0] - color['rgb'][0] >= diff_range or item['rgb'][0] - color['rgb'][0] <= diff_range
#             gdiff = item['rgb'][1] - color['rgb'][1] >= diff_range or item['rgb'][1] - color['rgb'][1] <= diff_range
#             bdiff = item['rgb'][2] - color['rgb'][2] >= diff_range or item['rgb'][2] - color['rgb'][2] <= diff_range
#             if rdiff or gdiff or bdiff:
#                 return (True, item)
        
#     return (False, None)

# top_colors = []
# diff_range = 10
# for index, sorted_color in enumerate(sorted_colors_by_count):
#     if index == 0:
#         top_colors.append(sorted_color)
#         print(sorted_color)
#     else:
#         is_different, top_color = color_is_different(top_colors, sorted_color, 10)
#         if is_different:
#             print(sorted_color, top_color)
            

# print(len(top_colors))
# print(top_colors)