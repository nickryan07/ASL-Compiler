# Nicholas Reimherr
# nrr9884 
# 2018-10-08
#---------#---------#---------#---------#---------#--------#
from .common import *

#---------#---------#---------#---------#---------#--------#
class PT_Expression_Literal() :
  def __init__( self, kind, value ) :
    self.m_Kind = kind
    self.m_Value = value

  def dump( self, fileName, indent = 0 ) :
    print( ((INDENTSTR*(indent+1))) + 'LITERAL ' + f'{self.m_Kind}', f'{self.m_Value!r}', file=open(fileName, 'a'))

  # String: check if each character is ascii
  # Integer: check if it fits in 2^31-1 bits
  # Double: check if IEEE754 standard is adhered to
  def semanticCheck( self ) :
    if(self.m_Kind == "STRING") :
      if (not all(ord(i) < 128 for i in self.m_Value)) :
        raise ValueError
    elif(self.m_Kind == "INTEGER") :
      if (int(self.m_Value) > (2**31-1)) and (int(self.m_Value) < 0) :
        raise OverflowError
    elif(self.m_Kind == "REAL") :
      if not (float(self.m_Value)) :
        raise ValueError

  def codeGen( self, fileName, literalTable) :
    if(self.m_Kind == "STRING") :
      literalTable[2] +=1
      name = "STRLIT0" + str(literalTable[2])
      print('.data', file=open(fileName, 'a'))
      print(name + ':  .asciz  ' + '\"' + self.m_Value + '\"' , file=open(fileName, 'a'))
      print('.text\n', file=open(fileName, 'a'))

      print('movq  $' + name + ',  %rdi', file=open(fileName, 'a'))
      print('call  writeString', file=open(fileName, 'a'))


    elif(self.m_Kind == "INTEGER") :
      literalTable[0] +=1
      name = "INTLIT0" + str(literalTable[0])
      print('.data', file=open(fileName, 'a'))
      print('.align 4', file=open(fileName, 'a'))
      print(name + ':  .int  ' + self.m_Value, file=open(fileName, 'a'))
      print('.text\n', file=open(fileName, 'a'))
      
      print('movl  ' + name + ',  %edi', file=open(fileName, 'a'))
      print('call  writeInteger', file=open(fileName, 'a'))

    elif(self.m_Kind == "REAL") :
      literalTable[1] +=1
      name = "REALIT0" + str(literalTable[1])
      print('.data', file=open(fileName, 'a'))
      print('.align 8', file=open(fileName, 'a'))
      print(name + ':  .double  ' + self.m_Value, file=open(fileName, 'a'))
      print('.text\n', file=open(fileName, 'a'))

      print('movq  ' + name + ',  %xmm0', file=open(fileName, 'a'))
      print('call  writeReal', file=open(fileName, 'a'))


#---------#---------#---------#---------#---------#--------#
