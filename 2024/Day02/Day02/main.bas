dim ax%(10)
dim a%(10)
lx%=0
p1%=0 
p2%=0
va%=0
ln%=0

CLS
OPEN "data02.do" for input as 1
@readline
input #1, zz$

st%=1   ' starting character for reading in each number; strings are 1 based..
lx%=0
@nextnum
x%=val(mid$(zz$,st%,2)) ' looks like numbers are 1 or 2 digit 
ax%(lx%)=x%
lx% = lx%+1
st%=instr(st%,zz$," ")
if st% = 0 then goto @endline
st%=st%+1             ' I sure hope there's only one space..
goto @nextnum
@endline
REM lx% has length of array, ax% is the current line in array form

ln%=ln%+1
for i%=0 to lx%
 a%(i%)=ax%(i%)
next
al%=lx%
gosub @isvalid
p1% = p1%+va%

' part 2: if invalid, then see if the problem dampener helps
if va%=1 then goto @skippd

i%=0
al%=lx%-1
@pdtop

if i%>=lx% then goto @skippd 'while (i% < lx%)
sk%=0
for j%=0 to lx%-1
if j%=i% then sk%=1 else a%(j%-sk%)=ax%(j%)
next
gosub @isvalid
if va%=1 goto @skippd ' breaks out of while(i%<lx%)
i%=i%+1
goto @pdtop  ' end while(i%<lx%)

@skippd
p2%=p2%+va%
if eof(1) goto @donereading
goto @readline

@donereading
close 1
print "Part 1: "; p1%
print "Part 2: "; p2%
end


@isvalid
' calculate if array a% is valid; has length al%, 'returns' va%
as% = sgn(a%(0)-a%(1))
if as% = 0 then va%=0: return
va%=1
for iv%=0 to al%-2
 df% = a%(iv%) - a%(iv%+1)
 if df% > 3 or df% < -3 then va%=0
 if sgn(df%) <> as% then va%=0
next
return

@printar
print@ 40,va%
for k%=0 to al%-1
 print@ 80+k%*3,a%(k%);
next
for k%=0 to lx%-1
 print@ 120+k%*3,ax%(k%);
next
return