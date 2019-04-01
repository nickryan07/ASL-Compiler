# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Expression_Record_Inits() :
  def __init__( self, r_id, inits ) :
    self.m_Id = r_id
    self.m_Inits = inits

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent+1))) + 'RECORD_CONSTRUCTOR', f'{self.m_Id!r}' )
    for init in self.m_Inits:
      init.dump(indent+1)

#---------#---------#---------#---------#---------#--------#
