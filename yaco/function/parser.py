import re

def def_parser(D):
    wordList = []
    wordForm = []
    defRanges = []
    parenDepth = 0
    for index in range(len(D)):
        if D[index] == ',' and not parenDepth:
            defRanges.append(index)
        elif D[index] == '(':
            parenDepth += 1
        elif D[index] == ')':
            parenDepth -= 1
    defRanges.append(len(D)+1)
    start = 0
    for word in defRanges:
        wordList.append(D[start:word])
        start = word+1
    for word in wordList:
        try:
            wordForm.append(re.search('{a_link\|(.+?)$', word).group(1).split("}"))
        except AttributeError:
            return None
    return wordForm

if __name__ == "__main__":
    inExampleList = [
        "{sx|fail||} {bc}fallarse (dícese de la vista, etc.), {a_link|gastarse} (dícese de pilas, etc.), {a_link|estropearse} (dícese de un motor, etc.)",
        '{sx|path||} {sx|road||} {bc}{a_link|camino}, {a_link|vía} ',
        "{sx|have||} {bc}{a_link|tener} (una garantía, etc.), {a_link|llevar} (una advertencia)"
    ]
    inExampleList = map(lambda x: def_parser(x),inExampleList)
    for res in inExampleList:
        print(res)
