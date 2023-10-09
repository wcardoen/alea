#!/usr/bin/env python3
import argparse
from datetime import date
import sys
from . import auxdate
from . import mydate

def parseInput():
    """
    Parse Input from command line
    :return: (filename,type, date1, date2)
    """
    today = date.today()
    today_str = "{0:02d}/{1:02d}/{2:04d}".format(today.month,today.day,today.year)

    descrip =  "  ALEA::\n"
    descrip += "  Check your MegaMillion, Powerball numbers\n"
    descrip += "  during a well-defined time period. "
    parser = argparse.ArgumentParser(description=descrip)
    parser.add_argument('--file','-f', action='store', required=True,
                        help="File containing your lottery numbers")
    parser.add_argument('--type','-t', action='store', required=True,
                        choices=['MM','PB'],help="Type of the lottery (MM/PB)")
    parser.add_argument('--begin', '-b', action='store', required=True,
                        help="Start Date MM/DD/YYYY")
    parser.add_argument('--end', '-e', action='store', default=today_str,
                        help="End Date MM/DD/YYYY")
    args = parser.parse_args()
    argDict = vars(args)

    # Convert start to Date Type
    start = auxdate.getPartsDate(argDict['begin'])
    if start[0]==True:
        startDate = mydate.MyDate(start[1],start[2],start[3])
    else:
        sys.exit("  Invalid Start date")

    # Convert end to Date Type
    end = auxdate.getPartsDate(argDict['end'])
    if end[0] == True:
        endDate = mydate.MyDate(end[1], end[2], end[3])
    else:
        sys.exit("  Invalid End date")

    print("  Input parameters::")
    print("    Input File: '{0}'".format(argDict['file']))
    print("    Type      : '{0}'".format(argDict['type']))
    print("    Start Date: '{0}'".format(startDate))
    print("    End Date  : '{0}'".format(endDate))
    return (argDict['file'],argDict['type'],startDate, endDate)
