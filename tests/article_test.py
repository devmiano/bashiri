import unittest
from ..app import Article

class TestArticle(unittest.TestCase):
  '''class that defines test cases for the article class'''
  
  def setUp(self):
    '''method to test the creation of a new user object'''
    self.new_user = Article('Annabel', 'Karish', 'annabelkarish', 'annabel@karish.com', 'Karish@Annabel2022')