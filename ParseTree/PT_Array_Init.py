# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Array_Init() :
  def __init__( self, expr1, expr2 ) :
    self.m_Expr1 = expr1
    self.m_Expr2 = expr2


  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent+1))) + 'INIT QUANTITY')
    self.m_Expr1.dump(indent+1)
    print( ((INDENTSTR*(indent+1))) + 'OF')
    self.m_Expr2.dump(indent+1)

#---------#---------#---------#---------#---------#--------#
