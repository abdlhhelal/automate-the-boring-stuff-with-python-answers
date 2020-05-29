def CommaCode(ListParameter):
    String=''
    for i in range(len(ListParameter)):

        String += ListParameter[i]
        if (i == (len(ListParameter)-2)):
            String += ' and '
        elif(i== (len(ListParameter)-1)):
            return String
        else:
            String += ', '
    return None
#arguments=[]
arguments = ['apples','bananas','tofu','cats']
String = CommaCode(arguments)
print(String)
