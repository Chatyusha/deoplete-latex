
def TexAnalyzeLine(line):
    parsedline=[]
    word=""
    for i in line:
        if i == " " or i == "\t":
            pass
        elif i == "\\" or i == "\n":
            if word != "" and word != "\n":
                parsedline.append(word)
            word = ""
            word = word + i
        elif i == r"{" or i == r"}":
            if word != "" and word != "\n":
                parsedline.append(word)
            word = ""
            word = word + i
        elif i == r"[" or i == r"]":
            if word != "" and word != "\n":
                parsedline.append(word)
            word = ""
            word = word + i
        else:
            word = word + i

    return parsedline

def TexAnalyze(path):
    ParsedList=[]
    with open(path) as f:
        for s_line in f:
            s_line = s_line + "\n"
            if s_line[0] == "%":
                pass
            else:
                ParsedList += TexAnalyzeLine(s_line)
    return ParsedList

