from bs4 import BeautifulSoup
import urllib.request
import requests
from google import search
from urllib.parse import urlparse

class AnimeLyrics:

	# SEARCH_TERM: SONG TITLE

	def __init__(self, keyword):
		self.SEARCH_TERM = keyword

	def lyrics(self):
		resultArray = []
		for url in search(self.SEARCH_TERM, tld='com.pk', lang='es', stop=10):
			if (urlparse(url).hostname == "www.animelyrics.com"):
				resultArray.append(url)
				print(url)

		url = resultArray[0]
		html = requests.get(url)
		soup = BeautifulSoup(html.text, 'html5lib')

		tdSearch = soup.findAll("td", {
			"class" : "translation"
			});
		count = 0
		for element in tdSearch:
			count = count + 1

		lyrics = []
		if count == 0:
			# --------------------- TABLES WITHOUT TRANSLATIONS ---------------------
			result = self.find_between(soup.text, "Lyrics from Animelyrics.com", "Transliterated")
			lyrics.append(result.replace("\xa0", " ").strip())

		elif count == 2:
			# --------------------- TABLES WITH TRANSLATIONS ---------------------
			for linebreak in soup.find_all('br'):
			    linebreak.extract()
			for line in soup.find_all('dt'):
			    line.extract()

			mydivs = soup.findAll("td", {
				"class" : "romaji"
				});

			for x in mydivs:
				lyrics.append(x.text.replace("\xa0", " ").strip())

		else: 
			lyrics.append("Unsupported Format")

		return ", ".join(lyrics)

	def find_between(self, s, first, last):
	    try:
	        start = s.index( first ) + len( first )
	        end = s.index( last, start )
	        return s[start:end]
	    except ValueError:
	        return ""
