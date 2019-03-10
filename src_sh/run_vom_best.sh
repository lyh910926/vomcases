#!/bin/sh
#


INPUTPARS=$1
INPUT=$2
OUTPUTPATH=$3
TMP_OUT=$4
TMP_IN=$5
EXE_FOLDER=$6
WORKDIR=$7
CODE=$8

dirname=$(pwd)

#compile code
make --directory $EXE_FOLDER

cp $EXE_FOLDER/model.x $WORKDIR/model.x


#filenum=${INPUTPARS#../pars/pars}
date

counter=1

for parfile in $INPUTPARS/* 
do 


cp $parfile $WORKDIR/$TMP_IN/pars.txt

cd $WORKDIR
./model.x
#../../../../src/VOM/VOM_Fortran/model.x
cd $dirname

   #remove files that are not needed
   rm $WORKDIR/$TMP_OUT/su_hourly.txt
   rm $WORKDIR/$TMP_OUT/delz_hourly.txt
   rm $WORKDIR/$TMP_OUT/results_hourly.txt
   rm $WORKDIR/$TMP_OUT/ruptkt_hourly.txt
   rm $WORKDIR/$TMP_OUT/results_yearly.txt
   rm $WORKDIR/$TMP_OUT/rsurf*
   #copy results and rename
   for outputfile in $WORKDIR/$TMP_OUT/*
   do
      #get filename
      filename=${outputfile#$WORKDIR/$TMP_OUT/}
      filename=${filename%.txt}


      #copy output
      echo 'counter'
      echo $counter
      cp $outputfile $OUTPUTPATH$filename$counter
   done
   rm $WORKDIR/$TMP_OUT/*
   rm $WORKDIR/$TMP_IN/pars.txt

  let counter++

done

rm $WORKDIR/model.x

make clean --directory $EXE_FOLDER

date
