a = __builtins__

# print = cHJpbnQ=

# get dict from ob

# __import__ = 6

g = lambda z, y: z.__getattribute__(y)

# get dict from object
s = lambda z: g(z, "__dict__")
t = lambda z: g(z, "__dir__")

# get callable
c = lambda z: g(z, "__call__")

# get keys from dict
v = lambda z: c(g(z, "keys"))

# convert to list
l = lambda z: list(z)

# get int from char
i = lambda z: ord(z)

# 'utf-8' as byte string
u = [0x75, 0x74, 0x66, 0x2D, 0x38]

# convert array of ints to string
its = lambda z: "".join(map(chr, z))

# decodes bytes to utf-8
bd = lambda z: g(z, t(b"")()[int(i("0") / 2)])(its(u))

# convert a string to numbers:
sti = lambda z: [i(iz) for iz in z]

# print
p = g(a, l(v(s(a))())[i("(")])
# returns '__import__'
import_name = l(v(s(a))())[i("*") - i("$")]
