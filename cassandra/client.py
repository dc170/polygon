
import rpyc

def noisy(string):
    print 'Noisy:', repr(string)

proxy = rpyc.connect('localhost', 18861, config={'allow_public_attrs': True})
fileobj = open('testfile.txt')
linecount = proxy.root.line_counter(fileobj, noisy)
print 'The number of lines in the file was', linecount
