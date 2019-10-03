#!/bin/sh
#compiles and runs the model

exe_dir=$1
inputdir=$2
input_weather=$3
input_soil=$4
nml_input=$5
outputdir=$6
input_extra=$7
restart_dir=$8

date

#compile code
make --directory $exe_dir FC=gfortran

#check if the outputdir exists and else make one
if [ ! -d "$outputdir" ]; then
   mkdir $outputdir
fi

if [ -f "$restart_dir/sce_lastloop.txt" ]; then
   cp $restart_dir/* $outputdir
fi

if [ ! -d  "$inputdir" ]; then
mkdir $inputdir
cp $input_weather $inputdir
cp $input_soil $inputdir
cp $input_extra $inputdir
fi

#run the model 
$exe_dir/model.x -i $inputdir -o $outputdir -n $nml_input

#clean again
make clean --directory $exe_dir

date
