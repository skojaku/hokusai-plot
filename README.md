# hokusai-plot
How to plot a network-looking great waves

# Dependency 
- pandas
- matplotlib
- numpy
- scipy
- networkx

# Tools
- inkscape
- gephi
- bash script

# Recipe

1. Find the background image on which you want to draw a network

2. Open the image with the inkscape

3. Place nodes on to the image using [the spary tool](https://wiki.inkscape.org/wiki/index.php/SpecSprayTool). 

4. Save the file as a svg file 

5. Open the svg file with your preferred editor

6. Extract the x,y coordinate of the points from the text file or the script below:
```bash
grep translate [svgfile] | sed -e 's/[a-z=()"\/ ><]//g'
```
The script may not work as the format may change depending on the version of the inkscape.

7. Once extracted the point, make a tsv file of two columns with column names "x" and "y", e.g., 
```
x   y
476.58875   287.11615
783.77599   -240.18003
866.21263   -182.80976
740.89176   -136.78241
799.52444   -137.24818
765.23085   -199.05479
761.35259   -151.52883
769.81723   -187.99191
```

8. Run the point2net.py in scripts/ directory, which will place edges between the nodes using the gravity model. 
```
python3 point2net.py [input] [output]
```
  - input: name of file that contains the x and y coordinate of nodes. Should be tsv file as specified above
  - output: graphml filename. Use "graphml" as the extention of the file
This program will create a network and save it as graphml file.

9. Open the generated graphml file with gephi. Add colors and change the size of nodes with the gephi. For the hokusai figure I made for NetSciX 2020, the colors are determined by the community detection and the size of nodes is proportional to the degree. 

10. Save the network as the svg file. 

11 Open the genearted svg and the original image. Overlay the two images. [QED]
