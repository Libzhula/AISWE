# Week 01 — Manual vs AI: Comparison

**Name:** Alexandr Vainshtok
**Group:** Monday 16:00-19:00
**Date:** 2026-10-05

---

## 1. Facts

| | Manual (Part 1) | Rocket (Part 2) |
| --- | --- | --- |
| Language / stack used | Python console script | Next.js / TypeScript / Tailwind CSS web app |
| Time to first version that ran | Not separately recorded | |
| Time to all 4 test cases passing | 17 minutes | Not fully passed; case A was not captured and case D behaved differently |
| Number of attempts / prompts needed | 1 manual script, formatting fixed after testing | Initial prompt, clarification answer, and 2 follow-up fix prompts |
| Lines of code you actually wrote | 24 | 0 manually; Rocket generated a multi-file web app |
| Did it handle invalid marks (case B)? | Yes | Partly; invalid values were rejected by UI validation instead of ignored |
| Did it handle an empty list (case D)? | Yes | Partly; no crash, but it showed parse errors rather than a clean no-valid-marks result |
| Did it use the ≥ 50 pass threshold? | Yes | Yes; threshold was visible as 50 |
| Output format matches the spec? | Yes after formatting fix | Partly; it displayed many extra dashboard fields |
| Can you explain every line of it? | Yes | No; it generated a multi-file web app |

## 2. Test results

| Case | Input | Manual output | Rocket output | Spec says | Match? |
| --- | --- | --- | --- | --- | --- |
| A | `85, 23, 45, 90, 92` | valid 5 · avg 67.00 · high 92 · low 23 · pass 60.0% | Not captured in screenshot set | avg 67.00 · high 92 · low 23 · pass 60.0% | Manual yes; Rocket not verified |
| B | `88, 47, -5, 101, abc, 73, 50, , 100` | valid 5 · avg 71.60 · high 100 · low 47 · pass 80.0% | Individual invalid inputs were rejected by validation | avg 71.60 · high 100 · low 47 · pass 80.0% | Manual yes; Rocket partly |
| C | `10, 20, 30` | valid 3 · avg 20.00 · high 30 · low 10 · pass 0.0% | avg 20.00 · high 30.00 · low 10.00 · pass 0.0% | avg 20.00 · high 30 · low 10 · pass 0.0% | Yes |
| D | `abc, , xyz` | No valid marks entered. | parse errors for `abc` and `xyz`, imports 0 marks | clear message, no crash | Partly |

## 3. What the AI added that I never asked for

<!-- Tech stack, UI, extra features, a pass threshold it invented, styling, etc. -->

-
- Next.js, TypeScript and Tailwind CSS stack
- Full web dashboard layout with charts, grade breakdown, pass/fail donut, sortable table and bulk paste
- Student names, median, standard deviation and configurable pass threshold

## 4. What the AI got wrong or silently skipped

<!-- Be concrete: input, expected, actual. -->

-
- It made the solution much larger than the requested small program.
- It originally required student names even though the prompt only asked for marks.
- It rejected invalid marks with UI validation instead of simply ignoring them like the specification said.

## 5. The defect I asked Rocket to fix

**Prompt I used:**

```text
plz make it such i dont have to add names all the time, just marks are fine too
```

```text
bulk paste too plz
```

**Result:** (fixed / partly fixed / broke something else)

Fixed. Rocket made the student name optional, auto-assigned names such as Student 1, and updated the bulk paste modal to accept score-only lines.

**What this tells me:**

The AI was useful for changing the UI quickly after feedback, but the first version still had assumptions that were not in the original task.

---

## 6. Reflection (200–300 words)

Answer all four, in your own words:

1. Which parts of the work did the AI genuinely speed up?
2. Where did the AI cost you time, or give you something that looked right but was not?
3. Which of these two artefacts would you be willing to put your name on, and why?
4. What must a human engineer still be responsible for after this experiment?

<!-- Write your reflection below this line -->
The AI genuinely sped up the visual and interface part. My manual version was only a small Python console script, while Rocket produced a full dashboard with cards, charts, a pass/fail donut, grade breakdown, table, bulk paste and a pass threshold slider. That would take me much longer to build manually. It also reacted quickly when I asked it to stop requiring student names and to support bulk paste.

At the same time, Rocket also cost time because it made the task much bigger than it needed to be. The original problem was just to process marks and print average, highest, lowest and pass rate. Rocket chose Next.js, TypeScript, Tailwind and many components, which looked cool but was harder to verify. It also added features I did not ask for, like median, standard deviation, grade categories and charts. For invalid inputs, the app used validation errors instead of simply ignoring invalid marks like the specification required.

I would be more comfortable putting my name on the manual version, because I can explain every line and I know exactly how it handles the four test cases. The Rocket version is more impressive visually, but I would need more time to inspect the generated code before trusting it fully. A human engineer is still responsible for checking requirements, testing edge cases, noticing wrong assumptions, and deciding whether the generated solution is appropriate for the actual problem.
