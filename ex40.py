class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing(self):
		for line in self.lyrics:
			print line
			
happybday = Song(["Happy birthday to you", 
					"I don't want to get sued", 
					"So I'll stop right there"])
					
bulls = Song(["They rally around the family", 
				"with pockets full of shells"])
				
happybday.sing()
bulls.sing()