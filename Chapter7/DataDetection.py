import re

def dateDetection(date):
    dateRegex=re.compile(r'''(([0-3][0-9])    # Days
                              /               # Slash
                              ([0-1][0-9])    # Months
                              /               # Slash
                              ([1-2][0-9]{3}) # Years
                                                )''',re.VERBOSE)
    dateFound=dateRegex.findall(date)
    DMY=[]
    for groups in dateFound:
        Day=int(groups[1])
        Month=int(groups[2])
        Year=int(groups[3])
        if  Day<=31 and Month<=12:
            if  Day==31 and Month!=4 and Month!=6 and Month!=9 and Month!=11:
                DMY.append(groups[0])
            elif Day==30 and Month!=2:
                DMY.append(groups[0])
            elif Day==29 and Month==2 and Year%4==0:
                if not Year%100==0 and Year%400!=0:
                    DMY.append(groups[0])
            elif Day<=28:
                DMY.append(groups[0])
    for i in DMY:
        print(i)
    return None

date='32/10/2005 31/11/1996 31/10/1994 30/02/2003\
      30/05/2005 29/02/1900 29/02/2000 29/02/2002\
      29/02/2004 28/14/2006 28/02/2005 25/03/1997 '
dateDetection(date)
