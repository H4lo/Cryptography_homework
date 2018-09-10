def Caesar_encryt(user_id,plain):
	key = int(user_id[len(user_id)-2:len(user_id)])
	if key%26 == 0:
		key = int(user_id[len(user_id)-1:len(user_id)])
	result = ''
	#print key
	for i in plain:
		result += chr(97 + (ord(i)-97+key)%26)
		
	return result
		
if __name__ == '__main__':
	user_id = '20160303310113'
	plain = 'hainandaxuexinxikexuejishuxueyuan'
	
	print 'The encryt result: ' +  Caesar_encryt(user_id,plain)
