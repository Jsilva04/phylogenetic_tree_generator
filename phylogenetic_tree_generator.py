import toyplot.pdf
import toytree
import toyplot
import sys
import os

tre = toytree.tree(sys.argv[1])

wildcard = sys.argv[2]

rtre = tre.root("~" + wildcard)

# Prompt the user to enter the file name and path
file_name = input("Enter the file name and path to save the phylogenetic tree: ")

# Save the figure to the specified file
if os.path.exists(file_name):
    overwrite = input(f"The file {file_name} already exists. Do you want to overwrite it? (y/n) ")
    if overwrite.lower() != "y":
        print("Aborting...")
        sys.exit()

canvas, axes, mark = rtre.draw(node_hover=True, node_sizes=16, tip_labels_align=True, node_labels='support', use_edge_lengths=False)
toyplot.pdf.render(canvas, file_name)
print(f"Phylogenetic tree saved to {file_name}")
