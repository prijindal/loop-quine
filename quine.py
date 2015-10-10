a = [
'---- Python Code -----',
'a = [',
']',
'print(a[9])',
'for i in a:',
'    print(chr(39) + i + chr(39) +",")',
'for i in range(10, 20):',
'    print(a[i])',
'---- Javascript Code -----',
'var l = [',
']',
'console.log(l[21])',
'console.log(l[22])',
'for(i = 0;i < l.length; ++i) {',
'    console.log(String.fromCharCode(39) + l[i] + String.fromCharCode(39) + ",")',
'}',
'console.log(l[23])',
'for(i = 24;i < 31;++i) {',
'    console.log(l[i])',
'}',
'---- PHP Code ----',
'<?php',
'$l = array(',
');',
'echo $l[1].PHP_EOL;',
'for($i = 0;$i < sizeof($l);++$i) {',
'   echo chr(39).$l[$i].chr(39).chr(44).PHP_EOL;',
'};',
'for($i = 2;$i < 8;++$i) {',
'   echo $l[$i].PHP_EOL;',
'};',
]
print(a[9])
for i in a:
    print(chr(39) + i + chr(39) +",")
for i in range(10, 20):
    print(a[i])
