from string import ascii_lowercase

def solution(myString):
    return "".join(['l' if i in ascii_lowercase[:ascii_lowercase.find('l')+1] else i for i in myString])