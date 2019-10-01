#!/bin/sh
#compiles and runs the model

exe_dir=$1
workdir=$2
input_weather=$3
input_soil=$4
nml_input=$5
outputdir=$6
restart_dir=$7

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

mkdir $workdir/input/
cp $input_weather $workdir/input/
cp $input_soil $workdir/input/

#run the model 
$exe_dir/model.x -i $workdir/input/ -o $outputdir -n $nml_input

#clean again
make clean --directory $exe_dir

date
