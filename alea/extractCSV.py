__author__ = 'sleipnir'
import csv
import sys
from . import mydate

class ExtractCSV(object):
    """
    Class to read a CSV file
    """
    def __init__(self, filename, DEBUG=False):
        """
        Constructor of
        :param filename: Name of the file
        :param DEBUG : Default is false
        """
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                self.array=[]
                for row in reader:
                    self.tag = row[0].upper()
                    tmp = [int(item) for item in row[1:]]
                    d = mydate.MyDate(tmp[0],tmp[1],tmp[2])
                    res = [d]
                    res += tmp[3:]
                    self.array.append(res)
        except TypeError as e:
            print(e)
            sys.exit()
        except:
            self.tag = "---"
            print("  ERROR:{0}".format(sys.exc_info()[0]))
            sys.exit()

        if DEBUG is True:
            print("  #Lines:{0}".format(len(self.array)))
            print("  #El. per line:{0}".format(len(self.array[0])))

    def getSlice(self, t1, t2):
        """
        Method to extract those lines from the array
        where t1 <= t <= t2
        :return: selRows
        """
        selRows = []
        for row in self.array:
            t = row[0]
            if t1 <= t <= t2:
                selRows.append(row)
        return selRows

if __name__ == "__main__":
    import getfile
    import mydate
    urlname= ["http://txlottery.org/export/sites/lottery/Games/Mega_Millions/Winning_Numbers/megamillions.csv",
              "http://txlottery.org/export/sites/lottery/Games/Powerball/Winning_Numbers/powerball.csv"]
    for item in urlname:
        print("\n  Read URL:'{0}'".format(item))
        myRead = getfile.RetrieveFileFromURL(item)
        content = ExtractCSV(myRead.filename,DEBUG=False)
        selRows = content.getSlice(t1=mydate.MyDate(6,10,2016),t2=mydate.MyDate(7,18,2016))
        print("  #Selected Rows for '{0}'::{1}".format(content.tag, len(selRows)))
        for item in selRows:
            print("    {0}".format(item))
