# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_Return() :
  def __init__( self, value ) :
    self.m_Value = value

  def dump( self, indent = 0 ) :
    if self.m_Value is None:
      print( ((INDENTSTR*(indent))) + 'RETURNVOID' )
    else:
      print( ((INDENTSTR*(indent))) + 'RETURN' )
      self.m_Value.dump(indent)
    

#---------#---------#---------#---------#---------#--------#
