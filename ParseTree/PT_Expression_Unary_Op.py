# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Expression_Unary_Op() :
  def __init__( self, op, expr ) :
    self.m_Op = op
    self.m_Expr = expr

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent+1))) + 'UNARYOP', f'{self.m_Op!r}' )
    self.m_Expr.dump(indent+1)

#---------#---------#---------#---------#---------#--------#
