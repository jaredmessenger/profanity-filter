from profanity_filter import Filter

text = "Cassandra is a fuCking piece of shit_on_a_long_stick"

print "We first test the three cleaning methods on the message:"
print text
print

f=Filter(text, "HAPPY")
print "Output from clean_anywhere:"
print f.clean_anywhere()
print "Output from clean_start:"
print f.clean_start()
print "Output from clean whole word:"
print f.clean_whole_word()


print

text = "Cassy is an asset to our company."
print "We now test the profanity check with the following:"
print text
print "Output from clean_anywhere:"

f=Filter(text,'HAPPY')
f.clean_anywhere()
if not f.is_profanity_found():
    print "No profanity."
else:
    print "Here is the clean anywhere:"
    print f.get_clean_string()


print
print "Output from clean_start:"
print f.clean_start()
if not f.is_profanity_found():
    print "No profanity."
else:
    print "Here is the clean string:"
    print f.get_clean_string()

print
print "Output from clean whole word:"
print f.clean_whole_word()
if not f.is_profanity_found():
    print "No profanity."
else:
    print "Here is the clean string:"
    print f.get_clean_string()





#print "We now make sure the error handling is working. An error should occur"
#f = Filter(text, "SAD")
#print f.is_profanity_found()
#print f.get_clean_string()

