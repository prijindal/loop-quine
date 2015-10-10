This python Program outputs a javascript file which outputs the original python program

It is based on the idea put foreword in https://github.com/mame/quine-relay

and it actually works

[![Build Status](https://travis-ci.org/prijindal/loop-quine.svg)](https://travis-ci.org/prijindal/loop-quine)
```
python quine.py > quine.js
node quine.js > quine2.py
diff -s quine.py quine2.py
```

quine.py and quine2.py are freaking same
