# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Expression_Func_Call() :
  def __init__( self, expr, expressions ) :
    self.m_Expr = expr
    self.m_Expressions = expressions

  def dump( self, indent = 0 ) :
    #print( ((INDENTSTR*(indent))) + 'EXPRESSION' )
    print( ((INDENTSTR*(indent+1))) + 'FUNC CALL' )
    print( ((INDENTSTR*(indent+2))) + 'OPERATOR' )
    self.m_Expr.dump(indent+2)
    #self.m_Lvalue.dump(indent)
    for ex in self.m_Expressions:
      print( ((INDENTSTR*(indent+2))) + 'ARG' )
      ex.dump(indent+2)

#---------#---------#---------#---------#---------#--------#
