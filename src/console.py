###############################################################################################################
#    console.py   Copyright (C) <2024>  <Kevin Scott>                                                         #
#                                                                                                             #
#    Config file for the console used by the rich package for fancy printing.                                 #
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

"""  Config file for the console used by the rich package for fancy printing.
     Rich is a Python library for writing rich text (with colour and style) to the terminal,
     and for displaying advanced content such as tables, markdown, and syntax highlighted code.

     usage : from src.console import console
     then    console.log
       or    console.print  etc
"""
from rich.console import Console
from rich.theme import Theme

#  Bold only seems to work, not underline or blink etc.
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red underline"
})

console = Console(theme=custom_theme)


