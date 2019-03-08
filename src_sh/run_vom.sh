#!/bin/sh
#compiles and runs the model

exe_src=$4
nml_input=$3
dailyweather_input=$2
workdir=$1

date

#compile code
make --directory src/VOM/VOM_Fortran

currdir=pwd

#go to workdirectory
cd $workdir

#run the model 
$currdir/src/VOM/VOM_Fortran/model.x

#go back to current directory
cd $currdir

#clean again
make clean --directory src/VOM/VOM_Fortran

date
