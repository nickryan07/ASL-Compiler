# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_Elif() :
  def __init__( self, expr, stmnt) :
    self.m_Expr = expr
    self.m_Stmnt = stmnt

  def dump( self, indent = 0 ) :
    if self.m_Expr is not None:
      print( ((INDENTSTR*(indent))) + 'ELIF' )
      self.m_Expr.dump(indent)
    if self.m_Stmnt is not None:
      print( ((INDENTSTR*(indent))) + 'THEN' )
      self.m_Stmnt.dump(indent+1)
    

#---------#---------#---------#---------#---------#--------#
