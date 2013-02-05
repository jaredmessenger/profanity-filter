profanity-filter
================

Python module that replaces inappropriate words with something more PG rated.    

This is a basic word filter to keep something safe and kid friendly    

Usage
-----   
```python
f = Filter('badword and bad words', clean_word='unicorn')
safe_string = f.clean()
print safe_string
```