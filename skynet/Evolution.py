from random import *

from skynet.DinoBot import DinoBot


def calculate_relative_fitnesses(pop_list):
    # TODO more dramatic fitness function?
    total = 0
    for bot in pop_list:
        total += bot.score

    for bot in pop_list:
        bot.fitness = bot.score / total

    return pop_list


def pick_one_member(pop_list):
    # TODO can use random.choices with weights instead?
    index = 0
    rand = random()

    while (rand > 0):
        rand = rand - pop_list[index].fitness
        index += 1

    index -= 1
    return pop_list[index]


def get_next_generation(dead_generation, mutation_rate, screen):
    dead_generation = calculate_relative_fitnesses(dead_generation)
    new_generation = []
    for i in range(len(dead_generation)):
        dead_member = pick_one_member(dead_generation)
        member_mutation_rate = mutation_rate * (1 - dead_member.fitness)
        mutated_member_brain = dead_member.net.copy().mutate(member_mutation_rate)
        new_generation.append(DinoBot(screen, brain=mutated_member_brain))
    return new_generation
