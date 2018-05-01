from z3 import *

v1=BitVec('flag[1]',8)
v2=BitVec('flag[2]',8)
v3=BitVec('flag[3]',8)
v4=BitVec('flag[4]',8)
v5=BitVec('flag[5]',8)
v6=BitVec('flag[6]',8)
v7=BitVec('flag[7]',8)
v8=BitVec('flag[8]',8)

s = Solver()
s.add(331 * v7 + 317 * v6 + 313 * v5 + 311 * v4 + 307 * v3 + 293 * v2 + 283 * v1 + 337 * v8 == 225643)
s.add(509 * v7 + 503 * v6 + 499 * v5 + 491 * v4 + 487 * v3 + 479 * v2 + 467 * v1 + 521 * v8 == 356507)
s.add(587 * v7 + 577 * v6 + 571 * v5 + 569 * v4 + 563 * v3 + 557 * v2 + 547 * v1 + 593 * v8 == 410769)
s.add(643 * v7 + 641 * v6 + 631 * v5 + 619 * v4 + 617 * v3 + 613 * v2 + 607 * v1 + 647 * v8 == 450797)
s.add(773 * v7 + 769 * v6 + 761 * v5 + 757 * v4 + 751 * v3 + 743 * v2 + 739 * v1 + 787 * v8 == 546531)
s.add(853 * v7 + 839 * v6 + 829 * v5 + 827 * v4 + 823 * v3 + 821 * v2 + 811 * v1 + 857 * v8 == 598393)
s.add(919 * v7 + 911 * v6 + 907 * v5 + 887 * v4 + 883 * v3 + 881 * v2 + 877 * v1 + 929 * v8 == 646297)
s.add(1319 * v7 + 1307 * v6 + 1303 * v5 + 1301 * v4 + 1297 * v3 + 1291 * v2 + 1289 * v1 + 1321 * v8 == 935881)

if s.check() == sat:
	m = s.model()
	print hex(m[v1].as_long().real)
	print hex(m[v2].as_long().real)
	print hex(m[v3].as_long().real)
	print hex(m[v4].as_long().real)
	print hex(m[v5].as_long().real)
	print hex(m[v6].as_long().real)
	print hex(m[v7].as_long().real)
	print hex(m[v8].as_long().real)
