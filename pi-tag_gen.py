# -*- coding: utf-8 -*-
"""
Author: Raul Acuna @ TU Darmstadt
Email: raultron@gmail.com

TODO :
- Convert to PDF
- Print guiding lines to indicate the crossratios

"""
import svgwrite
from svgwrite import cm, mm
import argparse
import sys

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("marker_size", help="Length from center of top-left circle to center of top-right circle", default=12.5, type=float)
    parser.add_argument("circle_radius", help="Radius of each circle", default=0.9, type=float)
    parser.add_argument("AB0", help="Cross relation AB in line 0",default=0.40, type=float)
    parser.add_argument("AC0", help="Cross relation AC in line 0",default=0.60, type=float)
    parser.add_argument("AB1", help="Cross relation AB in line 1",default=0.20, type=float)
    parser.add_argument("AC1", help="Cross relation AC in line 1",default=0.80, type=float)
    parser.add_argument("--A4", help="SVG output centered in A4 sheet size",action="store_true")
    parser.add_argument("--pdf", help="Convert final SVG file to pdf",action="store_true")
    parser.add_argument("--print_debug", help="Print debug information inside the marker",action="store_true")
    #parser.add_argument("--print_debug", help="Print debug information inside the marker",action="store_true")

    args = parser.parse_args()
    
    if args.A4:
        w, h = 21.0,29.7
        dwg = svgwrite.Drawing(filename='default.svg', size=(w*cm, h*cm), debug=True)    
        dwg.add(dwg.rect(insert=(0,0), size=(w*cm, h*cm), fill='white', stroke='none'))
    else:
        w, h = '100%', '100%'
        dwg = svgwrite.Drawing(filename='default.svg', size=(w, h), debug=True)    
        dwg.add(dwg.rect(insert=(0,0), size=(w, h), fill='white', stroke='none'))
    
    

    #The four corners of the square
    marker_size = args.marker_size
    circle_radius = args.circle_radius
    circle_clearance = 0.2 #white space around each black circle
    
    #CrossRatios 0 - 1.0 relative to marker_size
    
    d_line0_AB = marker_size * args.AB0 #AB
    d_line0_BD = marker_size - marker_size *args.AB0 #BD
    d_line0_AC = marker_size * args.AC0 #//AC
    d_line0_CD = marker_size - marker_size * args.AC0 #//CD
    cross_ration_0 = (d_line0_AB/d_line0_BD)/(d_line0_AC/d_line0_CD)
    
    d_line1_AB = marker_size * args.AB1 #AB
    d_line1_BD = marker_size - marker_size *args.AB1 #BD
    d_line1_AC = marker_size * args.AC1 #;//AC
    d_line1_CD = marker_size - marker_size * args.AC1 #;//CD
    cross_ration_1 = (d_line1_AB/d_line1_BD)/(d_line1_AC/d_line1_CD)
    
    print "cross_ration 0:  {0}".format(cross_ration_0)    
    print "cross_ration 1:  {0}".format(cross_ration_1)    
    print "delta:{0}".format(cross_ration_0 / cross_ration_1)    
    
    if cross_ration_0 < cross_ration_1:
        print "Error, Crossratio 0 must be greater that Crossratio 1"
        sys.exit()
    
    CR_Line0_AB = args.AB0
    CR_Line0_AC = args.AC0
    CR_Line1_AB = args.AB1
    CR_Line1_AC = args.AC1
    
    #center of the marker
    cx = cy = circle_clearance + circle_radius + marker_size/2
    
    
    
    #Squares for marker size reference
    size_inner_square = marker_size-circle_radius*2-circle_clearance*2
    corner_inner_square = 2*circle_radius + 2*circle_clearance
    size_outer_square = marker_size+circle_radius*2+circle_clearance*2
    
    #We create a group for the whole marker
    
    marker = dwg.defs.add(dwg.g(id='marker'))
    
    #Outer square
    marker.add(svgwrite.shapes.Rect((0*cm,0*cm),(size_outer_square*cm,size_outer_square*cm), fill='white', stroke='black'))
    
    #inner square
    marker.add(svgwrite.shapes.Rect((corner_inner_square*cm,corner_inner_square*cm),(size_inner_square*cm,size_inner_square*cm), fill='none', stroke='black'))
    
    
    
    
    x1 = y1 = circle_radius + circle_clearance
    x2 = y2 = circle_radius + circle_clearance + marker_size
    
    #lets draw the marker corner circles
    top_left_corner = (x1*cm,y1*cm)
    bottom_left_corner = (x1*cm,y2*cm)
    top_right_corner = (x2*cm,y1*cm)
    bottom_right_corner = (x2*cm,y2*cm)
    marker.add(svgwrite.shapes.Circle(top_left_corner, circle_radius*cm))
    marker.add(svgwrite.shapes.Circle(bottom_left_corner, circle_radius*cm))
    marker.add(svgwrite.shapes.Circle(top_right_corner, circle_radius*cm))
    marker.add(svgwrite.shapes.Circle(bottom_right_corner, circle_radius*cm))
    
    
    
    #Now we draw the Cross related circles for line 0
    
    
    
    
    marker.add(svgwrite.shapes.Circle(((x1+marker_size*CR_Line0_AB)*cm,y1*cm), circle_radius*cm))
    marker.add(svgwrite.shapes.Circle((x1*cm,(y1+marker_size*CR_Line0_AB)*cm), circle_radius*cm))
    
    marker.add(svgwrite.shapes.Circle(((x1+marker_size*CR_Line0_AC)*cm,y1*cm), circle_radius*cm))
    marker.add(svgwrite.shapes.Circle((x1*cm,(y1+marker_size*CR_Line0_AC)*cm), circle_radius*cm))
    
    #Now we draw the Cross related circles for line 1
    marker.add(svgwrite.shapes.Circle(((x1+marker_size*CR_Line1_AB)*cm,y2*cm), circle_radius*cm))
    marker.add(svgwrite.shapes.Circle((x2*cm,(y1+marker_size*CR_Line1_AB)*cm), circle_radius*cm))
    
    marker.add(svgwrite.shapes.Circle(((x1+marker_size*CR_Line1_AC)*cm,y2*cm), circle_radius*cm))
    marker.add(svgwrite.shapes.Circle((x2*cm,(y1+marker_size*CR_Line1_AC)*cm), circle_radius*cm))
    
    
    #Put text with information about the marker in the center
    t_x = cx - 5
    t_y = cy + size_outer_square/2 +1
    
    marker.add(dwg.text('| AB | BD | CD |', insert=((t_x+2.2)*cm, t_y*cm), fill='black', textLength = 10*cm))
    marker.add(dwg.text('| {0:.3f}cm | {1:.3f}cm | {2:.3f}cm |'.format(d_line0_AB,d_line0_BD,d_line0_CD), insert=((t_x+2.2)*cm, (t_y+0.5)*cm), fill='black'))
    marker.add(dwg.text('| {0:.3f}cm | {1:.3f}cm | {2:.3f}cm |'.format(d_line1_AB,d_line1_BD,d_line1_CD), insert=((t_x+2.2)*cm, (t_y+1.0)*cm), fill='black'))    
    marker.add(dwg.text('Line Top:', insert=((t_x)*cm, (t_y+0.5)*cm), fill='black'))
    marker.add(dwg.text('Line Bottom:', insert=((t_x)*cm, (t_y+1.0)*cm), fill='black'))    
    
    marker.add(dwg.text('Marker Size {0}'.format(marker_size), insert=((t_x)*cm, (t_y+2)*cm), fill='black'))
    marker.add(dwg.text('Crossratio 0: AB = {0:2.2f},  AC= {1:.2f}, CR= {2:.4f}'.format(CR_Line0_AB,CR_Line0_AC, cross_ration_0,4), insert=((t_x)*cm, (t_y+2+0.5)*cm), fill='black'))
    marker.add(dwg.text('Crossratio 1: AB = {0:2.2f},  AC= {1:.2f}, CR= {2:.4f}'.format(CR_Line1_AB,CR_Line1_AC, cross_ration_1,4), insert=((t_x)*cm, (t_y+2+1)*cm), fill='black'))
    
    
    
    
    
    
    
    
    d_line0_AB = marker_size * args.AB0 #AB
    d_line0_BD = marker_size - marker_size *args.AB0 #BD
    d_line0_AC = marker_size * args.AC0 #//AC
    d_line0_CD = marker_size - marker_size * args.AC0 #//CD
    cross_ration_0 = (d_line0_AB/d_line0_BD)/(d_line0_AC/d_line0_CD)
    
    d_line1_AB = marker_size * args.AB1 #AB
    d_line1_BD = marker_size - marker_size *args.AB1 #BD
    d_line1_AC = marker_size * args.AC1 #;//AC
    d_line1_CD = marker_size - marker_size * args.AC1 #;//CD
    
    #red do in the Center of the marker
    marker.add(svgwrite.shapes.Circle((cx*cm,cy*cm), 0.05*cm, fill='red'))
    
    marker.add(dwg.line((cx*cm, cy*cm), ((cx+2)*cm, cy*cm), stroke=svgwrite.rgb(10, 10, 16, '%')))
    marker.add(dwg.line((cx*cm, cy*cm), (cx*cm, (cy-2)*cm), stroke=svgwrite.rgb(10, 10, 16, '%')))
    marker.add(dwg.text('x', insert=((cx+2.1)*cm, (cy)*cm), fill='black'))
    marker.add(dwg.text('y', insert=((cx)*cm, (cy-2.2)*cm), fill='black'))
    
        
    if args.A4:
        #center marker in middle of A4 sheet
        x_m = ((w/2)-(size_outer_square/2))
        y_m = ((h/2)-(size_outer_square/2))
        u = dwg.use(marker, insert=(x_m*cm,y_m*cm))
    else:
        u = dwg.use(marker, insert=(0*cm,0*cm))
        
    
    
    dwg.add(u)
    
    dwg.save()

if __name__ == "__main__":
    main(sys.argv[1:])
    