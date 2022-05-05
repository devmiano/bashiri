import unittest
from ..app import Article

class TestArticle(unittest.TestCase):
  '''class that defines test cases for the article class'''
  
  def setUp(self):
    '''method to test the creation of a new user object'''
    self.process_results = Article('Article Title', 'Article Description', 'Article Url', 'Image URL', 'Date Created')
    
  def test_init(self):
    self.assertEqual(self.process_results.title, 'Article Title')
    self.assertEqual(self.process_results.description, 'Article Description')
    self.assertEqual(self.process_results.url, 'Article Url')
    self.assertEqual(self.process_results.urlToImage, 'Image URL')
    self.assertEqual(self.process_results.publishedAt, 'Date Created')
    
  def tearDown(self):
    '''method to test run after the test case is executed'''  
    Article.process_results = []
    
  
  def test_get_news(self):
    '''method to test that the news is retrieved'''
    self.get_news()
    self.assertEqual(len(Article.get_news), 1)
    
  def test_get_headlines(self):
    '''method to test that the headlines is retrieved'''
    self.get_headlines()
    self.assertEqual(len(Article.get_headlines), 1)