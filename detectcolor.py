# import the necessary packages
import numpy as np
import cv2
import webcolors as wc
import sys
if sys.version_info[0] >= 3:
    unicode = str

def equivalencia(case):
    return {
            'aliceblue': "b",
            'antiquewhite': "w",
            'aquamarine': "g",
            'azure': "b",
            'beige': "y",
            'bisque': "o",
            'black': "b",
            'blanchedalmond': "o",
            'blue': "b",
            'blueviolet': "b",
            'brown': "r",
            'burlywood': "y",
            'cadetblue': "g",
            'chartreuse': "g",
            'chocolate': "o",
            'coral': "o",
            'cornflowerblue': "b",
            'cornsilk': "y",
            'crimson': "r",
            'cyan': "b",
            'darkblue': "b",
            'darkcyan': "g",
            'darkgoldenrod': "y",
            'darkgreen': "g",
            'darkgrey': "w",
            'darkgray': "w",
            'darkslategray': 'g',
            'darkkhaki': "y",
            'darkmagenta': "r",
            'darkolivegreen': "g",
            'darkorange': "o",
            'darkorchid': "r",
            'darkred': "r",
            'darksalmon': "o",
            'darkseagreen': "g",
            'darkslateblue': "b",
            'darkslategrey': "g",
            'darkturquoise': "b",
            'darkviolet': "r",
            'deeppink': "r",
            'deepskyblue': "b",
            'dimgrey': "w",
            'dodgerblue': "b",
            'firebrick': "r",
            'floralwhite': "w",
            'forestgreen': "g",
            'gainsboro': "w",
            'ghostwhite': "w",
            'gold': "y",
            'goldenrod': "o",
            'green': "g",
            'greenyellow': "y",
            'grey': "while",
            'honeydew': "w",
            'hotpink': "r",
            'indianred': "r",
            'indigo': "b",
            'ivory': "w",
            'khaki': "y",
            'lavender': "w",
            'lavenderblush': "w",
            'lawngreen': "g",
            'lemonchiffon': "y",
            'lightblue': "b",
            'lightcoral': "r",
            'lightcyan': "b",
            'lightgoldenrodyellow': "y",
            'lightgreen': "g",
            'lightgrey': "w",
            'lightpink': "w",
            'lightsalmon': "o",
            'lightseagreen': "g",
            'lightskyblue': "b",
            'lightslategrey': "b",
            'lightsteelblue': "b",
            'lightyellow': "y",
            'lime': "g",
            'limegreen': "g",
            'linen': "w",
            'magenta': "r",
            'maroon': "r",
            'mediumaquamarine': "b",
            'mediumblue': "b",
            'mediumorchid': "r",
            'mediumpurple': "r",
            'mediumseagreen': "g",
            'mediumslateblue': "b",
            'mediumspringgreen': "g",
            'mediumturquoise': "b",
            'mediumvioletred': "r",
            'midnightblue': "b",
            'mintcream': "w",
            'mistyrose': "r",
            'moccasin': "y",
            'navajowhite': "y",
            'navy': "b",
            'oldlace': "w",
            'olive': "g",
            'olivedrab': "g",
            'orange': "o",
            'orangered': "r",
            'orchid': "r",
            'palegoldenrod': "y",
            'palegreen': "g",
            'paleturquoise': "b",
            'palevioletred': "r",
            'papayawhip': "y",
            'peachpuff': "y",
            'peru': "o",
            'pink': "r",
            'plum': "r",
            'powderblue': "b",
            'purple': "r",
            'red': "r",
            'rosybrown': "o",
            'royalblue': "b",
            'saddlebrown': "o",
            'salmon': "r",
            'sandybrown': "o",
            'seagreen': "g",
            'seashell': "w",
            'sienna': "o",
            'silver': "w",
            'skyblue': "b",
            'slateblue': "b",
            'slategrey': "b",
            'snow': "w",
            'springgreen': "g",
            'steelblue': "b",
            'tan': "o",
            'teal': "g",
            'thistle': "w",
            'tomato': "o",
            'lightslategray': "w",
            'turquoise': "b",
            'violet': "b",
            'wheat': "y",
            'white': "w",
            'whitesmoke': "w",
            'yellow': "y",
            'yellowgreen': "y"}.get(case)

def get_approx_color(hex_color):
    orig = wc.hex_to_rgb(hex_color)
    similarity = {}
    for hex_code, color_name in wc.CSS3_HEX_TO_NAMES.items():
        approx = wc.hex_to_rgb(hex_code)
        similarity[color_name] = sum(np.subtract(orig, approx) ** 2)
    return min(similarity, key=similarity.get)


def detectarColores():
    print("Detectando colores de la cara")
    img = cv2.imread('imagen.jpg')

    # ----------------
    # | 0  | 1  | 2  |
    # ----------------
    # | 3  | 4  | 5  |
    # ----------------
    # | 6  | 7  | 8  |
    # ----------------
    #
    # # ----------------
    # | 6  | 3  | 0 |
    # ----------------
    # | 7  | 4  | 1  |
    # ----------------
    # | 8  | 5  | 2  |
    # ----------------

    colores = [
        [163, 204], # 0
        [248, 317], # 1
        [345, 320], # 2
        [174, 217], # 3
        [253, 219], # 4
        [352, 216], # 5
        [178,122 ], # 6
        [261, 119], # 7
        [355, 106]  # 8
    ]
    coloresRGB = []
    stringColores = ''
    for color in colores:
        roi_values = img[color[0] : color[0] + 30, color[1] : color[1] + 30]
        mean_blue = np.mean(roi_values[:,:,0])
        mean_green = np.mean(roi_values[:,:,1])
        mean_red = np.mean(roi_values[:,:,2])
        rgb = [mean_red, mean_green, mean_blue]
        coloresRGB.append(rgb)
        #cv2.imshow('image',roi_values)
        #cv2.waitKey(1000)
        #cv2.destroyAllWindows()
    for colorRGB in coloresRGB:
        hex = '#%02x%02x%02x' % (int(colorRGB[0]), int(colorRGB[1]), int(colorRGB[2]))
        name_color = get_approx_color(hex.upper())
        stringColor = equivalencia(name_color)
        if stringColor:
            stringColores = stringColores + '' + stringColor
    return stringColores
