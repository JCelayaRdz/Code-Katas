def pig_it(text):
    res = []
    marks = ['.','?',',','!',':',';']
    for word in text.split(' '):
        if word not in marks:
            first_letter = word[0]
            substr = word[1:len(word)]
            res.append(substr+first_letter+'ay')
        else:
            res.append(word)
    return ' '.join(res)

        

assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
assert pig_it('This is my string') == 'hisTay siay ymay tringsay'