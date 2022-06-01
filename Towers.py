# I like python because it's simple :)
# I am convirting the code from what I see from the Java one
def towersOfHanoi(n, from_rod, to_rod, aux_rod):

    if n == 0:
        return

    towersOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk " + str(n) + " from rod " + from_rod +" to rod " + to_rod)
    towersOfHanoi(n - 1, aux_rod, to_rod, from_rod)


n = 4
towersOfHanoi(n, "A", "C", "B")