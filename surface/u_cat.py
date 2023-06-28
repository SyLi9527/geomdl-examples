#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2018
"""

import os
from geomdl import BSpline
from geomdl import exchange
from geomdl.visualization import VisMPL
from geomdl import utilities

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Set control points
surf.set_ctrlpts(*exchange.import_txt("u_cat.cpt", two_dimensional=True))





# Set knot vectors
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, 20)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_u, 20)

# Set evaluation delta
surf.delta = 0.025

# Evaluate surface points
surf.evaluate()

# Import and use Matplotlib's colormaps
from matplotlib import cm

# Plot the control point grid and the evaluated surface
vis_comp = VisMPL.VisSurface()
surf.vis = vis_comp
surf.render(colormap=cm.cool)

# Good to have something here to put a breakpoint
pass


