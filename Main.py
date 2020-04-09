from Read import read, readTSP
from Modularity import modularity, modularityTSP
from random import randint
from PermutationChromosome import Chromosome


class GA:
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres, net)

    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness > best.fitness):
                best = c
        return best

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__param['popSize'] - 1)
        pos2 = randint(0, self.__param['popSize'] - 1)
        if (self.__population[pos1].fitness < self.__population[pos2].fitness):
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        # generational
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()


net = read('data/50p_easy_01_tsp.txt')
MIN = 1
noDim = net["noNodes"]
# initialise de GA parameters
gaParam = {'popSize': 100, 'noGen': 1000, 'pc': 0.8, 'pm': 0.1}
# problem parameters
problParam = {'min': MIN, 'max': noDim, 'function': modularity, 'noDim': noDim, 'noBits': 8, 'noNodes': net['noNodes']}

# store the best/average solution of each iteration (for a final plot used to anlyse the GA's convergence)
allBestFitnesses = []
allAvgFitnesses = []
generations = []
ga = GA(gaParam, problParam)
ga.initialisation()
ga.evaluation()
maximFitness = 99999999
bestRepres = []
fileName_output = "easy.txt"
f = open(fileName_output, 'w')
for g in range(gaParam['noGen'] + 1):
    bestSolX = ga.bestChromosome().repres
    bestSolY = ga.bestChromosome().fitness
    if bestSolY < maximFitness:
        maximFitness = bestSolY
        bestRepres = bestSolX
    allBestFitnesses.append(bestSolY)
    ga.oneGeneration()

    bestChromo = ga.bestChromosome()
    f.write('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(
        bestChromo.fitness))
    f.write('\n')
f.write("Best repres&fitness: " + str(bestRepres) + " " + str(maximFitness))
f.write('\n')
f.close()
