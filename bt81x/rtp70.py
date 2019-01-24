# -*- coding: utf-8 -*-
# @Author: lorenzo
# @Date:   2018-11-15 10:51:15
# @Last Modified by:   lorenzo
# @Last Modified time: 2018-11-15 11:08:01

from bridgetek.bt81x import bt81x

bt81x.display_conf = bt81x.DisplayConf(
  800,     # width
  480,     # height
  1056,    # hcycle
  46,      # hoffset
  0,       # hsync0
  10,      # hsync1
  525,     # vcycle
  23,      # voffset
  0,       # vsync0
  10,      # vsync1
  2,       # pclk
  0,       # swizzle
  1,       # pclkpol
  0,       # cspread
  0,       # dither
  "Riverdi Resistive 7\"",
)