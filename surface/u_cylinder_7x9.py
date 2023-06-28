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
from geomdl import NURBS

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
surf = NURBS.Surface()

# Set degrees
# Defined as order = degree + 1
surf.order_u = 4
surf.order_v = 4

# Set number of control points
surf.ctrlpts_size_u = 7
surf.ctrlpts_size_v = 9

# Set control points
d2_ctrlpts = exchange.import_txt("u_cylinder_7x9.ctrlpts", separator=" ")
surf.ctrlpts = d2_ctrlpts





# Set knot vectors to be uniform
surf.knotvector_u = utilities.generate_knot_vector(3, 7)
surf.knotvector_v = utilities.generate_knot_vector(3, 9)


#####################################################################
### Uncomment either one to see if the surface changes

# 1. Change control points to see if the surface is disordered
# surf.ctrlpts_size_u = 9
# surf.ctrlpts_size_v = 7
# surf.knotvector_u = utilities.generate_knot_vector(3, 9)
# surf.knotvector_v = utilities.generate_knot_vector(3, 7)

# 2. Change knot vector to see if the surface is disordered
surf.knotvector_u = [0, 0, 0, 0, 0.1, 0.2, 0.21, 1, 1, 1, 1]
surf.knotvector_v = [0, 0, 0, 0, 0.1, 0.2, 0.21, 0.31, 0.41, 1, 1, 1, 1]

#####################################################################


# Set evaluation delta
surf.delta = 0.025

# Evaluate surface points
surf.evaluate()

# Import and use Matplotlib's colormaps
from matplotlib import cm

# Plot the control point grid and the evaluated surface
vis_comp = VisMPL.VisSurface(ctrlpts=True, legend=False)
surf.vis = vis_comp
# Render the surface with selected colormap
surf.render(colormap=cm.cool)
exchange.export_obj(surf, "u_cylinder_7x9.obj")
# Good to have something here to put a breakpoint
pass


