from . import aleainput
from . import extractCSV
from . import getfile
from . import getusernumbers

URLNAME = { "MM":"http://txlottery.org/export/sites/lottery/Games/Mega_Millions/Winning_Numbers/megamillions.csv",
            "PB":"http://txlottery.org/export/sites/lottery/Games/Powerball/Winning_Numbers/powerball.csv"}
 
def start(args=None):
    """
    The main routine
    """

    # Parse Input
    inp = aleainput.parseInput()

    # Read the User numbers from file
    arrLines = getusernumbers.readFile(inp[0])
    userArr  = getusernumbers.getNumbers(arrLines,sep=' ')
    print("  User Numbers::")
    for i, item in enumerate(userArr):
        print("    {0:2d} {1}".format(i,item))

    # From corresponding Data File find selRows
    myRead = getfile.RetrieveFileFromURL(URLNAME[inp[1]])
    content = extractCSV.ExtractCSV(myRead.filename, DEBUG=False)
    selRows = content.getSlice(t1=inp[2], t2=inp[3])
    print("  Selected Drawings for {0}".format(content.tag))
    for item in selRows:
        print("    {0}:: {1}".format(item[0],item[1:]))

    # Find Matching Numbers
    (resReg, resSpec) = getusernumbers.findMatchingNumbers(userArr,selRows)
    print("  Overlapping Numbers::")
    print("       Date            Reg. Num.     Spec. Num.")
    for k in sorted(resReg.keys()):
        print("    {0}".format(k))
        for i in range(len(resReg[k])):
            print("  {0:>8} {1:>20}    {2:>6}".format(i,str(resReg[k][i]),str(resSpec[k][i])))

if __name__ == "__main__":
    start()
