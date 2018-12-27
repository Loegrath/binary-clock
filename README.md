# binary-clock
Binary Clock Project

Create a clock that operates as follows:

Display:
```
 -------
 |0 0 0| 
 |0 0 0|
 |0 0 0|
 |0 0 0|
 -------

=========
||0 0 0||
||0 0 0||
||0 0 0||
||0 0 0||
=========
```
Reading the Display:
```
        ------- 
        |0 0 0| R0
        |0 0 0| R1
        |0 0 0| R2
        |0 0 0| R3
        -------
Columns: 0 1 2
```

--Border:
Single line: AM meridiem
Double line: PM meridiem

--Bottom to top number values:
Column 0 - Hours: 1, 2, 4, 8
Column 1 - Minutes: 1, 2, 4, 8
Column 2 - 15 Minute Increments: 15, 30, 45, 60

--Reading directions:
Add the activated values in the display columns together.

Examples:
```
 -------
 |0 1 0|
 |1 0 1|
 |1 0 0|
 |0 0 0|
 -------
 ```
 6:8+45
 Read as: 6:53 AM
```
=========
||0 1 0||
||1 0 0||
||1 1 1||
||1 0 0||
=========
```
  7:10+30
  Read as: 7:40 PM
