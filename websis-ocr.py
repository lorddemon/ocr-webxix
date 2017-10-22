#!/usr/bin/python

from pytesseract import image_to_string
from PIL import Image,ImageFilter
import re
import sys
import argparse


if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('path',help = 'Path del la imagen')
    args = argparser.parse_args()
    path = args.path

    img = Image.open(path)
    img = img.convert("RGBA")

    #Definiendo Variables
    pixel = img.load()


    ancho = img.size[0]
    alto = img.size[1]

    altom = img.size[1] * 0.78


    #Coloreando solo Letras lo Demas se Borra
    for y in xrange(alto):
        for x in xrange(ancho):
            if (pixel[x, y][0] > 170) and (pixel[x, y][1] > 220) and (pixel[x, y][2] < 250):
                pixel[x, y] = (0, 0, 0, 255)
            else:
                pixel[x, y] = (255, 255, 255, 255)
    for y in xrange(int(altom),alto):
        for x in xrange(ancho):
            pixel[x, y] = (255, 255, 255, 255)


    #Guardando en Blanco y Negro
    img.save("bn.gif", "GIF")
    print "Opcion 1: ",
    text1 = image_to_string(img)
    salida1 = re.sub('\W+','', text1 )
    print salida1

    im_orig = Image.open('bn.gif')
    porcentaje = 2

    big = im_orig.resize((ancho * porcentaje,alto * porcentaje), Image.NEAREST)
    ext = ".tif"
    big.save("salida2" + ext)
        
    #   Perform OCR using tesseract-ocr library


    image = Image.open('salida2.tif')
    img.filter(ImageFilter.EDGE_ENHANCE)
    print "Opcion 2: ",
    text = image_to_string(image)
    salida2 = re.sub('\W+','', text )
    print salida2