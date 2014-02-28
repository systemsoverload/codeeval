import sys

MORSE = {
    '.-':'A',     '-...':'B',   '-.-.':'C',
    '-..':'D',    '.':'E',      '..-.':'F',
    '--.':'G',    '....':'H',   '..':'I',
    '.---':'J',   '-.-':'K',    '.-..':'L',
    '--':'M',     '-.':'N',     '---':'O',
    '.--.':'P',   '--.-':'Q',   '.-.':'R',
    '...':'S',    '-':'T',      '..-':'U',
    '...-':'V',   '.--':'W',    '-..-':'X',
    '-.--':'Y',   '--..':'Z',

    '-----':'0',  '.----':'1',  '..---':'2',
    '...--':'3',  '....-':'4',  '.....':'5',
    '-....':'6',  '--...':'7',  '---..':'8',
    '----.':'9'
}


def solve(l):
    morse_words = map(str.strip, l.split('  '))

    words = []

    for morse_word in morse_words:
        word = []
        for letter in morse_word.split():
           word.append(MORSE.get(letter))

        words.append(''.join(word))

    print ' '.join(words)

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        l = line.strip()
        if l:
            solve(l)