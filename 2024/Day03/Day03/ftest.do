5 FD = 63842
6 FOR J=0 TO 15
15 X=FD+3+J*11
20 IF CHR$(PEEK(X))="Z" THEN AD=PEEK(X-2)+256*PEEK(X-1):PRINT(X)
30 NEXT
60 PRINT AD
70 FOR I=0 TO 10
80 PRINT CHR$(PEEK(AD+I));
90 NEXT
100 PRINT " "
