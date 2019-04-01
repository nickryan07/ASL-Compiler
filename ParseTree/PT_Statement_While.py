# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_While() :
  def __init__( self, expr, stmnt ) :
    self.m_Expr = expr
    self.m_Stmnt = stmnt

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'WHILE' )
    print( ((INDENTSTR*(indent+1))) + 'EXPRESSION' )
    self.m_Expr.dump(indent+1)
    print( ((INDENTSTR*(indent+1))) + 'BODY' )
    self.m_Stmnt.dump(indent+2)
    

#---------#---------#---------#---------#---------#--------#
