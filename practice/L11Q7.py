# Mini Leaderboard

Scores = [40, 80, 65, 95, 70]
Winner = Scores[0]
for i in range(0,len(Scores)):
    if Winner<Scores[i]:
        Winner= Scores[i]
Loser = Scores[0]
for i in range(0,len(Scores)):
    if Loser>Scores[i]:
        Loser= Scores[i]
print(f"Winner is at {Scores.index(Winner)}")
print(Winner)
print(Loser)