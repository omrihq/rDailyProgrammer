#alphabet
alphabet = {"A" : ".-",        
"B" : "-...",      
"C" : "-.-.",     
"D" : "-..",       
"E" : ".",         
"F" : "..-.",      
"G" : "--.",       
"H" : "....",      
"I" : "..",        
"J" : ".---",      
"K" : "-.-",      
"L" : ".-..",      
"M" : "--",        
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--.."}

##try using this: .... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--

code = raw_input("Enter the morse code you\'d like to translate, with each word divided by a \" / \" and each letter by a space")
morse = code.split(" / ")
#Not very pythonic...
for word in morse:
        word = word.split()
        for morse_letter in word:
                for letter, key in alphabet.iteritems():
                        if morse_letter == key:
                                print letter,