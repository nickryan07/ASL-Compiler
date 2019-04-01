# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Declaration_Const() :
  def __init__( self, c_id, c_type, expr ) :
    self.m_Const_Id = c_id
    self.m_Const_Type = c_type
    self.m_Expr = expr

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'CONSTANT', f'{self.m_Const_Id!r}' )
    if self.m_Const_Type is not None:
      print( ((INDENTSTR*(indent+1))) + 'TYPE' )
      self.m_Const_Type.dump(indent+1)
    else:
      print( ((INDENTSTR*(indent+1))) + 'TYPE' )
      print( ((INDENTSTR*(indent+2))) + '<epsilon>' )
    print( ((INDENTSTR*(indent+1))) + 'INITIAL')
    self.m_Expr.dump(indent+1)
    

#---------#---------#---------#---------#---------#--------#
