"""
Working with files in NiFi requires many more steps than you had to use when doing the same 
tasks in Python. There are benefits to using more steps and using Nifi, including that someone 
who does not know code can look at your data pipeline and understand what it is you are doing.

You may even find it easier to remember what it is you were trying to do when you come back to your
pipeline in the future. Also, changes to the data pipeline do not require refactoring a lot of code;
rather, you can reorder processors via drag and drop.
In this section, you will create a data pipeline that reads in the data.CSV file you created in Python.
It will run a query for people over the age of 40, then write out that record to
a file.
""
