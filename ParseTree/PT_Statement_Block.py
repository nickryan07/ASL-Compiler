# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_Block() :
  def __init__( self, block ) :
    self.m_Block = block

  def dump( self, indent = 0 ) :
    self.m_Block.dump( indent )

#---------#---------#---------#---------#---------#--------#
