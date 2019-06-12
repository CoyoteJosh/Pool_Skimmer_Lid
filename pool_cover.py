#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *

SEGMENTS = 60

def assembly():
    outer_sleeve_height = 13
    outer_sleeve_radius = 125
    inner_sleeve_radius = 114.3
    distance_from_outside_to_brace = 8
    top_thickness = 10

    outer = cylinder(outer_sleeve_radius, outer_sleeve_height)
    inner = cylinder(inner_sleeve_radius, outer_sleeve_height)
    lip = cylinder(inner_sleeve_radius + distance_from_outside_to_brace, top_thickness)
    cover_sleeve = outer - hole()(inner)
    cover_sleeve_with_lip = cover_sleeve - lip

    return cover_sleeve_with_lip * cube(outer_sleeve_radius, outer_sleeve_height)

def assembly_2():
    outer_sleeve_height = 13
    outer_sleeve_radius = 125
    inner_sleeve_radius = 114.3
    distance_from_outside_to_brace = 8
    top_thickness = 10

    base = cylinder(outer_sleeve_radius + 25, outer_sleeve_height - 10)
    lid_holder = cylinder(outer_sleeve_radius, outer_sleeve_height) - hole()(cylinder(inner_sleeve_radius, outer_sleeve_height))
    lip = cylinder(inner_sleeve_radius + distance_from_outside_to_brace, top_thickness)
    return ((base + down(outer_sleeve_height / 2)(lid_holder)) - lip) * down(outer_sleeve_height / 2)(cube(outer_sleeve_radius + 25, 50))

if __name__ == '__main__':
    a = assembly_2()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=True)
