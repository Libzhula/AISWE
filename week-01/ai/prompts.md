# Rocket prompt log

## Initial prompt

```text
Build a small program that processes a list of student marks and prints:
average, highest, lowest, and pass rate.
```

## Rocket's first reaction and questions

Rocket reported:

```text
Agent detected prompt score : 76%
This is good enough score to proceed. However, a few answers to my questions will help enhance prompt completeness and generate more accurate results.
```

Question shown:

```text
Who will be using this tool -- is it just for you, or will others on your team access it too?
```

## My answers to Rocket

```text
Just me (A single teacher or analyst running it solo)
```

## Rocket's rewritten / enhanced prompt

Rocket reported:

```text
Thank you for your responses. Your final prompt score is 89%.

I have redrafted your prompt as under and will proceed to execute on the same.
```

Rocket Enhanced:

```text
A personal-use internal tool for a single educator to input a list of student marks and instantly compute key statistics -- class average, highest score, lowest score, and overall pass rate -- presented in a clean, readable interface.

Building with Next.js and TypeScript.
```

## What Rocket added by itself

Rocket added a full web application structure using Next.js, TypeScript and Tailwind CSS. It also added UI layout components, a top bar, chart components, a score histogram, a grade breakdown, a pass/fail donut chart, a sortable marks table, a bulk paste modal, a configurable pass threshold, median, standard deviation, student names and inline pass/fail badges.

The original prompt did not ask for a web UI, charts, grading categories, student names, median, standard deviation, sorting, bulk paste, or a multi-file project.

## Preview / published link

No exported source code or public link was added to the repository. Evidence is saved as screenshots in `week-01/ai/screenshots/`.

## Test results

| Case | Input | Rocket output | Matches spec? | Notes |
| --- | --- | --- | --- | --- |
| A | `85, 23, 45, 90, 92` | Not captured in final screenshot set | Not verified | Required output: avg 67.00, high 92, low 23, pass 60.0%. |
| B | `88, 47, -5, 101, abc, 73, 50, , 100` | Not captured as one full case. Individual screenshots show `-1`, `101`, `abc`, and empty score are rejected by validation. | Partly verified | Rocket validates invalid values instead of silently ignoring them like the manual spec requires. |
| C | `10, 20, 30` | average 20.00, highest 30.00, lowest 10.00, pass rate 0.0%, 0/3 passed | Yes | This matches the required statistics, with extra dashboard fields added. |
| D | `abc, , xyz` | Bulk paste reports parse errors for `abc` and `xyz` and imports 0 marks. | Partly | It does not crash, but it shows validation errors instead of the manual program's simple "No valid marks entered" message. |

## Defect-fix prompt

```text
plz make it such i dont have to add names all the time, just marks are fine too
```

Follow-up prompt:

```text
bulk paste too plz
```

## Defect-fix result

Rocket fixed this. It made the student name field optional, auto-assigned names like "Student 1", and updated bulk paste so score-only lines such as `10`, `20`, `30` could be imported.
