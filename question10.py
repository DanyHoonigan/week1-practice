songs = ["song A", "song B", "song C", "song D", "song E", "song F", "song G", "song H"]
print(f"Complete Playlist: {songs}")
print(f"First 3 songs: {songs[0:3]}")
print(f"Last 3 songs: {songs[-3:]}")
print(f"Songs from Position 3 to 6: {songs[3:7]}")
print(f"Every Alternative Song: {songs[::2]}")
print(f"Playlist in Reverse Order: {songs[::-1]}")
print(f"Playlist Without First and Last Song: {songs[1:-1]}")