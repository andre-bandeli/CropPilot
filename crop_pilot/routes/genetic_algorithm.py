from deap import base, creator, tools, algorithms
import math
import numpy as np

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

def calculate_distance(point1, point2):
    """Calcula distância usando a fórmula de Haversine (em quilômetros)"""
    R = 6371.0  # Raio da Terra em km
    lat1 = math.radians(point1['latitude'])
    lon1 = math.radians(point1['longitude'])
    lat2 = math.radians(point2['latitude'])
    lon2 = math.radians(point2['longitude'])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def optimize_route(points, machine_capacity, machine_id):
    depot = next(p for p in points if p['is_depot'])
    other_points = [p for p in points if not p['is_depot']]
    
    for p in other_points:
        if p['estimated_load'] > machine_capacity:
            raise ValueError(f"Talhão {p['name']} excede a capacidade da máquina!")

    toolbox = base.Toolbox()
    num_points = len(other_points)
    toolbox.register("indices", np.random.permutation, num_points)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def eval_vrp(individual):
        total_distance = 0
        current_load = 0
        current_trip = [depot]
        
        for idx in individual:
            point = other_points[idx]
            if current_load + point['estimated_load'] > machine_capacity:
                
                total_distance += calculate_distance(current_trip[-1], depot)
                current_trip = [depot] 
                current_load = 0
            
            total_distance += calculate_distance(current_trip[-1], point)
            current_trip.append(point)
            current_load += point['estimated_load']
        
        total_distance += calculate_distance(current_trip[-1], depot)
        return (total_distance,)

    toolbox.register("evaluate", eval_vrp)
    toolbox.register("mate", tools.cxOrdered)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)

    population = toolbox.population(n=100)
    CXPB, MUTPB, NGEN = 0.7, 0.2, 100

    for _ in range(NGEN):
        offspring = algorithms.varAnd(population, toolbox, CXPB, MUTPB)
        fits = [toolbox.evaluate(ind) for ind in offspring]
        
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit
            
        population = toolbox.select(offspring, k=len(population))

    best_ind = tools.selBest(population, k=1)[0]
    
    optimized_route = []
    current_load = 0
    current_trip = [depot['name']]
    
    for idx in best_ind:
        point = other_points[idx]
        if current_load + point['estimated_load'] > machine_capacity:
            current_trip.append(depot['name'])
            optimized_route.append(current_trip)
            current_trip = [depot['name']] 
            current_load = 0
        
        current_trip.append(point['name'])
        current_load += point['estimated_load']
    
    current_trip.append(depot['name']) 
    optimized_route.append(current_trip)

    return {
        "machine_id": machine_id,
        "optimized_route": optimized_route,
        "total_distance": eval_vrp(best_ind)[0],
        "message": "Rota otimizada com sucesso!"
    }