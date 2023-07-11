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
from scipy.optimize import minimize

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
d2_ctrlpts =exchange.import_txt("u_cylinder_7x9.ctrlpts", separator=" ")
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
# surf.knotvector_u = [0, 0, 0, 0, 0.9, 0.99, 0.999, 1, 1, 1, 1]
# surf.knotvector_v = [0, 0, 0, 0, 0.9, 0.99, 0.999, 0.9999, 0.99999, 1, 1, 1, 1]
#####################################################################


# Set evaluation delta
surf.delta = 0.025

# Evaluate surface points
surf.evaluate()

# Import and use Matplotlib's colormaps
from matplotlib import cm

# Plot the control point grid and the evaluated surface
vis_comp = VisMPL.VisSurface(ctrlpts=True, legend=False, 
                             axes=True, evalpts=False,
                             bbox=False, trims=False,
                             figure_size=[10, 10], 
                             figure_dpi=100)
surf.vis = vis_comp
# Render the surface with selected colormap
surf.render(colormap=cm.cool)
exchange.export_obj(surf, "u_cylinder_7x9.obj")
# Good to have something here to put a breakpoint

surf.ctrlpts = d2_ctrlpts[30:] + d2_ctrlpts[:30]

# Import and use Matplotlib's colormaps
from matplotlib import cm

# Plot the control point grid and the evaluated surface
vis_comp = VisMPL.VisSurface(ctrlpts=True, legend=False, 
                             axes=True, evalpts=False,
                             bbox=False, trims=False,
                             figure_size=[10, 10], 
                             figure_dpi=100)
surf.vis = vis_comp
# Render the surface with selected colormap
surf.render(colormap=cm.cool)
exchange.export_obj(surf, "u_cylinder_7x9.obj")



def point_surface_distance(point, surface):
    def objective(uv):
        # Evaluate the surface at the given parameter values (u, v)
        pt_on_surf = surface.evaluate_single(uv)

        # Compute the Euclidean distance between the point and the surface point
        return np.linalg.norm(np.array(point) - np.array(pt_on_surf))

    # Define the bounds for the parameters (u, v)
    bounds = [(0, 1), (0, 1)]

    # Minimize the objective function to find the minimum distance
    result = minimize(objective, x0=[0.5, 0.5], bounds=bounds)

    # Return the minimum distance and the corresponding parameter values (u, v)
    return result.fun, result.x


point = [-21.74657330197829, -5.518218307919339, 7.538113723858469]
distance, uv = point_surface_distance(point, surf)
print("Distance between the point and the surface is:", distance)
print("Parameter values are:", uv)


pass


