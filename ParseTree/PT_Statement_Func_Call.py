# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_Func_Call() :
  def __init__( self, op, exprs ) :
    self.m_Operator = op
    self.m_Exprs = exprs

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'FUNC CALL' )
    print( ((INDENTSTR*(indent+1))) + 'OPERATOR' )
    self.m_Operator.dump(indent+1)
    for expr in self.m_Exprs: 
      print( ((INDENTSTR*(indent+1))) + 'ARG' )
      expr.dump(indent+1)
    

#---------#---------#---------#---------#---------#--------#
