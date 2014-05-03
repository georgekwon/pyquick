import sys

# Define a main() function that prints a little greeting.
'''def main():
  # Get the name from the command line, using 'World' as a fallback.
  name = sys.argv[1]
  fruit1 = sys.argv[2]
  fruit2 = sys.argv[3]
  text = ("%s went to the bathroom after eating %s and %s" % (name, fruit1, fruit2))
  print text
'''

#testing for in functions
'''def main():
    squares = [2,4,6,8,10]
    sum = 0
    for num in squares[1:3]:
        sum += num
    print sum
    '''

#testing while loops and list methods
'''def main():
    squares = [2,4,6,8,10]
    i = 0
    while i < len(squares):
            print squares[i]
            i = i + 3
    print squares
    squares.extend([12, 14])
    print squares
    squares.pop(squares.index(6))
    print squares
    squares[0:3] = 1
    print squares
'''
f = open('small.txt','r')
for line in f:
    print line
f.close()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
