# Pi-Tag generator
Pi-Tag fiducial marker generator.

PiTag stands for Projective Invariant Tag, due to the detection algorithm which is based on projective invariants. More information on Pi-Tag can be found on the original [publication](www.dsi.unive.it/~atorsell/papers/Journals/MVA(24-6)2013.pdf). If you want to detect this markers I suggest to use the ROS package [cob_fiducials](http://wiki.ros.org/cob_fiducials).

This script generates Pi-Tag fiducial markers in an SVG file with the following format:

![Reference PiTag Marker](/examples/reference_marker.png?raw=true "Reference PiTag Marker")

SVG stands for Scalable Vector Graphics, this files can be easily edited with open source tools like Inkscape.

### Installation and execution

The script is based on svgwrite and python. The following installation instructions apply for Ubuntu 14.04:

Install dependencies on a new terminal:

    sudo apt-get install python-pip python-argparse python-cairosvg
    sudo pip install svgwrite

#### Then clone this repository

    git clone https://github.com/raultron/PiTag-generator.git

#### Inside the PiTag-generator folder execute:

    python pi-tag_gen.py 0.40 0.60 0.30 0.70

This command will generate a generic marker of 10cm wide with circles of 0.9cm Radius in a file named pitag_marker.svg in the same folder of the script.

Example with all the implemented options:

     python pi-tag_gen.py 0.40 0.60 0.30 0.70 --output_file pitag_marker.svg --A4 --pdf --show_info --marker_size 10.0 --circle_radius 0.9 --circle_clearance 0.2


### Positional arguments


3. **AB0**

 Cross relation AB in top and left sides

4. **AC0**

 Cross relation AC in top and left sides

5. **AB1**

 Cross relation AB in bottom and right sides

6. **AC1**

 Cross relation AC in bottom and right sides

### Optional arguments

1. **marker_size**

 Size of the marker in centimeters, measured from Top-Left circle center to Top-Right circle center. Default = 10.0 cm
2. **circle_radius**

 Radius of the circle in centimeters. Default = 0.9 cm
3. **circle_clearance**

  Minimum white space surrounding the black circles. Default = 0.2 cm
4. **output_file**

  Name of the output file. Default = "pitag_marker.svg"

5. **--A4**

 The marker will be centered in A4 sheet dimensions. Useful for printing. Other sheet sizes not currently available (make a pull request!). Defaults to False.

6. **--pdf**

 The script will generate a PDF from the SVG file. Defaults to False (only SVG).

7. **--show_info**

 Print additional information inside the marker. Useful when doing tests or comparing markers. Defaults to False.
