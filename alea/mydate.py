__author__ = 'sleipnir'
import sys

class MyDate(object):
    """
    This class has been designed to compare dates of the
    type MM/DD/YYYY
    """
    def __init__(self,month,day,year):
        """
        :param args:
        """
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def cmp(self,other):
        """
        Compares self with other date
        If self<other
            return -1
        Elseif self == other
            return 0
        Else (self > other)
            return 1
        """
        if self.year > other.year:
            return 1
        elif self.year < other.year:
            return -1
        else:  # self.year == other.year
            if self.month > other.month:
                return 1
            elif self.month < other.month:
                return -1
            else:  # self.month == other.month
                if self.day > other.day:
                    return 1
                elif self.day < other.day:
                    return -1
                else:
                    return 0

    def __eq__(self,other):
        if self.cmp(other) == 0:
            return True
        return False

    def __ge__(self,other):
        if self.cmp(other) == 1 or self.cmp(other) == 0:
            return True
        return False

    def __gt__(self,other):
        if self.cmp(other) == 1:
            return True
        return False

    def __le__(self,other):
        if self.cmp(other) == -1 or self.cmp(other) == 0:
            return True
        return False

    def __lt__(self,other):
        if self.cmp(other) == -1:
            return True
        return False

    def __ne__(self, other):
        if self.cmp(other) !=0 :
            return True
        return False

    def __str__(self):
        str= "{0:02d}/{1:02d}/{2:04d}".format(self.month,self.day,self.year)
        return str

    def __repr__(self):
        str= "MyDate({0:d},{1:d},{2:d})".format(self.month,self.day,self.year)
        return str

if __name__ == "__main__":
    print("Testing Module:")
    d1 = MyDate(3,5,2014)
    d2 = MyDate(3,4,2014)
    print("  {0} <  {1}: {2}".format(d1,d2,d1<d2))
    print("  {0} <= {1}: {2}".format(d1,d2,d1<=d2))
    print("  {0} >= {1}: {2}".format(d1,d2,d1>=d2))
    print("  {0} == {1}: {2}".format(d1,d2,d1==d2))
    print("  {0} >  {1}: {2}".format(d1,d2,d1>d2))
    print("  {0} != {1}: {2}".format(d1,d2,d1!=d2))

    d1 = MyDate(4,1,2014)
    d2 = MyDate(3,1,2014)
    print("\n  {0} <  {1}: {2}".format(d1,d2,d1<d2))
    print("  {0} <= {1}: {2}".format(d1,d2,d1<=d2))
    print("  {0} >= {1}: {2}".format(d1,d2,d1>=d2))
    print("  {0} == {1}: {2}".format(d1,d2,d1==d2))
    print("  {0} >  {1}: {2}".format(d1,d2,d1>d2))
    print("  {0} != {1}: {2}".format(d1,d2,d1!=d2))

    d1 = MyDate(3,12,2015)
    d2 = MyDate(3,12,2016)
    print("\n  {0} <  {1}: {2}".format(d1,d2,d1<d2))
    print("  {0} <= {1}: {2}".format(d1,d2,d1<=d2))
    print("  {0} >= {1}: {2}".format(d1,d2,d1>=d2))
    print("  {0} == {1}: {2}".format(d1,d2,d1==d2))
    print("  {0} >  {1}: {2}".format(d1,d2,d1>d2))
    print("  {0} != {1}: {2}".format(d1,d2,d1!=d2))

    d1 = MyDate(7,14,2016)
    d2 = MyDate(7,14,2016)
    print("\n  {0} <  {1}: {2}".format(d1,d2,d1<d2))
    print("  {0} <= {1}: {2}".format(d1,d2,d1<=d2))
    print("  {0} >= {1}: {2}".format(d1,d2,d1>=d2))
    print("  {0} == {1}: {2}".format(d1,d2,d1==d2))
    print("  {0} >  {1}: {2}".format(d1,d2,d1>d2))
    print("  {0} != {1}: {2}".format(d1,d2,d1!=d2))

    res = [d1]
    res += [1,2,3]
    print("\n  Resulting List:{0}".format(res))
    print("  Date d1:{0}".format(res[0]))
    print("  Type:{0}".format(type(res[0])))

    print("  Is d1 an instance of MyDate class:{0}".format(isinstance(d1,MyDate)))
