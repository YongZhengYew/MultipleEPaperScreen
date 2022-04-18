#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd4in2b_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd4in2b_V2 Demo")
    
    epd0 = epd4in2b_V2.EPD(17,25,8,24,0)
    epd1 = epd4in2b_V2.EPD(3,2,18,4,1)
    logging.info("init and Clear")
    epd0.init()
    epd0.Clear()
    epd1.init()
    epd1.Clear()
    time.sleep(1)
    
    # Drawing on the image
    logging.info("Drawing")    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    
    # Drawing on the Horizontal image
    
    # Drawing on the Vertical image
    logging.info("2.Drawing on the Vertical image...")
    LBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 126*298
    LRYimage = Image.new('1', (epd.height, epd.width), 255)  # 126*298
    drawblack = ImageDraw.Draw(LBlackimage)
    drawry = ImageDraw.Draw(LRYimage)
    
    drawblack.text((2, 0), 'hello world', font = font18, fill = 0)
    drawblack.text((2, 20), '4.2inch epd bc', font = font18, fill = 0)
    drawblack.text((20, 50), u'微雪电子', font = font18, fill = 0)
    drawblack.line((10, 90, 60, 140), fill = 0)
    drawblack.line((60, 90, 10, 140), fill = 0)
    drawblack.rectangle((10, 90, 60, 140), outline = 0)
    drawry.line((95, 90, 95, 140), fill = 0)
    drawry.line((70, 115, 120, 115), fill = 0)
    drawry.arc((70, 90, 120, 140), 0, 360, fill = 0)
    drawry.rectangle((10, 150, 60, 200), fill = 0)
    drawry.chord((70, 150, 120, 200), 0, 360, fill = 0)
    epd0.display(epd0.getbuffer(LBlackimage), epd0.getbuffer(LRYimage))
    epd1.display(epd1.getbuffer(LBlackimage), epd1.getbuffer(LRYimage))
    time.sleep(2)
    
    logging.info("Clear...")
    epd0.init()
    epd0.Clear()
    epd1.init()
    epd1.Clear()
    
    logging.info("Goto Sleep...")
    epd0.sleep()
    epd1.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in2b_V2.epdconfig.module_exit()
    exit()
