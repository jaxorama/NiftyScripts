# NiftyScripts
Simple useful scripts that I often use

PDF2Word.py
===========
python.exe PDF2Word.py C:\PDFs<br>
This converts all the PDF files in the C:\PDFs folder to docx Word documents. <br>
Better than using paid sites like zamzar which cost a lot and limit the number of conversions per day. 

WordleSolver.py
===============
python.exe WordleSolver.py <br>
This uses the word-list.txt file. You can enter the guess and Wordle's response as GGBBY. (Green, Black, Yellow)<br>
When all the letters show GGGGG, you have cracked the game.<br>
Credit: the word list is taken from https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt

SpellingBee.py
==============
python.exe words_alpha.txt abcdefg a<br>
Provide the word list as first parameter, all the letters as second parameter and central letter as third parameter.<br>
The script will generate several options. Also list all the possible pangrams in the end. <br>
Credit: the word list is taken from https://github.com/dwyl/english-words/blob/master/words_alpha.txt

dbdump.py
=========
Dumps the contents of a SQLite3 database in tabulated form. Needs the use of tabulate python library.
