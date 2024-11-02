import numpy as np
from scipy.interpolate import interp1d
import os

def process_propeller_file(input_path, output_path=None, scale= 0.0254):
    """
    Process a propeller geometry file and create a BEM file.
    
    Args:
        input_path (str): Path to the input PE0 file
        output_path (str, optional): Path for the output BEM file. If None, uses input path with .bem extension
        scale (float, optional): Scale factor from inches to meters. Defaults to 0.0254
    
    Returns:
        str: Path to the output file
    """
    # Handle output path
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + '.bem'
    
    # Read and process input file
    with open(input_path, 'r') as f:
        # Read until the column headers
        while True:
            line = f.readline()
            if '(IN)       (IN)       (QUOTED)    (LE-TE)     (PRATHER)      (IN)     RATIO         (DEG)       (IN)      (IN**2)      (IN)         (IN)         (IN)' in line:
                break
        
        # Read geometry data until 'RADIUS: '
        geom_lines = []
        while True:
            line = f.readline()
            if 'RADIUS: ' in line:
                break
            if line.strip():  # Skip empty lines
                geom_lines.append(line)
        
        # Parse geometry data
        apc = np.loadtxt(geom_lines)
        
        # Get radius value
        radius_line = line.split('RADIUS: ')[1]
        R = float(radius_line.split('PROPELLER RADIUS (IN)')[0].strip())

        # Get number of blades
        while True:
            line = f.readline()
            if 'BLADES:' in line:
                break
        num_blade = int(line.split('BLADES:')[1].split('NUMBER OF BLADES')[0].strip())
    
    num_sections = len(apc)
    
    # Process geometry data
    station = apc[:,0]  # STATION (IN)
    radius_R = station/R
    chord = apc[:,1]    # CHORD (IN)
    chord_R = chord/R
    sweep = apc[:,5]    # SWEEP (IN)
    skew_R = -sweep/R
    t_c = apc[:,6]      # THICKNESS RATIO
    twist_deg = apc[:,7] # TWIST (DEG)
    
    # Initialize arrays
    rake_R = np.zeros(num_sections)
    sweep_deg = np.zeros(num_sections)
    CLi = np.zeros(num_sections)
    axial = np.zeros(num_sections)
    tangential = np.zeros(num_sections)
    
    # Create BEM matrix
    bem = np.column_stack([
        radius_R, chord_R, twist_deg, rake_R, skew_R, 
        sweep_deg, t_c, CLi, axial, tangential
    ])
    
    # Calculate additional parameters
    diameter = 2 * R * scale
    interp = interp1d(radius_R, twist_deg, kind='linear')
    beta3_4 = float(interp(0.75))
    feather = 0.0
    pre_cone = 0.0
    center = [0.0, 0.0, 0.0]
    normal = [-1.0, 0.0, 0.0]
    
    # Write output file
    with open(output_path, 'w') as f:
        f.write('...BEM Propeller...\n')
        f.write(f'Num_Sections: {num_sections}\n')
        f.write(f'Num_Blade: {num_blade}\n')
        f.write(f'Diameter: {diameter:.8f}\n')
        f.write(f'Beta 3/4 (deg): {beta3_4:.8f}\n')
        f.write(f'Feather (deg): {feather:.8f}\n')
        f.write(f'Pre_Cone (deg): {pre_cone:.8f}\n')
        f.write(f'Center: {center[0]:.8f}, {center[1]:.8f}, {center[2]:.8f}\n')
        f.write(f'Normal: {normal[0]:.8f}, {normal[1]:.8f}, {normal[2]:.8f}\n')
        f.write('\n')
        f.write('Radius/R, Chord/R, Twist (deg), Rake/R, Skew/R, Sweep, t/c, CLi, Axial, Tangential\n')
        for row in bem:
            line = ', '.join([f'{x:.8f}' for x in row])
            f.write(line + '\n')
    
    print("After importing BEM file, set the following properties:")
    print("Construction X/C: 0.000")
    print("    Feather Axis: 0.125")
    
    return output_path