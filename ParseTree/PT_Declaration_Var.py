# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Declaration_Var() :
  def __init__( self, c_id, c_type, expr ) :
    self.m_Var_Id = c_id
    self.m_Var_Type = c_type
    self.m_Expr = expr

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'VARIABLE', f'{self.m_Var_Id!r}' )
    if self.m_Var_Type is not None:
      if type(self.m_Var_Type) is list:
        for i in self.m_Var_Type:
          i.dump(indent+1)
      else:
        print( ((INDENTSTR*(indent+1))) + 'TYPE' )
        self.m_Var_Type.dump(indent+1)

    else:
      print( ((INDENTSTR*(indent+1))) + 'TYPE' )
      print( ((INDENTSTR*(indent+2))) + '<epsilon>' )
    print( ((INDENTSTR*(indent+1))) + 'INITIAL')
    self.m_Expr.dump(indent+1)
    

#---------#---------#---------#---------#---------#--------#
