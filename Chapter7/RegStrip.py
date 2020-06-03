import re

def regStrip(*String):

    try:
        if String[1]!=True:
            StripChar=String[1]
    except:
        StripChar='\s'
    StripRegex = re.compile(r'^[%s]*((\w|\W)*?)[%s]*$'%(StripChar,StripChar))
    try:
        StrippedString=StripRegex.search(String[0]).group(1)
        return StrippedString
    except:
        return String[0]

String=',,,,,   ,, , , A 4s rsrsr sAIt''sWorking,,,,,,,,A4srs,A'
Stripped1=regStrip(String,'A, 4rs')
Stripped2=String.strip('A, 4rs')
print(Stripped1)
print(Stripped2)
print(Stripped1==Stripped2)
