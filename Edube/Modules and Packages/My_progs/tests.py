import sys
print('-> ', sys.path[0])
the_path = sys.path[0]
the_path = the_path.replace("My_progs", "My_modules")
print('-> ', the_path)