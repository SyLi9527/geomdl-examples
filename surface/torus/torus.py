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
import numpy as np

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))


for i in range(59):
    # Create a BSpline surface instance
    surf = NURBS.Surface()

    # Set degrees
    # Defined as order = degree + 1
    surf.order_u = 4
    surf.order_v = 4
    # Set number of control points
    

    # Set control points
    d2_ctrlpts = exchange.import_txt("ctrlpts/torus"+ str(i + 1) + ".ctrlpts", separator=" ")
    surf.ctrlpts_size_u = int(np.sqrt(len(d2_ctrlpts)))
    surf.ctrlpts_size_v = int(np.sqrt(len(d2_ctrlpts)))
    surf.ctrlpts = d2_ctrlpts
    

    # Set knot vectors to be uniform
    surf.knotvector_u = utilities.generate_knot_vector(3, surf.ctrlpts_size_u)
    surf.knotvector_v = utilities.generate_knot_vector(3, surf.ctrlpts_size_v)


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
    surf.render(colormap=cm.cool, plot=False)
    exchange.export_obj(surf, "parts/torus"+ str(i + 1) + ".obj")
# Good to have something here to put a breakpoint
pass


