###############################################################################################################
#    bikeRideUtils.py   Copyright (C) <2024>  <Kevin Scott>                                                   #                                                                                                             #                                                                                                             #
#    A number of helper and utility functions                                                                 #
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

import os
import pathlib

from src.console import console

######################################################################################## loadExplorer() ######
def loadExplorer(logger):
    """  Load program working directory into file explorer.
    """
    try:
        os.startfile(os.getcwd(), "explore")
    except NotImplementedError as error:
        logger.error(error)


########################################################################################### logPrint() #######
def logPrint(logger, verbose, message, style):
    """  If a logger is supplied, log message.
         If screen is True, print message to screen.
    """
    if logger:
        logger.info(message)

    if verbose:
        if style == "warning":
            console.log(f"{message}", style="warning")
        else:
            console.log(f"{message}", style="info")

########################################################################################### checkPaths() #########
def checkPaths(logger, dirIn, dirOut, verbose):
    """  Checks the data directories exist, if not create them.
    """

    logPrint(logger, verbose, "Checking Paths", "info")

    path     = pathlib.Path(__file__).parents[2]        #  Needs [2], because script is run in src\utils
    data_dir = path.joinpath(path, f"{dirIn}")
    out_dir  = path.joinpath(path, f"{dirOut}")
    log_dir  = path.joinpath(path, "logs")

    if data_dir.exists():
        logPrint(logger, verbose, f"{data_dir} exists", "info")
    else:
        logPrint(logger, verbose, f"{data_dir} doesn't exists, will create", "warning")
        data_dir.mkdir(parents=True)

    if out_dir.exists():
        logPrint(logger, verbose, f"{out_dir} exists", "info")
    else:
        logPrint(logger, verbose, f"{out_dir} doesn't exists, will create", "warning")
        out_dir.mkdir(parents=True)

    if log_dir.exists():
        logPrint(logger, verbose, f"{log_dir} exists", "info")
    else:
        logPrint(logger, verbose, f"{log_dir} doesn't exists, will create", "warning")
        log_dir.mkdir(parents=True)

