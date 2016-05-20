# -*- coding: utf-8 -*-
"""
Author: Raul Acuna @ TU Darmstadt
Email: raultron@gmail.com

TODO :
- Center the figure in a A4 paper

"""
import svgwrite
from svgwrite import cm
import argparse
import sys

def main(argv):
    outputfile = 'test.svg'
    parser = argparse.ArgumentParser()
    parser.add_argument("marker_size", help="Length from center of top-left circle to center of top-right circle", default=12.5, type=float)
    parser.add_argument("circle_radius", help="Radius of each circle", default=0.9, type=float)
    parser.add_argument("AB0", help="Cross relation AB in line 0",default=0.40, type=float)
    parser.add_argument("AC0", help="Cross relation AC in line 0",default=0.60, type=float)
    parser.add_argument("AB1", help="Cross relation AB in line 1",default=0.20, type=float)
    parser.add_argument("AC1", help="Cross relation AC in line 1",default=0.80, type=float)
    
    args = parser.parse_args()
    
    
    dwg = svgwrite.Drawing('default.svg')    
    
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
    
    #Outer square
    dwg.add(svgwrite.shapes.Rect((0*cm,0*cm),(size_outer_square*cm,size_outer_square*cm), fill='white', stroke='black'))
    
    #inner square
    dwg.add(svgwrite.shapes.Rect((corner_inner_square*cm,corner_inner_square*cm),(size_inner_square*cm,size_inner_square*cm), fill='none', stroke='black'))
    
    
    
    
    x1 = y1 = circle_radius + circle_clearance
    x2 = y2 = circle_radius + circle_clearance + marker_size
    
    #lets draw the marker corner circles
    top_left_corner = (x1*cm,y1*cm)
    bottom_left_corner = (x1*cm,y2*cm)
    top_right_corner = (x2*cm,y1*cm)
    bottom_right_corner = (x2*cm,y2*cm)
    dwg.add(svgwrite.shapes.Circle(top_left_corner, circle_radius*cm))
    dwg.add(svgwrite.shapes.Circle(bottom_left_corner, circle_radius*cm))
    dwg.add(svgwrite.shapes.Circle(top_right_corner, circle_radius*cm))
    dwg.add(svgwrite.shapes.Circle(bottom_right_corner, circle_radius*cm))
    
    
    
    #Now we draw the Cross related circles for line 0
    
    
    
    
    dwg.add(svgwrite.shapes.Circle(((x1+marker_size*CR_Line0_AB)*cm,y1*cm), circle_radius*cm))
    dwg.add(svgwrite.shapes.Circle((x1*cm,(y1+marker_size*CR_Line0_AB)*cm), circle_radius*cm))
    
    dwg.add(svgwrite.shapes.Circle(((x1+marker_size*CR_Line0_AC)*cm,y1*cm), circle_radius*cm))
    dwg.add(svgwrite.shapes.Circle((x1*cm,(y1+marker_size*CR_Line0_AC)*cm), circle_radius*cm))
    
    #Now we draw the Cross related circles for line 1
    dwg.add(svgwrite.shapes.Circle(((x1+marker_size*CR_Line1_AB)*cm,y2*cm), circle_radius*cm))
    dwg.add(svgwrite.shapes.Circle((x2*cm,(y1+marker_size*CR_Line1_AB)*cm), circle_radius*cm))
    
    dwg.add(svgwrite.shapes.Circle(((x1+marker_size*CR_Line1_AC)*cm,y2*cm), circle_radius*cm))
    dwg.add(svgwrite.shapes.Circle((x2*cm,(y1+marker_size*CR_Line1_AC)*cm), circle_radius*cm))
    
    
    #Put text with information about the marker in the center
    dwg.add(dwg.text('Marker Size {0}'.format(marker_size), insert=((cx-4)*cm, (cy+3)*cm), fill='black'))
    dwg.add(dwg.text('Crossratio 0: AB = {0:2.2f},  AC= {1:.2f}, CR= {2:.4f}'.format(CR_Line0_AB,CR_Line0_AC, cross_ration_0,4), insert=((cx-4)*cm, (cy+3+0.4)*cm), fill='black'))
    dwg.add(dwg.text('Crossratio 1: AB = {0:2.2f},  AC= {1:.2f}, CR= {2:.4f}'.format(CR_Line1_AB,CR_Line1_AC, cross_ration_1,4), insert=((cx-4)*cm, (cy+3+0.8)*cm), fill='black'))
    
    
    
    dwg.add(dwg.text('| AB | BD | CD |', insert=((cx-3)*cm, (cy-5)*cm), fill='black', textLength = 10*cm))
    dwg.add(dwg.text('| {0:.3f}cm | {1:.3f}cm | {2:.3f}cm |'.format(d_line0_AB,d_line0_BD,d_line0_CD), insert=((cx-3)*cm, (cy-4.5)*cm), fill='black'))
    dwg.add(dwg.text('| {0:.3f}cm | {1:.3f}cm | {2:.3f}cm |'.format(d_line1_AB,d_line1_BD,d_line1_CD), insert=((cx-3)*cm, (cy-4)*cm), fill='black'))    
    dwg.add(dwg.text('Line Top:', insert=((cx-5.2)*cm, (cy-4.5)*cm), fill='black'))
    dwg.add(dwg.text('Line Bottom:', insert=((cx-5.2)*cm, (cy-4)*cm), fill='black'))
    
    
    
    
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
    dwg.add(svgwrite.shapes.Circle((cx*cm,cy*cm), 0.05*cm, fill='red'))
    
    dwg.add(dwg.line((cx*cm, cy*cm), ((cx+2)*cm, cy*cm), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.add(dwg.line((cx*cm, cy*cm), (cx*cm, (cy-2)*cm), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.add(dwg.text('x', insert=((cx+2.1)*cm, (cy)*cm), fill='black'))
    dwg.add(dwg.text('y', insert=((cx)*cm, (cy-2.2)*cm), fill='black'))
    
    dwg.save()

if __name__ == "__main__":
    main(sys.argv[1:])
    