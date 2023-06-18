

nMovies, itemsOnHL, nOfSimilarities = map(int, input().strip().split())

# Initial horror nodes
hList = list(map(int, input().strip().split()))

#Initialising similarities
similarities = {}
for i in range(nMovies):
    similarities[i] = []

#Initialising scores and setting values to 0 if on horror list
scores = {}
for movies in hList:
    scores[movies] = 0


# Adding similarities
for i in range(nOfSimilarities):
    id1, id2 = map(int, input().strip().split())
    similarities[id1].append(id2)
    similarities[id2].append(id1)


#going through and adding 1 to score of movies that have similarity to horror movies
current = hList
while current:
    newList = []
    for movie in current:
        for similarity in similarities[movie]:
            if similarity not in scores:
                scores[similarity] = scores[movie] + 1
                newList.append(similarity)
    current = newList

# finding movie with highest score
maxScore = -1 
bestMovie = -1
for movie in range(nMovies):
    #if movie has no score, it has infinite score and wins
    if movie not in scores:
        bestMovie = movie
        break 
    elif scores[movie] > maxScore:
        maxScore = scores[movie]
        bestMovie = movie

print(bestMovie)
