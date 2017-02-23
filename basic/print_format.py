aName = 'name'
age = 12
print("%s is %d years old." % (aName, age))

itemdict = {"item": "banana", "cost": 24}
print("The %(item)s costs %(cost)10.1f cents" %itemdict)

name = "@hello@"
print("| %s |" % name)
print("| %10s |" % name)
print("| %+10s |" % name)
print("| %-10s |" % name)
