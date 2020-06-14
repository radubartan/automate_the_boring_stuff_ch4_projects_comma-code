
def commaFunction(userEnteredList, inputValue):
    i = 0
    while i < len(userEnteredList):
        if inputValue == '':
            #userEnteredList = userEnteredList + listOnlyContainsAnd
            userEnteredList = userEnteredList + ['and']
            userEnteredList[len(userEnteredList)-1] = userEnteredList[len(userEnteredList)-2]
            userEnteredList[len(userEnteredList)-2] = 'and'
            print('userEnteredList: ' + ' '.join(userEnteredList))
            break    
        break
        i = i + 1
    

userEnteredList = []
finalList = []
while True:
    print('Enter a value in the list (or enter nothing to stop.):')
    inputValue = input()
    if inputValue == '':
        commaFunction(userEnteredList, inputValue)
        break
    userEnteredList = userEnteredList + [inputValue]
    print('The values entered are:')
    for inputValue in userEnteredList:
        print(' ' + inputValue)


