__author__ = 'sleipnir'
import datetime
import os
import sys
import urllib.request

class RetrieveFileFromURL(object):

    def __init__(self, urlname):
        """
        Constructor of the ReadURL class
        :param urlname: Name of the URL to be read
        :return:
        """
        self.filename = None
        try:
            g = urllib.request.urlopen(urlname)

            # Retrieve MM-DD-YY
            today = datetime.date.today()
            str_today = str(today.month) + "-" + str(today.day) + "-" + str(today.year)
 
            # Write file as MM-DD-YY-filename to pwd
            lst = urlname.split("/")
            self.filename = lst[-1].strip().lower()
            self.filename = str_today + "-" + self.filename
            with open(self.filename,'b+w') as f:
                f.write(g.read())            
        except:
            print("  URL '{0}' can't be opened".format(urlname))
            sys.exit()

    def __del__(self):
        try:
            if self.filename is not None:
                print("  Removing (temp) file '{0}'".format(self.filename))
                os.remove(self.filename)
        except OSError:
            print("   Error removing '{0}'".format(self.filename))

if __name__ == "__main__" :
    urlname1 = "http://txlottery.org/export/sites/lottery/Games/Mega_Millions/Winning_Numbers/megamillions.csv"
    urlname2 = "http://txlottery.org/export/sites/lottery/Games/Powerball/Winning_Numbers/powerball.csv"

    myFileRead = RetrieveFileFromURL(urlname1)
    if myFileRead.filename is not None:
       print("  File (temp):'{0}'".format(myFileRead.filename))