# a b c d e f g h i j k l m n o p q r s t u v w x y z

#alpha = "abcdefghijklmnopqrstuvwxyz"
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Calpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphalength = len(alpha)

def convert(text):
    text1 = ""
    textlength = len(text)
    for i in range(0, textlength):
            for j in range(0, alphalength):
                if text[i].islower():
                    if text[i] == alpha[j]:
                        if j+13 < alphalength:
                            text1 += alpha[j + 13]
                            break
                        else:
                            j = (j+13) - alphalength
                            text1 += alpha[j]
                            break
                elif text[i].isupper():
                    if text[i] == Calpha[j]:
                        if j+13 < alphalength:
                            text1 += Calpha[j + 13]
                            break
                        else:
                            j = (j+13) - alphalength
                            text1 += Calpha[j]
                            break
                else:
                    text1 += text[i]
                    break
    return text1
