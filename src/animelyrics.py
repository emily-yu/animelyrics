from bs4 import BeautifulSoup
import urllib.request
import requests
from google import search
from urllib.parse import urlparse

class AnimeLyrics:

	# SEARCH_TERM: SONG TITLE
	# PAGE_URL: animelyrics.com PAGE URL
	# SOUP: HTML CONTENT FOR PAGE_URL

	def __init__(self, keyword):
		self.SEARCH_TERM = keyword
		for url in search(self.SEARCH_TERM, tld='com.pk', lang='es', stop=10):
			if (urlparse(url).hostname == "www.animelyrics.com"):
				self.PAGE_URL = url

		html = requests.get(self.PAGE_URL)
		self.SOUP = BeautifulSoup(html.text, 'html5lib')

	def lyrics(self):
		tdSearch = self.SOUP.findAll("td", {
			"class" : "translation"
		});

		count = 0
		for element in tdSearch:
			count = count + 1

		lyrics = []

		# --------------------- TABLES WITHOUT TRANSLATIONS ---------------------
		if count == 0:
			result = self.find_between(self.SOUP.text, "Lyrics from Animelyrics.com", "Transliterated")
			lyrics.append(result.replace("\xa0", " ").strip())

		# --------------------- TABLES WITH TRANSLATIONS ------------------------
		elif count == 2:
			for linebreak in self.SOUP.find_all('br'):
			    linebreak.extract()
			for line in self.SOUP.find_all('dt'):
			    line.extract()

			mydivs = self.SOUP.findAll("td", {
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
			return "Error in Page Structure"

	def song_title(self):
		return self.SOUP.findAll("h1")[1].get_text()

