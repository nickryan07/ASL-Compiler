# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Type_Expr_Id() :
  def __init__( self, type_id ) :
    self.m_Type = type_id

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent+1))) + 'TYPE ID', f'{self.m_Type!r}' )

#---------#---------#---------#---------#---------#--------#
