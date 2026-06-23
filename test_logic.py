# -*- coding: utf-8 -*-
"""
Тест чистой логики квиза: подсчёт правильных ответов и выбор зверя по доле.

Это зеркало двух функций из index.html (countCorrect, pickBeast).
ВАЖНО: держать в синхроне с index.html — правила здесь и там должны совпадать.
Запуск:  python3 test_logic.py
"""

# Правильные ответы по вопросам (индексы вариантов) — как в index.html (QUIZ.correct)
CORRECT = [0, 1, 1, 1]


def count_correct(answers):
    """Сколько ответов совпало с правильными."""
    return sum(1 for k, a in enumerate(answers) if a == CORRECT[k])


def pick_beast(correct, total):
    """Зверь по доле правильных. Совпадает с границами из 04_КОНТЕНТ.md."""
    if correct == 0:
        return "straus"          # 0%
    share = correct / total
    if share >= 1:
        return "oryol"           # 100%
    if share < 1 / 3:
        return "surikat"         # до 33%
    if share < 2 / 3:
        return "bober"           # 34–66%
    return "lis"                 # 67–99%


import math


def js_round(x):
    # как Math.round в JS: половину округляем вверх (в Python round() иначе)
    return math.floor(x + 0.5)


def audience_percents(counts):
    """Проценты аудитории по вариантам. Зеркало audiencePercents из index.html."""
    total = sum(counts)
    if total == 0:
        return [0] * len(counts)
    return [js_round(c / total * 100) for c in counts]


def passes_threshold(total, min_=5):
    """Показывать ли среднее. Зеркало passesThreshold из index.html."""
    return total >= min_


def run():
    checks = []

    def expect(name, got, want):
        ok = got == want
        checks.append((ok, name, got, want))

    # --- подсчёт правильных: крайние случаи ---
    expect("0 правильных (все мимо)", count_correct([1, 0, 0, 0]), 0)
    expect("все 4 правильных",        count_correct([0, 1, 1, 1]), 4)
    expect("2 правильных",            count_correct([0, 1, 0, 0]), 2)

    # --- зверь по доле для квиза из 4 вопросов ---
    expect("0 из 4 -> Страус",  pick_beast(0, 4), "straus")
    expect("1 из 4 -> Сурикат", pick_beast(1, 4), "surikat")
    expect("2 из 4 -> Бобёр",   pick_beast(2, 4), "bober")
    expect("3 из 4 -> Лис",     pick_beast(3, 4), "lis")
    expect("4 из 4 -> Орёл",    pick_beast(4, 4), "oryol")

    # --- та же логика работает и для другого числа вопросов (например, 6) ---
    expect("0 из 6 -> Страус",  pick_beast(0, 6), "straus")
    expect("1 из 6 -> Сурикат", pick_beast(1, 6), "surikat")
    expect("3 из 6 -> Бобёр",   pick_beast(3, 6), "bober")
    expect("5 из 6 -> Лис",     pick_beast(5, 6), "lis")
    expect("6 из 6 -> Орёл",    pick_beast(6, 6), "oryol")

    # --- проценты аудитории из счётчиков ---
    expect("аудитория: пусто",      audience_percents([0, 0, 0, 0]), [0, 0, 0, 0])
    expect("аудитория: 3/1/0/0",    audience_percents([3, 1, 0, 0]), [75, 25, 0, 0])
    expect("аудитория: поровну",    audience_percents([1, 1, 1, 1]), [25, 25, 25, 25])
    expect("аудитория: 5/3/2/0",    audience_percents([5, 3, 2, 0]), [50, 30, 20, 0])
    expect("аудитория: округление", audience_percents([1, 2, 0, 0]), [33, 67, 0, 0])

    # --- порог показа среднего (от 5 ответов) ---
    expect("порог: 4 -> скрыть",   passes_threshold(4), False)
    expect("порог: 5 -> показать",  passes_threshold(5), True)
    expect("порог: 0 -> скрыть",   passes_threshold(0), False)

    failed = 0
    for ok, name, got, want in checks:
        if ok:
            print(f"  OK  {name}")
        else:
            failed += 1
            print(f"FAIL  {name}: получили {got!r}, ждали {want!r}")

    print("-" * 40)
    if failed == 0:
        print(f"Все тесты прошли: {len(checks)} из {len(checks)} зелёные.")
        return 0
    print(f"Провалено: {failed} из {len(checks)}.")
    return 1


if __name__ == "__main__":
    import sys
    sys.exit(run())
