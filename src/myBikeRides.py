###############################################################################################################
#    pyBikeRides   Copyright (C) <2024>  <Kevin Scott>                                                        #
#    A skeleton program for a python command line script.                  .                                  #
#                                                                                                             #
#                                                                                                             #
#     For changes see history.txt                                                                             #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2024>  <Kevin Scott>                                                                      #
#                                                                                                             #
#    This program is free software: you can redistribute it and/or modify it under the terms of the           #
#    GNU General Public License as published by the Free Software Foundation, either Version 3 of the         #
#    License, or (at your option) any later Version.                                                          #
#                                                                                                             #
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without        #
#    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#    GNU General Public License for more details.                                                             #
#                                                                                                             #
#    You should have received a copy of the GNU General Public License along with this program.               #
#    If not, see <http://www.gnu.org/licenses/>.                                                              #
#                                                                                                             #
###############################################################################################################

import pathlib
from io import FileIO

import gpxpy
import gpxpy.gpx
import operator
import src.srtm as srtm
from gpxplotter import add_segment_to_map, create_folium_map, read_gpx_file

import src.srtm as srtm

class routes():

    def __init__(self, dirIn, dirOut):
        self.dirIn  = dirIn
        self.dirOut = dirOut
        self.path   = pathlib.Path(__file__).parents[1]
        self.files  = self. findFiles()


    def build(self):

        count = 0

        # create new GPX file, append a blank track
        self.new_gpx = gpxpy.gpx.GPX()
        new_track    = gpxpy.gpx.GPXTrack()
        self.new_gpx.tracks.append(new_track)

        for f in self.files:
            count += 1
            print(f"Processing {f}")
            with open(f, "r") as self.gpx_file:
                gpx = gpxpy.parse(self.gpx_file)
                new_track.segments.append(gpx.tracks[0].segments[0])

        print(f"Processed {count} files")
        #add elevations for all points in a GPS track
        print("Adding Elevation data")
        elevation_data = srtm.get_data()                    #  Uses srtm.py @ https://github.com/tkrajina/srtm.py
        elevation_data.add_elevations(self.new_gpx)


        self.writeNewFile()


    def plot(self):
        print("Plotting route")

        oneFile = FileIO(self.path.joinpath(self.path, f"{self.dirOut}\\onefile.gpx").absolute())

        line_options = {"weight": 4}

        the_map = create_folium_map(tiles="openstreetmap")

        for track in read_gpx_file(oneFile):
            for i, segment in enumerate(track["segments"]):
                add_segment_to_map(
                    the_map,
                    segment,
                    #color_by="elevation",
                    cmap="viridis",
                    line_options=line_options,
                )

        # To store the map as a HTML page:
        saveFile = self.path.joinpath(self.path, f"{self.dirOut}\\oneMap.html")
        the_map.save(saveFile)



    def findFiles(self):

        files = self.path.joinpath(self.path, self.dirIn).iterdir()

        return files


    def writeNewFile(self):

        print("Writing Combined track")

        oneFile = self.path.joinpath(self.path, f"{self.dirOut}\\onefile.gpx")

        with open(oneFile, "w") as f:
            f.write(self.new_gpx.to_xml())


