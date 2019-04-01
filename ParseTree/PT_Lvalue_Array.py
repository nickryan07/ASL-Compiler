# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Lvalue_Array() :
  def __init__( self, l_value, expr ) :
    self.m_Value = l_value
    self.m_Expr = expr

  def dump( self, indent = 0 ) :
    #print( ((INDENTSTR*(indent))) + 'LVALUE' )
    print( ((INDENTSTR*(indent+1))) + 'LVALUE ARRAY SUBSCRIPT')
    self.m_Value.dump(indent+1)
    self.m_Expr.dump(indent+1)

#---------#---------#---------#---------#---------#--------#
