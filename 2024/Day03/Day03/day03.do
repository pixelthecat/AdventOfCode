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
230 gosub 280
240 if fp = -1 then goto 260
250 goto 230
260 print "part 1: ";p1
270 end
280 ' advances FP to the next valid mul; if not found, sets fp to -1!
290 ' alternately, if we need to look for multiple things, might do mp for mul pointer..
300 ' m,u,l :  109, 117, 108; (,): 40,41; 0-9: 48-57; ',': 44; eof: 26
310 ' uses r/w :  x%, i%, ta%(), fp
320 ' uses r :  ml%
330 x%=peek(fp)
340 if x%=26 then fp=-1 : RETURN
350 if x%<>109 then fp=fp+1 : goto 280  ' finds an 'm'
360 ta%(0)=x%
370 ' ok, we can go past the end of the file, but this won't actually make an error
380 ' sloppy on most machines, but fine on the M100. There is a non-zero but very small
390 ' chance this will have a false-positive.
400 for i%=1 to 3 :  ta%(i%)=peek(fp+i%)  :  next
410 if ta%(0)<>ml%(0) or ta%(1)<>ml%(1) or ta%(2)<>ml%(2) or ta%(3)<>ml%(3) then fp=fp+1 : goto 280
420 ' next byte should be a digit(s) then comma then digit(s) then )
430 i%=0
440 x1=0 ' first multiplicand
450 x2=0 ' second multiplicand
460 x%=peek(fp+4+i%)
470 if x%>=48 and x%<=57 then x1=x1*10+x%-48 :  i%=i%+1 : goto 460
480 if x%=44 and i%>0 then goto 500
490 fp=fp+1 : goto 280
500 i%=i%+1  ' get past the comma
510 x%=peek(fp+4+i%)
520 if x% < 48 or x% > 57 then fp=fp+1 : goto 280 else x2=x%-48
530 i%=i%+1
540 x%=peek(fp+4+i%)
550 if x%>=48 and x%<=57 then x2=x2*10+x%-48  :  i%=i%+1 : goto 540
560 if x%<>41 then fp=fp+1 : goto 280  ' sooo close, but no closing paren
570 ' if we get here, then we've actually found a valid mul and fp points to the start of it
580 ' perhaps we should just do the calculation as we find the numbers?
590 ' could save off pointers to first num, comma, second num, paren? or first num, len, second num, len
600 ' then do the multiplication and place in a variable to be used in the main prog
610 p1 = p1 + x1*x2
620 fp=fp+4+i%
630 RETURN
640 ' DATA03DO
650 data 68,65,84,65,48,51,68,79
660 ' mul(
670 data 109,117,108,40
680 END