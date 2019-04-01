# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Expression_Lvalue() :
  def __init__( self, lvalue ) :
    self.m_Lvalue = lvalue

  def dump( self, indent = 0 ) :
    #print( ((INDENTSTR*(indent))) + 'EXPRESSION' )
    self.m_Lvalue.dump(indent)

#---------#---------#---------#---------#---------#--------#
