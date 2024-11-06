10 CLS
20 print time$
30 DIM HX%(2700)
40 DIM HY%(2700)
50 REM x,y are current position; hn is end of array
60 defint x,y
70 x=0 : y=0 : hn%=0 : pg%=0
80 gosub 220
90 OPEN "RAM:ac1503.do" FOR INPUT AS 1
100 N$=INPUT$(1,1)
110 pg%=pg%+1
120 print@ 41,pg%,hn%
130 if N$="^" THEN Y=Y+1 : GOSUB 220 : GOTO 170
140 if N$="v" THEN Y=Y-1 : GOSUB 220 : GOTO 170
150 if N$="<" THEN X=X-1 : GOSUB 220 : GOTO 170
160 IF N$=">" THEN X=X+1 : GOSUB 220 : GOTO 170
170 if not eof(1) goto 100
180 close(1)
190 print@ 81,"Part 1: "hn%+1
200 print@ 121,time$
210 end
220 for i=0 to hn%
230 if x=hx%(i) then goto 240 else goto 250
240 if y=hy%(i) then return
250 next
260 hn% = hn%+1
270 hs%(0,hn%)=x : hs%(1,hn%)=y
280 RETURN
290 END