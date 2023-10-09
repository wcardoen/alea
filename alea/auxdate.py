__author__ = 'sleipnir'
from . import mydateerror

def isLeapYear(year):
    """
    Test whether a year is a leap year
    :param year:
    :return: Boolean
    """
    if year%4 !=0:
        return False
    elif year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    else:
        return True


def isDateInRange(month, day, year):
    """
    Test whether a certain month/day/year
    combination is a valid Date
    :param month: integer
    :param day:   integer
    :param year:  integer
    :return: bool
    """

    NUMDAYS = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year <=0:
        return False

    # Check whether the month is valid
    if month < 1 or month >12:
        return False

    # Leap YEAR
    if isLeapYear(year):
        NUMDAYS[1] = 29

    # Check the # days for a particular month
    if day<0 or day> NUMDAYS[month-1]:
        return False
    return True

def getPartsDate(*args, **kwargs):
    """
    Method to extract the month, day & year from
    a 'date' object which can have different formats:
       a. "MM/DD/YYYY"
       b. "MM"/mm , "DD"/dd   "YYYY"/yyyy
       c. dictionary:
          month="MM"/mm
          day="DD"/dd
          year="YYYY"/yyyy
    It also checks whether the day, month fields are valid.

    If the day, month & year fields are valid, the function
    returns (True, month, day, year)
    Else if an error occurs -> (False,..,..,..)

    """
    isValid = False
    month,day,year = -1,-1,-1
    try:
        # Check the FORMAT
        if len(args) == 1:  #  Input string a la "MM/DD/YYYY"
            lst = args[0].split("/")
            if len(lst) !=3:
                raise mydateerror.MyDateError(" MyDate :: The string must be of the form 'MM/DD/YYYY'")
            else:
                month = int(lst[0])
                day = int(lst[1])
                year = int(lst[2])

        elif len(args) == 3:  # MM, DD, YY  (either as string or int)
            month = int(args[0])
            day = int(args[1])
            year = int(args[2])

        elif len(kwargs)==3:
            month = int(kwargs['month'])
            day = int(kwargs['day'])
            year = int(kwargs['year'])

        else:
            str  = " MyDate :: Supports the following input data "
            str += "           MyDate('MM/DD/YYYY') \n"
            str += "           MyDate( m, d , y) or MyDate('MM','DD','YY')\n"
            str += "           MyDate(month=m, day=d, year=y) or MyDate(month='MM', day='DD', year='YY')"
            raise mydateerror.MyDateError(str)

        # Check the RANGE
        if not(isDateInRange(month,day,year)):
            str = " MyDate :: Invalid Date"
            raise mydateerror.MyDateError(str)
        else:
            isValid = True

    except ValueError as e:
        print("  MyDate::{0}".format(e))

    except mydateerror.MyDateError as e:
        print(e.code)

    else:
        isValid = True

    finally:
        return (isValid,month,day,year)


if __name__ == "__main__":
     year = [1903, 1900, 1904, 2000]
     print("Check Leap Year Function:")
     for item in year:
         print("  Year:{0} Leap Year?{1}".format(item,isLeapYear(item)))

     print("Check where dates are in range::")
     datum = [[2,29,2012], [2,29,2013],[13,12,2015],[4,31,2012], [5,25,1972] ]
     for item in datum:
         print("  Date:{0:02d}/{1:02d}/{2:04d} -> In range:{3}".format(item[0],item[1],item[2],\
                            isDateInRange(item[0],item[1],item[2])))

     print("Get components of Date (Format & Range)::")
     res = getPartsDate("1/2/2013")
     print(res)

     res = getPartsDate("23/2013")
     print(res)

     res = getPartsDate(1,2,2013)
     print(res)

     res = getPartsDate("1","2","2013")
     print(res)

     res = getPartsDate(day="23",year="2005",month="11")
     print(res)

     res = getPartsDate(day=31, year=2017, month=4)
     print(res)
