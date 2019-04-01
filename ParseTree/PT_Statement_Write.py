# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Statement_Write() :
  def __init__( self, exprs ) :
    self.m_Exprs = exprs

  def dump( self, fileName, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'WRITE', file=open(fileName, 'a'))
    for ex in self.m_Exprs:
      print( ((INDENTSTR*(indent+1))) + 'ARG', file=open(fileName, 'a'))
      ex.dump(fileName, indent+1)
    
  def semanticCheck( self ) :
    for expr in self.m_Exprs:
      expr.semanticCheck()

  def codeGen( self, fileName, literalTable) :
    for expr in self.m_Exprs:
      expr.codeGen(fileName, literalTable)
    print('call  writeNewLine\n', file=open(fileName, 'a'))
#---------#---------#---------#---------#---------#--------#
