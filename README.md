# PiTag-generator
Pi-Tag fiducial marker generator.

For more information on Pi-Tag can be found on the original [publication](www.dsi.unive.it/~atorsell/papers/Journals/MVA(24-6)2013.pdf). If you want to detect this markers I suggest that you use the ROS package [cob_fiducials](http://wiki.ros.org/cob_fiducials). 

This script generates Pi-Tag fiducial markers with the following format:

![Reference PiTag Marker](/examples/reference_marker.png?raw=true "Reference PiTag Marker")




## Script execution

    python pi-tag_gen.py 10 0.9 0.40 0.60 0.30 0.70

This command will generate a generic marker of 10cm wide with circles of 0.9cm Radius in a file named pitag_marker.svg in the same folder of the script.

Example with all the implemented options:

     python pi-tag_gen.py 10 0.9 0.40 0.60 0.30 0.70 --output_file my_marker_name.svg --A4 --show_info


### Positional arguments

1. **marker_size**

 Size of the marker in centimeters, measured from Top-Left circle center to Top-Right circle center.
2. **circle_radius**

 Radius of the circle in centimeters.
3. **AB0**

 Cross relation AB in top (line 0)

4. **AC0**

 Cross relation AC in top (line 0)

5. **AB1**

 Cross relation AB in bottom (line 1)

6. **AC1**

 Cross relation AC in bottom (line 1)

### Optional arguments

1. **--A4**

 The marker will be centered in A4 sheet dimensions. Useful for printing. Other sheet sizes not currently available (make a pull request!). Defaults to False.

2. **--pdf**

 TODO, not yet implemented. The script will generate a PDF from the SVG file. Defaults to False (only SVG).

3. **--show_info**

 Print additional information inside the marker. Useful when doing tests or comparing markers. Defaults to False.
