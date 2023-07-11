# List of OBJ files to combine
obj_files = []
for i in range(60):
    obj_files.append("parts/torus"+ str(i + 1) + ".obj")
    

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

# Write out combined OBJ file
with open('combined.obj', 'w') as f:
    # Write out vertices
    for vertex in vertices:
        f.write(vertex + '\n')
    
    # Write out faces
    for face in faces:
        f.write(face + '\n')