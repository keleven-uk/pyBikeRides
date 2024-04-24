###############################################################################################################
#    pyBikeRides   Copyright (C) <2024>  <Kevin Scott>                                                        #                                                                                                             #    A skeleton program for a python command line script.                  .                                  #
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

import srtm
import pathlib
from io import FileIO
from gpxplotter import add_segment_to_map, create_folium_map, read_gpx_file

def run():

    files = findFiles()

    line_options = {"weight": 8}

    the_map = create_folium_map(tiles="openstreetmap")

    for file in files:
        #file = addElevation(file)
        fileName = FileIO(pathlib.Path(file).absolute())

        print(f"Processing {fileName.name}")

        for track in read_gpx_file(fileName):
            for _, segment in enumerate(track["segments"]):
                add_segment_to_map(
                    the_map,
                    segment,
                    #color_by="elevation",
                    cmap="RdPu_09",
                    line_options=line_options,
            )

    # To store the map as a HTML page:
    the_map.save("map.html")

    # To display the map in a Jupyter notebook:
    #the_map


def findFiles():

    path = pathlib.Path(__file__).parents[1]
    files = path.joinpath(path, "data").iterdir()

    return files

def addElevation(gpx):

    #add elevations for all points in a GPS track
    elevation_data = srtm.get_data()
    elevation_data.add_elevations(gpx)

    return gpx

