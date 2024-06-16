# 8장_유전자 알고리즘

# 유전자 알고리즘
GeneticAlgorithm(population, FitnessFunc)
{
    repeat
        new_population <- []
        for i=1 to size(population) do
            father <- select(population, FitnessFunc)
            mother <- select(population, FitnessFunc)
            child <- crossover(father, mother)
            if (난수 < 변이_확률) then child <- mutate(child)
            new_population <- new_population + childe
        population = new_population
        until 충분히 적합한 개체가 얻어지거나 충분한 반복 횟수가 지나면
        return 가장 적합한 개체
}
