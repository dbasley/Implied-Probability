# Implied Probability Calculator

def implied_probability(first_odds, second_odds):
    first_odds = int(first_odds)
    second_odds = int(second_odds)

    # Account for negative odds
    if first_odds < 0:
        first_probs = abs(first_odds) / (100 + abs(first_odds))

    else:
        first_probs = 100 / (100 + abs(first_odds))

    # Account for negative odds
    if second_odds < 0:
        sec_probs = abs(second_odds) / (100 + abs(second_odds))

    else:
        sec_probs = 100 / (100 + abs(second_odds))


   
    total_probability = first_probs + sec_probs
    first_implied_probability = first_probs / total_probability * 100
    sec_implied_probability = sec_probs / total_probability * 100

    print("No-Vig Implied Probability", "\n", 
          "Odds 1:", round(first_implied_probability, 3), "%", "\n", 
          "Odds 2", round(sec_implied_probability, 3), "%")



first_odds = input("Enter the first odds: ")
second_odds = input("Enter the second odds: ")


implied_probability(first_odds, second_odds)