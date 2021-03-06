#!/usr/bin/env python

###############################################################################
# Copyright Daniel Davies, Adam J. Jackson (2016)                             #
#                                                                             #
# This file is part of SMACT: compound_electroneg.py is free software: you    #
# can redistribute it and/or modify it under the terms of the GNU General     #
# Public License as published by the Free Software Foundation, either version #
# 3 of the License, or (at your option) any later version.  This program is   #
# distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;   #
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A       #
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.   #
# You should have received a copy of the GNU General Public License along     #
# with this program.  If not, see <http://www.gnu.org/licenses/>.             #
#                                                                             #
###############################################################################

"""
Convenience script for compound electronegativity estimation as a geometric
mean of its components
"""


import argparse
from smact.properties import compound_electroneg

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="""Compound electronegativity from geometric mean of
                       elemental Mulliken electronegativities.""")
    parser.add_argument("-e", "--elements", type=str,
                        help="""Space-separated string of elements
                                (e.g. \"Cu Zn Sn S\")"""
                        )
    parser.add_argument("-s", "--stoichiometry", type=str,
                        help="""Space-separated string of stoichiometry
                                (e.g. \"2 1 1 4\")""" % ()
                        )
    parser.add_argument("-v", "--verbose", help="More verbose output",
                        action="store_true")
    parser.add_argument("-q", "--quiet", help="Quiet output",
                        action="store_true")
    args = parser.parse_args()
    if args.quiet:
        verbose_flag = False
    else:
        verbose_flag = True

    print compound_electroneg(verbose=verbose_flag, elements=args.elements,
                              stoichs=args.stoichiometry)
