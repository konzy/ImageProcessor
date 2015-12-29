__author__ = 'konzy'

from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import os, sys

#import StringIO #reading from a string

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    im = Image.open(infile)
    #im = Image.open(StringIO.StringIO(buffer))
    blurred = im.filter(ImageFilter.BLUR)

    enh = ImageEnhance.Contrast(im)
    enh.enhance(1.3).show("30% More contrast")


    outfile = f + 'aug' + e
    rotated = im.rotate(10)


    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)

#PIL Modes
#1 (1-bit pixels, black and white, stored with one pixel per byte)
#L (8-bit pixels, black and white)
#P (8-bit pixels, mapped to any other mode using a color palette)
#RGB (3x8-bit pixels, true color)
#RGBA (4x8-bit pixels, true color with transparency mask)
#CMYK (4x8-bit pixels, color separation)
#YCbCr (3x8-bit pixels, color video format)
#LAB (3x8-bit pixels, the L*a*b color space)
#HSV (3x8-bit pixels, Hue, Saturation, Value color space)
#I (32-bit signed integer pixels)
#F (32-bit floating point pixels)