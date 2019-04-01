# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_Loop() :
  def __init__( self, stmnt ) :
    self.m_Statement = stmnt

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'LOOP' )
    self.m_Statement.dump(indent+1)
    

#---------#---------#---------#---------#---------#--------#
