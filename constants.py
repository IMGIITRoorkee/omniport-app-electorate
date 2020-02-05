#There must be a key in Posts_dict same as a category in categories_array
categories_tuple = (("B","Bhawan"),("I","Institute"))
posts_dict = {
  "Bhawan": (("Technical Secretary","Technical Secretary"),("Social and Cultural Secry","Social and Cultural Secretary"),("Maintenance Secretary-1","Maintenance Secretary-1"),("Maintenance Secretary-2","Maintenance Secretary-2"),("Sports Secretary","Sports Secretary"),("Mess Secretary","Mess Secretary")),
  "Institute": (("G.S. Hostel Affairs","G.S. Hostel Affairs"),("G.S. Academics Affairs(UG)","G.S. Academics Affairs(UG)"),("G.S. Academics Affairs(PG)","G.S. Academics Affairs(PG)"),("G.S. Technical Affairs","G.S. Technical Affairs"),("G.S. Alumni Affairs","G.S. Alumni Affairs"),("G.S. Sports Affairs","G.S. Sports Affairs"),("G.S. Cultural Council","G.S. Cultural Council"), ("D.G.S. Hostel Affairs(UG)","D.G.S. Hostel Affairs(UG)"), ("D.G.S. Hostel Affairs(PG)","D.G.S. Hostel Affairs(PG)"), ("D.G.S. Hostel Affairs(GIRLS)","D.G.S. Hostel Affairs(GIRLS)"))
}

all_posts = ()
for category in categories_tuple:
  all_posts = all_posts + posts_dict[category[1]]
