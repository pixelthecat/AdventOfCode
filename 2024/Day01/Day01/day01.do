10 dim ar!(1,1000)
20 i%=0 : st%=0 : en%=0 : ro%=0 : tm!=0 : lc%=0 : i%=0
30 open "0:data01.do" for input as 1
40 input #1,lz$
50 ar!(0,i%)=val(left$(lz$,5))
60 ar!(1,i%)=val(right$(lz$,5))
70 if eof(1) goto 100
80 i% = i% + 1
90 goto 40
100 sz%=i%+1
110 print "Read in ";sz%;" lines"
120 i%=0
130 gosub 370
140 i%=1
150 gosub 370
160 ds=0
170 for i%=0 to sz%-1
180 tm=ar!(0,i%)-ar!(1,i%)
190 ds = ds + tm*sgn(tm)
200 next
210 print "part 1: ";ds
220 beep
230 p2=0
240 st%=0
250 for i%=0 to sz%-1
260 tm%=0
270 j%=st%
280 if j% > sz%-1 goto 330
290 if ar!(0,j%) = ar!(1,i%) then tm%=tm%+1 : st%=j%
300 if ar!(0,j%) > ar!(1,i%) then goto 330
310 j%=j%+1
320 goto 280
330 p2 = p2 + ar!(1,i%)*tm%
340 next
350 print "part 2: ";p2
360 end
370 st%=fix((sz%-1)/2)+1  
380 en%=sz%     
390 if en% <= 1 then return  :  rem while end > 1
400 if st% > 0 then st% = st% - 1 else en%=en%-1 : tm!=ar!(i%,en%) : ar!(i%,en%)=ar!(i%,0) : ar!(i%,0)=tm!
410 ro%=st%
420 lc%=2*ro%+1
430 if lc%>=en% goto 390
440 ch%=lc%
450 if ch%+1 < en% and ar!(i%,ch%) < ar!(i%,ch%+1) then ch%=ch%+1
460 if ar!(i%,ro%) < ar!(i%,ch%) then tm!=ar!(i%,ro%) : ar!(i%,ro%)=ar!(i%,ch%) : ar!(i%,ch%)=tm! : ro%=ch% else goto 390
470 goto 420
480 REM print array helper
490 print "Array:"
500 for j%=0 to sz%-1
510 print j%;ar!(0,j%);ar!(1,j%)
520 next
530 RETURN
540 END