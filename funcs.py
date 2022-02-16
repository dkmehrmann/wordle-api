def word_eval(guess, ans):
    if len(guess) != 5:
        raise ValueError('guess is not 5 letters')
    if '_' in guess:
        raise ValueError('special characters not allowed in guess')

    res = []
    for i, letter in enumerate(guess):
        if letter == ans[i]:
            res.append('Y')
            ans = ans.replace(letter, '_', 1)
        elif letter in ans:
            res.append('M')
            ans = ans.replace(letter, '_', 1)
        else:
            res.append('N')
    return res


def commit_guess(guess, ans, game_id, table):
    if len(table[game_id]) >= 5:
        raise ValueError('too many guesses')
    res = word_eval(guess, ans)
    table[game_id].append(res)
    return table
