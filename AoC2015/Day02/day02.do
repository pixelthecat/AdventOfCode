10 CLS
20 DEFSTR N
30 DEFDBL A,B,C,TW,TR
40 TW=0 : TR=0
50 OPEN "RAM:ac1502.do" FOR INPUT AS 1
60 N=INPUT #1
70 xa=INSTR(N$,"x")
80 xb=INSTR(xa+1,N$,"x")
90 ln=LEN(N$)
100 A=VAL(LEFT$(N$,xa-1))
110 C=VAL(RIGHT$(N$,ln-xb))
120 B=VAL(MID$(N$,xa+1,xb-xa-1))
130 if A>B THEN X=A : A=B : B=X
140 if B>C THEN X=B : B=C : C=X
150 if A>B THEN X=A : A=B : B=X
160 TW=TW+(3*A*B)+(2*A*C)+(2*B*C)
170 TR=TR+A+A+B+B+A*B*C
180 IF NOT EOF(1) GOTO 60
190 CLOSE(1)
200 print "Part 1:"TW
210 print "Part 2:"TR
220 end
