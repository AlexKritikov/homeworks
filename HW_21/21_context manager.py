# Task 1. File Context Manager class.
# Create your own class, which can behave like a built-in function 'open'. Also, you need to extend its functionality
# with counter and logging. Pay special attention to the implementation of '__exit__' method, which has to cover all
# the requirements to context managers mentioned here
from logging import FileHandler
from datetime import datetime
import time
from unittest import TestCase
import os
class Opener:
    counter=0
    def __init__(self,name,mode='w' ):
        self.name=name
        self.mode=mode
        self.file=open(name,mode)
        self.logger=open('logger.txt','a+')
    def __enter__(self):
        Opener.counter+= 1
        self.logger.write(f'File "{self.name}" was opened {datetime.now()}\n')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.write(f'File "{self.name}" was closed {datetime.now()}\n')
        self.file.close()
        self.logger.close()
        print(f'File of "Opener" class was created {Opener.counter} time/times')

# Task 2. Writing tests for context manager
# Take your implementation of the context manager class from Task 1 and write tests for it. Try to cover as many use cases
# as you can, positive ones when a file exists and everything works as designed. And also, write tests when your class
# raises errors or you have errors in the runtime context suite.
class TestContextManager(TestCase):
    def test_file_exist(self):#file exist
        with open ('open_file.txt','r') as file:
            self.assertFalse(file.closed)
            file.close()
    def test_logger_exist(self):#logger exist
        with open('logger.txt', 'r') as logger:
            self.assertFalse(logger.closed)
            logger.close()
    def test_count_instance(self):#correct count instances of context manager
        with Opener('first file. text','w') as ff:
            ff.close()
        with Opener('second file. text', 'w') as sf:
            sf.close()
        self.assertEqual(Opener.counter,2)

    def test_logger_logs(self):  # logger takes in logs
        with open('logger.txt', 'r') as logger:
            logs=len(logger.readlines())
        self.assertTrue(logs>0)

    def test_logger_contains(self):  # logger contains proper messages
        with open('logger.txt', 'r') as logger:
            message=logger.read()
        self.assertIn('opened',message)
        self.assertIn('closed', message)
