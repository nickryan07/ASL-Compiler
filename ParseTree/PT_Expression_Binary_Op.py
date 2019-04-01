# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Expression_Binary_Op() :
  def __init__( self, left_expr, op, right_expr ) :
    self.m_Left_Expr = left_expr
    self.m_Op = op
    self.m_Right_Expr = right_expr

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent+1))) + 'BINARYOP', f'{self.m_Op!r}' )
    self.m_Left_Expr.dump(indent+1)
    self.m_Right_Expr.dump(indent+1)

#---------#---------#---------#---------#---------#--------#
