import unittest
from SortedList import SortedList 

class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case. And create a SortedList object """
        self.testList = SortedList()

        #add some nodes
        self.testList.insertNode(2)
        self.testList.insertNode(1)
        self.testList.insertNode(5)
        self.testList.insertNode(3)
        

    def test1(self):
        """This test method checkd for the getLength method"""

        assert self.testList.getLength() == 4, "getLength() not providing correct length of list"

    def test2(self):
        """test case 2 checks for insertNode() method"""

        assert self.testList.insertNode(4) == 3, "insertNode() node adding new element correctly"

    def test3(self):
        """test case 3 checks for removeLowest() method"""

        supposedRemoved = self.testList.getFirst()

        assert self.testList.removeLowest() == supposedRemoved, "removeLowest() not removing lowest value correctly"


    def test4(self):
        """test case 4 checks for removeHighest() method"""

        supposedRemoved = self.testList.getLast()

        assert self.testList.removeHighest() == supposedRemoved, "removeHighest() not removing hiughest value correctly" 


    def test5(self):
        """test case 5 checks for isEmpty() method"""

        assert self.testList.isEmpty() == False, "isEmpty() not providing correct information about list"       



if __name__ == "__main__":

    tester = SimpleTestCase()

    #first we test each test one by one

    tester.setUp()
    tester.test1()
    tester.test2()
    tester.test3()
    tester.test4()
    tester.test5()

    """ Now we run all cases in once """

    unittest.main() # run all tests
