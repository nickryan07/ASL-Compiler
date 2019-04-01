# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Type_Expr_Func_Result() :
  def __init__( self, type_id ) :
    self.m_Type = type_id

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent+3))) + 'RESULT TYPE' )
    #for t in self.m_Type:
    self.m_Type.dump(indent+3)

#---------#---------#---------#---------#---------#--------#
