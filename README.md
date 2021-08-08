# dictionary-app

A dictionary app made using Python that reads data from a json file (available as data.json), checks 
for the word, and prints out the output in a clean, readbale format. The app also uses the difflib library to check for
closeness of a word to that of a user input, and helps auto suggest a close word taking in a default cut-off value of 0.6

Optimized for:
- Auto suggestion of misspelled words using difflib
- checking for words like New York or USA which can have different capitalizations
- Displaying the output in a clean, readable format

What can be better:
- A way to query the data from a database instead of a json file (because it slows down)

Thank you
