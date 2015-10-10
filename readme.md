This python Program outputs a javascript file which outputs the original python program

It is based on the idea put foreword in https://github.com/mame/quine-relay

and it actually works

[![Build Status](https://travis-ci.org/prijindal/loop-quine.svg)](https://travis-ci.org/prijindal/loop-quine)
```
python multi.py > multi.js
node multi.js > out.py
```

out.py and multi.py are freaking same
