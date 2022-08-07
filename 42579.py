# 베스트앨범


def solution(genres, plays):
    answer = []
    max_genre = {}  # {hiphop: [2, 4]}
    sum_genre = {}  # {hiphop: 1400}]

    # values in plays explored once : O(n)
    for i in range(len(plays)):
        if genres[i] not in max_genre.keys() or genres[i] not in sum_genre.keys():
            # Initialize
            max_genre[genres[i]] = [i]
            sum_genre[genres[i]] = plays[i]
        else:
            # Sum Increased,
            sum_genre[genres[i]] += plays[i]
            # Max Checked
            if len(max_genre[genres[i]]) == 1:
                if plays[max_genre[genres[i]][0]] < plays[i]:
                    max_genre[genres[i]].insert(0, i)
                else:
                    max_genre[genres[i]].append(i)
            elif len(max_genre[genres[i]]) == 2:
                max1 = plays[max_genre[genres[i]][0]]
                max2 = plays[max_genre[genres[i]][1]]
                if plays[i] > max1:
                    max_genre[genres[i]].insert(0, i)
                    max_genre[genres[i]].pop()
                elif plays[i] > max2:
                    max_genre[genres[i]][1] = i

    print(max_genre)
    print(sum_genre)

    # genres are explored to sort by sum : O(n)
    sorted_by_genres = sorted(sum_genre.items(), key=lambda item: item[1], reverse=True)
    for each in sorted_by_genres:
        answer.extend(max_genre[each[0]])

    print(sorted_by_genres)
    print(answer)

    return answer


# solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])

# solid example added,
# considering cases where only one song in genre, same play values in one genre...
solution(["hiphop", "rock", "rock", "pop", "pop", "pop"], [3, 2, 8, 9, 9, 10])
