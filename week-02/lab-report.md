# Lab report — Practice #02: The Prompt Is an Engineering Input

**Name:** Alexandr Vainshtok
**Group:** Monday 16:00-19:00
**Date:** 2026-10-05

> Fill in every section. **Do not delete or renumber the headings** — the grading pass reads them
> by number. If something did not happen, write "did not happen" and why; an empty section and a
> fabricated one are graded the same way.

---

## 1. The frozen experiment

| | |
| --- | --- |
| AI assistant | ChatGPT Codex |
| Exact model name | GPT-5 |
| Implementation language | Python |
| Date of the runs | 2026-10-05 |

**Non-Python students only** — paste your substituted Prompt B text here, so the substitution can
be checked:

```
n/a — used Python
```

**Confirmations:**

- Each prompt was sent in a **fresh chat**: no — same Codex session, but each prompt was treated as a separate isolated output
- No follow-up questions were asked before Part 7: yes
- Every output was saved **before** any editing: yes

---

## 2. Prompt A — minimal

**Prompt sent** (should be exactly one sentence):

```
Write Python code to analyze student marks.
```

**Assumptions the AI made that I never gave it** — list them, one per line. A data format, a pass
threshold, a rounding rule, an input method, an invented feature all count.

1. The AI assumed input could be a comma-separated console string.
2. It assumed invalid marks should be ignored instead of raising errors.
3. It assumed shorter dictionary keys such as `avg`, `high`, and `low` were acceptable.

**Questions it should have asked and did not:**

1. Should invalid inputs be ignored or rejected?
2. What exact function name, signature, and return keys are required?

**Is the function named `analyze_marks` with the required signature?** no — it is called `analyze_student_marks`.

**First impression before testing** (one sentence — you will compare this with section 6 later): It looks usable for a human console demo, but probably fails the harness because the function name and keys are wrong.

---

## 3. Prompt B — structured context

**Prompt sent** (paste it in full, including any substitutions):

```
You are a Python developer. Implement analyze_marks(marks, pass_mark=50). Return
average, highest, lowest, and pass_rate in a dictionary. Accept marks from 0 to 100;
raise ValueError for an empty list, non-numeric values, or out-of-range values. Use
no external libraries. Return code plus a short explanation.
```

**What B fixed compared to A:**

1. It used the required function name `analyze_marks`.
2. It returned the required dictionary keys and raised `ValueError` for invalid input.

**What B still leaves open:**

1. It did not state how many decimals pass_rate should use.
2. It did not include tests, so I could not verify its assumptions from the output alone.

---

## 4. Prompt C — examples and tests

**What I appended to Prompt B:**

```
Example: analyze_marks([40, 60, 80], 50) → average 60, highest 80, lowest 40,
pass_rate 66.67. Include tests for: one mark, decimals, custom pass_mark, empty list,
text value, and marks below 0 or above 100. State any remaining assumptions before
the code.
```

**Tests the AI wrote for itself** — how many, and which situations do they cover?

| Situation | Covered by the AI's tests? |
| --- | --- |
| one mark | yes |
| decimals | yes |
| custom pass_mark | yes |
| empty list | yes |
| text value | yes |
| below 0 / above 100 | yes |

**Do the AI's own tests pass against the AI's own code?** yes

**Do they agree with the harness in section 6?** yes

**Assumptions C stated explicitly before the code:** marks must be a non-empty list of int/float values; marks must be from 0 to 100 inclusive; a mark equal to pass_mark passes; pass_rate is rounded to two decimals.

---

## 5. Prompt D — my combined prompt

**The complete prompt I wrote** (one message, sent to a fresh chat):

```
You are a Python developer. Implement analyze_marks(marks, pass_mark=50).

Return a dictionary with exactly these keys: average, highest, lowest, pass_rate.
Accept only a non-empty list of numeric int or float marks from 0 to 100 inclusive.
Raise ValueError for an empty list, any non-numeric value, or any out-of-range mark.
Use no external libraries.

Passing means mark >= pass_mark, so a mark exactly equal to pass_mark passes.
Calculate pass_rate as passing marks / total marks * 100 and round it to two decimals,
so analyze_marks([40, 60, 80], 50) returns pass_rate 66.67.

Example: analyze_marks([40, 60, 80], 50) should return:
{"average": 60.0, "highest": 80, "lowest": 40, "pass_rate": 66.67}

Also ensure these cases work:
- one mark
- decimal marks
- custom pass_mark
- empty list raises ValueError
- text value raises ValueError
- marks below 0 or above 100 raise ValueError

Return only the Python code.
```

**What I deliberately added that A, B and C did not have:**

1. I explicitly said that equality counts as passing: `mark >= pass_mark`.
2. I resolved the pass_rate ambiguity by asking for rounding to two decimals.
3. I required exact dictionary keys and ValueError behavior for all invalid cases.

**The ambiguity I found in the specification, and how I resolved it inside Prompt D:** The worked example says `66.67`, while plain division gives `66.666666...`. I resolved this by asking D to round pass_rate to two decimals. I also stated that a mark exactly equal to the pass mark counts as passing.

---

## 6. Test results — the evidence

Six cases × four prompts. Verdicts are **PASS**, **FAIL** or **ERROR** only.

| # | Call | Required | A | B | C | D |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `analyze_marks([40, 60, 80], 50)` | avg 60 · high 80 · low 40 · rate 66.67 | ERROR | PASS | PASS | PASS |
| 2 | `analyze_marks([100], 50)` | avg 100 · high 100 · low 100 · rate 100 | ERROR | PASS | PASS | PASS |
| 3 | `analyze_marks([49.5, 50], 50)` | avg 49.75 · high 50 · low 49.5 · rate 50 | ERROR | PASS | PASS | PASS |
| 4 | `analyze_marks([], 50)` | raises ValueError | ERROR | PASS | PASS | PASS |
| 5 | `analyze_marks([40, "60"], 50)` | raises ValueError | ERROR | PASS | PASS | PASS |
| 6 | `analyze_marks([-1, 50, 101], 50)` | raises ValueError | ERROR | PASS | PASS | PASS |
| | **Totals** | | 0/6 | 6/6 | 6/6 | 6/6 |

**For every FAIL and ERROR above, one line: what was returned or raised instead.**

| Prompt | Case | What actually happened |
| --- | --- | --- |
| A | 1-6 | The file defines `analyze_student_marks`, not `analyze_marks`, so the harness could not run any case. |

### Pasted terminal output — all four runs

> This is the part that makes the table above count. Paste the **whole** output, unedited,
> including the header lines. A table with nothing behind it is not accepted.

**Prompt A**

```
ERROR: code/prompt_a.py defines no callable named 'analyze_marks'.
All six cases count as ERROR. Record that in lab-report.md.
```

**Prompt B**

```
========================================================================
analyze_marks harness — code/prompt_b.py
tolerance for numeric comparison: 0.01
========================================================================
SIGNATURE: ok
------------------------------------------------------------------------
case 1  PASS   analyze_marks([40, 60, 80], 50)
          expect: average=60.0, highest=80, lowest=40, pass_rate=66.67
          got   : average=60.0, highest=80, lowest=40, pass_rate=66.66666666666666
------------------------------------------------------------------------
case 2  PASS   analyze_marks([100], 50)
          expect: average=100.0, highest=100, lowest=100, pass_rate=100.0
          got   : average=100.0, highest=100, lowest=100, pass_rate=100.0
------------------------------------------------------------------------
case 3  PASS   analyze_marks([49.5, 50], 50)
          expect: average=49.75, highest=50, lowest=49.5, pass_rate=50.0
          got   : average=49.75, highest=50, lowest=49.5, pass_rate=50.0
------------------------------------------------------------------------
case 4  PASS   analyze_marks([], 50)
          expect: ValueError
          got   : raised ValueError: marks list cannot be empty
------------------------------------------------------------------------
case 5  PASS   analyze_marks([40, '60'], 50)
          expect: ValueError
          got   : raised ValueError: all marks must be numeric
------------------------------------------------------------------------
case 6  PASS   analyze_marks([-1, 50, 101], 50)
          expect: ValueError
          got   : raised ValueError: marks must be between 0 and 100
------------------------------------------------------------------------
RESULT  6 PASS · 0 FAIL · 0 ERROR   (code/prompt_b.py)
========================================================================
```

**Prompt C**

```
========================================================================
analyze_marks harness — code/prompt_c.py
tolerance for numeric comparison: 0.01
========================================================================
SIGNATURE: ok
------------------------------------------------------------------------
case 1  PASS   analyze_marks([40, 60, 80], 50)
          expect: average=60.0, highest=80, lowest=40, pass_rate=66.67
          got   : average=60.0, highest=80, lowest=40, pass_rate=66.67
------------------------------------------------------------------------
case 2  PASS   analyze_marks([100], 50)
          expect: average=100.0, highest=100, lowest=100, pass_rate=100.0
          got   : average=100.0, highest=100, lowest=100, pass_rate=100.0
------------------------------------------------------------------------
case 3  PASS   analyze_marks([49.5, 50], 50)
          expect: average=49.75, highest=50, lowest=49.5, pass_rate=50.0
          got   : average=49.75, highest=50, lowest=49.5, pass_rate=50.0
------------------------------------------------------------------------
case 4  PASS   analyze_marks([], 50)
          expect: ValueError
          got   : raised ValueError: marks cannot be empty
------------------------------------------------------------------------
case 5  PASS   analyze_marks([40, '60'], 50)
          expect: ValueError
          got   : raised ValueError: all marks must be numeric
------------------------------------------------------------------------
case 6  PASS   analyze_marks([-1, 50, 101], 50)
          expect: ValueError
          got   : raised ValueError: marks must be between 0 and 100
------------------------------------------------------------------------
RESULT  6 PASS · 0 FAIL · 0 ERROR   (code/prompt_c.py)
========================================================================
```

**Prompt D**

```
========================================================================
analyze_marks harness — code/prompt_d.py
tolerance for numeric comparison: 0.01
========================================================================
SIGNATURE: ok
------------------------------------------------------------------------
case 1  PASS   analyze_marks([40, 60, 80], 50)
          expect: average=60.0, highest=80, lowest=40, pass_rate=66.67
          got   : average=60.0, highest=80, lowest=40, pass_rate=66.67
------------------------------------------------------------------------
case 2  PASS   analyze_marks([100], 50)
          expect: average=100.0, highest=100, lowest=100, pass_rate=100.0
          got   : average=100.0, highest=100, lowest=100, pass_rate=100.0
------------------------------------------------------------------------
case 3  PASS   analyze_marks([49.5, 50], 50)
          expect: average=49.75, highest=50, lowest=49.5, pass_rate=50.0
          got   : average=49.75, highest=50, lowest=49.5, pass_rate=50.0
------------------------------------------------------------------------
case 4  PASS   analyze_marks([], 50)
          expect: ValueError
          got   : raised ValueError: marks must not be empty
------------------------------------------------------------------------
case 5  PASS   analyze_marks([40, '60'], 50)
          expect: ValueError
          got   : raised ValueError: each mark must be numeric
------------------------------------------------------------------------
case 6  PASS   analyze_marks([-1, 50, 101], 50)
          expect: ValueError
          got   : raised ValueError: marks must be from 0 to 100 inclusive
------------------------------------------------------------------------
RESULT  6 PASS · 0 FAIL · 0 ERROR   (code/prompt_d.py)
========================================================================
```

---

## 7. Scoring

0–2 per criterion, using the rubric in `README.md` Part 7.

| Criterion | A | B | C | D |
| --- | --- | --- | --- | --- |
| Correctness (cases passed) | 0 | 2 | 2 | 2 |
| Requirement coverage | 0 | 2 | 2 | 2 |
| Verifiability (tests) | 0 | 0 | 2 | 0 |
| Assumptions stated | 0 | 0 | 2 | 1 |
| Noise (2 = none) | 1 | 2 | 2 | 2 |
| **Total / 10** | 1 | 6 | 10 | 7 |

**Prompt length, in words:** A 7 · B 52 · C 82 · D 136

**Words added per point gained** — B over A, C over B, D over C. One line on what that ratio says: B added 45 words and gained 5 points, so its extra structure was efficient. C added 30 more words and gained 4 points because tests and assumptions mattered. D added 54 more words but lost 3 points because the generated output did not include tests.

---

## 8. Conclusion — 150–200 words

Answer in this order: (1) which prompt scored best, and whether it is the one you would actually
use at work; (2) which single addition bought the most correctness, naming the exact case that
changed verdict; (3) what was pure noise; (4) the ambiguity and your resolution.

Name test cases and real returned values. "More detailed prompts work better" scores zero.

```
Prompt C scored best with 10/10, and it is the one I would use for this lab because it produced correct code and included runnable tests. In a work setting I would probably start closer to D's wording, but I would explicitly ask for tests too, because D passed the harness but scored lower on verifiability.

The single most valuable addition was the exact function contract in Prompt B: analyze_marks(marks, pass_mark=50) with required keys and ValueError. That changed every case from ERROR in A to PASS in B. For example, Prompt A could not run case 1 at all because it defined analyze_student_marks, while B returned the required dictionary.

The pure noise was not in C's tests, because those were requested and useful. The weaker part was adding more wording in D without requiring tests in the returned code.

The ambiguity was pass_rate formatting: case 1 mathematically gives 66.666..., but the spec shows 66.67. I resolved it in D by asking for two-decimal rounding and also stated that marks equal to the pass mark pass.
```

**Word count:** 173

---

## 9. Two questions for the debrief

Written before class, answered in class.

1. If B already passed all harness cases, how much extra prompt detail is still worth adding?
2. Should prompts always ask for tests in the same file, or is a separate test file cleaner?
