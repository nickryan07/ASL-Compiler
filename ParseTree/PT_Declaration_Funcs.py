# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Declaration_Funcs() :
  def __init__( self, func_decls ) :
    self.m_Funcs = func_decls

  def dump( self, indent = 0 ) :
    print( ((INDENTSTR*(indent))) + 'FUNCSET' )
    for decls in self.m_Funcs:
      decls.dump(indent+1)
    

#---------#---------#---------#---------#---------#--------#
