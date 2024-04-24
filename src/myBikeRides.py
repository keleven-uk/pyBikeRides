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

import pathlib

import gpxpy
import gpxpy.gpx

def run():

    path  = pathlib.Path(__file__).parents[1]
    files = findFiles(path)

    # create new GPX file, append a blank track
    new_gpx = gpxpy.gpx.GPX()
    new_track = gpxpy.gpx.GPXTrack()
    new_gpx.tracks.append(new_track)

    for f in files:
        print(f"Processing {f}")
        with open(f, "r") as gpx_file:
            gpx = gpxpy.parse(gpx_file)
            new_track.segments.append(gpx.tracks[0].segments[0])

    writeNewFile(path, new_gpx)


def findFiles(path):

    files = path.joinpath(path, "data").iterdir()

    return files


def writeNewFile(path, new_gpx):

    print("Writing Combined track")

    oneFile = path.joinpath(path, "out\\onefile.gpx")

    with open(oneFile, "w") as f:
        f.write(new_gpx.to_xml())


