# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Record_Init() :
  def __init__( self, rec_id, expr ) :
    self.m_Id = rec_id
    self.m_Expr = expr


  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent+1))) + 'INIT', f'{self.m_Id!r}' )
    print( ((INDENTSTR*(indent+1))) + 'VALUE')
    self.m_Expr.dump(indent+1)

#---------#---------#---------#---------#---------#--------#
