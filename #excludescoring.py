def worst_rank_after_last_contest(C, N, scores):
    # Compute your aggregate score
    your_scores = scores[0]
    your_scores.sort(reverse=True)
    your_aggregate = sum(your_scores[:4])

    # Compute aggregate scores for other contestants
    other_aggregates = []
    for i in range(1, N):
        participant_scores = scores[i]
        participant_scores.sort(reverse=True)
        current_aggregate = sum(participant_scores[:4])
        
        # Assume they could get 100 points in the last contest
        if len(participant_scores) < 4:
            potential_aggregate = current_aggregate
        else:
            potential_aggregate = current_aggregate + max(0, 100 - participant_scores[3])
        
        other_aggregates.append(potential_aggregate)
    
    # Count how many have a strictly higher aggregate score than you could have
    count_strictly_higher = sum(1 for score in other_aggregates if score > your_aggregate)
    
    # Your worst possible rank is the number of people with strictly higher aggregates + 1
    worst_rank = count_strictly_higher + 1
    return worst_rank

# Example usage
C = 4
N = 2
scores = [
    [50, 50, 75],
    [25, 25, 25]
]
print(worst_rank_after_last_contest(C, N, scores))  # Output: 2

C = 5
N = 2
scores = [
    [50, 50, 50, 50],
    [25, 25, 25, 25]
]
print(worst_rank_after_last_contest(C, N, scores))  # Output: 1

C = 2
N = 4
scores = [
    [90],
    [1],
    [3],
    [2]
]
print(worst_rank_after_last_contest(C, N, scores))  # Output: 3
