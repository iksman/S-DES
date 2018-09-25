#key = int(input("Key ?>"),2)
#choice = input("1= encrypt, 2= decrypt ?>")
#string = int(input("Input text ?>"),2)

def permutate(permeation, inp):
    result = ""

    for letter in permeation:
        index = int(letter) - 1
        result += inp[index]

    return result

def XORstring(inp1, inp2):
    result = ""
    if len(inp1) == len(inp2):
        for i in range(0, len(inp1)):
            result += str(int(inp1[i],2) ^ int(inp2[i],2))
    return result

def LeftShift(inp, characters):
    if characters == 0:
        return inp
    else:
        result = inp[1:]
        result += inp[:1]
        return LeftShift(result, characters - 1)

def StitchHalves(array):
    return array[0] + array[1]

def GetLetter(binary):
    result = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
    if len(binary) == 4:
        return result[int(binary,2)]
    else:
        return Exception("binary input not in 4bit size")

def genKeys(key):
    P1 = permutate(["3","5","2","7","4","10","1","9","8","6"], key)
    LS1halves = [
        LeftShift(  P1[:5],  1), 
        LeftShift(  P1[5:],  1)
    ]
    Key1 = permutate(["6","3","7","4","8","5","10","9"], StitchHalves(LS1halves))
    LS2halves = [
        LeftShift(  LS1halves[0],  2),
        LeftShift(  LS1halves[1],  2)
    ]
    Key2 = permutate(["6","3","7","4","8","5","10","9"], StitchHalves(LS2halves))
    return [Key1, Key2]

def GetFromMatrix(row, column, s):
    
    s0 = [["01","00","11","10"],["11","10","01","00"],["00","10","01","11"],["11","01","11","00"]]
    s1 = [["00","01","10","11"],["10","00","01","11"],["11","00","01","00"],["10","01","00","11"]]
    
    sToUse = s0
    if s == 1:
        sToUse = s1

    return sToUse[row][column]

def Algorithm(keys, text, choice="2"):
    keysToUse = keys
    if choice == "2":
        keysToUse = [keys[1], keys[0]]

    P1 = permutate(["2","6","3","1","4","8","5","7"], text)

    step1 = AlgoStep(keysToUse[0], P1)
    switch = step1[4:] + step1[:4]
    step2 = AlgoStep(keysToUse[1], switch)

    return permutate(["4","1","3","5","7","2","8","6"], step2)
    



def AlgoStep(key, text):
    
    FirstHalves = [
        text[:4],
        text[4:]
    ]
    EP = permutate(["4","1","2","3","2","3","4","1"], FirstHalves[1])
    xoredString = XORstring(EP, key)

    s0bits = GetFromMatrix(int((xoredString[0] + xoredString[3]),2), int((xoredString[1] + xoredString[2]),2),0)
    s1bits = GetFromMatrix(int((xoredString[4] + xoredString[7]),2), int((xoredString[5] + xoredString[6]),2),1)

    FirstF = permutate(["2","4","3","1"],(s0bits + s1bits))
    xoredFirstF = XORstring(FirstF, FirstHalves[0])
    return xoredFirstF + FirstHalves[1]
    
    
    
    
key = input("Key ?>")
text = input("Text ?>")
choice = input("1= encrypt, 2= decrypt ?>")
keys = genKeys(key)
output = Algorithm(keys, text, choice)
print("Output = " + output)
Letter1 = GetLetter(output[:4])
Letter2 = GetLetter(output[4:])
print("Letters: " + Letter1 + Letter2)

