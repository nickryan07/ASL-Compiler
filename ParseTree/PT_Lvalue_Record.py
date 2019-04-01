# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Lvalue_Record() :
  def __init__( self, l_value, l_id ) :
    self.m_Value = l_value
    self.m_Id = l_id

  def dump( self, indent = 0 ) :
    #print( ((INDENTSTR*(indent))) + 'LVALUE' )
    print( ((INDENTSTR*(indent+1))) + 'LVALUE RECORD COMPONENT' )
    self.m_Value.dump(indent+1)
    print( ((INDENTSTR*(indent+2))) + 'COMPONENT ' + f'{self.m_Id!r}' )

#---------#---------#---------#---------#---------#--------#
