# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
import ply.yacc
import ply.lex
from pathlib import Path
from ParseTree import *

#---------#---------#---------#---------#---------#--------#
keywords = {
    'and': 'AND',
    'by': 'BY',
    'const': 'CONST',
    'div': 'DIV',
    'do': 'DO',
    'else': 'ELSE', 
    'elif': 'ELIF',
    'exit': 'EXIT',
    'extends': 'EXTENDS',
    'fi': 'FI',
    'for': 'FOR', 
    'func': 'FUNC', 
    'if': 'IF',
    'loop': 'LOOP',
    'mod': 'MOD',
    'next': 'NEXT',
    'not': 'NOT',
    'of': 'OF',
    'or': 'OR',
    'read': 'READ',
    'record': 'RECORD',
    'return': 'RETURN',
    'then': 'THEN',
    'to': 'TO',
    'var': 'VAR',
    'while': 'WHILE',
    'write': 'WRITE'
}

tokens = [
    'INTEGER',
    'REAL',
    'STRING',
    'ID',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'ASSIGN',
    'AT',
    'PTR',
    'GT',
    'LT',
    'GE',
    'LE',
    'EQ',
    'NE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COLON',
    'SEMICOLON',
    'COMMA',
    'PERIOD'
] + list(keywords.values())

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULTIPLY   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_PERIOD = r'\.'
t_AT = r'@'
t_PTR = r'->'
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_NE = r'<>'
t_EQ = r'=='

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_COMMENT(t):
  r'\/\/((.)*)'

def t_ID(t):
  r'[_a-zA-Z][_a-zA-Z0-9]*'
  t.type = keywords.get(t.value, 'ID')
  return t

def t_REAL_LITERAL(t):
  r'\d+\.\d*([eE]([-+])?\d+)?'
  t.type = keywords.get(t.value, 'REAL')
  return t

def t_INTEGER_LITERAL(t):
  r'\d+'
  t.type = keywords.get(t.value, 'INTEGER')
  return t

def t_STRING_LITERAL(t):
  r'"[^"\n]*"'
  t.value = t.value[1:-1]
  t.type = keywords.get(t.value, 'STRING')
  return t

t_ignore = ' \f\t\r\v'

def t_error( t ) :
  print('Illegal character', "\""+ t.value[0] +"\"", "on line", str(t.lineno) + ".")
  t.lexer.skip(1)

  raise ValueError( 'Lexical error' )

#---------#---------#---------#---------#---------#--------#

precedence = (
  ( 'left', 'OR' ),
  ( 'left', 'AND'),
  ( 'right', 'NOT'),
  ( 'nonassoc', 'LT', 'LE', 'EQ', 'NE', 'GE', 'GT' ),
  ( 'left',  'PLUS', 'MINUS' ),
  ( 'left',  'MULTIPLY', 'DIVIDE', 'MOD', 'DIV'),
  ( 'right', 'UMINUS' ),
  ( 'nonassoc', 'FUNC_CALL'),
  )

start = 'program'

def p_program_decls_many( p ):
  'program_decls : program_decls recordtype_decl'
  p[0] = p[1] + [p[2]]

def p_program_decls_epsilon( p ):
  'program_decls : epsilon'
  p[0] = []

def p_program_block( p ):
  'program : program_decls block'
  p[0] = PT_Program( p[1], p[2] )

def p_record_type_decl( p ):
  'recordtype_decl : RECORD ID record_extends LBRACE components RBRACE SEMICOLON'
  p[0] = PT_Recordtype_Decl( p[2], p[3], p[5])

def p_components_epsilon( p ):
  'components : epsilon'
  p[0] = []

def p_components_one( p ):
  'components : component'
  p[0] = [p[1]]

def p_components_many( p ):
  'components : components COMMA component'
  p[0] = p[1] + [p[3]]

def p_component( p ):
  'component : ID COLON type_expr'
  p[0] = PT_Component( p[1], p[3] )

def p_record_type_decl_extends_one( p ):
  'record_extends : EXTENDS ID'
  p[0] = p[2]

def p_record_type_decl_extends_epsilon( p ):
  'record_extends : epsilon'
  p[0] = None

def p_block( p ):
  'block : LBRACE block_items RBRACE'
  p[0] = PT_Block( p[2] )

def p_block_item_declaration( p ):
  'block_item : declaration'
  p[0] = p[1]

def p_block_item_statement( p ):
  'block_item : statement'
  p[0] = p[1]

def p_block_items_epsilon( p ):
  'block_items : epsilon'
  p[0] = ( [] ) 

def p_block_items_one( p ):
  'block_items : block_item'
  p[0] = [p[1]]

def p_block_items_many( p ):
  'block_items : block_items SEMICOLON block_item'
  p[0] = p[1] + [p[3]]

def p_declaration_const( p ):
  '''declaration : const_decl
                 | var_decl'''
  p[0] = p[1]

def p_declaration_funcs_decl( p ):
  'declaration : funcs_decl'
  p[0] = PT_Declaration_Funcs( p[1] )

def p_funcs_decl_one( p ):
  'funcs_decl : func_decl'
  p[0] = [p[1]]

def p_funcs_decl_many( p ):
  'funcs_decl : funcs_decl AND func_decl'
  p[0] = p[1] + [p[3]]

def p_func_decl( p ):
  'func_decl : FUNC ID LPAREN params RPAREN optional_ptr_type block'
  p[0] = PT_Declaration_Func( p[2], p[4], p[6], p[7] )

def p_param_const( p ):
  'param : CONST ID COLON type_expr'
  p[0] = PT_Param( p[1], p[2], p[4] )

def p_param_no_const( p ):
  'param : ID COLON type_expr'
  p[0] = PT_Param( None, p[1], p[3] )

def p_params_epsilon( p ):
  'params : epsilon'
  p[0] = []

def p_params_one( p ):
  'params : param'
  p[0] = [p[1]]

def p_params_many( p ):
  'params : params COMMA param'
  p[0] = p[1] + [p[3]]

def p_optional_ptr_type_epsilon( p ):
  'optional_ptr_type : epsilon'
  p[0] = PT_Type_Expr_Id( 'void' )

def p_optional_ptr_type_one( p ):
  'optional_ptr_type : PTR type_expr'
  p[0] = p[2]

def p_const_decl( p ):
  'const_decl : CONST ID optional_type ASSIGN expression'
  p[0] = PT_Declaration_Const( p[2], p[3], p[5] )

def p_var_decl( p ):
  'var_decl : VAR ID optional_type ASSIGN expression'
  p[0] = PT_Declaration_Var( p[2], p[3], p[5] )

def p_optional_type_epsilon( p ):
  'optional_type : epsilon'
  p[0] = None

def p_optional_type_one( p ):
  'optional_type : COLON type_expr'
  p[0] = p[2]

def p_expression_integer( p ):
  'expression : INTEGER'
  p[0] = PT_Expression_Literal( 'INTEGER', p[1] )

def p_expression_real( p ):
  'expression : REAL'
  p[0] = PT_Expression_Literal( 'REAL', p[1] )

def p_expression_string( p ):
  'expression : STRING'
  p[0] = PT_Expression_Literal( 'STRING', p[1] )

def p_expression_lvalue( p ):
  'expression : lvalue'
  p[0] = PT_Expression_Lvalue( p[1] )

def p_expression_nested( p ):
  'expression : LPAREN expression RPAREN %prec FUNC_CALL'
  p[0] = p[2] #PT_Expression_Nested( p[2] )#PT_Statement_Func_Call

def p_expression_unary_op( p ):
  'expression : unary_op expression'
  p[0] = PT_Expression_Unary_Op( p[1], p[2] )

'''def p_expression_binary_op( p ):
  'expression : expression binary_op expression'
  p[0] = PT_Expression_Binary_Op( p[1], p[2], p[3] )'''

def p_expression_binary_op_plus( p ):
  'expression : expression PLUS expression'
  p[0] = PT_Expression_Binary_Op( p[1], p[2], p[3] )

def p_expression_binary_op_minus( p ):
  'expression : expression MINUS expression %prec MINUS'
  p[0] = PT_Expression_Binary_Op( p[1], p[2], p[3] )

def p_expression_binary_op_multiply( p ):
  'expression : expression MULTIPLY expression'
  p[0] = PT_Expression_Binary_Op( p[1], p[2], p[3] )

def p_expression_binary_op_divide( p ):
  'expression : expression DIVIDE expression'
  p[0] = PT_Expression_Binary_Op( p[1], p[2], p[3] )

def p_expression_binary_op_and( p ):
  'expression : expression AND expression'
  p[0] = PT_Expression_Binary_Op ( p[1], p[2], p[3] )

def p_expression_binary_op_or( p ):
  'expression : expression OR expression'
  p[0] = PT_Expression_Binary_Op ( p[1], p[2], p[3] )

def p_expression_binary_op_mod( p ):
  'expression : expression MOD expression'
  p[0] = PT_Expression_Binary_Op ( p[1], p[2], p[3] )

def p_expression_binary_op_div( p ):
  'expression : expression DIV expression'
  p[0] = PT_Expression_Binary_Op ( p[1], p[2], p[3] )

def p_expression_binary_op_ge( p ):
  'expression : expression GE expression'
  p[0] = PT_Expression_Binary_Op ( p[1], p[2], p[3] )

def p_expression_binary_op_gt( p ):
  'expression : expression GT expression'
  p[0] = PT_Expression_Binary_Op ( p[1], p[2], p[3] )

def p_expression_binary_op_le( p ):
  'expression : expression LE expression'
  p[0] = PT_Expression_Binary_Op ( p[1], p[2], p[3] )

def p_expression_binary_op_lt( p ):
  'expression : expression LT expression'
  p[0] = PT_Expression_Binary_Op ( p[1], p[2], p[3] )

def p_expression_binary_op_ne( p ):
  'expression : expression NE expression'
  p[0] = PT_Expression_Binary_Op ( p[1], p[2], p[3] )

def p_expression_binary_op_eq( p ):
  'expression : expression EQ expression'
  p[0] = PT_Expression_Binary_Op ( p[1], p[2], p[3] )

def p_expression_func_call( p ):
  'expression : expression LPAREN expressions RPAREN %prec FUNC_CALL'
  p[0] = PT_Expression_Func_Call( p[1], p[3] )

def p_expression_record_inits( p ):
  'expression : ID LBRACE record_inits RBRACE'
  p[0] = PT_Expression_Record_Inits( p[1], p[3] )

def p_expression_array_inits( p ):
  'expression : AT type_expr LBRACE array_inits RBRACE'
  p[0] = PT_Expression_Array_Inits( p[2], p[4] )

def p_array_init( p ):
  'array_init : expression'
  p[0] = PT_Array_Init( PT_Expression_Literal( 'INTEGER' , '1' ), p[1] )

def p_array_init_of( p ):
  'array_init : expression OF expression'
  p[0] = PT_Array_Init( p[1], p[3] )

def p_array_init_epsilon( p ):
  'array_inits : epsilon'
  p[0] = []

def p_array_inits_one( p ):
  'array_inits : array_init'
  p[0] = [p[1]]

def p_array_inits_many( p ):
  'array_inits : array_inits COMMA array_init'
  p[0] = p[1] + [p[3]]

def p_type_expr_id( p ):
  'type_expr : ID'
  p[0] = PT_Type_Expr_Id( p[1] )

def p_type_expr_at( p ):
  'type_expr : AT type_expr'
  p[0] = PT_Type_Expr_Array( p[2] )

'''def p_type_expr_func( p ):
  'type_expr : LPAREN type_expr RPAREN'
  p[0] = PT_Type_Expr_Func_Arg( p[2] )
'''

def p_type_expr_args( p ):
  'type_expr : type_args PTR type_expr'
  p[0] = p[1] + [PT_Type_Expr_Func_Result( p[3] )]


def p_type_args_empty( p ):
  'type_args : LPAREN RPAREN'
  p[0] = None

def p_type_args_expr( p ):
  'type_args : type_expr_many'
  p[0] = [PT_Type_Expr_Func_Arg( p[1] )]

def p_type_args_expr_one( p ):
  'type_args : LPAREN type_expr type_expr_many RPAREN'
  p[0] = [PT_Type_Expr_Func_Arg( p[2] )] + p[3]

def p_type_args_expr_epsilon( p ):
  'type_expr_many : epsilon'
  p[0] = []

def p_type_args_expr_optional( p ):
  'type_expr_many : type_expr_many COMMA type_expr'
  p[0] = p[1] + [PT_Type_Expr_Func_Arg( p[3] )]

def p_record_init( p ):
  'record_init : ID ASSIGN expression'
  p[0] = PT_Record_Init( p[1], p[3] )
  
def p_record_inits_epsilon( p ):
  'record_inits : epsilon'
  p[0] = []

def p_record_inits_one( p ):
  'record_inits : record_init'
  p[0] = [p[1]]

def p_record_inits_many( p ):
  'record_inits : record_inits COMMA record_init'
  p[0] = p[1] + [p[3]]

def p_expressions_epsilon( p ):
  'expressions : epsilon'
  p[0] = ( [] ) 

def p_expressions_one( p ):
  'expressions : expression'
  p[0] = [p[1]]

def p_expressions_many( p ):
  'expressions : expressions COMMA expression'
  p[0] = p[1] + [p[3]]

def p_unary_op_minus( p ):
  'unary_op : MINUS %prec UMINUS'
  p[0] = p[1]

def p_unary_op_uminus( p ):
  'unary_op : NOT %prec NOT'
  p[0] = p[1]

def p_lvalue_id( p ):
  'lvalue : ID'
  p[0] = PT_Lvalue_ID( p[1] )

def p_lvalue_expression( p ):
  'lvalue : lvalue LBRACKET expression RBRACKET'
  p[0] = PT_Lvalue_Array( p[1], p[3] )

def p_lvalue_per_id( p ):
  'lvalue : lvalue PERIOD ID'
  p[0] = PT_Lvalue_Record( p[1], p[3] )

def p_statement_block( p ):
  'statement : block'
  p[0] = PT_Statement_Block( p[1] )

def p_statement_assign( p ):
  'statement : lvalue ASSIGN expression'
  p[0] = PT_Statement_Assign( p[1], p[3] )

def p_statement_nested_expr( p ):
  'statement : expression LPAREN expressions RPAREN %prec FUNC_CALL'
  p[0] = PT_Statement_Func_Call( p[1], p[3] )

def p_statement_loop( p ):
  'statement : LOOP statement'
  p[0] = PT_Statement_Loop( p[2] )

def p_statement_while( p ):
  'statement : WHILE expression DO statement'
  p[0] = PT_Statement_While( p[2], p[4] )

def p_statement_read( p ):
  'statement : READ LPAREN lvalues RPAREN'
  p[0] = PT_Statement_Read( p[3] )

def p_lvalues_one( p ):
  'lvalues : lvalue'
  p[0] = [p[1]]

def p_lvalues_many( p ):
  'lvalues : lvalues COMMA lvalue'
  p[0] = p[1] + [p[3]]

def p_statement_return_epsilon( p ):
  'statement : RETURN'
  p[0] = PT_Statement_Return( None )

def p_statement_return_one( p ):
  'statement : RETURN expression'
  p[0] = PT_Statement_Return( p[2] )

def p_statement_next( p ):
  'statement : NEXT'
  p[0] = PT_Statement_Next( )

def p_statement_exit( p ):
  'statement : EXIT'
  p[0] = PT_Statement_Exit( )

def p_statement_write( p ):
  'statement : WRITE LPAREN expressions RPAREN'
  p[0] = PT_Statement_Write( p[3] )

def p_statement_for_rules( p ):
  'statement : FOR lvalue ASSIGN expression TO expression optional_by DO statement'
  p[0] = PT_Statement_For( p[2], p[4], p[6], p[7], p[9] )

def p_optional_by_epsilon( p ):
  'optional_by : epsilon'

def p_optional_by_one( p ):
  'optional_by : BY expression'
  p[0] = p[2]

def p_statement_if_nested( p ):
  'statement : if_statement'
  p[0] = p[1]

def p_statement_if( p ):
  'if_statement : IF expression THEN statement optional_elifs optional_else FI'
  p[0] = PT_Statement_If( p[2], p[4], p[5], p[6] )

def p_optional_elifs_epsilon( p ):
  'optional_elifs : epsilon'
  p[0] = []

def p_optional_elifs_many( p ):
  'optional_elifs : optional_elifs ELIF expression THEN statement'
  p[0] = p[1] + [PT_Statement_Elif( p[3], p[5] )]

def p_optional_else_epsilon( p ):
  'optional_else : epsilon'
  p[0] = None

def p_optional_else_one( p ):
  'optional_else : ELSE statement'
  p[0] = p[2]

def p_error( p ) :
  if p is None :
    print( 'Syntax error!' )

  else :
    print( f'Syntax error at "{p.value}", line {p.lineno}' )

  raise ValueError( 'Syntactic error' )
  
def p_epsilon( p ):
  'epsilon :'
  p[0] = None

#---------#---------#---------#---------#---------#--------#
def _main( inputFile ) :
  with open( inputFile, 'r' ) as fp :
    data = fp.read()
  
  fileName = str(Path(inputFile).name)
  parseFile = str(Path(inputFile).with_suffix('.parse'))
  codeFile = str(Path(inputFile).with_suffix('.s'))

  try :
    _  = ply.lex.lex()
    parser = ply.yacc.yacc()
    value = parser.parse( data )

    with open(parseFile, 'w') as fp:
      value.dump(fileName=parseFile)

    print( 'Parse complete ...' )
    
    value.semanticCheck()

    print( 'Semantic checks complete ...' )

    literalTable = [
      0, # 0 = integer
      0, # 1 = real
      0  # 2 = string
    ]

    with open(codeFile, 'w') as fp:
      value.codeGen(codeFile, literalTable)

    print( 'Assembly generated at', codeFile )

  except ValueError :
    print( 'Error during processing.  Abort.' )

#---------#---------#---------#
if __name__ == '__main__' :
  import sys

  if len( sys.argv ) > 1 :
    _main( sys.argv[ 1 ] )

  else :
    print( 'Input file name required.' )

#---------#---------#---------#---------#---------#--------#
