#  Restaurant Rating Summary

ratings = [3.8, 4.5, 2.9, 4.8, 4.1]

highest = max(ratings)
lowest = min(ratings)

ranked = sorted(ratings, reverse=True)

top_rating = ranked[0]

print("Highest:", highest, "| Lowest:", lowest)
print("Ranked:", ranked)

if top_rating >= 4.5:
    print("Top restaurant qualifies for Featured badge!")
else:
    print("No featured badge this week")