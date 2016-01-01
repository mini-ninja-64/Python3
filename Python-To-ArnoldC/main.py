FileLocation=input("""Python File (try not to use =, (), ", ', in strings): """)

pyFile=open(FileLocation,'r')

for line in pyFile:
    formattedLine=line.replace(" ","")
    formattedLine=formattedLine.replace('\n', '').replace('\r', '')
    arnCEquiv=""
    if (("=input") in formattedLine): #input
        varName=formattedLine.split('=')[0]
        arnCEquiv=arnCEquiv + 'CHRISTMAS TREE ' + varName + '\n'
        arnCEquiv=arnCEquiv + '\t' + 'YOU SET US UP 0' + '\n' + '\n'

        inputString = ((line.split('input')[1]).replace("'",'"').split('"'))[1]  #[:-1])[1:].replace("'",'"').replace(" ","") <-- old stuff
        if not inputString=="":
            arnCEquiv=arnCEquiv+'TALK TO THE HAND "' + inputString +'"'+ '\n'
        arnCEquiv=arnCEquiv+'GET YOUR ASS TO MARS '+varName+ '\n'
        arnCEquiv=arnCEquiv+'DO IT NOW'+'\n'
        arnCEquiv=arnCEquiv+'I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY'
    elif ((("=") in formattedLine)) and (not("if") in formattedLine) and (not("==") in formattedLine): #variable decleration
        varName=formattedLine.split('=')[0]
        arnCEquiv=arnCEquiv + 'CHRISTMAS TREE ' + varName + '\n'
        arnCEquiv=arnCEquiv + '\t' + 'YOU SET US UP ' + (formattedLine.split('=')[1]) + '\n'


    if not line.strip():
        print("")
    else:
        if not (arnCEquiv == ""):
            print("")
            print(arnCEquiv)
