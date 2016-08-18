def main():
    score = get_score()
    mark = get_mark(score)
    print(mark)


def get_score():
    score = int(input("enter a score: "))
    return score

def get_mark(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score == 100:
        mark = "perfect"
    elif score >= 90:
        mark = "excellent"
    elif score >= 50:
        mark = "passable"
    else:
        mark = "fail"
    return mark
main()
