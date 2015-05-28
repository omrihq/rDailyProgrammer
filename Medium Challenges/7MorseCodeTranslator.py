alphabet = {".-"   : "A",          
"-..." : "B",          
"-.-." : "C",          
"-.."  : "D",          
"."    : "E",          
"..-." : "F",          
"--."  : "G",          
"...." : "H",          
".."   : "I",          
".---" : "J",          
"-.-"  : "K",          
".-.." : "L",          
"--"   : "M",          
"-." : "N",
"---" : "O",
".--." : "P",
"--.-" : "Q",
".-." : "R",
"..." : "S",
"-" : "T",
"..-" : "U",
"...-" : "V",
".--" : "W",
"-..-" : "X",
"-.--" : "Y",
"--.." : "Z",
"/" : " "}
##try using this: .... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--

code = raw_input("Enter the morse code you\'d like to translate, with each word divided by a \" / \" and each letter by a space")
#Beautifully pythonic if I do say so myself
print (''.join(alphabet[letter] for letter in code.split()))

