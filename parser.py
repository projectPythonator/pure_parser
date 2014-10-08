#!/usr/bin/env python
#Author: Chunpai Wang
#Email: cwang64@u.rochester.edu
import tokenizer
import sys


class Parser:
    def __init__(self,scanner):
        self.scanner = scanner
        self.input_token = scanner.next_token()    
        self.variables  = 0
        self.functions  = 0
        self.statements = 0
    
    #match by token_value or token_name(token type)
    def match(self,attribute,expected_token):
        if attribute == 'name':
            if self.input_token.get_name() == expected_token:
                #print self.input_token.get_value()
                self.input_token = self.scanner.next_token()
            else:
                raise SyntaxError('Not Match !')
        elif attribute == 'value':
            if self.input_token.get_value() == expected_token:
                #print self.input_token.get_value()
                self.input_token = self.scanner.next_token()
            else:
                raise SyntaxError('Not Match !')

    def program(self):
        if self.input_token.get_value() in ['int','void']:
            self.data_decls()
            self.func_list()
        elif self.input_token.get_value() == '$$':
            print 'pass'
        else:
            raise SyntaxError('ERROR1!!!')

    def func_list(self):
        if self.input_token.get_value() in ['int','void']:
            self.func()
            self.func_list()
        elif self.input_token.get_value() == '$$':
            pass
        else:
            raise SyntaxError('ERROR2!!!')

    def func(self):
        if self.input_token.get_value() in ['int','void']:
            self.func_decl()
            self.func_tail()
        else:
            raise SyntaxError('ERROR2!!!')

    def func_tail(self):
        #print self.input_token.get_value() +'hahahah'
        if self.input_token.get_value() == ';':
            self.match('value',';')
        elif self.input_token.get_value() == '{':
            self.match('value','{')
            self.functions += 1
            self.data_decls()
            #print self.input_token.get_name() +'88888ah'
            self.stmts()
            self.match('value','}')
        else:
            raise SyntaxError('ERROR3!!!')

    def func_decl(self):
        if self.input_token.get_value() in ['int','void']:
            self.type_name()
            self.match('name','identifier')
            self.match('value','(')
            self.parameter_list()
            self.match('value',')')
        else:
            raise SyntaxError('ERROR4!!!')

    def type_name(self):
        if self.input_token.get_value() in ['int','void']:
            self.match('value',self.input_token.get_value())
        else:
            raise SyntaxError('ERROR5!!!')

    def parameter_list(self):
        if self.input_token.get_value() == 'void':
            self.match('value','void')
        elif self.input_token.get_value() == 'int':
            self.non_empty_list()
        elif self.input_token.get_value() == ')':
            pass
        else:
            raise SyntaxError('ERROR6!!!')

    def non_empty_list(self):
        if self.input_token.get_value() == 'int':
            self.variables += 1
            self.match('value','int')
            self.match('name','identifier')
            self.non_empty_list_prime()
        else:
            raise SyntaxError('ERROR7!!!')

    def non_empty_list_prime(self):
        if self.input_token.get_value() == ',':
            self.variables += 1
            self.match('value',',')
            self.match('value','int')
            self.match('name','identifier')
            self.non_empty_list_prime()
        elif self.input_token.get_value() == ')':
            pass
        else:
            raise SyntaxError('ERROR8!!!')


    # since data_decls can be empty and func_lists can be empty too.
    # And both start with type_name ID, we need to peek 3 tokens to check 
    # which production rule to use.
    def data_decls(self):
        #print self.input_token.get_value()
        last_pos = self.scanner.infile.tell()
        last_token = self.input_token
        #print last_pos
        if self.input_token.get_value() in ['int']:
            next_token = self.scanner.next_token()
            #print next_token.get_value()
            if next_token.get_name() == 'identifier':
                next_token = self.scanner.next_token()
                if next_token.get_value() in ['[',',',';']:
                    self.scanner.infile.seek(last_pos)
                    self.input_token = last_token
                    self.type_name()
                    self.id_list()
                    self.match('value',';')
                    self.data_decls()
                elif next_token.get_value() == '(':
                    self.scanner.infile.seek(last_pos)
                    self.input_token =  last_token
                    pass
                else:
                    raise SyntaxError('ERROR9!!!')
            else:
                self.scanner.infile.seek(last_pos)
                self.input_token = last_token
                raise SyntaxError('ERROR10!!!')
        elif self.input_token.get_name() in ['identifier','reserved_words','eof','type_name']:
            pass
        else:
            raise SyntaxError('ERROR11!!!')

    def id_list(self):
        if self.input_token.get_name() == 'identifier':
            self.id_()
            self.variables += 1
            self.id_list_prime()
        else:
            raise SyntaxError('ERROR12!!!')

    def id_list_prime(self):
        if self.input_token.get_value() == ',':
            self.match('value',',')
            self.id_()
            self.variables += 1
            self.id_list_prime()
        elif self.input_token.get_value() == ';':
            pass
        else:
            raise SyntaxError('ERROR13!!!')

    def id_(self):
        if self.input_token.get_name() == 'identifier':
            self.match('name','identifier')
            self.id_tail()
        else:
            raise SyntaxError('ERROR14!!!')

    def id_tail(self):
        if self.input_token.get_value() == '[':
            self.match('value','[')
            self.expression()
            self.match('value',']')
        elif self.input_token.get_value() in [',','==',';']:
            pass
        else:
            raise SyntaxError('ERROR15!!!')

    def block_stmts(self):
        if self.input_token.get_value() == '{':
            self.match('value','{')
            self.stmts()
            self.match('value','}')
        elif self.input_token.get_name() == 'identifier':
            self.statement()
        elif self.input_token.get_value() in ['printf','scanf','if','while','return','break','continue','for']: 
            self.statement()
        else:
            raise SyntaxError('ERROR16!!!')

    def stmts(self):
        if self.input_token.get_name() in ['identifier','reserved_words','type_name']:
            self.statement()
            self.stmts()
        elif self.input_token.get_value() == '}':
            pass
        else:
            raise SyntaxError('ERROR17!!!')

    # since assignment and general function both start with ID
    def statement(self):
        self.statements += 1
        if self.input_token.get_name() == 'identifier':
            self.match('name','identifier')
            if self.input_token.get_value() in ['[','=','++','--']:
                self.assignment()
            elif self.input_token.get_value() == '(':
                self.general_func_call()
            else:
                print self.input_token.get_value()
                raise SyntaxError('ERROR18!!!')
        elif self.input_token.get_value() == 'printf':
            self.printf_func_call()
        elif self.input_token.get_value() == 'scanf':
            self.scanf_func_call()
        elif self.input_token.get_value() == 'if':
            self.if_else_stmt()
        elif self.input_token.get_value() == 'while':
            self.while_stmt()
        elif self.input_token.get_value() == 'return':
            self.return_stmt()
        elif self.input_token.get_value() == 'break':
            self.break_stmt()
        elif self.input_token.get_value() == 'continue':
            self.continue_stmt()
        elif self.input_token.get_value() == 'for':
            self.for_stmt()
        else:
            raise SyntaxError('ERROR19!!!')
    
    def assignment(self):
        if self.input_token.get_value() == '[':
            self.id_tail()
            self.match('value','=')
            self.expression()
            self.match('value',';')
        elif self.input_token.get_value() == '=':
            self.match('value','=')
            self.expression()
            self.match('value',';')
        elif self.input_token.get_value() in ['++','--']:
            self.double_plus_or_minus()
            self.match('value',';')
        else:
            raise SyntaxError('ERROR20!!!')

    def general_func_call(self):
        if self.input_token.get_value() == '(':
            self.match('value','(')
            self.expr_list()
            self.match('value',')')
            self.match('value',';')
        else:
            raise SyntaxError('ERROR21!!!')


    def printf_func_call(self):
        if self.input_token.get_value() == 'printf':
            self.match('value','printf')
            self.match('value','(')
            self.match('name','string')
            self.printf_func_call_tail()
        else:
            raise SyntaxError('ERROR22!!!')

    def printf_func_call_tail(self):
        if self.input_token.get_value() == ')':
            self.match('value',')')
            self.match('value',';')
        elif self.input_token.get_value() == ',':
            self.match('value',',')
            self.expression()
            self.match('value',')')
            self.match('value',';')
        else:
            raise SyntaxError('ERROR23!!!')

    def scanf_func_call(self):
        if self.input_token.get_value() == 'scanf':
            self.match('value','scanf')
            self.match('value','(')
            self.match('name','string')
            self.match('value',',')
            self.match('value','&')
            self.expression()
            self.match('value',')')
            self.match('value',';')
        else:
            raise SyntaxError('ERROR24!!!')

    def expr_list(self):
        if self.input_token.get_name() in ['identifier','number','string']: # add 'string' as parameter for function call
            self.non_empty_expr_list()
        elif self.input_token.get_value() in ['-','(']:
            self.non_empty_expr_list()
        elif self.input_token.get_value() == ')':
            pass
        else:
            raise SyntaxError('ERROR25!!!')

    def non_empty_expr_list(self):
        if self.input_token.get_name() in ['identifier','number','string']: #add 'string'
            self.expression()
            self.non_empty_expr_list_prime()
        elif self.input_token.get_value() in ['-','(']:
            self.expression()
            self.non_empty_expr_list_prime()
        elif self.input_token.get_value() == ')':
            pass
        else:
            raise SyntaxError('ERROR26!!!')

    def non_empty_expr_list_prime(self):
        if self.input_token.get_value() == ',':
            self.match('value',',')
            self.expression()
            self.non_empty_expr_list_prime()
        elif self.input_token.get_value() == ')':
            pass
        else:
            raise SyntaxError('ERROR27!!!')
    
    def if_else_stmt(self):
        if self.input_token.get_value() == 'if':
            self.if_stmt()
            self.else_stmt()
        else:
            raise SyntaxError('ERROR28!!!')


    def if_stmt(self):
        if self.input_token.get_value() == 'if':
            self.match('value','if')
            self.match('value','(')
            self.condition_expr()
            self.match('value',')')
            self.block_stmts()
        else:
            raise SyntaxError('ERROR28!!!')
    

    def else_stmt(self):
        if self.input_token.get_value() == 'else':
            self.match('value','else')
            self.block_stmts()
        elif self.input_token.get_value() in ['}','printf','scanf','if','while','return','break','continue','for']:
            pass
        elif self.input_token.get_name() == 'identifier':
            pass
        else:
            #print self.input_token.get_value()+'**********************'
            raise SyntaxError('ERROR28!!!')

    def for_stmt(self):
        if self.input_token.get_value() == 'for':
            self.match('value','for')
            self.match('value','(')
            self.for_block_1()
            self.for_block_2()
            self.for_block_3()
            self.match('value',')')
            self.block_stmts()
        else:
            raise SyntaxError('ERROR28!!!')

    def for_block_1(self):
        if self.input_token.get_name() == 'identifier':
            self.match('name','identifier')
            self.assignment()
        else:
            raise SyntaxError('ERROR28!!!')

    def for_block_2(self):
        if self.input_token.get_name() in ['identifier','number']:
            self.condition_expr()
            self.match('value',';')
        elif self.input_token.get_value() in ['-','(']:
            self.condition_expr()
            self.match('value',';')
        else:
            raise SyntaxError('ERROR28!!!')

    def for_block_3(self):
        if self.input_token.get_name() == 'identifier':
            self.match('name','identifier')
            self.double_plus_or_minus()
        else:
            raise SyntaxError('ERROR28!!!')

    def double_plus_or_minus(self):
        if self.input_token.get_value() in ['++','--']:
            self.match('value',self.input_token.get_value())
        else:
            raise SyntaxError('ERROR28!!!')

    def condition_expr(self):
        if self.input_token.get_name() in ['identifier','number']:
            self.condition()
            self.condition_tail()
        elif self.input_token.get_value() in ['-','(']:
            self.condition()
            self.condition_tail()
        else:
            raise SyntaxError('ERROR29!!!')

    def condition_tail(self):
        if self.input_token.get_value() in ['&&','||']:
            self.condition_op()
            self.condition()
        elif self.input_token.get_value() in [')',';']:
            pass
        else:
            raise SyntaxError('ERROR30!!!')

    def condition_op(self):
        if self.input_token.get_value() in ['&&','||']:
            self.match('value',self.input_token.get_value())
        else:
            raise SyntaxError('ERROR31!!!')

    def condition(self):
        if self.input_token.get_name() in ['identifier','number']:
            self.expression()
            self.comparison_op()
            self.expression()
        elif self.input_token.get_value() in ['-','(']:
            self.expression()
            self.comparison_op()
            self.expression()
        else:
            raise SyntaxError('ERROR32!!!')

    def comparison_op(self):
        if self.input_token.get_value() in ['==','!=','>','>=','<','<=']:
            self.match('value',self.input_token.get_value())
        else:
            raise SyntaxError('ERROR33!!!')

    def while_stmt(self):
        if self.input_token.get_value() == 'while':
            self.match('value','while')
            self.match('value','(')
            self.condition_expr()
            self.match('value',')')
            self.block_stmts()
        else:
            raise SyntaxError('ERROR34!!!')

    def return_stmt(self):
        if self.input_token.get_value() == 'return':
            self.match('value','return')
            self.return_stmt_tail()
        else:
            raise SyntaxError('ERROR35!!!')

    def return_stmt_tail(self):
        if self.input_token.get_name() in ['identifier','number']:
            self.expression()
            self.match('value',';')
        elif self.input_token.get_value() in ['-','(']:
            self.expression()
            self.match('value',';')
        elif self.input_token.get_value() == ';':
            self.match('value',';')
        else:
            raise SyntaxError('ERROR36!!!')

    def break_stmt(self):
        if self.input_token.get_value() == 'break':
            self.match('value','break')
            self.match('value',';')
        else:
            raise SyntaxError('ERROR37!!!')

    def continue_stmt(self):
        if self.input_token.get_value() == 'continue':
            self.match('value','continue')
            self.match('value',';')
        else:
            raise SyntaxError('ERROR38!!!')

    def expression(self):
        if self.input_token.get_name() in ['identifier','number']:
            self.term()
            self.expression_prime()
        elif self.input_token.get_value() in ['-','(']:
            self.term()
            self.expression_prime()
        elif self.input_token.get_name() == 'string':
            self.match('name','string')
        else:
            raise SyntaxError('ERROR39!!!')

    def expression_prime(self):
        if self.input_token.get_value() in ['+','-']:
            self.addop()
            self.term()
            self.expression_prime()
        elif self.input_token.get_value() in [';','==','!=','>','>=','<','<=',',',')',']','&&','||']:
            pass
        else:
            raise SyntaxError('ERROR40!!!')

    def addop(self):
        if self.input_token.get_value() in ['+','-']:
            self.match('value',self.input_token.get_value())
        else:
            raise SyntaxError('ERROR41!!!')

    def term(self):
        if self.input_token.get_name() in ['identifier','number']:
            self.factor()
            self.term_prime()
        elif self.input_token.get_value() in ['-','(']:
            self.factor()
            self.term_prime()
        else:
            raise SyntaxError('ERROR42!!!')

    def term_prime(self):
        if self.input_token.get_value() in ['*','/']:
            self.mulop()
            self.factor()
            self.term_prime()
        elif self.input_token.get_value() in ['+','-',';','==','!=','>','>=','<','<=',',',')',']','&&','||']:
            pass
        else:
            raise SyntaxError('ERROR43!!!')

    def mulop(self):
        if self.input_token.get_value() in ['*','/']:
            self.match('value',self.input_token.get_value())
        else:
            raise SyntaxError('ERROR44!!!')

    def factor(self):
        if self.input_token.get_name() == 'identifier':
            self.match('name','identifier')
            self.factor_tail()
        elif self.input_token.get_name() == 'number':
            self.match('name','number')
        elif self.input_token.get_value() == '-':
            self.match('value','-')
            self.match('name','number')
        elif self.input_token.get_value() == '(':
            self.match('value','(')
            self.expression()
            self.match('value',')')
        else:
            raise SyntaxError('ERROR45!!!')

    def factor_tail(self):
        if self.input_token.get_value() == '[':
            self.match('value','[')
            self.expression()
            self.match('value',']')
        elif self.input_token.get_value() == '(':
            self.match('value','(')
            self.expr_list()
            self.match('value',')')
        elif self.input_token.get_value() in ['+','-','*','/',';','==','!=','>','>=','<','<=',',',')',']','&&','||']:
            pass
        else:
            #print self.input_token.get_value() +'********************'
            raise SyntaxError('ERROR46!!!')



if __name__ == '__main__':
    scanner = tokenizer.Scanner(sys.argv[1])
    parser =  Parser(scanner)
    parser.program()
    print 'pass'
    print parser.variables
    print parser.functions
    print parser.statements
