# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Program() :
  def __init__( self, decls, block ) :
    self.m_Decls = decls
    self.m_Block = block

  def dump( self, fileName, indent = 0 ) :
    print( (INDENTSTR*indent) + 'PROGRAM' , file=open(fileName, 'w'))
    for dec in self.m_Decls:
      dec.dump( fileName, indent+1 )
    self.m_Block.dump( fileName, indent+1 )

  def semanticCheck( self ) :
    for dec in self.m_Decls:
      dec.semanticCheck()
    self.m_Block.semanticCheck()
  
  def codeGen( self, fileName, literalTable):
    print('.global main', file=open(fileName, 'w'))
    print('.text', file=open(fileName, 'a'))
    print('main:', file=open(fileName, 'a'))
    print('  pushq  %rbp', file=open(fileName, 'a'))
    print('  movq  %rsp, %rbp', file=open(fileName, 'a'))
    print('\n', file=open(fileName, 'a'))

    #need to attach the program exit status after code gen for the rest of the program
    self.m_Block.codeGen(fileName, literalTable)

    print('  movl    $0, %eax', file=open(fileName, 'a'))
    print('  leave', file=open(fileName, 'a'))
    print('  ret', file=open(fileName, 'a'))

#---------#---------#---------#---------#---------#--------#
