import re

def def_parser(D):
    wordList = []
    wordForm = []
    defRanges = []
    parenDepth = 0
    print(D)
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
            regex = re.search('{a_link\|(.+?)$', word).group(1).split('}')
            if len(regex[1]) > 2 and regex[1][0] == ' ':
                wordForm.append([regex[0], regex[1][1:]])
            else:
                wordForm.append(regex)
        except AttributeError:
            try:
                regex = re.search('}([^{}]+?)$', word).group(1).split('(')
                if len(regex) == 1:
                    wordForm.append([regex[0], ''])
                else:
                    wordForm.append([regex[0], '('+'('.join(regex[1:])])
            except AttributeError:
                try:
                    regex = re.search('(\w+ *)+$',word)
                    wordForm.append([regex[0], ''])
                except AttributeError:
                    wordForm.append(None)
    for word in wordForm:
        if re.fullmatch(' +',word[1]):
            word[1] = ''
    return wordForm

if __name__ == "__main__":
    inExampleList = [
       # "{sx|fail||} {bc}fallarse (dícese de la vista, etc.), {a_link|gastarse} (dícese de pilas, etc.), {a_link|estropearse} (dícese de un motor, etc.)",
       # '{sx|path||} {sx|road||} {bc}{a_link|camino}, {a_link|vía} ',
       # "{sx|have||} {bc}{a_link|tener} (una garantía, etc.), {a_link|llevar} (una advertencia)",
        #"{sx|select||} {bc}decidirse por a",
        " reanudar algo"
    ]
    inExampleList = map(lambda x: def_parser(x),inExampleList)
    for res in inExampleList:
        print(res)
