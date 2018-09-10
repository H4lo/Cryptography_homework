#coding: utf-8

from string import ascii_uppercase
letter_list = ascii_uppercase.replace('I','')
 
#密码表
T_letter=['','','','','']
 
#根据密钥建立密码表
def Create_Matrix(key):
  key=Remove_Duplicates(key)  #移除密钥中的重复字母
  key=key.replace(' ','') #去除密钥中的空格
  
  for ch in letter_list:  #根据密钥获取新组合的字母表
    if ch not in key:
      key+=ch
  
  j=0
  for i in range(len(key)): #将新的字母表里的字母逐个填入密码表中，组成5*5的矩阵
    T_letter[j]+=key[i]     #j用来定位字母表的行
    if 0==(i+1)%5:
      j+=1
 
#移除字符串中重复的字母
def Remove_Duplicates(key):
  key=key.upper() #转成大写字母组成的字符串
  _key=''
  for ch in key:
    if ch=='I':
      ch='J'
    if ch in _key:
      continue
    else:
      _key+=ch
  return _key
 
#获取字符在密码表中的位置
def Get_MatrixIndex(ch):
  for i in range(len(T_letter)):
    for j in range(len(T_letter)):
      if ch==T_letter[i][j]:
        return i,j #i为行，j为列
 
#加密算法
def Encrypt(plaintext,T_letter):
  ciphertext=''
  
  if len(plaintext) % 2 !=0:  #如果新的明文长度为奇数，在其末尾添上'Z'
    plaintext+='Z'
  
  i=0
  while i<len(plaintext): #对明文进行遍历
    if True==plaintext[i].isalpha():  
      j=i+1                           
      while j<len(plaintext):         
        if True==plaintext[j].isalpha():
          if 'I'==plaintext[i].upper():             
            x=Get_MatrixIndex('J')                 
          else:                                     
            x=Get_MatrixIndex(plaintext[i].upper())
          if 'I'==plaintext[j].upper():             #同时将'I'作为'J'来处理
              y=Get_MatrixIndex('J')                
          else:                                     
            y=Get_MatrixIndex(plaintext[j].upper()) 
          
          if x[0]==y[0]:    #如果在同一行
            ciphertext+=T_letter[x[0]][(x[1]+1)%5]+T_letter[y[0]][(y[1]+1)%5]
          elif x[1]==y[1]:  #如果在同一列
            ciphertext+=T_letter[(x[1]+1)%5][x[0]]+T_letter[(y[1]+1)%5][y[0]]
          else:             #如果不同行不同列
            ciphertext+=T_letter[x[0]][y[1]]+T_letter[y[0]][x[1]]
          break;  
        j+=1
      i=j+1  
      continue
    else:
      ciphertext+=plaintext[i]  
    i+=1
    
  return ciphertext
 

#主函数
if __name__=='__main__':
  
	key='ZHONGWENJIE'
  
	Create_Matrix(key)  #建立密码表
 
	plaintext='hainandaxuexinxikexuejishuxueyuan'
	print "密文为: %s" % Encrypt(plaintext,T_letter)
 
