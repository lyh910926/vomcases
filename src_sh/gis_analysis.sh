#!/bin/bash
# script to run a series of grass gis commands to get several statistics
# produces three output-files:
# 1. file with elevation statistics (mean, range, max, min, etc)
# 2. file with slope statistics (mean, range, max, min, etc)
# 3. file with the basin area in m2

input=$1            #input file with dem as geotiff
coor1=$2            #coordinate for basin outlet (east)
coor2=$3            #coordinate for basin outlet (north)
output_file=$4       #outputfile with elevation statistics



#outlet howardspring: 131.150007276, -12.4882868434
#outlet adelaideriver: 131.120860633, -13.0756093192
#outlet dalyuncleared: 131.3833422, -14.1591689096
#outlet dryriver: 132.374447643, -15.262510562
#outlet litchfield: 130.795565681,-13.179210211
#outlet sturtplains: 133.346086362, -17.1438801023



mkdir tmp

#create data
grass74 -c $1 -e tmp/loc_tmp

#add data
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.external input=$input output=dem

#derive facc and fdir-maps
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.watershed --overwrite elevation=dem@PERMANENT accumulation=facc drainage=fdir

#create basin
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.water.outlet input=fdir output=basin coordinates=$coor1,$coor2

#set mask
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.mask raster=basin maskcats=1

#calculate statistics
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.univar map=dem output=- > $output_file

#determine slopes
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.slope.aspect elevation=dem slope=slopes

#calculate statistics of slopes
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.univar map=slopes output=- >> $output_file

#convert raster to vector for area
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.to.vect input=basin@PERMANENT output=basin_vec type=area            

#area in meters**2
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec v.to.db -p map=basin_vec@PERMANENT option=area columns=value >> $output_file                

#remove temporary directory
rm -r tmp/
