ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
REV_ALPHA = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
CODE = dict(zip(ALPHA,REV_ALPHA)) #creates a dictionary from two lists
                                  #first list becomes the keys
                                  #second list becomes the values

"""
CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
        '{':'[','[':'{','}':']',']':'}'}
"""

def main():
    choice = str(input("Do you want to (E)ncrypt or (D)ecrypt? "))
    if choice == 'E':
        plain_text_string = input('Enter a string of text to encrypt: ').upper()
        encrypted_text = convert_2_encrypted(plain_text_string)
        print(encrypted_text)
    else:
        encrypted_text_string = input('Enter a string of text to decrypt: ').upper()
        plain_text = convert_2_decrypted(encrypted_text_string)    
        print(plain_text)

def convert_2_encrypted(plain_text_string):

    encrypted_text_string = ''

    for ch in plain_text_string:

        if ch.isspace():
            encrypted_text_string += ch
        else:
            encrypted_text_string += CODE[ch]

    return encrypted_text_string

def convert_2_decrypted(encrypted_text_string):

    plain_text_string = ''

    for ch in encrypted_text_string:

        if ch.isspace():
            plain_text_string += ch
        else:
            plain_text_string += CODE[ch]

    return plain_text_string

if __name__ == "__main__":
    main()

