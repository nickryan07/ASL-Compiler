# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_Assign() :
  def __init__( self, lvalue, expr ) :
    self.m_Lvalue = lvalue
    self.m_Expr = expr

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'ASSIGN' )
    print( ((INDENTSTR*(indent+1))) + 'LVALUE' )
    self.m_Lvalue.dump(indent+1)
    print( ((INDENTSTR*(indent+1))) + 'EXPRESSION' )
    self.m_Expr.dump(indent+1)
    

#---------#---------#---------#---------#---------#--------#
