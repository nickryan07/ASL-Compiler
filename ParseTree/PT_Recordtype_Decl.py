# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Recordtype_Decl() :
  def __init__( self, r_id, e_id, components ) :
    self.m_Record_Id = r_id
    self.m_Extends_Id = e_id
    self.m_Components = components

  def dump( self, indent = 0 ) :
    if self.m_Extends_Id is not None:
      print( ((INDENTSTR*(indent))) + 'RECORDTYPE', f'{self.m_Record_Id!r}', 'EXTENDS', f'{self.m_Extends_Id!r}' )
    else:
      print( ((INDENTSTR*(indent))) + 'RECORDTYPE', f'{self.m_Record_Id!r}', 'EXTENDS', '<epsilon>' )
    for component in self.m_Components:
      component.dump(indent)

  def semanticCheck( self ) :
    raise NotImplementedError
    

#---------#---------#---------#---------#---------#--------#
