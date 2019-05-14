# -*- coding: utf-8 -*-

"""
This is a script to scrap Linux Academy question pool and it's answers.

How to use:

1. Click Practice Exam in any course in Linux Academy.
2. Save the HTML of the test result (you can randomly choose answer to get the result quicker)
3. set ``nth_exam``, it gives you only the NEW questions you never seen before.
"""

import bs4
from pathlib_mate import PathCls as Path

question_counts = dict()


class Exam(object):
    def __init__(self, new_questions):
        self.new_questionts = new_questions

    def __len__(self):
        return len(self.new_questionts)


class Question(object):
    def __init__(self, title, body):
        self.title = title
        self.body = body


exam_list = list()
question_title_filter = set()

p_list = list(Path(__file__).parent.select_by_ext(".html"))
p_list.sort()
for p in p_list:
    html = p.read_text(encoding="utf-8")
    soup = bs4.BeautifulSoup(html, "html.parser")

    new_questions = list()

    div_question_item_list = soup.find_all("div", class_="question-item")
    for div in div_question_item_list:
        span = div.find("span", class_="mat-content")
        question_title = span.text
        question_title = question_title.split(" ", 1)[1]
        question_body = div.text
        question_body = question_body.replace("done Correct", "[**Correct Answer**]")

        if question_title not in question_title_filter:
            question = Question(title=question_title, body=question_body)
            question_title_filter.add(question_title)
            new_questions.append(question)

    exam = Exam(new_questions=new_questions)
    exam_list.append(exam)

unique_question_count = len(question_title_filter)

print("Unique Questions: %s" % unique_question_count)
for nth_exam in range(1, len(p_list) + 1):
    print("New Questions in %s th exam: %s" % (nth_exam, len(exam_list[nth_exam - 1])))


def write_new_questions_in_nth_exam_to_file(nth_exam):
    lines = list()
    for question in exam_list[nth_exam - 1].new_questionts:
        lines.append("-" * 80 + "\n" + question.body)
    content = "\n\n".join(lines)
    p = Path(__file__).change(new_basename="new_questions.md")
    p.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    nth_exam = 7
    write_new_questions_in_nth_exam_to_file(nth_exam)
