from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import os
import sys
import StringIO

__author__ = 'konzy'
filters = [ImageFilter.BLUR, ImageFilter.EDGE_ENHANCE, ImageFilter.SMOOTH, ImageFilter.GaussianBlur,
           ImageFilter.SHARPEN, ImageFilter.DETAIL, ImageFilter.EDGE_ENHANCE_MORE]
enhancements = [[""]*10 for i in range(2)]


def filter_image(image, i_filter):
    infile = image.filter(i_filter)
    f, e = os.path.splitext(inf)
    outfile = f + str(i_filter) + e

    try:
        Image.open(infile).save(outfile)
    except IOError:
        print("cannot convert", infile)


def string_to_image():
    return Image.open(StringIO.StringIO(buffer))


factor = 1.1
for inf in sys.argv[1:]:

    im = Image.open(inf)
    for i in range(len(filters)):
        filter_image(inf, filters[i])

    degrees = (factor - 1) * 100
    enhancements[0][0] = ImageEnhance.Contrast(im).enhance(factor)
    enhancements[0][1] = "contrast"

    color = ImageEnhance.Color(im).enhance(factor)
    rotatedPos = im.rotate(degrees)
    rotatedNeg = im.rotate(-degrees)




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
