import sys
for i in range(0,4):
    someFile= open( "test%s.txt"%i , "r" )
    sys.stdin= someFile
#execfile("numpy array.py" )
    exec(compile(open("waterplatform.py", "rb").read(),"waterplatform.py",'exec'))

#import sys

#def main():
 #   in_file = open('test1.in')
  #  for line in in_file:
   #     sys.stdout.write(line)

#if __name__ == "__main__":
   # main()
#, "numpy array.py", 'exec'), globals, locals
