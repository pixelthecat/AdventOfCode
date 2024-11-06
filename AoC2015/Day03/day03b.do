10 CLS
20 print time$
30 DIM HX%(2700)
40 DIM HY%(2700)
50 REM x,y are current position, a,b are robosanta position; c,d are temp positions
60 defint x,y,a,b,c,d
70 x=0 : y=0 : hn%=1 : pg%=0
80 gosub 270
90 OPEN "RAM:ac1503.do" FOR INPUT AS 1
100 N$=INPUT$(1,1)
110 M$=INPUT$(1,1)
120 pg%=pg%+2
130 print@ 41,pg%,hn%
140 if N$="^" THEN Y=Y+1 : D=Y : C=X : GOSUB 270 : GOTO 180
150 if N$="v" THEN Y=Y-1 : D=Y : C=X : GOSUB 270 : GOTO 180
160 if N$="<" THEN X=X-1 : D=Y : C=X : GOSUB 270 : GOTO 180
170 IF N$=">" THEN X=X+1 : D=Y : C=X : GOSUB 270 : GOTO 180
180 if M$="^" THEN B=B+1 : D=B : C=A : GOSUB 270 : GOTO 220
190 if M$="v" THEN B=B-1 : D=B : C=A : GOSUB 270 : GOTO 220
200 if M$="<" THEN A=A-1 : D=B : C=A : GOSUB 270 : GOTO 220
210 IF M$=">" THEN A=A+1 : D=B : C=A : GOSUB 270 : GOTO 220
220 if not eof(1) goto 100
230 close(1)
240 print@ 81,"Part 2: "hn%
250 print@ 121,time$
260 end
270 for i=hn% to 0 step -1
280 if C=HX%(i) then goto 290 else goto 300
290 if D=HY%(i) then return
300 next
310 hn% = hn%+1
320 hx%(hn%)=C : hy%(hn%)=D
330 RETURN
340 END