from deap import base, creator, tools, algorithms
import numpy as np

def calculate_distance(point1, point2):
    lat1, lon1 = point1['latitude'], point1['longitude']
    lat2, lon2 = point2['latitude'], point2['longitude']
    return np.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def optimize_route(points):
    num_points = len(points)
    
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    
    toolbox = base.Toolbox()
    toolbox.register("indices", np.random.permutation, num_points)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    
    def eval_route(individual):
        total_distance = 0
        for i in range(len(individual)):
            p1 = points[individual[i]]
            p2 = points[individual[(i+1) % num_points]]
            total_distance += calculate_distance(p1, p2)
        return (total_distance,)
    
    toolbox.register("evaluate", eval_route)
    toolbox.register("mate", tools.cxOrdered)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    
    population = toolbox.population(n=50)
    CXPB, MUTPB, NGEN = 0.7, 0.2, 40
    
    for _ in range(NGEN):
        offspring = algorithms.varAnd(population, toolbox, CXPB, MUTPB)
        fits = toolbox.map(toolbox.evaluate, offspring)
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit
        population = toolbox.select(offspring, k=len(population))
    
    best_ind = tools.selBest(population, k=1)[0]
    return best_ind