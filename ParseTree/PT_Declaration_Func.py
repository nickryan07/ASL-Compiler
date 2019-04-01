# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *
from .PT_Type_Expr_Id import PT_Type_Expr_Id

#---------#---------#---------#---------#---------#--------#
class PT_Declaration_Func() :
  def __init__( self, f_id, params, f_type, f_block ) :
    self.m_Func_Id = f_id
    self.m_Func_Params = params
    self.m_Func_Type = f_type
    self.m_Block = f_block

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'FUNC' , f'{self.m_Func_Id!r}' )
    print( ((INDENTSTR*(indent+1))) + 'RETURN TYPE' )
    #print(self.m_Func_Type)
    if type(self.m_Func_Type) is list:
      print( ((INDENTSTR*(indent+2))) + 'TYPE FUNC' )
      for f in self.m_Func_Type:
        #print( ((INDENTSTR*(indent+2))) + 'ARG TYPE' )
        f.dump(indent+1)
    else:
      self.m_Func_Type.dump(indent+1)
    for param in self.m_Func_Params:
      param.dump(indent+1)
    self.m_Block.dump(indent+1)

    

#---------#---------#---------#---------#---------#--------#
