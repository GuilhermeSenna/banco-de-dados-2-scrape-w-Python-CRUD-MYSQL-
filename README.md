# banco-de-dados-2-scrape-w-Python-CRUD-MYSQL-
Database 2 discipline work involving data mining, data analysis and plotting in graphs

Language used in the slide and text document: PT/BR

The job consists of mining data from a dataset, in my work was chosen a public dataset, related to data from a school, from the math class (https://archive.ics.uci.edu/ml/datasets/Student+Performance), i obtained this data in a .csv file (student-mat.csv).

From this I created a python program called "Estudentes_Insert.py" responsible for reading this data from the .csv file and adding it to the MySQL database in the table stored in the file "Avaliacao II.sql", for this purpose a python library called "mysql.connector" was used.

After that, with another script of mine, "Estudents_Select.py" I read from the same MySQL database "Avaliacao II.sql", using the same library mentioned above, did some statistical calculations using the dictionary data structure, added these in a dictionary that includes all these called "arguments" and the result was plotted using the "matplotlib" library, in the "graficos BD" folder.

The text document "Explanation.txt" is a complementary explanation to all of this.

