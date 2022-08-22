import numpy as np
import cv2 as cv

# Length of the tag in mm
aruco_length = 28

# Padding on one side of the tag in mm
padding = 1

# Width of margin on one side
margin = 10

# Number of rows/columns of aruco tags
rows = 4
cols = 5

# Starting id for tags (DICT_4X4_100)
start_id = 10

# Number of pixels for generating .pngs
aruco_pixels = 1024


def generate_aruco():
    aruco_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_100)
    for i in range(rows):
        for j in range(cols):
            id = start_id + (i * cols + j)
            tag = np.zeros((aruco_pixels, aruco_pixels, 1), dtype="uint8")
            cv.aruco.drawMarker(aruco_dict, id, aruco_pixels, tag)
            cv.imwrite(f"tags/tag_{id}.png", tag)
    with open('tags.svg', 'w+') as file:
        file.write(f'<svg width="100%" height="100%" viewBox="0 0 {2 * margin + cols * (aruco_length + 2 * padding)}mm {2 * margin + rows * (aruco_length + 2 * padding)}mm" version="1.1" xmlns="http://www.w3.org/2000/svg">')
        file.write(f'\t<rect width="{2 * margin + cols * (aruco_length + 2 * padding)}mm" height="{2 * margin + rows * (aruco_length + 2 * padding)}mm" x="0mm" y="0mm" fill-opacity="0" stroke-width="0.5mm" stroke="black"/>\n')
        file.write("\n")
        for i in range(rows):
            for j in range(cols):
                file.write(f'\t<rect width="{aruco_length + 2 * padding}mm" height="{aruco_length + 2 * padding}mm" x="{margin + j * (aruco_length + 2 * padding)}mm" y="{margin + i * (aruco_length + 2 * padding)}mm" fill-opacity="0" stroke-width="0.2mm" stroke="black" stroke-dasharray="1 2"/>\n')

        for i in range(rows):
            for j in range(cols):
                file.write(f'\t<image x="{margin + padding + j * (aruco_length + 2 * padding)}mm" y="{margin + padding + i * (aruco_length + 2 * padding)}mm" width="{aruco_length}mm" height="{aruco_length}mm" href="tags/tag_{start_id + (i * cols + j)}.png" />\n')
        file.write(r'</svg>')



if __name__ == "__main__":
    generate_aruco()