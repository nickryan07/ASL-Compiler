# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Type_Expr_Func_Arg() :
  def __init__( self, type_id ) :
    self.m_Type = type_id

  def dump( self, indent = 0 ) :
    #if type(self.m_Type) is PT_Type_Expr_Func_Arg:
    print( ((INDENTSTR*(indent+2))) + 'TYPE FUNC' )
    print( ((INDENTSTR*(indent+3))) + 'ARG TYPE' )
      #self.m_Type.dump(indent+2)
    #else:
    self.m_Type.dump(indent+3)

#---------#---------#---------#---------#---------#--------#
