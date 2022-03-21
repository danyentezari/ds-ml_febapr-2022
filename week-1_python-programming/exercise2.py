# Prompt the user to name their top 5
# favorite movies

# (1) Use the input() function to prompt user for input

# (2) Use the appropriate List method to add user's input into 
# the list, favorite_movies

# (3) Use print() and square bracket notation to print each movie
# one by one

# (4 - bonus) if the user's input is empty, print "Please enter a name"
favorite_movies = []

# Add your code below this line
movie1 = input("Please enter your first favorite movie: ")
movie2 = input("Please enter your first favorite movie: ")
movie3 = input("Please enter your first favorite movie: ")
movie4 = input("Please enter your first favorite movie: ")
movie5 = input("Please enter your first favorite movie: ")

favorite_movies.append(movie1)
favorite_movies.append(movie2)
favorite_movies.append(movie3)
favorite_movies.append(movie4)
favorite_movies.append(movie5)

print( favorite_movies[0] )
print( favorite_movies[1] )
print( favorite_movies[2] )
print( favorite_movies[3] )
print( favorite_movies[4] )