#!/bin/bash


input=$1
outputput=$2
coor1=$3 #coordinate for basin outlet (east)
coor2=$4 #coordinate for basin outlet (north)

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
grass74 -c tmp/loc_tmp/PERMANENT/ -e --exec r.univar map=dem output=$output

rm -r tmp/
