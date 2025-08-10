import re
from collections import OrderedDict

od = OrderedDict()

od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)

od.move_to_end('a')
print(od)

od.popitem(last=False)
od.popitem(last=True)
print(od)


from collections import Counter

c = Counter("abracadabra")
print(c)

print(f'tos. {c.most_common(2)}')

print(list(c.elements()))


from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(10, 20)

print(p.x, p.y)

p2 = p._replace(x=15)
print(p2)

print(p._asdict())


from collections import deque

dq = deque([1, 2, 3])

dq.append(4)
dq.appendleft(0)

print(dq)

dq.rotate(2)
print(dq)


szoveg = """
ab
ax
bz
a123b
a--b
aXYZb
"""

minta = r'[a][b]'
talalat = re.findall(minta, szoveg)
print(talalat)

minta = r'[abc][xyz]'
talalat = re.findall(minta, szoveg)
print(talalat)

minta = r'a.*b'
talalat = re.findall(minta, szoveg)
print(talalat)