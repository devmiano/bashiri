import unittest
from ..app import Source

class TestSource(unittest.TestCase):
  '''class that defines test cases for the source class'''
  
  def setUp(self):
    '''method to test the creation of a new source object'''
    self.process_sources = Source('Source ID', 'Source Name', 'Source Description', 'Source Url', 'Category')
    
  def test_init(self):
    self.assertEqual(self.process_sources.id, 'Source ID')
    self.assertEqual(self.process_sources.name, 'Source Name')
    self.assertEqual(self.process_sources.description, 'Source Description')
    self.assertEqual(self.process_sources.url, 'Source URL')
    self.assertEqual(self.process_sources.category, 'Source Category')
    
  def tearDown(self):
    '''method to test run after the test case is executed'''  
    Source.process_sources = []
    
  
  def test_get_sources(self):
    '''method to test that the source is retrieved'''
    self.get_sources()
    self.assertEqual(len(Source.get_sources), 1)