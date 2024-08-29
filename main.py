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

from windows_toasts import WindowsToaster, Toast, ToastDisplayImage

import src.myBikeRides as BikeRides
import src.args as args
import src.myTimer as myTimer
import src.myConfig as myConfig
import src.myLogger as myLogger
import src.myLicense as myLicense
import src.utils.bikeRideUtils as utils

############################################################################################### __main__ ######

if __name__ == "__main__":

    myConfig = myConfig.Config()                   # Need to do this first.

    # Prepare the toaster for bread (or your notification)
    toaster = WindowsToaster(myConfig.NAME)
    # Initialise the toast
    newToast = Toast()
    icon    = "resources\\tea.ico"                 #  icon used by notifications
    newToast.AddImage(ToastDisplayImage.fromPath(icon))

    LGpath  = "logs\\" +myConfig.NAME +".log"      #  Must be a string for a logger path.
    logger  = myLogger.get_logger(LGpath)          #  Create the logger.
    timer   = myTimer.Timer()                      #  Create a timer.

    try:
        timer.Start()
        utils.logPrint(logger, False, "-" * 100, "info")
        utils.logPrint(logger, True, f"{myConfig.NAME} {myConfig.VERSION} .::. Started at {timer.rightNow}", "info")
        if myConfig.NOTIFICATION:
            # Set the body of the notification
            newToast.text_fields = [f"{myConfig.NAME} started"]
            # And display it!
            toaster.show_toast(newToast)
    except (TimeoutError, AttributeError, NameError) as error:
        logger.debug(error)

    plot, dirIn, dirOut = args.parseArgs(myConfig.NAME, myConfig.VERSION, logger)     #  **  Need to catch arguments if required.  **

    utils.checkPaths(logger, dirIn, dirOut, False)                                    #  set to True to print to screen.

    myLicense.printShortLicense(myConfig.NAME, myConfig.VERSION)

    bikeRides = BikeRides.routes(dirIn, dirOut)

    bikeRides.build()
    if plot:
        bikeRides.plot()

    try:
        timeStop = timer.Stop
        utils.logPrint(logger, True, f"{myConfig.NAME} {myConfig.VERSION} .::. Completed in {timeStop}", "info")
        if myConfig.NOTIFICATION:
            newToast.text_fields = [f"{myConfig.NAME} .::. Completed in {timeStop}"]
            toaster.show_toast(newToast)
    except (TimeoutError, AttributeError, NameError) as error:
        logger.debug(error)

    exit(0)
