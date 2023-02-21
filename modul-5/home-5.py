def show_grade(score: int, total_score: int = 100) -> float:
    percent_score = score / total_score

    if percent_score < 0.45:
        return 'niedostateczny'
    elif percent_score < 0.55:
        return 'dopuszczający'
    elif percent_score < 0.80:
        return 'dostateczny'
    elif percent_score < 0.90:
        return 'dobry'
    elif percent_score < 0.95:
        return 'bardzo dobry'
    elif percent_score <= 1.00:
        return 'celujący'


print(show_grade(36))
print(show_grade(56))
print(show_grade(86))
