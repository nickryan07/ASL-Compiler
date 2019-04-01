# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_For() :
  def __init__( self, lvalue, expr, to_expr, by_expr, stmnt ) :
    self.m_Lvalue = lvalue
    self.m_Expr = expr
    self.m_To_Expr = to_expr
    self.m_By_Expr = by_expr
    self.m_Stmnt = stmnt

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'FOR' )
    print( ((INDENTSTR*(indent+1))) + 'LVALUE' )
    self.m_Lvalue.dump(indent+1)
    print( ((INDENTSTR*(indent+1))) + 'START' )
    self.m_Expr.dump(indent+1)
    print( ((INDENTSTR*(indent+1))) + 'END' )
    self.m_To_Expr.dump(indent+1)
    print( ((INDENTSTR*(indent+1))) + 'BY' )
    self.m_By_Expr.dump(indent+1)
    print( ((INDENTSTR*(indent+1))) + 'DO' )
    self.m_Stmnt.dump(indent+2)
    

#---------#---------#---------#---------#---------#--------#
