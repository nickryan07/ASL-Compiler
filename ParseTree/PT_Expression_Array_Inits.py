# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Expression_Array_Inits() :
  def __init__( self, array_type, inits ) :
    self.m_Type = array_type
    self.m_Inits = inits

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent+1))) + 'ARRAY_CONSTRUCTOR' )
    print( ((INDENTSTR*(indent+2))) + 'ELEMENT_TYPE' )
    if type(self.m_Type) is list:
      for types in self.m_Type:
        types.dump(indent+1)
    else:
      self.m_Type.dump(indent+2)
    for init in self.m_Inits:
      init.dump(indent+1)

#---------#---------#---------#---------#---------#--------#
