'''
Created on 2012/06/02

@author: ishii0514
'''
import unittest
from bloomfilter import *


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testgetHashList(self):
        bf = bloomfilter()
        l = bf.getHashList(200000000)
        self.assertEqual( 10,len(l))
        self.assertEqual([98, 128, 162, 200, 242, 288, 338, 392, 450, 512], l)

    def testexists(self):
        bf = bloomfilter()
        bf.setData(100000000)
        bf.setData(100005000)
        bf.setData(100004000)
        bf.setData(100002000)
        
        self.assertEqual(True,bf.exists(100000000))
        self.assertEqual(True,bf.exists(100002000))
        self.assertEqual(True,bf.exists(100004000))
        self.assertEqual(True,bf.exists(100005000))
        
        self.assertEqual(False,bf.exists(100005001))
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()