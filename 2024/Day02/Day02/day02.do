10 dim ax%(10)
20 dim a%(10)
30 lx%=0
40 p1%=0
50 p2%=0
60 va%=0
70 ln%=0
80 CLS
90 OPEN "data02.do" for input as 1
100 input #1, zz$
110 st%=1   ' starting character for reading in each number; strings are 1 based..
120 lx%=0
130 x%=val(mid$(zz$,st%,2)) ' looks like numbers are 1 or 2 digit
140 ax%(lx%)=x%
150 lx% = lx%+1
160 st%=instr(st%,zz$," ")
170 if st% = 0 then goto 200
180 st%=st%+1             ' I sure hope there's only one space..
190 goto 130
200 REM lx% has length of array, ax% is the current line in array form
210 ln%=ln%+1
220 for i%=0 to lx%
230 a%(i%)=ax%(i%)
240 next
250 al%=lx%
260 gosub 480
270 p1% = p1%+va%
280 ' part 2 :  if invalid, then see if the problem dampener helps
290 if va%=1 then goto 410
300 i%=0
310 al%=lx%-1
320 if i%>=lx% then goto 410 'while (i% < lx%)
330 sk%=0
340 for j%=0 to lx%-1
350 if j%=i% then sk%=1 else a%(j%-sk%)=ax%(j%)
360 next
370 gosub 480
380 if va%=1 goto 410 ' breaks out of while(i%<lx%)
390 i%=i%+1
400 goto 320  ' end while(i%<lx%)
410 p2%=p2%+va%
420 if eof(1) goto 440
430 goto 100
440 close 1
450 print "Part 1: "; p1%
460 print "Part 2: "; p2%
470 end
480 ' calculate if array a% is valid; has length al%, 'returns' va%
490 as% = sgn(a%(0)-a%(1))
500 if as% = 0 then va%=0 : RETURN
510 va%=1
520 for iv%=0 to al%-2
530 df% = a%(iv%) - a%(iv%+1)
540 if df% > 3 or df% < -3 then va%=0
550 if sgn(df%) <> as% then va%=0
560 next
570 RETURN
580 print@ 40,va%
590 for k%=0 to al%-1
600 print@ 80+k%*3,a%(k%);
610 next
620 for k%=0 to lx%-1
630 print@ 120+k%*3,ax%(k%);
640 next
650 RETURN
660 END