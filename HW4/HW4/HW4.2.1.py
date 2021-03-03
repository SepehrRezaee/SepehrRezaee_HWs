scores = {'Art':
              [{'first_name': 'Robert', 'last_name': 'Smith', 'score': 4},
               {'first_name': 'Mary', 'last_name': 'Hernandez', 'score': 3}],
          'Math':
              [{'first_name': 'Robert', 'last_name': 'Smith', 'score': 1},
               {'first_name': 'Maria', 'last_name': 'Garcia', 'score': 2},
               {'first_name': 'Mary', 'last_name': 'Hernandez', 'score': 3}],
          'Literature':
              [{'first_name': 'Robert', 'last_name': 'Smith', 'score': 3},
               {'first_name': 'Maria', 'last_name': 'Garcia', 'score': 4},
               {'first_name': 'Mary', 'last_name': 'Hernandez', 'score': 1},
               {'first_name': 'James', 'last_name': 'Johnson', 'score': 2}],
          'Physics':
              [{'first_name': 'Robert', 'last_name': 'Smith', 'score': 4}],
          'Chemistry':
              [{'first_name': 'Robert', 'last_name': 'Smith', 'score': 2},
               {'first_name': 'James', 'last_name': 'Johnson', 'score': 3}]}


def whole_scores_of_each_student(par, f_Name):
    a = []
    checkers = ""
    for i in par:
        for j in range(len(par[i])):
            checkers = par[i][j]['first_name'] + " " + par[i][j]['last_name']
            if checkers == f_Name:
                a += [par[i][j]['score']]
            else:
                continue
    return a


def set_of_full_names(par):
    b = []
    for char in par:
        for i in range(len(par[char])):
            b += [par[char][i]['first_name'] + " " + par[char][i]['last_name']]
        else:
            continue
    return set(b)


def whole_scores_of_each_lessons(lesson):
    return [scores[lesson][n]['score'] for n in range(len(scores[lesson]))]


# In part A, we extract the scores of each lessons
scores_of_lessons = {}
for i in range(len(scores)):
    scores_of_lessons[list(scores.keys())[i]] = whole_scores_of_each_lessons(list(scores.keys())[i])
print("part A: ", scores_of_lessons)

# In part B, we extract the scores of each people and match them together
scores_of_lessons = {}
for i in range(len(set_of_full_names(scores))):
    scores_of_lessons[list(set_of_full_names(scores))[i]] = whole_scores_of_each_student(scores, list(
        set_of_full_names(scores))[i])
print("part B: ", scores_of_lessons)

# In part C, we match the scores of each people with the lessons and store
name_lessons_score = {}
for i in range(len(scores_of_lessons)):
    checker = ""
    lessons_list = []
    for lessons in scores:
        for j in range(len(scores[lessons])):
            checker = scores[lessons][j]['first_name'] + " " + scores[lessons][j]['last_name']
            if checker == list(set_of_full_names(scores))[i]:
                lessons_list += [lessons]
            name_lessons_score[list(set_of_full_names(scores))[i]] = dict(
                zip(lessons_list, scores_of_lessons[list(set_of_full_names(scores))[i]]))
        else:
            continue
print("part C: ", name_lessons_score)
