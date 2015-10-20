class foo():
    def __enter__(self):
        global y
        y = 5
        print "enter"
        self.setx(2)
        return self

    def __exit__(self, type, value, traceback):
        print y
        print "exit"
    
    def setx(self, arg):
        self.x = arg
        
    def status(self):
        print "status %d" % self.x
    
def as_tester():
	""" TODO """
	temp = foo()
	temp.setx(1)
	temp.status()
	with temp as t:
	    t.status()

def assert_tester():
	""" TODO """

def break_tester():
	counter = 0
	while True:
		counter += 1
		print "counter"
		if counter > 3:
			break

def continue_tester():
    i = 0
    while i < 3:
        i += 1
        print "continue_tester()"
        continue
        print "Tego nie ma"
        
def lambda_tester():
    bar = lambda y: 2 * y         			
    print bar(1)
    
def del_tester():
    m_dict = {1: 1, "1": "str-1", 'a': 2}
    print m_dict
    del m_dict['1']
    print m_dict
    del m_dict[1]
    print m_dict
    
def finally_tester(str):
    try:
        print "Int %d" % int(str)
    except ValueError:
        print "ValueError"
    finally:
        print "Finally"
        
def raise_tester():
    try:
        raise(TypeError)
    except ValueError:
        print "ValueError"
    except TypeError:
        print "TypeError"        
    finally:
        print "Finally"     
        
def pass_tester():
    if True:
        pass
        print "will this occur?"
    while True:
        pass   
			
#as_tester()
#break_tester()
#continue_tester()			
#lambda_tester()
#del_tester()
#finally_tester('abc')
#finally_tester('1')
raise_tester()
pass_tester()
