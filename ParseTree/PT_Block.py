# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Block() :
  def __init__( self, items ) :
    self.m_Items = items

  def dump( self, fileName, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + '{' , file=open(fileName, 'a'))
    for item in self.m_Items:
      #if callable(getattr(item, "dump"))
      item.dump(fileName, indent+1)
    print( ((INDENTSTR*(indent))) + '}' , file=open(fileName, 'a'))

  def semanticCheck( self ) :
    for item in self.m_Items:
      item.semanticCheck()

  def codeGen( self, fileName, literalTable) :
    for item in self.m_Items:
      item.codeGen(fileName, literalTable)



#---------#---------#---------#---------#---------#--------#
