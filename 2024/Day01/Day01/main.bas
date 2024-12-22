dim ar!(1,1000)
i%=0:st%=0:en%=0:ro%=0:tm!=0:lc%=0:i%=0

open "0:data01.do" for input as 1
@readline
input #1,lz$
ar!(0,i%)=val(left$(lz$,5))
ar!(1,i%)=val(right$(lz$,5))
if eof(1) goto @readdone
i% = i% + 1
goto @readline
@readdone
sz%=i%+1
print "Read in ";sz%;" lines"
i%=0
gosub @heapsort
i%=1
gosub @heapsort

ds=0
for i%=0 to sz%-1
tm=ar!(0,i%)-ar!(1,i%)
ds = ds + tm*sgn(tm)
next 
print "part 1: ";ds
beep
p2=0
st%=0
for i%=0 to sz%-1
tm%=0
j%=st%
@whilej
if j% > sz%-1 goto @skiptonext
if ar!(0,j%) = ar!(1,i%) then tm%=tm%+1:st%=j%
if ar!(0,j%) > ar!(1,i%) then goto @skiptonext
j%=j%+1
goto @whilej
@skiptonext
p2 = p2 + ar!(1,i%)*tm%
next
print "part 2: ";p2
end


@heapsort
st%=fix((sz%-1)/2)+1  
en%=sz%    
@hsouterloop
if en% <= 1 then return : rem while end > 1
if st% > 0 then st% = st% - 1 else en%=en%-1:tm!=ar!(i%,en%):ar!(i%,en%)=ar!(i%,0):ar!(i%,0)=tm!

ro%=st%
@hsinnerloop
lc%=2*ro%+1
if lc%>=en% goto @hsouterloop
ch%=lc%
if ch%+1 < en% and ar!(i%,ch%) < ar!(i%,ch%+1) then ch%=ch%+1

if ar!(i%,ro%) < ar!(i%,ch%) then tm!=ar!(i%,ro%):ar!(i%,ro%)=ar!(i%,ch%):ar!(i%,ch%)=tm!:ro%=ch% else goto @hsouterloop
goto @hsinnerloop

@printarray
REM print array helper
print "Array:"
for j%=0 to sz%-1
print j%;ar!(0,j%);ar!(1,j%)
next
return
 