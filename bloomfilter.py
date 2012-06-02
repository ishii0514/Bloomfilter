# -*- coding: utf-8 -*-
'''
Created on 2012/06/02

@author: ishii0514
'''

class bloomfilter:
    '''
    ブルームフィルタ
    現状
    '''
    #ハッシュ関数の数
    HASH_FUNCTION_COUNT = 10
    
    #ハッシュ関数に使う素数
    HASH_PRIMER = 10007
    
    #ハッシュ値の数
    HASH_COUNT = HASH_PRIMER + HASH_FUNCTION_COUNT
    
    #TODOとりあえず数値listで実装
    bloomarray = [0]*(HASH_COUNT)
    
    def __init__(self):
        ''''
        Constructor
        '''
    def setData(self,data):
        hashlist = self.getHashList(data)
        for num in hashlist:
            self.bloomarray[num] = 1
        
    def exists(self,data):
        hashlist = self.getHashList(data)
        for num in hashlist:
            if self.bloomarray[num] == 0:
                return False
        return True
    
    def getHashList(self,data):
        #hash number list
        hashlist = []
        for i in range(self.HASH_FUNCTION_COUNT):
            hashlist.append(self.hash_function(data, self.HASH_PRIMER+i))
        return hashlist
    
    def hash_function(self,data,num):
        #hash function
        return data % num