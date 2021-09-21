import copy
import math
import random
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import sys


purpose = sys.argv[3]  # Maximize or Minimize


def fitness_function(var):
    x = var[0]**2 + var[1]**3 + var[2]**4
    return x


variables_ranges = [
    {"min": -10, "max": 10},
    {"min": -10, "max": 10},
    {"min": -10, "max": 10}
]

variables_lengths = np.array([5, 5, 5])  # ([4,2])
# Max length 31. max_unsigned_number_with_n_bits()
twos_complement_bool = True  # False or True
map_bool = False

population_size = int(sys.argv[1])
breed_percentage = 50
mutation_probability = 10  # If it is big, dom't function properly
mutation_range = "All"  # All, Left or Right
maximum_generation = int(sys.argv[2])

print_trace_bool = False
write_trace_bool = True
random_crossover_point_bool = False

# Secondary variables
chromosome_length = np.sum(variables_lengths)
crossover_point = math.ceil((breed_percentage/100)*chromosome_length)
mutation_rate = mutation_probability/100
epoch = 0

if(len(variables_lengths) == len(variables_ranges)):
    variables_number = len(variables_lengths)
    if variables_number == 0:
        raise Exception('Cannot have 0 variables')
else:
    raise Exception('Variable ranges and lengths are different')

if twos_complement_bool and map_bool:
    raise Exception("Cannot have two's complement and mat a t the same time")

twins_in_first_generation = True  # Most charge in memory if is False

best_score = 0
if purpose == "Minimize":
    best_score = float("inf")
elif purpose == "Maximize":
    best_score = float("-inf")

best_individual = 0
best_score_progress = []
mean_score_progress = []
mean_int_population_progress = []

# Auxiliary functions


def print_population(population):
    end = ""
    print("[")
    for i in range(len(population)):
        print("[", end=end)
        print(population[i][0], end=end)
        for j in range(1, len(population[i])):
            print(", ", population[i][j], end=end)
        print("]")
    print("]")


def print_trace(population, scores, mutations, breed):
    global epoch

    for i in breed:
        print(i)

    for i in mutations:
        print(i)
    print()

    print("Epoch: ", epoch)

    print("Population: ", end="")
    print_population(population)

    print("Int population: ")
    int_population = get_int_population(population)
    if map_bool:
        int_population = map_all_population(int_population)
    print(int_population)

    print("Scores:\n", scores)


file = None


def write_population(population):
    file.write("[\n")
    for i in range(len(population)):
        file.write("[")
        file.write(str(population[i][0]))
        for j in range(1, len(population[i])):
            file.write(", "+str(population[i][j]))
        file.write("]\n")
    file.write("]\n")


def write_trace(population, scores, mutations, breed, file):
    global epoch

    for i in breed:
        file.write(i+"\n")

    for i in mutations:
        file.write(i+"\n")
    file.write("\n")

    file.write("Epoch: "+str(epoch)+"\n")

    file.write("Population: \n")
    write_population(population)

    file.write("Int population: \n")
    int_population = get_int_population(population)
    if map_bool:
        int_population = map_all_population(int_population)
    file.write(str(int_population)+"\n")

    file.write("Scores:\n" + str(scores)+"\n")


def add_plot_data(population, scores):
    global best_score_progress, mean_int_population_progress, mean_score_progress, best_score, best_individual

    mean_score = np.mean(scores)
    mean_score_progress.append(mean_score)

    int_population = get_int_population(population)
    int_population_mapped = []
    if map_bool:
        int_population_mapped = map_all_population(int_population)
    mean_int_population = np.mean(int_population)
    mean_int_population_progress.append(mean_int_population)

    np_scores = np.array(scores)
    if purpose == "Minimize":
        maximum = np.ndarray.min(np.array(scores))
        if maximum < best_score:
            best_score = maximum
            if map_bool:
                best_individual = int_population_mapped[np.argmin(
                    np.array(scores))]
            else:
                best_individual = int_population[np.argmin(np.array(scores))]
        best_score_progress.append(maximum)
    elif purpose == "Maximize":
        maximum = np.ndarray.max(np.array(scores))
        if maximum > best_score:
            best_score = maximum
            if map_bool:
                best_individual = int_population_mapped[np.argmax(
                    np.array(scores))]
            else:
                best_individual = int_population[np.argmax(np.array(scores))]

        best_score_progress.append(maximum)


def individual_to_string(individual):
    string = ""
    for i in range(len(individual)):
        string = string+str(individual[i])
    return string

# Binary auxiliar functions


def int_to_binary_array_ts(var, bits_number, variable_index):
    if map_bool:
        var = round(map(var, variables_ranges[variable_index]["min"], variables_ranges[variable_index]["max"], 0, max_unsigned_number_with_n_bits(
            variables_lengths[variable_index])))
    array = np.array([var])
    binary = (
        ((array[:, None] & (1 << np.arange(bits_number)))) > 0).astype(float)

    binary[0] = binary[0][:: -1]

    return (binary[0])


def twos_complement(binary_string):
    value = int(binary_string, 2)
    bits = len(binary_string)

    if (value & (1 << (bits - 1))) != 0:
        value = value - (1 << bits)
    return value


def binary_array_to_int_ts(individual):
    string = ''

    for i in range(0, individual.size):
        string = string+str(int(individual[i]))

    return twos_complement(string)


def binary_array_to_int(individual):  # Has to be a numpy array
    string = ''

    for i in range(0, individual.size):
        string = string+str(int(individual[i]))

    return int(string, 2)


def get_int_population(population):
    global population_size, variables_number, twos_complement_bool
    ints = []

    for i in range(population_size):
        ints.append([])
        for j in range(variables_number):
            if twos_complement_bool:
                ints[i].append(binary_array_to_int_ts(population[i][j]))
            else:
                ints[i].append(binary_array_to_int(population[i][j]))
    return ints


def get_int_individual(individual):
    global population_size, variables_number, twos_complement_bool
    int_individual = []

    for j in range(variables_number):
        if twos_complement_bool:
            int_individual.append(binary_array_to_int_ts(individual[j]))
        else:
            int_individual.append(binary_array_to_int(individual[j]))
    return int_individual


def max_unsigned_number_with_n_bits(bits_number):
    return pow(2, bits_number) - 1


def individual_have_twins(population, individual):
    for i in range(len(population)):
        if np.array_equal(individual, population[i]):
            return True
    return False


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def map_all_population(int_population):
    mapped_int_population = []
    for i in range(len(int_population)):
        mapped_int_population.append([])
        for j in range(len(int_population[i])):
            mapped_int_population[i].append(map(int_population[i][j], 0, max_unsigned_number_with_n_bits(
                variables_lengths[j]), variables_ranges[j]["min"], variables_ranges[j]["max"]))
    return mapped_int_population


def is_in_range(individual, variable_index):
    global variables_ranges, twos_complement_bool

    if twos_complement_bool:
        integer = binary_array_to_int_ts(individual)
        if map_bool:
            integer = map(integer, 0, max_unsigned_number_with_n_bits(
                variables_lengths[variable_index]), variables_ranges[variable_index]["min"], variables_ranges[variable_index]["max"])
    else:
        integer = binary_array_to_int(individual)
        if map_bool:
            integer = map(integer, 0, max_unsigned_number_with_n_bits(
                variables_lengths[variable_index]), variables_ranges[variable_index]["min"], variables_ranges[variable_index]["max"])

    if integer < variables_ranges[variable_index]["min"] or integer > variables_ranges[variable_index]["max"]:
        return False
    else:
        return True


def variables_are_in_range(individual):
    are_variables_in_range = True
    for i in range(len(individual)):
        if not is_in_range(individual[i], i):
            are_variables_in_range = False
    return are_variables_in_range


def put_in_range(individual, variable_index):
    global variables_ranges, variables_lengths, twos_complement_bool

    if twos_complement_bool:
        integer = binary_array_to_int_ts(individual)
        if map_bool:
            integer = map(integer, 0, max_unsigned_number_with_n_bits(
                variables_lengths[variable_index]), variables_ranges[variable_index]["min"], variables_ranges[variable_index]["max"])
    else:
        integer = binary_array_to_int(individual)
        if map_bool:
            integer = map(integer, 0, max_unsigned_number_with_n_bits(
                variables_lengths[variable_index]), variables_ranges[variable_index]["min"], variables_ranges[variable_index]["max"])

    if integer < variables_ranges[variable_index]["min"]:
        return int_to_binary_array_ts(variables_ranges[variable_index]["min"], variables_lengths[variable_index], variable_index)
    elif integer > variables_ranges[variable_index]["max"]:
        return int_to_binary_array_ts(variables_ranges[variable_index]["max"], variables_lengths[variable_index], variable_index)


def separate_variables(individual):
    global variables_lengths
    variables = []
    j = 0
    for i in range(len(variables_lengths)):
        variables.append(individual[j: j+variables_lengths[i]])
        j = j+variables_lengths[i]
    return variables


def concatenate_variables(population):
    bits_population = []

    for i in range(len(population)):
        bits_population.append(np.concatenate(population[i]))
    return bits_population


# Genetic algorithm functions
def create_starting_population(individuals,  variables_lengths):
    population = []
    for i in range(individuals):
        individual = []
        for j in range(len(variables_lengths)):
            if map_bool:
                number = (np.random.random() *
                          ((variables_ranges[j]["max"])-variables_ranges[j]["min"]))+variables_ranges[j]["min"]

                number = round(map(
                    number, variables_ranges[j]["min"], variables_ranges[j]["max"], 0, variables_lengths[j]))

            else:
                number = int(
                    (np.random.random()*((variables_ranges[j]["max"]+1)-variables_ranges[j]["min"]))+variables_ranges[j]["min"])

            individual.append(int_to_binary_array_ts(
                number, variables_lengths[j], j))
        population.append(individual)

    return population


def calculate_fitness(population):
    int_population = get_int_population(population)
    int_population_mapped = []
    if map_bool:
        int_population_mapped = map_all_population(int_population)
    fitness_scores = []

    for i in range(len(int_population)):
        if map_bool:
            fitness_scores.append(fitness_function(int_population_mapped[i]))
        else:
            fitness_scores.append(fitness_function(int_population[i]))

    return fitness_scores


def select_parents(population, scores, parents_number):
    global purpose
    population_copy = copy.copy(population)
    scores_copy = copy.copy(scores)
    parents = []

    individuals = [*range(parents_number)]

    for i in range(math.ceil(parents_number/2)):
        figther1_index = random.randrange(0, len(individuals))
        del individuals[figther1_index]

        figther2_index = random.randrange(0, len(individuals))
        del individuals[figther2_index]

        if(purpose == "Maximize"):
            if(scores_copy[figther1_index] > scores_copy[figther2_index]):
                parents.append(population_copy[figther1_index])
            else:
                parents.append(population_copy[figther2_index])
        elif(purpose == "Minimize"):
            if(scores_copy[figther1_index] < scores_copy[figther2_index]):
                parents.append(population_copy[figther1_index])
            else:
                parents.append(population_copy[figther2_index])

    return parents


def breed_two_parents(parent_1, parent_2, childs, breed_reg):
    global crossover_point
    if random_crossover_point_bool:
        crossover_point = int(np.random.random()*(chromosome_length-1))+1
    x1 = parent_1[0: crossover_point]
    x2 = parent_1[crossover_point:]
    x3 = parent_1[0: (parent_1.size)-crossover_point]
    x4 = parent_1[(parent_1.size)-crossover_point:]

    y1 = parent_2[0: crossover_point]
    y2 = parent_2[crossover_point:]
    y3 = parent_2[0: (parent_1.size)-crossover_point]
    y4 = parent_2[(parent_1.size)-crossover_point:]

    combinations = [
        (x1, y2),
        (y1, x2),
        (x2, y1),
        (y2, x1)
    ]
    if print_trace_bool or write_trace_bool:
        breed_reg.append("Parent 1: "+str(parent_1))
        breed_reg.append("Parent 2: "+str(parent_2))

    for i in range(len(combinations)):
        individual = separate_variables(np.concatenate(combinations[i]))

        if np.array_equal(np.concatenate(combinations[i]), parent_1) or np.array_equal(np.concatenate(combinations[i]), parent_2):
            if print_trace_bool or write_trace_bool:
                breed_reg.append(
                    "Child: " + individual_to_string(individual) + ": No, es igual a padre")
            continue

        if not variables_are_in_range(individual):
            if print_trace_bool or write_trace_bool:
                breed_reg.append(
                    "Child: " + individual_to_string(individual)+": No, la variable sale de los rangos")
            continue

        # if purpose == "Maximize":
        #     if fitness_function(get_int_individual(individual)) < fitness_function(get_int_individual(separate_variables(parent_1))) or fitness_function(get_int_individual(individual)) < fitness_function(get_int_individual(separate_variables(parent_2))):
        #         if print_trace_bool or write_trace_bool:
        #             breed_reg.append(
        #                 "Child: " + individual_to_string(individual)+": No, el hijo no maximiza a los padres")
        #             continue
        # elif purpose == "Minimize":
        #     # print(individual)
        #     # print(get_int_individual(individual))
        #     # print(fitness_function(get_int_individual(individual)))
        #     if fitness_function(get_int_individual(individual)) > fitness_function(get_int_individual(separate_variables(parent_1))) or fitness_function(get_int_individual(individual)) > fitness_function(get_int_individual(separate_variables(parent_2))):
        #         if print_trace_bool or write_trace_bool:
        #             breed_reg.append(
        #                 "Child: " + individual_to_string(individual)+": No, el hijo no minimiza a los padres")
        #             continue
        #     pass

        if (len(childs) != population_size):
            if print_trace_bool or write_trace_bool:
                breed_reg.append(
                    "Child: " + individual_to_string(individual)+": Ok")
            childs.append(individual)
        else:
            break


def breed(parents):
    global population_size, variables_lengths
    childs = []

    breed_reg = []

    for i in range(1, len(parents)):
        for j in range(i):
            if len(childs) != population_size:
                breed_two_parents(parents[j], parents[i], childs, breed_reg)
            else:
                break

    for i in range(len(parents)):
        if len(childs) != population_size:
            breed_two_parents(parents[i], parents[i], childs, breed_reg)
        else:
            break

    if len(childs) != population_size:
        if print_trace_bool or write_trace_bool:
            breed_reg.append("There was not sufficient childs")
        while len(childs) != population_size:
            individual = []
            for j in range(len(variables_lengths)):
                if map_bool:
                    number = (np.random.random() *
                              ((variables_ranges[j]["max"])-variables_ranges[j]["min"]))+variables_ranges[j]["min"]

                    number = round(map(
                        number, variables_ranges[j]["min"], variables_ranges[j]["max"], 0, variables_lengths[j]))
                else:
                    number = int(
                        (np.random.random()*((variables_ranges[j]["max"]+1)-variables_ranges[j]["min"]))+variables_ranges[j]["min"])
                individual.append(int_to_binary_array_ts(
                    number, variables_lengths[j], j))

            childs.append(individual)

            if print_trace_bool or write_trace_bool:
                breed_reg.append("Child Random: " +
                                 individual_to_string(individual))

    return childs, breed_reg


def mutate_population(population, mutation_probability):
    global population_size, variables_number, variables_lengths, twos_complement_bool, mutation_range

    mutations = []

    for i in range(population_size):

        if mutation_range == "All":
            for j in range(len(variables_lengths)):
                for k in range(variables_lengths[j]):

                    if np.random.random() <= mutation_probability:
                        mutations.append(
                            "Mutated [" + str(i) + "][" + str(j) + "][" + str(k) + "]")
                        population[i][j][k] = np.logical_not(
                            int(population[i][j][k]))
                        if not is_in_range(population[i][j], j):
                            if print_trace_bool or write_trace_bool:
                                if(twos_complement_bool):
                                    mutations.append(str(binary_array_to_int_ts(
                                        population[i][j])) + " to "+str(binary_array_to_int_ts(put_in_range(population[i][j], j))))
                                else:
                                    mutations.append(str(binary_array_to_int(
                                        population[i][j])) + " to "+str(binary_array_to_int(put_in_range(population[i][j], j))))
                            population[i][j] = put_in_range(
                                population[i][j], j)

        elif mutation_range == "Left":
            j = 0
            k = 0

            if np.random.random() <= mutation_probability:
                mutations.append(
                    "Mutated [" + str(i) + "][" + str(j) + "][" + str(k) + "]")
                population[i][j][k] = np.logical_not(
                    int(population[i][j][k]))
                if not is_in_range(population[i][j], j):
                    if print_trace_bool or write_trace_bool:
                        if(twos_complement_bool):
                            mutations.append(str(binary_array_to_int_ts(
                                population[i][j])) + " to "+str(binary_array_to_int_ts(put_in_range(population[i][j], j))))
                        else:
                            mutations.append(str(binary_array_to_int(
                                population[i][j])) + " to "+str(binary_array_to_int(put_in_range(population[i][j], j))))
                    population[i][j] = put_in_range(population[i][j], j)

        elif mutation_range == "Right":
            j = variables_number-1
            k = variables_lengths[j]-1

            if np.random.random() <= mutation_probability:
                mutations.append(
                    "Mutated [" + str(i) + "][" + str(j) + "][" + str(k) + "]")
                population[i][j][k] = np.logical_not(
                    int(population[i][j][k]))
                if not is_in_range(population[i][j], j):
                    if print_trace_bool or write_trace_bool:
                        if(twos_complement_bool):
                            mutations.append(str(binary_array_to_int_ts(
                                population[i][j])) + " to "+str(binary_array_to_int_ts(put_in_range(population[i][j], j))))
                        else:
                            mutations.append(str(binary_array_to_int(
                                population[i][j])) + " to "+str(binary_array_to_int(put_in_range(population[i][j], j))))
                    population[i][j] = put_in_range(population[i][j], j)

        else:
            raise(Exception("Mutation range are invalid"))

    return population, mutations


def create_file():
    now = datetime.now()
    name = ".\\src\\logic\\output"
    f = open(name+".txt", "w")
    return f


def write_starting_data(file):
    file.write("Purpose: "+str(purpose)+"\n\n")

    file.write("Population size: "+str(population_size)+"\n\n")

    file.write("Breed percentage: "+str(breed_percentage)+"\n")
    file.write("Crossover point: "+str(crossover_point)+"\n\n")

    file.write("Mutation probability: "+str(mutation_probability)+"\n")
    file.write("Mutation rate: "+str(mutation_rate)+"\n")
    file.write("Mutation range: "+str(mutation_range)+"\n\n")

    file.write("Maximum generation: "+str(maximum_generation)+"\n\n")

    file.write("Number of variables: "+str(variables_number)+"\n")
    file.write("Chromosome length: "+str(chromosome_length)+"\n")
    for i in range(variables_number):
        file.write("Variable "+str(i)+":\n")
        file.write("\tMin: "+str(variables_ranges[i]["min"])+"\n")
        file.write("\tMax: "+str(variables_ranges[i]["max"])+"\n")
        file.write("\tLength: "+str(variables_lengths[i])+"\n")

    file.write("\n")


if __name__ == "__main__":
    mutations = []
    breed_reg = []

    population = create_starting_population(population_size, variables_lengths)

    if write_trace_bool:
        file = create_file()
        write_starting_data(file)

    for i in range(maximum_generation):
        scores = calculate_fitness(population)

        add_plot_data(population, scores)

        if write_trace_bool:
            write_trace(population, scores, mutations, breed_reg, file)

        if print_trace_bool:
            print_trace(population, scores, mutations, breed_reg)

        epoch = epoch+1

        parents = select_parents(concatenate_variables(
            population), scores, population_size)
        childs, breed_reg = breed(parents)
        population = childs
        # population, mutations = mutate_population(population, mutation_rate)

    print("Best score: ", best_score)
    print("Best individual: ", best_individual)

    figure, ax = plt.subplots(nrows=2, ncols=1)

    ax[0].plot(mean_score_progress)  # row=0, col=0
    ax[0].set_title("Mean score")
    ax[0].set_xlabel('Generation')
    ax[0].set_ylabel('Mean score')

    ax[1].plot(best_score_progress, 'g')  # row=1, col=0
    ax[1].set_title("Best score")
    ax[1].set_xlabel('Generation')
    ax[1].set_ylabel('Best score')

    figure.tight_layout(pad=1.5)

    if write_trace_bool:
        file.write("\n")
        file.write("Best score: " + str(best_score)+"\n")
        file.write("Best individual: " + str(best_individual))
        file.close()

    plt.show()
