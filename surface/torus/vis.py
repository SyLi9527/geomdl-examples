import gradio as gr
import os
from geomdl import BSpline
from geomdl import exchange
from geomdl.visualization import VisMPL
from geomdl import utilities
from geomdl import NURBS
import numpy as np
# Import and use Matplotlib's colormaps
from matplotlib import cm

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def generate_seperate_objs(files):
    
    obj_files = []
    
    for i in range(len(files)):
        # Create a BSpline surface instance
        surf = NURBS.Surface()

        # Set degrees
        # Defined as order = degree + 1
        surf.order_u = 4
        surf.order_v = 4
        # Set number of control points
        

        # Set control points
        d2_ctrlpts = exchange.import_txt(files[i].name, separator=" ")
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

        # Plot the control point grid and the evaluated surface
        vis_comp = VisMPL.VisSurface(ctrlpts=True, legend=False)
        surf.vis = vis_comp
        # Render the surface with selected colormap
        surf.render(colormap=cm.cool, plot=False)
        exchange.export_obj(surf, "generated/part"+ str(i + 1) + ".obj")
        obj_files.append("generated/part"+ str(i + 1) + ".obj")
        
    # Initialize empty lists for vertices and faces
    vertices = []
    faces = []

    # Initialize counters for vertices and faces
    vertex_count = 0
    face_count = 0

    # Loop over each OBJ file
    for obj_file in obj_files:
        with open(obj_file, 'r') as f:
            # Read in lines from file
            lines = f.readlines()
            
            # Loop over each line
            for line in lines:
                # Check if line is a vertex or face
                if line.startswith('v '):
                    # Add vertex to list
                    vertices.append(line.strip())
                elif line.startswith('f '):
                    # Parse face indices
                    face_indices = line.strip().split()[1:]
                    
                    # Adjust face indices based on vertex count
                    adjusted_indices = [int(index) + vertex_count for index in face_indices]
                    
                    # Add face to list
                    faces.append('f ' + ' '.join(str(index) for index in adjusted_indices))
                    
                    # Increment face count
                    face_count += 1
            
            # Increment vertex count by number of vertices in file
            vertex_count += len([line for line in lines if line.startswith('v ')])
    combined_file = 'combined.obj'
    # Write out combined OBJ file
    with open('combined.obj', 'w') as f:
        # Write out vertices
        for vertex in vertices:
            f.write(vertex + '\n')
        
        # Write out faces
        for face in faces:
            f.write(face + '\n')
    gr.Model3D(combined_file)

iface = gr.Interface(fn=generate_seperate_objs, 
                     inputs=gr.inputs.File(file_count="multiple"),
                     outputs=gr.Model3D(clear_color=[0.0, 0.0, 0.0, 0.0],  label="3D Model"))
iface.launch()