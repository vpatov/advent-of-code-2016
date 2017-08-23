"""
swap position X with position Y 
	means that the letters at indexes X and Y (counting from 0) should be swapped.
swap letter X with letter Y 
	means that the letters X and Y should be swapped (regardless of where they appear in the string).
rotate left/right X steps 
	means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
rotate based on position of letter X 
	means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
reverse positions X through Y 
	means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
move position X to position Y 
	means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.
"""
password = "abcdefgh"

instructions = [line.strip() for line in open('day21.txt','r').readlines()]


operations = {
	1: None,
	2: None,
	3: None,
	4: None,
	5: None,
	6: None
}