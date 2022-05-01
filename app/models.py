

class Article:
  def __init__(self, source, title, description, url, urlToImage, publishedAt):
    self.source = source
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
    
class Source:
  def __init__(self, id, name, description, url, category):
    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.name = category
