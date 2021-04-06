from functools import lru_cache
import time

orders = set()

a = int(input())

scenesTodo = list(map(int, input().split()))

start = time.time()


allScenes = len(scenesTodo)

@lru_cache(maxsize=None)
def scenes(scenesLeft, scenesDone):
#    print(scenesLeft, scenesDone)
    if sum(scenesLeft) == 1: return 1
    tot = []
    for actor in range(a):
        if scenesLeft[actor] > 0:
            if actor == 0 or scenesDone[actor-1] > scenesDone[actor]:
                d = list(scenesLeft)
                d[actor] -= 1
                l = list(scenesDone)
                l[actor] += 1
                tot.append(scenes(tuple(d), tuple(l)))
    return sum(tot)


blank = tuple([0 for i in range(a)])
print(scenes(tuple(scenesTodo), blank))
print("Time:", time.time() - start)

"""
b) 6 (2 actors, 2 scenes)
   a,A,b,B
   A,a,b,B
   a,A,B,b
   A,a,B,b
   a,b,A,B
   A,B,a,b
   1680 (3 actors, 3 scenes)
   
c) If the junior actor's scene must be the last scene shot, then each actor must have the same number of scenes, as if 
the junior actor's last scene wasn't the last scene shot, then the hierarchy would be broken. The hierarchy means that
the most junior actor cannot have shot more scenes than any other actor. If the actors have different numbers of scenes,
there must be an actor with more scenes than the most junior actor, and so they may film their last scene after the most
junior actor has shot all of their scenes.

d) If 
   
"""
