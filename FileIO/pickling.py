import pickle

master = "Master", "Anirudh", 2020,(
    (1,"Vaathi Ride"),
    (2,"Kutty Story"),
    (3,"Vaathi coming"),
    (4,"Polakattum"))
#================ write pickle data =============
# with open("master.pickle", 'wb') as master_file:
#     pickle.dump(master, master_file)

#================ read pickled data =============
# with open("master.pickle", 'rb') as master_read:
#      master2 = pickle.load(master_read)
# print(master2)
#
# album, artist, year, tracks = master2
#
# print(album)
# print(artist)
# print(year)
# for track in tracks:
#     trac_no, track_tiltle = track
#     print(trac_no, track_tiltle)

#================ read pickled data =============
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("master.pickle", 'wb') as master_file:
    # You can set the protocol while writing to a file
    pickle.dump(master, master_file, protocol= 0)
    pickle.dump(even, master_file, protocol= pickle.HIGHEST_PROTOCOL)
    pickle.dump(odd, master_file = pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, master_file)

with open("master.pickle", 'rb') as master_read:
     master2 = pickle.load(master_read)
     even_list = pickle.load(master_read)
     odd_list = pickle.load((master_read))
     x = pickle.load(master_read)
print(master2)

album, artist, year, tracks = master2

print(album)
print(artist)
print(year)
for track in tracks:
    trac_no, track_tiltle = track
    print(trac_no, track_tiltle)
print("-" * 40)
for e in even_list:
    print(e)
print("-" * 40)

for o in odd_list:
    print(o)
print("-" * 40)
print(x)

