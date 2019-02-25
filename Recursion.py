# Factorial recursion
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


# Computes cumulative sum from 0 to a given integer
def rec_sum(n):
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)


# Return the sum of all individual digits in a given integer
def sum_func(n):
    if len(str(n)) == 1:
        return int(n)
    else:
        return int(str(n)[-1]) + sum_func(str(n)[0: len(str(n))-1])


# Return words in list of words that can be made by splitting phrase
def word_split(phrase, list_of_words, output=None):
    if output == None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

        return output


# Reverse string with recursion
def reverse(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse(s[:len(s)-1])


# Return permutations for a given string and treat each occurence distinct
def permute(s):

    out = []

    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [let+perm]

    return out


# Fibonacci recursion
def fibonacci_recur(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recur(n-1) + fibonacci_recur(n-2)


# Fibonacci iterative
def fibonacci_iter(n):

    a, b = 0, 1

    for i in range(n):
        a, b = b, a+b

    return a


# Memoization
def memoize(fn, arg):
    memo = {}
    if arg not in memo:
        memo[arg] = fn(arg)
        return memo[arg]


# Classic coin change problem with recursion
def coin_recur(target, coins):

    min_coins = target

    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + coin_recur(target-i, coins)

            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


# Classic coin change problem with memoization
def coin_dynam(target, coins, known_results):

    min_coins = target

    if target in coins:
        known_results[target] = 1
        return 1

    elif known_results[target] > 0:
        return known_results[target]

    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + coin_dynam(target-i, coins, known_results)

            if num_coins < min_coins:
                min_coins = num_coins

                known_results[target] = min_coins

    return min_coins
