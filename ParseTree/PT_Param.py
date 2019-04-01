# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Param() :
  def __init__( self, const, p_id, p_type ) :
    self.m_Const = const
    self.m_Param_Id = p_id
    self.m_Param_Type = p_type

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'PARAM', f'{self.m_Param_Id!r}' )
    if type(self.m_Param_Type) is list:
      for i in self.m_Param_Type:
        i.dump(indent)
      
    else:
      self.m_Param_Type.dump(indent)
    
    

#---------#---------#---------#---------#---------#--------#
