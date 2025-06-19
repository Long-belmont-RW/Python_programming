#!/usr/bin/env python3

def remove_char_at(text, n):
	if abs(n) >= len(text) or len(text) == 0: 
		return "Invalid Format as index is out of range"
	else:
		return text[:n] + text[n+1:]

print(remove_char_at("Best School", 3)) 
print(remove_char_at("Chicago", 2)) 
print(remove_char_at("C is fun!", 0)) 
print(remove_char_at("School", 10)) 
print(remove_char_at("Python", -5))

		
