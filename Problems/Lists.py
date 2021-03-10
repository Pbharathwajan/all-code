
def cheemsify(text):
    text = text
    output = []
    vowels = 'aeiou '
    
    i = 0
    for i in text.split(' '):
        novow = [j for j in i if j not in vowels]
        try:
            cheemsdict = {'so':'such',
            "such":"so",
            "cheese":"cheems",
            'insert_english_word_here':'Insert_cheemse_word_here'
            
            }
            output.append(cheemsdict[i])
        except: 
            if len(novow) > 2:
                temp = i.rstrip('e')
                j = 0
                for x in range(len(i)):
                    if j < len(i)-1:
                        if temp[j-1] in vowels and temp[j] not in vowels+'m':
                            temp = temp[:j] + 'm' + temp[j:]
                            j+=1
                    j+=1
                output.append(temp.lstrip('m'))
            else:
                output.append(i)

    text = ' '.join(output)
    out = ''
    for i in range(len(text)):
        out += (text[i].upper() if i%2 else text[i])

    return outdef cheemsify(text):
    text = text
    output = []
    vowels = 'aeiou '
    
    i = 0
    for i in text.split(' '):
        novow = [j for j in i if j not in vowels]
        try:
            cheemsdict = {'so':'such',
            "such":"so",
            "cheese":"cheems",
            'insert_english_word_here':'Insert_cheemse_word_here'
            
            }
            output.append(cheemsdict[i])
        except: 
            if len(novow) > 2:
                temp = i.rstrip('e')
                j = 0
                for x in range(len(i)):
                    if j < len(i)-1:
                        if temp[j-1] in vowels and temp[j] not in vowels+'m':
                            temp = temp[:j] + 'm' + temp[j:]
                            j+=1
                    j+=1
                output.append(temp.lstrip('m'))
            else:
                output.append(i)

    text = ' '.join(output)
    out = ''
    for i in range(len(text)):
        out += (text[i].upper() if i%2 else text[i])

    return out