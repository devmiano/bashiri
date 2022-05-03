class Article:
  '''class that creates new articles from a source'''
  def __init__(self, title, description, url, urlToImage, publishedAt):
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
    
      
    
class Source:
  '''class that creates a list of sources'''
  def __init__(self, id, name, description, url, category):
    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
