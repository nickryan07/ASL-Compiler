# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Component() :
  def __init__( self, c_id, type_expr ) :
    self.m_Id = c_id
    self.m_Type = type_expr

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent+1))) + 'COMPONENT', f'{self.m_Id!r}' )
    if type(self.m_Type) is list:
      #print( ((INDENTSTR*(indent+2))) + 'TYPE FUNC' )
      
      for item in self.m_Type:
        #print( ((INDENTSTR*(indent+3))) + 'ARG TYPE' )
        item.dump(indent)
    else:
      #print( ((INDENTSTR*(indent+2))) + 'ARG TYPE' )
      self.m_Type.dump(indent+1)
    

#---------#---------#---------#---------#---------#--------#
