#!/usr/bin/env python3
def uppercase(text):
	result = ""
	for char in text:
		if 'a' <= char <= 'z':
			result += chr(ord(char) - 32)
		else:
			result += char
	print(result)
uppercase("best") 
uppercase("Best School 98 Battery street")
