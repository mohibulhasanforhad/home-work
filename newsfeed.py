# News Feed — Latest 3 Headlines

headlines = [ "new ai law passed",
    "budget cuts announced",
    "school reform bill",
    "sports final tonight",
    "weather alert issued"]

if len(headlines) >= 3:

    recent = headlines[-3:]

    print("Total headlines:", len(headlines), "| Showing:", len(recent))

    print("1.", recent[0].title())
    print("2.", recent[1].title())
    print("3.", recent[2].title())

else:
    print("Not enough news yet")