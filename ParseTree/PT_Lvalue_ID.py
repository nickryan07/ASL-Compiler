# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Lvalue_ID() :
  def __init__( self, l_id ) :
    self.l_Id = l_id

  def dump( self, indent = 0 ) :
    #print( ((INDENTSTR*(indent))) + 'LVALUE' )
    print( ((INDENTSTR*(indent+1))) + 'LVALUE ID ' + f'{self.l_Id!r}' )

#---------#---------#---------#---------#---------#--------#
