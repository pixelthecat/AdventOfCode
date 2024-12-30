cls
dim fn%(7)
dim ta%(3)    ' temp array for matching with mul(/ml%
dim ml%(3)    ' will have ASCII for mul(
p1=0

rd=63842  ' beginning of the ram directory 0xf962
REM find the input file DATA03DO
REM directory format:
REM Byte 0: directory flag 
REM Byte 1-2: File start address
REM Byte 3-10: File name

for i%=0 to 7 : read fn%(i%) : next
for i%=0 to 3 : read ml%(i%) : next

@findfile
fd=1
for i%=0 to 7
if peek(rd+3+i%)<>fn%(i%) then fd=0
next
if fd=0 then rd=rd+11:goto @findfile else goto @ffound
if rd >= 64116 then print "Input file not found. Quitting." : END

@ffound
REM 
fp=peek(rd+1)+peek(rd+2)*256   ' calculate the starting address of the file

' do... while fp != -1
@readfile
gosub @advtomul
if fp = -1 then goto @p1done
goto @readfile

@p1done
print "part 1: ";p1

end





@advtomul
' advances FP to the next valid mul; if not found, sets fp to -1!
' alternately, if we need to look for multiple things, might do mp for mul pointer..
' m,u,l: 109, 117, 108; (,): 40,41; 0-9: 48-57; ',': 44; eof: 26
' uses r/w: x%, i%, ta%(), fp
' uses r: ml%

x%=peek(fp)
if x%=26 then fp=-1:return
if x%<>109 then fp=fp+1:goto @advtomul  ' finds an 'm'
ta%(0)=x%
' ok, we can go past the end of the file, but this won't actually make an error
' sloppy on most machines, but fine on the M100. There is a non-zero but very small
' chance this will have a false-positive. 
for i%=1 to 3: ta%(i%)=peek(fp+i%) : next
if ta%(0)<>ml%(0) or ta%(1)<>ml%(1) or ta%(2)<>ml%(2) or ta%(3)<>ml%(3) then fp=fp+1:goto @advtomul
' next byte should be a digit(s) then comma then digit(s) then )
i%=0
x1=0 ' first multiplicand
x2=0 ' second multiplicand
@am_readfirstnum
x%=peek(fp+4+i%)
if x%>=48 and x%<=57 then x1=x1*10+x%-48: i%=i%+1:goto @am_readfirstnum
if x%=44 and i%>0 then goto @am_readnextnum
fp=fp+1:goto @advtomul

@am_readnextnum
i%=i%+1  ' get past the comma
x%=peek(fp+4+i%)
if x% < 48 or x% > 57 then fp=fp+1:goto @advtomul else x2=x%-48
i%=i%+1
@am_rnn
x%=peek(fp+4+i%)
if x%>=48 and x%<=57 then x2=x2*10+x%-48 : i%=i%+1:goto @am_rnn
if x%<>41 then fp=fp+1:goto @advtomul  ' sooo close, but no closing paren
' if we get here, then we've actually found a valid mul and fp points to the start of it
' perhaps we should just do the calculation as we find the numbers? 
' could save off pointers to first num, comma, second num, paren? or first num, len, second num, len
' then do the multiplication and place in a variable to be used in the main prog
p1 = p1 + x1*x2
fp=fp+4+i%
return

' DATA03DO
data 68,65,84,65,48,51,68,79
' mul(
data 109,117,108,40   