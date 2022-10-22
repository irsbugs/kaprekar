# kaprekar

Kaprekar constants apply to all three and four digit numbers, except where the number is all the same digits.

The program **keprekar_constant.py** provides a demonstration.

Reference:
https://en.wikipedia.org/wiki/Kaprekar%27s_routine

*In number theory, Kaprekar's routine is an iterative algorithm that, with each iteration, takes a natural number 
in a given number base, creates two new numbers by sorting the digits of its number by descending and ascending order, 
and subtracts the second from the first to yield the natural number for the next iteration*


Snippets of program output:
```
$ python kaprekar_constant.py 105

Kaprekar Constant
Initial integer:             105

Iteration count:               1
Rearranged decending:        510
Rearranged accending:        015
Sutraction result:           495

Iteration count:               2
Rearranged decending:        954
Rearranged accending:        459
Sutraction result:           495
Repeating sequence was reached...

105 took 1 iterations to reach a repeating 495
...

$ python kaprekar_constant.py 1963

Kaprekar Constant
Initial integer:            1963

Iteration count:               1
Rearranged decending:       9631
Rearranged accending:       1369
Sutraction result:          8262

Iteration count:               2
Rearranged decending:       8622
Rearranged accending:       2268
Sutraction result:          6354

Iteration count:               3
Rearranged decending:       6543
Rearranged accending:       3456
Sutraction result:          3087

Iteration count:               4
Rearranged decending:       8730
Rearranged accending:       0378
Sutraction result:          8352

Iteration count:               5
Rearranged decending:       8532
Rearranged accending:       2358
Sutraction result:          6174

Iteration count:               6
Rearranged decending:       7641
Rearranged accending:       1467
Sutraction result:          6174
Repeating sequence was reached...

1963 took 5 iterations to reach a repeating 6174

$ python kaprekar_constant.py

Kaprekar Constant
100 6 495
101 6 495
102 5 495
103 4 495
104 3 495
105 1 495
106 2 495
107 3 495
108 4 495
109 5 495
110 6 495
Initial integer can not be all the same digit.
Initial integer can not be all the same digit.
111 1 000
112 6 495
113 5 495
114 4 495
115 3 495
116 1 495
...
990 5 495
991 4 495
992 3 495
993 2 495
994 1 495
995 3 495
996 4 495
997 5 495
998 6 495
Initial integer can not be all the same digit.
Initial integer can not be all the same digit.
999 1 000
1000 5 6174
1001 4 6174
1002 3 6174
1003 3 6174
1004 7 6174
1005 7 6174
1006 7 6174
1007 3 6174
1008 3 6174
1009 4 6174
1010 4 6174
...
6173 3 6174
6174 0 6174
6175 7 6174
...
9990 4 6174
9991 6 6174
9992 4 6174
9993 6 6174
9994 6 6174
9995 4 6174
9996 6 6174
9997 4 6174
9998 5 6174
Initial integer can not be all the same digit.
Initial integer can not be all the same digit.
9999 1 0000
```
