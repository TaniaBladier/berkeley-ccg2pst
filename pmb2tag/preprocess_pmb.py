import re

def right_replace(s, old, new, count):
    return (s[::-1].replace(old[::-1], new[::-1], count))[::-1]


def has_several_brackets(string):
    count = string.count('(')
    if count > 1:
        return True


def replace_brackets(str):
    if has_several_brackets(str):
        str = str.replace('(','-###-',1)
        str = right_replace(str,')','-$$$-',1)
        str = str.replace('(','{').replace(')', '}')
        str = str.replace('-###-', '(').replace('-$$$-', ')')
        return str
    else:
        return str

def readFile_ccg_prolog(path):
    sentences = []
    sentence = []
    for line in open(path, 'r'):
        line = line.rstrip().replace(',,', '$comma$,')

        if len(line) == 0 or line.startswith(':-'):
            if len(sentence) > 0:
                sent_str = ' '.join(sentence)[:-1].replace('CONJ', 'conj')
                sentences.append(sent_str)
                sentence = []
        else:
            if ']' in line:# lexical lines
                # find the lexical element
                lex = line.split(', ')[1].replace("'", "").replace('(','-LRB-').replace(')','-RRB-')

                pos_tag = re.sub(r".+pos:'([A-Z.$]+)'.+", r'\1', line)

                ccg_cat = line.split(',')[0].replace('t(','').strip().upper()
                ccg_cat = re.sub(r":([A-Z.]+)", lambda m: m.expand(r'[\1]').lower() , ccg_cat)
                
                brackets = line.split("']")[1]
                brackets = "".join(c for c in brackets if c==')')

                w = '(<L ' + ccg_cat + ' ' + pos_tag + ' ' + pos_tag + ' ' + lex + ' ' + ccg_cat + '>' + brackets

                sentence.append(w)
            else:
                if not line.startswith('ccg'):
                    line = line.strip().upper()
                    #print(line)
                    first_cat = re.sub(r"^([A-Z]+)\(.+", r"\1", line)
                    ccg_cat = re.sub(r"^[A-Z]+\((.+)", r"\1", line)[:-1]
                    ccg_cat = re.sub(r":([A-Z.]+)", lambda m: m.expand(r'[\1]').lower() , ccg_cat)
                    ccg_cat = ccg_cat.split(',')[0]
                    #print(first_cat)
                    print(ccg_cat)
                    w = '(<' + first_cat + ' ' + ccg_cat + '>'
                    sentence.append(w)
    if len(sentence) > 0:
            sentences.append(' '.join(sentence)[:-1].replace('CONJ', 'conj'))
    return sentences

input_ccg_file = '/home/tania/Dropbox/berkeley-ccg2pst/pmb2tag/example.pmb'
#input_ccg_file = '/home/tania/Dropbox/berkeley-ccg2pst/pmb2tag/pmb-3.0.0-en-gold-p03.parse.tags'

output_ccgbank_style = '/home/tania/Dropbox/berkeley-ccg2pst/pmb2tag/pmb_in_ccgbank_format.pmb'
outf = open(output_ccgbank_style, 'w')

ccg_trees_lst = readFile_ccg_prolog(input_ccg_file)

for x in ccg_trees_lst:
    outf.write(x + '\n')


outf.close()
