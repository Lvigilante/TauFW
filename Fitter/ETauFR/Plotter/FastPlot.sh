#!/bin/bash
filename=PlotShapes.C

declare -a arr=("VVLoose" "VLoose" "Loose" "Medium" "Tight" "VTight" "VVTight")

part="VVLoose"
## now loop through the above array
for i in "${arr[@]}"
do
      
  sed -i "s/$part/$i/" $filename
  
  root -b -q PlotShapes.C

  search="bool posfit = true,"
  replace="bool posfit = false,"

  sed -i "s/$search/$replace/" $filename

  root -b -q PlotShapes.C


  searchA="bool passProbe = true,"
  replaceA="bool passProbe = false,"

  sed -i "s/$searchA/$replaceA/" $filename

  root -b -q PlotShapes.C


  searchB="bool posfit = false,"
  replaceB="bool posfit = true,"

  sed -i "s/$searchB/$replaceB/" $filename

  root -b -q PlotShapes.C

  searchC="bool passProbe = false,"
  replaceC="bool passProbe = true,"


  sed -i "s/$searchC/$replaceC/" $filename

  sed -i "s/$i/$part/" $filename
done
