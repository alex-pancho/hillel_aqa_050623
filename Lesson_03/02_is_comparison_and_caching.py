s1 = 'A'
s2 = 'A'
print(id(s1))
print(s1 == s2)
print(s1 is s2)


# cache all integers between -5 and 256, values for empty tuples, some strings
x = int('245')
y = int('245')
print(x is y)

x = int('257')
y = int('257')
print(x is y)
#
#
x = 909090000000000000000.1
y = 909090000000000000000.1
print(x is y)


x = None
y = False
z = True

print(x is None)

# Summary:
# Try to use is only for "var1 is None" "var2 is True"
# Be careful using 'is' for other types

# #variable id
# sudo gdb --pid <PID>
# dump memory /tmp/mem_file 0x7fe4d46f90b0 0x7fe4d46f90b0




