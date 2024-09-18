 PyBikeRides.

A Python script to display my bike rides.

A class that contains some routines for merging, correcting and plotting gpx files.
The class uses gpxpy to parse the gpx files.
Elevation data is corrected using srtm.py @ https://github.com/tkrajina/srtm.py.

build()   - merges all the gpx files in a given import directory, corrects the elevation data in the merged file
            and save the merged file to the given directory.
correct() - Loads the all the gpx files in a given directory corrects the elevation data and  saves
            the files into the given output directory.  The files are save with the same filename
            OES NOT MERGE.
plot()    - Produces a HTML map of a gpx file, usually called on the output of build().

To install dependencies pip install -r requirements.txt
Also need srtm.py @ https://github.com/tkrajina/srtm.py>

For changes see history.txt
