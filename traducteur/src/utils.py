def to_ascii(string):
 return unicodedata.normalize('NFD',unicode(string,'utf-8')).encode('ascii', 'ignore')

def with_underscore(string):
  tab = string.split()
  return '_'.join(tab)
