profanity-filter
================

Python module that replaces inappropriate words with something more PG rated. Used in project that allows individuals to text message to sign used in Xmas decorations.

Uses a line separated file listing bad words as it's source
to check if a user submitted something inappropriate.

Code modified from orginal by Jared Mess

Modified by: jjb
Date 1/2/2016

Example of code use in test_profanity_filter.py:
Run
$ python test_profnaity_filter.py

Example Use:
text = "Cassandra is a fuCking piece of shit_on_a_long_stick"
f=Filter(text, "HAPPY")
f.clean_anywhere()
f.clean_start()
f.clean_whole_word()

Example Output---
Original:
Cassandra is a fuCking piece of shit_on_a_long_stick
Output from clean_anywhere:
CHAPPYandra is a HAPPYing piece of HAPPY_on_a_long_stick
Output from clean_start:
Cassandra is a HAPPYing piece of HAPPY_on_a_long_stick
Output from clean whole word:
Cassandra is a HAPPY piece of shit_on_a_long_stick
