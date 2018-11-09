import shutil, os, re
def main(inputpath):
    datePattern = re.compile(r"""^(.*?)              # all text before the date
                         ((0|1)?\d)-             # one or two digits for the month
                         ((0|1|2|3)?\d)-         # one or two digits for the day
                         ((19|20)\d\d)           # four digits for the year
                         (.*?)$                   # all text after the date
                          """, re.VERBOSE)
    for amerFilename in os.listdir(os.path.abspath(inputpath)):
        mo = datePattern.search(amerFilename)
        if mo == None:
            continue
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))

if __name__ == '__main__':
    inputpath = '.\\resource'
    main(inputpath)