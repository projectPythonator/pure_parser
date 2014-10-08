#Author: Chunpai Wang
#Email: cwang64@u.rochester.edu
#CSC254 HWK02 : Tokenizer

#build a tokenizer for C program with python2.7
import sys
import os

class Token:
    # constructor, token has two parameters (name and value)
    def __init__(self,token_name, token_value):
        self.token_name  = token_name
        self.token_value = token_value
    # return the name of token
    def get_name(self):
        return self.token_name
    # return the value of token
    def get_value(self):
        return self.token_value

class Scanner:
    # constructor can read file as a string,
    # remove all comments, 
    # and return a list of tokens.
    def __init__(self, file_name):
        self.infile = open(file_name,'r')
        #print self.infile.tell()
        #print self.infile.read(1)
        #print self.infile.tell()
        #self.infile.seek(0)
        #print self.infile.tell()
        self.cursor = 0
        if os.path.getsize(file_name) == 0:
            print 'Empty File!'
    
    """
    #peek next character, but not effect the infile position
    def peek_next(self, size):
        last_pos   = self.infile.tell()
        chars = self.infile.read(size)
        self.infile.seek(last_pos)
        return chars
    """
    
    # return the next token (as a Token object) or EOF
    # this function will remove the whitespace before see valid characters
    # and read the char by char to match the patterns
    def next_token(self):
        letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_']
        digit = ['0','1','2','3','4','5','6','7','8','9']
        ch = self.infile.read(1)
        while(ch == ' ' or ch == '\t' or ch == '\n' or ch =='\r'):
            ch = self.infile.read(1)
        if(ch == ' ' or ch == '\t' or ch == '\n' or ch =='\r'):
            self.infile.close()
        else:
            # detect identifiers and reserved words
            if ch.lower() in letter:
                value = ch
                if ch == 'i': # if char is 'i', then read the char until reach whitespcae or symbol, check if this identifier is the reserved word 'int'.
                    last_pos = self.infile.tell()  #remenber the position of char is reading.
                    next_ch = self.infile.read(1)  # read next char
                    while(next_ch.lower() in letter+digit):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    self.infile.seek(self.infile.tell() -1) # go back to last position of char where is reading
                    if value == 'int':
                        token = Token('type_name',value)
                        return token
                    elif value == 'if':
                        token = Token('reserved_words',value)
                        return token
                    else:
                        token = Token('identifier',value)
                        return token
                elif ch == 'v':
                    last_pos = self.infile.tell()
                    next_ch = self.infile.read(1)
                    while(next_ch.lower() in letter+digit):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    self.infile.seek(self.infile.tell() -1)
                    if value == 'void':
                        token = Token('type_name',value)
                        return token
                    else:
                        token = Token('identifier',value)
                        return token
                elif ch == 'w':
                    last_pos = self.infile.tell()
                    next_ch = self.infile.read(1)
                    while(next_ch.lower() in letter+digit):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    self.infile.seek(self.infile.tell() -1)
                    if value == 'while':
                        token = Token('reserved_words',value)
                        return token
                    else:
                        token = Token('identifier',value)
                        return token
                elif ch == 'r':
                    last_pos = self.infile.tell()
                    next_ch = self.infile.read(1)
                    while(next_ch.lower() in letter+digit):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    self.infile.seek(self.infile.tell() -1)
                    if value == 'return':
                        token = Token('reserved_words',value)
                        return token
                    else:
                        token = Token('identifier',value)
                        return token
                elif ch == 'c':
                    last_pos = self.infile.tell()
                    next_ch = self.infile.read(1)
                    while(next_ch.lower() in letter+digit):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    self.infile.seek(self.infile.tell() -1)
                    if value == 'continue':
                        token = Token('reserved_words',value)
                        return token
                    else:
                        token = Token('identifier',value)
                        return token
                elif ch == 'b':
                    last_pos = self.infile.tell()
                    next_ch = self.infile.read(1)
                    while(next_ch.lower() in letter+digit):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    self.infile.seek(self.infile.tell() -1)
                    if value == 'break':
                        token = Token('reserved_words',value)
                        return token
                    else:
                        token = Token('identifier',value)
                        return token
                elif ch == 's':
                    last_pos = self.infile.tell()
                    next_ch = self.infile.read(1)
                    while(next_ch.lower() in letter+digit):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    self.infile.seek(self.infile.tell() -1)
                    if value == 'scanf':
                        token = Token('reserved_words',value)
                        return token
                    else:
                        token = Token('identifier',value)
                        return token
                elif ch == 'p':
                    last_pos = self.infile.tell()
                    next_ch = self.infile.read(1)
                    while(next_ch.lower() in letter+digit):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    self.infile.seek(self.infile.tell() -1)
                    if value == 'printf':
                        token = Token('reserved_words',value)
                        return token
                    else:
                        token = Token('identifier',value)
                        return token
                elif ch == 'm':
                    last_pos = self.infile.tell()
                    next_ch = self.infile.read(1)
                    while(next_ch.lower() in letter+digit):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    self.infile.seek(self.infile.tell() -1)
                    if value == 'main':
                        token = Token('identifier',value)
                        return token
                    else:
                        token = Token('identifier',value)
                        return token
                elif ch == 'f':
                    last_pos = self.infile.tell()
                    next_ch = self.infile.read(1)
                    while(next_ch.lower() in letter+digit):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    self.infile.seek(self.infile.tell() -1)
                    if value == 'for':
                        token = Token('reserved_words',value)
                        return token
                    else:
                        token = Token('identifier',value)
                        return token
                else: 
                    next_ch = self.infile.read(1)
                    while(next_ch.lower() in letter+digit):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    new_pos = self.infile.tell() - 1
                    self.infile.seek(new_pos)
                    token = Token('identifier',value)
                    return token
            #detect numbers
            elif ch in digit:
                value = ch
                next_ch = self.infile.read(1)
                while(next_ch in digit):
                    value += next_ch
                    next_ch = self.infile.read(1)
                if next_ch.lower() in letter:
                    print 'ERROR: illegal token \"'+ value + next_ch +'\"'
                else:
                    new_pos = self.infile.tell() -1
                    self.infile.seek(new_pos)
                    token = Token('number',value)
                    return token
            #detect symbols
            elif ch in ['*','(',')','[',']','{','}',',',';']:
                token = Token('symbol',ch)
                self.cursor = self.infile.tell()
                return token
            elif ch in ['+','-','=','&','|']:
                last_pos = self.infile.tell()
                next_ch = self.infile.read(1)
                if next_ch == ch :
                    token = Token('symbol',ch+next_ch)
                    return token
                else:
                    self.infile.seek(last_pos)
                    token = Token('symbol',ch)
                    return token
            elif ch in ['>','<']:
                last_pos = self.infile.tell()
                next_ch = self.infile.read(1)
                if next_ch == '=':
                    token = Token('symbol',ch+next_ch)
                    return token
                else:
                    self.infile.seek(last_pos)
                    token = Token('symbol',ch)
                    return token
            elif ch == '!':
                last_pos = self.infile.tell()
                next_ch = self.infile.read(1)
                if next_ch == '=':
                    token = Token('symbol',ch+next_ch)
                    return token
                else:
                    raise SyntaxError('ERROR: illegal token \"!\"')
            #detect forward slash and meta_statements
            elif ch == '/':
                value = ch
                last_pos = self.infile.tell()
                next_ch = self.infile.read(1)
                if next_ch == '/':
                    value += next_ch
                    while(next_ch != '\n'):
                        value += next_ch
                        next_ch = self.infile.read(1)
                    token = Token('meta_stmt',value)
                    #return token
                    return self.next_token()
                elif next_ch == '*':
                    value += next_ch
                    next_ch = self.infile.read(2)
                    while(next_ch != '*/'):
                        value += next_ch[0]
                        new_pos = self.infile.tell()-1
                        self.infile.seek(new_pos)
                        next_ch = self.infile.read(2)
                    if next_ch == '*/':
                        value += next_ch
                        token = Token('meta_stmt',value)
                        #return token
                        return self.next_token()
                    else:
                        raise SyntaxError('ERROR: NOT MATCH OF \"/*\"')
                else:
                    self.infile.seek(last_pos)
                    token = Token('symbol','/')
                    return token
            elif ch == '#':
                #print 'hahahahhahhhaha'
                value = ch
                #print value
                while(ch != '\n'):
                    ch = self.infile.read(1)
                    value += ch
                    #print value
                #print ch
                token = Token('meta_stmt',value)
                #return token
                return self.next_token()

            #detect string
            elif ch in ['\"','\'']:
                value = ch
                next_ch = self.infile.read(1)
                while(next_ch != ch):
                    value += next_ch
                    next_ch = self.infile.read(1)
                    if not next_ch:
                        break
                if next_ch == ch:
                    value += next_ch
                    token = Token('string',value)
                    return token
                else:
                    raise SyntaxError('ERROR: illegal quotation mark')
            elif not ch:
                token = Token('eof','$$')
                return token
            else:
                print 'ERROR: illegal token \"'+value+'\"'


if __name__ == "__main__":
    output_file = open('output_file.c','w')
    scanner = Scanner(sys.argv[1])
    token = scanner.next_token()
    while token.get_name() != 'eof': # while not END of FILE
        print (token.get_name(),token.get_value())
        if token.get_name() == 'identifier':
            output_file.write(token.get_value()+'_cs254'+' ')
        else:
            output_file.write(token.get_value()+' ')
        token = scanner.next_token()
    output_file.close()
     


    """
    letter = '[a-zA-Z|_]'
    digit  = '[0-9]'
    identifier = letter+'('+letter+'|'+digit +')*'
    number = '(' + digit+ ')+'
    reserverd_word = 'int|void|if|while|return|continue|break|scanf|printf'
    symbol = '\(|\)|\[|\]|\{|\}|,|;|\+|-|\*|/|==|!=|>|<|>=|<=|=|&&|(\|\|)|&'
    string = '(\'.*\')|(\".*\")'
    meta_stmt = '(#|//).*\n'
    """
