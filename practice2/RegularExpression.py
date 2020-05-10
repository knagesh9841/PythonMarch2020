from re import *

"""
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string

Metacharacters
Metacharacters are characters with a special meaning:

Character	Description	Example	
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"world$"	
*	Zero or more occurrences	"aix*"	
+	One or more occurrences	"aix+"	
{}	Exactly the specified number of occurrences	"al{2}"	
|	Either or	"falls|stays"	
()	Capture and group


\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"

Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	Description	Try it
[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

"""


txt = "The rain in Spain"
x = findall("ai", txt)
print(x)

# Return an empty list if no match was found:

txt = "The rain in Spain"
x = findall("Portugal", txt)
print(x)

p = compile('[a-e]')

# findall() searches for the Regular Expression and return a list upon finding
print(p.findall("Aye, said Mr. Gibenson Stark"))

p = compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# \d+ will match a group on [0-9], group of one or greater size
p = compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# \w is equivalent to [a-zA-Z0-9_].
p = compile('\w')
print(p.findall("He said * in some_lang."))

# \w+ matches to group of alphanumeric character.
p = compile('\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))

# \W matches to non alphanumeric characters.
p = compile('\W')
print(p.findall("he said *** in some_language."))

# '*' replaces the no. of occurrence of a character.
p = compile('ab*')
print(p.findall("ababbaabbb"))

# '\W+' denotes Non-Alphanumeric Characters or group of characters
# Upon finding ',' or whitespace ' ', the split(), splits the string from that point
print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's words Words"))

# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))

# '\d+' denotes Numeric Characters or group of characters
# Splitting occurs at '12', '2016', '11', '02' only
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))

print(sub('ub', '~*', 'Subject has Uber booked already', flags=IGNORECASE))

# Consider the Case Sensitivity, 'Ub' in "Uber", will not be reaplced.
print(sub('ub', '~*', 'Subject has Uber booked already'))

# As count has been given value 1, the maximum times replacement occurs is 1
print(sub('ub', '~*', 'Subject has Uber booked already', count=1, flags=IGNORECASE))

# 'r' before the patter denotes RE, \s is for start and end of a String.
print(sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=IGNORECASE))

"""
Function subn()
Syntax:
 re.subn(pattern, repl, string, count=0, flags=0)
subn() is similar to sub() in all ways, except in its way to providing output. 
It returns a tuple with count of total of replacement and the new string rather than just the string.
"""

print(subn('ub', '~*', 'Subject has Uber booked already'))
t = subn('ub', '~*', 'Subject has Uber booked already', flags=IGNORECASE)
print(t)
print(len(t))

# This will give same output as sub() would have
print(t[0])

txt = "The rain in Spain"
x = search("rain", txt)
print(x.start(), x.end())
