import sqlite3

# Create a SQLite database (or connect to an existing one)
conn = sqlite3.connect('music_data.db')
cursor = conn.cursor()

# Create a table named 'billboard_data'
cursor.execute('''CREATE TABLE IF NOT EXISTS billboard_data (
                    id INTEGER PRIMARY KEY,
                    issue_date TEXT,
                    song TEXT,
                    artist TEXT
                )''')

#Data including #1 songs for each week in 2023. This is a dictionary
data = [
    {"Issue date": "January 7", "Song": "All I Want for Christmas Is You", "Artist(s)": "Mariah Carey"},
    {"Issue date": "January 14", "Song": "Anti-Hero", "Artist(s)": "Taylor Swift"},
    {"Issue date": "January 21", "Song": "Anti-Hero", "Artist(s)": "Taylor Swift"},
    {"Issue date": "January 28", "Song": "Flowers", "Artist(s)": "Miley Cyrus"},
    {"Issue date": "February 4", "Song": "Flowers", "Artist(s)": "Miley Cyrus"},
    {"Issue date": "February 11", "Song": "Flowers", "Artist(s)": "Miley Cyrus"},
    {"Issue date": "February 18", "Song": "Flowers", "Artist(s)": "Miley Cyrus"},
    {"Issue date": "February 25", "Song": "Flowers", "Artist(s)": "Miley Cyrus"},
    {"Issue date": "March 4", "Song": "Flowers", "Artist(s)": "Miley Cyrus"},
    {"Issue date": "March 11", "Song": "Die for You", "Artist(s)": "The Weeknd and Ariana Grande"},
    {"Issue date": "March 18", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "March 25", "Song": "Flowers", "Artist(s)": "Miley Cyrus"},
    {"Issue date": "April 1", "Song": "Flowers", "Artist(s)": "Miley Cyrus"},
    {"Issue date": "April 8", "Song": "Like Crazy", "Artist(s)": "Jimin"},
    {"Issue date": "April 15", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "April 22", "Song": None, "Artist(s)": None},
    {"Issue date": "April 29", "Song": "Kill Bill", "Artist(s)": "SZA"},
    {"Issue date": "May 6", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "May 13", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "May 20", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "May 27", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "June 3", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "June 10", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "June 17", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "June 24", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "July 1", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "July 8", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "July 15", "Song": "Vampire", "Artist(s)": "Olivia Rodrigo"},
    {"Issue date": "July 22", "Song": "Last Night", "Artist(s)": "Morgan Wallen"},
    {"Issue date": "July 29", "Song": "Seven", "Artist(s)": "Jungkook featuring Latto"},
    {"Issue date": "August 5", "Song": "Try That in a Small Town", "Artist(s)": "Jason Aldean"},
    {"Issue date": "August 12", "Song": "Last Night", "Artist(s)": "Morgan Wallen"}
]    


# Insert data into the table
for entry in data:
    cursor.execute('INSERT INTO billboard_data (issue_date, song, artist) VALUES (?, ?, ?)',
                   (entry['Issue date'], entry['Song'], entry['Artist(s)']))


# Query the data to calculate weeks at #1 for each song
query = '''
    SELECT artist, song, COUNT(*) as weeks_at_1
    FROM billboard_data
    WHERE song IS NOT NULL
    GROUP BY artist, song
    ORDER BY artist, song
'''

# Execute the query and fetch the results
cursor.execute(query)
results = cursor.fetchall()

# Display the results
for result in results:
    artist = result[0]
    song = result[1]
    weeks_at_1 = result[2]
    print(f"{song} by {artist} was #1 {weeks_at_1} weeks in 2023, so far.")







# Query the data to calculate weeks at #1 for each song
query = '''
    SELECT artist, song, COUNT(*) as weeks_at_1
    FROM billboard_data
    WHERE song IS NOT NULL
    GROUP BY artist, song
    ORDER BY artist, song
'''

# Execute the query and fetch the results
cursor.execute(query)
results = cursor.fetchall()

# Create a table named 'top_songs' with columns: song, artist, weeks_at_1
cursor.execute('''CREATE TABLE IF NOT EXISTS top_songs (
                    id INTEGER PRIMARY KEY,
                    song TEXT,
                    artist TEXT,
                    weeks_at_1 INTEGER
                )''')

# Insert results into the 'top_songs' table
for result in results:
    artist = result[0]
    song = result[1]
    weeks_at_1 = result[2]
    cursor.execute('INSERT INTO top_songs (song, artist, weeks_at_1) VALUES (?, ?, ?)',
                   (song, artist, weeks_at_1))

# Commit changes and close the connection
conn.commit()
conn.close()
