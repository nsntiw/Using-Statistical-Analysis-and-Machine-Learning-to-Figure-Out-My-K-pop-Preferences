import csv
import random

# Read the CSV file and get the title list
title_list = []
with open("Data/3_myplaylist_formatted.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title_list.append(row['title'])

def compare_tracks(track1, track2):
    """Compare two tracks and return the user's choice."""
    print(f'Track 1: {track1} vs Track 2: {track2}')
    while True:
        pick = input("Pick track (1 or 2): ")
        if pick == '1':
            return track1
        elif pick == '2':
            return track2
        else:
            print("Invalid choice, please pick 1 or 2.")

def random_pair_sort(tracks):
    """Sort tracks based on user comparisons using a random pairing approach."""
    if len(tracks) <= 1:
        return tracks
    
    sorted_tracks = []
    while tracks:
        #Shuffle the tracks for random pairing
        random.shuffle(tracks)
        track = tracks.pop(0)
        inserted = False
        for i, sorted_track in enumerate(sorted_tracks):
            if compare_tracks(track, sorted_track) == track:
                sorted_tracks.insert(i, track)
                inserted = True
                break
        if not inserted:
            sorted_tracks.append(track)
    
    return sorted_tracks

print(len(title_list))
# Sort the tracks
sorted_titles = random_pair_sort(title_list)

# Print the sorted titles
print("Sorted Titles:")
for i, title in enumerate(sorted_titles):
    print(f"{i + 1}: {title}")