from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import os
import sys
import StringIO

__author__ = 'konzy'
filters = [ImageFilter.BLUR, ImageFilter.EDGE_ENHANCE, ImageFilter.SMOOTH, ImageFilter.GaussianBlur,
           ImageFilter.SHARPEN, ImageFilter.DETAIL, ImageFilter.EDGE_ENHANCE_MORE]


def filter_image(image, i_filter):
    infile = image.filter(i_filter)
    f, e = os.path.splitext(inf)
    outfile = f + str(i_filter) + e

    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)


def string_to_image():
    return Image.open(StringIO.StringIO(buffer))


for inf in sys.argv[1:]:

    im = Image.open(inf)
    # noinspection PyTypeChecker
    for i in range(len(filters)):
        filter_image(inf, filters[i])
    contrast = ImageEnhance.Contrast(im)
    color = ImageEnhance.Color(im)
    contrast.enhance(1.3).show("30% More contrast")

    rotated = im.rotate(10)




# PIL Modes
# 1 (1-bit pixels, black and white, stored with one pixel per byte)
# L (8-bit pixels, black and white)
# P (8-bit pixels, mapped to any other mode using a color palette)
# RGB (3x8-bit pixels, true color)
# RGBA (4x8-bit pixels, true color with transparency mask)
# CMYK (4x8-bit pixels, color separation)
# YCbCr (3x8-bit pixels, color video format)
# LAB (3x8-bit pixels, the L*a*b color space)
# HSV (3x8-bit pixels, Hue, Saturation, Value color space)
# I (32-bit signed integer pixels)
# F (32-bit floating point pixels)
