if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))  # convert map object to list
    scores = set(list(arr))
    scores.remove(max(scores))
    running_up_score=max(scores)
    print(running_up_score)