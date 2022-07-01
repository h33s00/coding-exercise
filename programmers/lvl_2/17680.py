# 캐시


def solution(cacheSize, cities):
    time = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    for item in cities:
        city = item.lower()
        print(city, cache)
        # cache hit
        if city in cache:
            print("cache hit!")
            time += 1
            cache.remove(city)
            cache.append(city)
        # cache miss
        else:
            print("cache miss!")
            time += 5
            if len(cache) < cacheSize:
                cache.append(city)
            elif len(cache) == cacheSize:
                del cache[0]
                cache.append(city)

    return time


# cacheSize = 3
# cities = [
#     "Jeju",
#     "Pangyo",
#     "Seoul",
#     "NewYork",
#     "LA",
#     "Jeju",
#     "Pangyo",
#     "Seoul",
#     "NewYork",
#     "LA",
# ]

# cacheSize = 2
# cities = [
#     "Jeju",
#     "Pangyo",
#     "Seoul",
#     "NewYork",
#     "LA",
#     "SanFrancisco",
#     "Seoul",
#     "Rome",
#     "Paris",
#     "Jeju",
#     "NewYork",
#     "Rome",
# ]

# cacheSize = 5
# cities = [
#     "Jeju",
#     "Pangyo",
#     "Seoul",
#     "NewYork",
#     "LA",
#     "SanFrancisco",
#     "Seoul",
#     "Rome",
#     "Paris",
#     "Jeju",
#     "NewYork",
#     "Rome",
# ]

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

# cacheSize = 0
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))
