# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_If() :
  def __init__( self, expr, stmnt, elif_stmnts, else_stmnt) :
    self.m_Expr = expr
    self.m_Stmnt = stmnt
    self.m_Elif_Stmnts = elif_stmnts
    self.m_Else_Stmnt = else_stmnt

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'IF' )
    self.m_Expr.dump(indent)
    print( ((INDENTSTR*(indent))) + 'THEN' )
    self.m_Stmnt.dump(indent+1)
    for el_if in self.m_Elif_Stmnts:
      el_if.dump(indent)
    if self.m_Else_Stmnt is not None:
      print( ((INDENTSTR*(indent))) + 'ELSE' )
      self.m_Else_Stmnt.dump(indent+1)
    print( ((INDENTSTR*(indent))) + 'FI' )
    

#---------#---------#---------#---------#---------#--------#
