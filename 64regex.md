Regex Quick Reference
=====================

Make your own regex cheat sheet
Format it in Markdown


# Regex Cheat Sheet

## General Uses
+ \ to short-circuit literals
+ \+ to include any number of preceding
+ . for any character
+ () to form groups
+ {} to specify a certain number
+ [] to specify certain values/range of values
+ \* to specify 0 or more of preceding
+ ? to specify 0 or 1 of preceding
+ | to specify preceding OR anteceding

## Specific Examples
+ \w+ for any number of word symbols (letters, numbers, underscore)
+ \W for any non-word symbols
+ \d for any number
+ \D for any non-decimal digit (opposite of /d)
+ \s matches whitespace characters
+ \S matches not whitespace characters (opposite of \s)
+ \. for actual dot
+ \) for right parentheses
+ [ab] matches a or b
+ [a-c] matches a, b, c
+ \d{5} matches 5 digits
+ A{2,5} matches 2-5 A's
+ A{2,} matches 2 to infinity A's
+ A{,2} matches 0 to 2 A's
+ [0-3][0-5] matches all 2 digit numbers 00-35
+ [(+-)] matches (, +, -, )  
+ \d[^8] matches any number except 8
+ A|B matches A or B
