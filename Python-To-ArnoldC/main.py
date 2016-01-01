#Functions
def stringOrVar(normLine, formatLine):
    var=False
    str=False
    if '"' in formatLine:
        str = True

    else:
        var= True

    if str:
        return ("string")
    elif var:
        return ("variable")

FileLocation=input("""Python File (try not to use =, (), ", ', input in strings, also dont use variable called temp123456): """)

pyFile=open(FileLocation,'r')

print("IT'S SHOWTIME")

print("HEY CHRISTMAS TREE temp123456\n\tYOU SET US UP 0\n")

pyFileVars=[]

for line in pyFile:
    formattedLine=line.replace(" ","")
    formattedLine=formattedLine.replace('\n', '').replace('\r', '')
    arnCEquiv=""

    #things like multipliction and stuff
    if (("+") in formattedLine):
        firstArg=((formattedLine.split('=')[1]).split('+')[0]).replace('(','').replace(')','')
        secondArg=((formattedLine.split('=')[1]).split('+')[1]).replace('(','').replace(')','')
        varToEdit=((formattedLine.split('=')[0]))

        if not varToEdit in pyFileVars:
            pyFileVars.append(varToEdit)
            arnCEquiv=arnCEquiv + 'HEY CHRISTMAS TREE ' + varToEdit + '\n'
            arnCEquiv=arnCEquiv + '\t' + 'YOU SET US UP 0' + '\n' + '\n'

        arnCEquiv= arnCEquiv + 'GET TO THE CHOPPER temp123456' + '\n'
        arnCEquiv= arnCEquiv + 'HERE IS MY INVITATION ' + firstArg + '\n'
        arnCEquiv= arnCEquiv + 'GET UP ' + secondArg + '\n'
        arnCEquiv= arnCEquiv + 'ENOUGH TALK' + '\n' + '\n'

        arnCEquiv= arnCEquiv +'GET TO THE CHOPPER ' + varToEdit + '\n'
        arnCEquiv= arnCEquiv + 'HERE IS MY INVITATION temp123456 ' + '\n'
        arnCEquiv= arnCEquiv + 'ENOUGH TALK' + '\n' + '\n'
    elif (("-") in formattedLine):
        firstArg=((formattedLine.split('=')[1]).split('-')[0]).replace('(','').replace(')','')
        secondArg=((formattedLine.split('=')[1]).split('-')[1]).replace('(','').replace(')','')
        varToEdit=((formattedLine.split('=')[0]))

        if not varToEdit in pyFileVars:
            pyFileVars.append(varToEdit)
            arnCEquiv=arnCEquiv + 'HEY CHRISTMAS TREE ' + varToEdit + '\n'
            arnCEquiv=arnCEquiv + '\t' + 'YOU SET US UP 0' + '\n' + '\n'

        arnCEquiv= arnCEquiv + 'GET TO THE CHOPPER temp123456' + '\n'
        arnCEquiv= arnCEquiv + 'HERE IS MY INVITATION ' + firstArg + '\n'
        arnCEquiv= arnCEquiv + 'GET DOWN ' + secondArg + '\n'
        arnCEquiv= arnCEquiv + 'ENOUGH TALK' + '\n' + '\n'

        arnCEquiv= arnCEquiv +'GET TO THE CHOPPER ' + varToEdit + '\n'
        arnCEquiv= arnCEquiv + 'HERE IS MY INVITATION temp123456 ' + '\n'
        arnCEquiv= arnCEquiv + 'ENOUGH TALK' + '\n' + '\n'
    elif (("*") in formattedLine):
        firstArg=((formattedLine.split('=')[1]).split('*')[0]).replace('(','').replace(')','')
        secondArg=((formattedLine.split('=')[1]).split('*')[1]).replace('(','').replace(')','')
        varToEdit=((formattedLine.split('=')[0]))

        if not varToEdit in pyFileVars:
            pyFileVars.append(varToEdit)
            arnCEquiv=arnCEquiv + 'HEY CHRISTMAS TREE ' + varToEdit + '\n'
            arnCEquiv=arnCEquiv + '\t' + 'YOU SET US UP 0' + '\n' + '\n'

        arnCEquiv= arnCEquiv + 'GET TO THE CHOPPER temp123456' + '\n'
        arnCEquiv= arnCEquiv + 'HERE IS MY INVITATION ' + firstArg + '\n'
        arnCEquiv= arnCEquiv + "YOU'RE FIRED " + secondArg + '\n'
        arnCEquiv= arnCEquiv + 'ENOUGH TALK' + '\n' + '\n'

        arnCEquiv= arnCEquiv +'GET TO THE CHOPPER ' + varToEdit + '\n'
        arnCEquiv= arnCEquiv + 'HERE IS MY INVITATION temp123456 ' + '\n'
        arnCEquiv= arnCEquiv + 'ENOUGH TALK' + '\n' + '\n'
    elif (("/") in formattedLine):
        firstArg=((formattedLine.split('=')[1]).split('/')[0]).replace('(','').replace(')','')
        secondArg=((formattedLine.split('=')[1]).split('/')[1]).replace('(','').replace(')','')
        varToEdit=((formattedLine.split('=')[0]))

        if not varToEdit in pyFileVars:
            pyFileVars.append(varToEdit)
            arnCEquiv=arnCEquiv + 'HEY CHRISTMAS TREE ' + varToEdit + '\n'
            arnCEquiv=arnCEquiv + '\t' + 'YOU SET US UP 0' + '\n' + '\n'

        arnCEquiv= arnCEquiv + 'GET TO THE CHOPPER temp123456' + '\n'
        arnCEquiv= arnCEquiv + 'HERE IS MY INVITATION ' + firstArg + '\n'
        arnCEquiv= arnCEquiv + 'HE HAD TO SPLIT ' + secondArg + '\n'
        arnCEquiv= arnCEquiv + 'ENOUGH TALK' + '\n' + '\n'

        arnCEquiv= arnCEquiv +'GET TO THE CHOPPER ' + varToEdit + '\n'
        arnCEquiv= arnCEquiv + 'HERE IS MY INVITATION temp123456 ' + '\n'
        arnCEquiv= arnCEquiv + 'ENOUGH TALK' + '\n' + '\n'

    #statements
    if (("=input") in formattedLine): #input
        varToEdit=formattedLine.split('=')[0]
        if not varToEdit in pyFileVars:
            pyFileVars.append(varToEdit)
            arnCEquiv=arnCEquiv + 'HEY CHRISTMAS TREE ' + varToEdit + '\n'
            arnCEquiv=arnCEquiv + '\t' + 'YOU SET US UP 0' + '\n' + '\n'

        if stringOrVar(line, formattedLine) == ("string"):
            inputString = ((line.split('input')[1]).replace("'",'"').split('"'))[1]  #[:-1])[1:].replace("'",'"').replace(" ","") <-- old stuff
        elif stringOrVar(line, formattedLine) == ("variable"):
            inputString =  (((formattedLine.split('input')[1]).replace("'",'"').split('('))[1])[:-1]  #[:-1])[1:].replace("'",'"').replace(" ","") <-- old stuff

        if not inputString=="":
            arnCEquiv=arnCEquiv+'TALK TO THE HAND "' + inputString +'"'+ '\n'
        arnCEquiv=arnCEquiv+'GET YOUR ASS TO MARS '+varToEdit+ '\n'
        arnCEquiv=arnCEquiv+'DO IT NOW'+'\n'
        arnCEquiv=arnCEquiv+'I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY'
    elif ((("=") in formattedLine)) and (not("if") in formattedLine) and (not("==") in formattedLine): #variable decleration
        varToEdit=formattedLine.split('=')[0]
        if stringOrVar(line, formattedLine) == "string:":
            if not varToEdit in pyFileVars:
                pyFileVars.append(varToEdit)
                arnCEquiv=arnCEquiv + 'HEY CHRISTMAS TREE ' + varToEdit + '\n'
                arnCEquiv=arnCEquiv + '\t' + 'YOU SET US UP ' + (formattedLine.split('=')[1])
        else:
            if not varToEdit in pyFileVars:
                pyFileVars.append(varToEdit)
                arnCEquiv=arnCEquiv + 'HEY CHRISTMAS TREE ' + varToEdit + '\n'
                arnCEquiv=arnCEquiv + '\t' + 'YOU SET US UP temp123456'
    #elif (("if") in formattedLine):#if statements
        #if (("==") in formattedLine):
        #elif (("<=") in formattedLine):
        #elif ((">=") in formattedLine):
        #elif (("<")) in formattedLine):
        #elif ((">")) in formattedLine):
    elif (("print") in formattedLine):
        if stringOrVar(line, formattedLine) == "string":
            textPrint=line.split('"')[1]
            arnCEquiv=arnCEquiv+'TALK TO THE HAND "' + textPrint +'"'+ '\n'
        else:
            varPrint=(formattedLine.split('(')[1])[:-1]
            arnCEquiv=arnCEquiv+'TALK TO THE HAND ' + varPrint + '\n'


    if not line.strip():
        print("")
    else:
        if not (arnCEquiv == ""):
            print(arnCEquiv)

print("YOU HAVE BEEN TERMINATED")
