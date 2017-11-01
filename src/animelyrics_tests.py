from animelyrics import AnimeLyrics

al = AnimeLyrics("catch in the moment")

print("------------------------------------------")
print("LYRICS:")
print(al.lyrics("jp"))
print("------------------------------------------")
print("TITLE:")
print(al.song_title())
print("------------------------------------------")