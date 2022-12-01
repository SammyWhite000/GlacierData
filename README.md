# GlacierData

* This is for CS150B Class for Colorado State University

## Introduction

I was given a csv file loaded with glacier data. To break it down, I want to take the longitude and latitude columns out of this dataset
and plot each glacier onto a rendered map. 

## Process

1. Read in a csv file
2. Extract the longitude and latitude out of the file and create a new csv file
3. With this new csv file, put the long and lat into it
    * The only data this new file will contain is the long and lat columns
4. Create a pandas dataframe
5. Load newly created csv file into pandas dataframe.
6. Use pandas geodataframe to plot each place on a real, rendered map

## Sources

* For plotting lat and long onto a map
    * https://stackoverflow.com/questions/53233228/plot-latitude-longitude-from-csv-in-python-3-6
