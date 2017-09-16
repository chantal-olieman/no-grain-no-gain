ins = open( "data/clean.txt", "r" )
data = [[int(n) for n in line.split()] for line in ins]
print data
