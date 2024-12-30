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
x%=peek(fp)
if x%=26 then goto @p1done
if x%=109 then gosub @isvalidmul
fp=fp+1
goto @readfile

@p1done
print "part 1: ";p1


' reset the file pointer to the beginning
fp=peek(rd+1)+peek(rd+2)*256
en%=1   ' start enabled
p1=0
@scanp2
x%=peek(fp)
if x%=26 then goto @p2done
if x%=109 and en%=1 then gosub @isvalidmul
if x%=100 then gosub @isvaliddd
fp=fp+1
goto @scanp2

@p2done
print "Part 2: "; p1

end

@isvaliddd
if peek(fp)=100 and peek(fp+1)=111 and peek(fp+2)=40 and peek(fp+3)=41 then fp=fp+3:en%=1:return
if peek(fp)=100 and peek(fp+1)=111 and peek(fp+2)=110 and peek(fp+3)=39 and peek(fp+4)=116 and peek(fp+5)=40 and peek(fp+6)=41 then fp=fp+5:en%=0:return
return

@isvalidmul
' uses r/w: ta%, i%, x1, x2, p1, fp
' uses r  : ml%
REM starting: fp points at an 'm'
ta%(0)=peek(fp)
for i%=1 to 3: ta%(i%)=peek(fp+i%) : next
' see if starts with mul(
if ta%(0)<>109 or ta%(1)<>117 or ta%(2)<>108 or ta%(3)<>40 then return
fp=fp+4 : REM advance to putative digit
i%=0
x1=0 ' first multiplicand
x2=0 ' second multiplicand
@ivm_readfirstnum
x%=peek(fp+i%)
if x%>=48 and x%<=57 then x1=x1*10+x%-48: i%=i%+1:goto @ivm_readfirstnum
if x%=44 and i%>0 then goto @ivm_readnextnum
REM not valid, return without further updating fp
return 

@ivm_readnextnum
i%=i%+1  ' get past the comma
x%=peek(fp+i%)
if x% < 48 or x% > 57 then return else x2=x%-48
i%=i%+1
@ivm_rnn
x%=peek(fp+i%)
if x%>=48 and x%<=57 then x2=x2*10+x%-48 : i%=i%+1:goto @ivm_rnn
if x%<>41 then return  
p1 = p1 + x1*x2
fp=fp+i%
return

' DATA03DO
data 68,65,84,65,48,51,68,79
' mul(
data 109,117,108,40   