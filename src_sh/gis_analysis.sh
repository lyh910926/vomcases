#!/bin/bash


input=$1
coor1=$2 #coordinate for basin outlet (east)
coor2=$3 #coordinate for basin outlet (north)
output_dem=$4
output_slopes=$5
output_area=$6

#tmp-dir
#pourpoint litchfield: 130.795565681,-13.179210211
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
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.univar input=dem output=$output_dem

#determine slopes
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.slope.aspect map=dem slope=slopes

#calculate statistics of slopes
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.univar map=slopes output=$output_slopes

#convert raster to vector for area
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.to.vect input=basin@PERMANENT output=basin_vec type=area            

#area in meters**2
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec v.to.db -p map=basin_vec@PERMANENT option=area columns=value >  $output_area                

#remove temporary directory
rm -r tmp/
