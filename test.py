import unittest
import test_func
import pytest

@pytest.fixture(autouse=True)
def recordAttr(request,record_property):
    class Record():
        def __init__(self):
            print "123"
        def record_property(self,key,value):
            print key
            record_property(key,value)
    request.cls.recordAttr =  Record()
    return Record()

@pytest.mark.usefixtures("recordAttr")
class Test_TestIncrementDecrement(unittest.TestCase):

    def test_increment(self):
        
        self.recordAttr.record_property("c","d")
        self.assertEquals(test_func.increment(3), 4)

    def test_decrement(self):
        self.assertEquals(test_func.decrement(3), 2)

#if __name__ == '__main__':
    # nose2.discover(argv=[sys.argv[0],  '-X', '-N 2'] )
 #   with open('results.xml', 'wb') as output:
  #      unittest.main( testRunner=xmlrunner.XMLTestRunner(output=output),
   #         failfast=False, buffer=False, catchbreak=False)