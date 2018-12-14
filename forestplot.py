import numpy as np
import matplotlib.pyplot as plt 

# ========================================== USER INPUT ===========================================
'''
* Input file must be of the following format: label, estimate, conf_lower, conf_upper, pvalue
* The delimiter can be defined below. 
* Specify if file has header below.
'''

filepath = '/home/julyankb/Workspace/Osteotoxic-drugs/OR_hip_ondrugs.txt'

# If input file has header, set True. Else, set false.
header = True

# Delimiter in text file
delimiter = '\t'

# Plot title
title = ''

xlabel = 'OR of hip fracture in FRD users'

# Set to False if want no ylabels
y_labels = True

# Set to True if want pvalues
show_pvalues = False

# Vertical line at 0 for BETA, at 1 for OR
vertical_line = 1

# Fontsize for figure
fontsize = 14

# Custom point shapes --> {label: (shape, point size)}
# Shape mappings can be found at https://matplotlib.org/api/markers_api.html
# Example: 'D' --> Diamond
custom_shapes = {
    'all': ('D', 100)
}
# =================================================================================================
class Point:
    def __init__(self, label, estimate, CIL, CIU, pvalue):
        self.label = label
        self.estimate = estimate
        self.CIL = CIL
        self.CIU = CIU
        self.pvalue = pvalue

point_list = []
with open(filepath, 'r') as infile:
    if header:
        next(infile)
    for line in infile:
        line = line.rstrip().split(delimiter)
        label, estimate, CIL, CIU, pvalue = [line[0]] + [float(i) for i in line[1:]]
        point_list.append(Point(label, estimate, CIL, CIU, pvalue))

point_list = list(reversed(point_list))

for i, point in enumerate(point_list, start=0):
    
    # Plot point estimates
    if point.label in custom_shapes:
        plt.scatter(point.estimate, i,
                    marker = custom_shapes[point.label][0],
                    s = custom_shapes[point.label][1],
                    color='r')
    else:
        plt.scatter(point.estimate, i, marker='s', color='r')
    
    # Plot confidence intervals
    plt.plot((point.CIL, point.CIU),(i,i), 'k-', linewidth=1)

# Plot vertical line
plt.axvline(vertical_line, ls ='-', color='k',linewidth=0.5)

# Plot horizontal line
plt.axhline(0.5, ls ='--', color='k',linewidth=0.5)

# Plot y_labels
if y_labels:
    if show_pvalues:
        plt.yticks([y for y in range(len(point_list)+0)],
                   ['%s (p = %s)'%(point.label, point.pvalue) for point in point_list],
                   fontsize=fontsize)
    else:
        plt.yticks([y for y in range(len(point_list)+0)],
           ['%s'%(point.label) for point in point_list],
           fontsize=fontsize)
else:
    plt.yticks([])

# Plot xlabels
plt.xlabel(xlabel, fontsize=fontsize)
# Plot title
plt.title(title)
# Make it fit
plt.tight_layout()
# Show it
plt.show()
