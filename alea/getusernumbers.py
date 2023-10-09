import sys

def readFile(filename):
    """
    Read file with user numbers
    :param filename:
    :return:
    """
    try:
        f = open(filename,'r')
        arrLines = f.readlines()
        f.close()
        return arrLines
    except IOError:
        print("  File '{0}' can not be read".format(filename))
        sys.exit()

def getNumbers(arrLines,sep=''):
    """
    Retrieve the numbers
    The numbers are separated by blanks
    :param arr:
    :return:
    """
    res = []
    for line in arrLines:
        lst = line.strip().split(sep)
        res.append([int(item) for item in lst])
    return res


def findMatchingNumbers(userRows,drawingRows):
    """

    :param userRows:
    :param drawingsRows:
    :return:
    """
    regDrawingRows  =  [item[1:-2] for item in drawingRows]
    regUserRows     = [item[0:-1] for item in userRows]

    specDrawingRows = [item[-2] for item in drawingRows]
    specUserRows    = [item[-1] for item in userRows]

    # Loop over ALLE officiele trekkingen
    resReg = {}
    resSpec = {}
    for i, drawLst in enumerate(regDrawingRows):

        tmpReg, tmpSpec = [], []
        for j, userLst in enumerate(regUserRows):
            interSecReg = list(set(drawLst) & set(userLst))
            tmpReg.append(interSecReg)

            interSecSpec = list(set([specDrawingRows[i]]) &
                                set([specUserRows[j]]))
            tmpSpec.append(interSecSpec)

        resReg[str(drawingRows[i][0])]  = tmpReg
        resSpec[str(drawingRows[i][0])] = tmpSpec
    return (resReg,resSpec)

    print("\n       Date           Reg. Numbers                Spec. Numbers")
    for k in sorted(resReg.keys()):
        print("     '{0}'".format(k))
        for i in range(len(resReg[k])):
            print("         {0}       {1}".format(resReg[k][i],resSpec[k][i]))
    return

