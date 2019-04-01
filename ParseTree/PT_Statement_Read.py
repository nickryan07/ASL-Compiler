# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_Read() :
  def __init__( self, lvalues ) :
    self.m_Lvalues = lvalues

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'READ' )
    for ex in self.m_Lvalues:
      print( ((INDENTSTR*(indent+1))) + 'ARG' )
      ex.dump(indent+1)
    

#---------#---------#---------#---------#---------#--------#
