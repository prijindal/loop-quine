a = [
"---- Python Code -----",
"a = [",
"]",
"print(a[9])",
"for i in a:",
"    print(chr(34) + i + chr(34) +',')",
"for i in range(10, 18):",
"    print(a[i])",
"---- Javascript Code -----",
"var l = [",
"]",
"console.log(l[1])",
"for(i = 0;i < l.length; ++i) {",
"    console.log(String.fromCharCode(34) + l[i] + String.fromCharCode(34) + ',')",
"}",
"for(i = 2;i < 8;++i) {",
"    console.log(l[i])",
"}",
]
print(a[9])
for i in a:
    print(chr(34) + i + chr(34) +',')
for i in range(10, 18):
    print(a[i])
