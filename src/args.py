###############################################################################################################
#    args.py   Copyright (C) <2024>  <Kevin Scott>                                                            #
#                                                                                                             #
#    Parse the command line arguments.                                     .                                  #
#    Will handle argument of -v, -h & -e                                                                      #
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
import textwrap
import argparse
import src.myLicense as myLicense
import src.utils.bikeRideUtils as utils

############################################################################################## parseArgs ######
def parseArgs(Name, Version, logger):
    """  Process the command line arguments.

         Checks the arguments and will exit if not valid.

         Exit code 0 - program has exited normally, after print version, licence or help.
         Exit code 0 - program has exited normally, after Loading program working directory into file explorer.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=textwrap.dedent("""\
        pyBikeRides.
        -----------------------
        A Python script to display my bike rides."""),
        epilog=f" Kevin Scott (C) 2021-24 :: {Name} {Version}")

    parser.add_argument("-l", "--license",  action="store_true", help="Print the Software License.")
    parser.add_argument("-v", "--version",  action="store_true", help="Print the version of the application.")
    parser.add_argument("-e", "--explorer", action="store_true", help="Load program working directory into file explorer.")
    parser.add_argument("-p", "--plot",     action="store_true", help="Plot the one route using gpxplotter.")
    parser.add_argument("-i", "--inp",      default="data", type=pathlib.Path, help="Directory which hold the input data.  Default=data")
    parser.add_argument("-o", "--out",      default="out",  type=pathlib.Path, help="Directory which hold the output data. Default=out")

    args = parser.parse_args()

    if args.version:
        myLicense.printShortLicense(Name, Version)
        logger.info(f"End of {Name} V{Version}: version")
        print("Goodbye.")
        exit(0)

    if args.license:
        myLicense.printLongLicense(Name, Version)
        logger.info(f"End of {Name} {Version} : Printed Licence")
        print("Goodbye.")
        exit(0)

    if args.explorer:
        utils.loadExplorer(logger)             # Load program working directory n file explorer.
        print("Goodbye.")
        exit(0)

    return args.plot, args.inp, args.out
