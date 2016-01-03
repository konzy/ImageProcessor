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


def string_to_image():
    return Image.open(StringIO.StringIO(buffer))

factor = 1.1
for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)

    try:
        blur = Image.open(infile)
        blur = blur.filter(ImageFilter.BLUR)
        outfile = f + "blur_" + e
        blur.save(outfile)
    except IOError:
        print("cannot apply filter blur", infile)

    im = Image.open(infile)
    degrees = (factor - 1) * 100
    enhancements[0][0] = ImageEnhance.Contrast(im).enhance(factor)
    enhancements[1][0] = "contrast"
    enhancements[0][1] = ImageEnhance.Color(im).enhance(factor)
    enhancements[1][1] = "color"
    enhancements[0][2] = im.rotate(degrees)
    enhancements[1][2] = "rotate_positive"
    enhancements[0][3] = im.rotate(-degrees)
    enhancements[1][3] = "rotate_negative"

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
