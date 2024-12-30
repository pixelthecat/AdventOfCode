10 cls
20 dim fn%(7)
30 dim ta%(3)    ' temp array for matching with mul(/ml%
40 dim ml%(3)    ' will have ASCII for mul(
50 p1=0
60 rd=63842  ' beginning of the ram directory 0xf962
70 REM find the input file DATA03DO
80 REM directory format
90 REM Byte 0 :  directory flag
100 REM Byte 1-2 :  File start address
110 REM Byte 3-10 :  File name
120 for i%=0 to 7  :  read fn%(i%)  :  next
130 for i%=0 to 3  :  read ml%(i%)  :  next
140 fd=1
150 for i%=0 to 7
160 if peek(rd+3+i%)<>fn%(i%) then fd=0
170 next
180 if fd=0 then rd=rd+11 : goto 140 else goto 200
190 if rd >= 64116 then print "Input file not found. Quitting."  :  END
200 REM
210 fp=peek(rd+1)+peek(rd+2)*256   ' calculate the starting address of the file
220 ' do... while fp != -1
230 x%=peek(fp)
240 if x%=26 then goto 280
250 if x%=109 then gosub 440
260 fp=fp+1
270 goto 230
280 print "part 1: ";p1
290 ' reset the file pointer to the beginning
300 fp=peek(rd+1)+peek(rd+2)*256
310 en%=1   ' start enabled
320 p1=0
330 x%=peek(fp)
340 if x%=26 then goto 390
350 if x%=109 and en%=1 then gosub 440
360 if x%=100 then gosub 410
370 fp=fp+1
380 goto 330
390 print "Part 2: "; p1
400 end
410 if peek(fp)=100 and peek(fp+1)=111 and peek(fp+2)=40 and peek(fp+3)=41 then fp=fp+3 : en%=1 : RETURN
420 if peek(fp)=100 and peek(fp+1)=111 and peek(fp+2)=110 and peek(fp+3)=39 and peek(fp+4)=116 and peek(fp+5)=40 and peek(fp+6)=41 then fp=fp+5 : en%=0 : RETURN
430 RETURN
440 ' uses r/w :  ta%, i%, x1, x2, p1, fp
450 ' uses r   :  ml%
460 REM starting :  fp points at an 'm'
470 ta%(0)=peek(fp)
480 for i%=1 to 3 :  ta%(i%)=peek(fp+i%)  :  next
490 ' see if starts with mul(
500 if ta%(0)<>109 or ta%(1)<>117 or ta%(2)<>108 or ta%(3)<>40 then return
510 fp=fp+4  :  REM advance to putative digit
520 i%=0
530 x1=0 ' first multiplicand
540 x2=0 ' second multiplicand
550 x%=peek(fp+i%)
560 if x%>=48 and x%<=57 then x1=x1*10+x%-48 :  i%=i%+1 : goto 550
570 if x%=44 and i%>0 then goto 600
580 REM not valid, return without further updating fp
590 RETURN
600 i%=i%+1  ' get past the comma
610 x%=peek(fp+i%)
620 if x% < 48 or x% > 57 then return else x2=x%-48
630 i%=i%+1
640 x%=peek(fp+i%)
650 if x%>=48 and x%<=57 then x2=x2*10+x%-48  :  i%=i%+1 : goto 640
660 if x%<>41 then return
670 p1 = p1 + x1*x2
680 fp=fp+i%
690 RETURN
700 ' DATA03DO
710 data 68,65,84,65,48,51,68,79
720 ' mul(
730 data 109,117,108,40
740 END