# Lab report — Practice #03, Requirements Engineering with AI

Name: Alexandr Vainshtok
Student ID: 24B070505
GitHub username: Libzhula

---

## 1. Setup

| | |
| --- | --- |
| AI assistant (tool) | ChatGPT Codex |
| Exact model name and version | GPT-5 |
| Date of the session | 2026-10-05 |
| Diagram renderer used | PlantUML source checked only; no rendered image committed |

One tool and one model were used for all three prompts.

---

## 2. Original AI output — user stories (Part 1)

```
1. As a Student, I want to view available study rooms and time slots, so that I can choose a suitable place to study.
   Priority: High
   Assumption: Availability data is current enough for booking decisions.

2. As a Student, I want to book a study room for a future time, so that I can reserve space for individual or group study.
   Priority: High
   Assumption: The selected room is not blocked and has no overlapping booking.

3. As a Student, I want to cancel a booking I made, so that the room can be used by someone else.
   Priority: High
   Assumption: Students can only cancel their own bookings.

4. As an Administrator, I want to block or unblock a room, so that unavailable rooms are not booked.
   Priority: High
   Assumption: Blocked rooms are excluded from new bookings.

5. As an Administrator, I want to review room usage over a time period, so that library staff can understand demand.
   Priority: Medium
   Assumption: Usage is calculated from booking records.

6. As a Student, I want to receive a confirmation after booking, so that I know the reservation succeeded.
   Priority: Medium
   Assumption: Confirmation is sent only after the booking is accepted.

7. As a Student, I want to receive a confirmation after cancellation, so that I know the room was released.
   Priority: Medium
   Assumption: Confirmation is sent only after a valid cancellation.
```

---

## 3. Story review (Part 2)

| Story (as generated) | What I did | Why | Final ID |
| --- | --- | --- | --- |
| View available study rooms and time slots | Reworded slightly | Made the goal say "availability" like UC-01 and kept it testable. | US-01 |
| Book a study room for a future time | Kept and clarified | Added room, start time, end time, and campus identity as expected booking inputs. | US-02 |
| Cancel a booking I made | Kept | It names the real stakeholder and matches UC-03 directly. | US-03 |
| Block or unblock a room | Kept and clarified | Added assumption that existing bookings are not automatically deleted. | US-04 |
| Review room usage | Kept | It matches UC-05 and stays inside the scenario. | US-05 |
| Receive confirmation after booking | Kept | It covers part of UC-06 without inventing SMS or reminders. | US-06 |
| Receive confirmation after cancellation | Kept | It covers the cancellation side of UC-06. | US-07 |

**Did the assistant invent anything outside the scenario?** No. I checked against the out-of-scope list: there are no payments, fines, check-ins, QR codes, maintenance requests, reminders, account registration, queues, UI details, databases, or servers.

**How many stories did you end with, and why that number?** I kept seven stories. Six functions are fixed, and UC-06 naturally splits into booking confirmation and cancellation confirmation.

---

## 4. Original AI output — acceptance criteria (Part 3)

```
Assumptions:
- Touching bookings are allowed: a booking ending at 14:00 and another starting at 14:00 do not overlap.
- Exactly two hours is allowed because the rule says at most two hours.

US-02 Book room
AC: Given a student chooses a free room, when they book a future slot within two hours, then the booking is created.
AC: Given the requested start is in the past, when the student submits the booking, then the system rejects it.
AC: Given the booking is longer than two hours, when submitted, then the system rejects it.
AC: Given another booking overlaps the room, when submitted, then the system rejects it.
AC: Given the room is blocked, when submitted, then the system rejects it.

US-03 Cancel booking
AC: Given a student has a booking, when they cancel it, then the system releases the room.
AC: Given a student tries to cancel another student's booking, when requested, then the system rejects it.
AC: Given a booking has been cancelled, when availability is viewed, then the slot is free.

US-04 Block or unblock room
AC: Given an administrator blocks an active room, when the change is saved, then new bookings are prevented.
AC: Given a blocked room, when a student books it, then the system rejects it.
AC: Given an administrator unblocks a room, when the change is saved, then valid future bookings are allowed.
```

---

## 5. Criteria review (Part 3)

| Criterion (as generated) | Problem | What I changed it to | Final ID |
| --- | --- | --- | --- |
| "free room" booking success | Too vague about overlap and blocked state | Added unblocked room and no overlapping booking as the Given condition. | AC-01 |
| Past start rejection | Good but did not name R1 | Added explicit R1 reference. | AC-02 |
| Longer than two hours rejection | Good but did not name R2 | Added explicit R2 reference. | AC-03 |
| Overlap rejection | Needed concrete boundary example | Used 14:00-15:00 and 14:30-15:30. | AC-04 |
| Blocked room rejection | Good, kept and tied to R4 | Reworded to match blocked-room rule. | AC-05 |
| Cancel own booking | Good | Kept as observable release of the slot. | AC-06 |
| Cancel another student's booking | Good invalid case | Kept because it protects ownership of cancellation. | AC-07 |
| Availability after cancellation | Good trace to UC-01/UC-03 | Kept as visible consequence. | AC-08 |
| Block active room | Good | Reworded to say unavailable for new bookings. | AC-09 |
| Student books blocked room | Good invalid case | Kept and tied to R4. | AC-10 |
| Unblock room | Good | Kept as future valid booking requests allowed. | AC-11 |

**The two open questions.**

| Question | My decision | Why |
| --- | --- | --- |
| A booking ending exactly when another begins — overlap under R3? | allowed | The two bookings do not occupy the room at the same time. |
| Is exactly two hours allowed under R2? | allowed | "At most two hours" includes exactly two hours. |

**Which invalid or boundary case did the assistant leave out?** It did not first give a concrete overlap example, so I added AC-04 with exact times.

---

## 6. Original AI output — use-case diagram (Part 4)

```
@startuml
actor Student
actor Administrator

rectangle "Smart Campus study room booking" {
  usecase "View availability" as UC01
  usecase "Book room" as UC02
  usecase "Cancel booking" as UC03
  usecase "Block or unblock room" as UC04
  usecase "Review usage" as UC05
  usecase "Send confirmation" as UC06
}

Student --> UC01
Student --> UC02
Student --> UC03
Student --> UC06
Administrator --> UC04
Administrator --> UC05
UC02 ..> UC06 : <<include>>
UC03 ..> UC06 : <<include>>
@enduml
```

Rendered diagram (image, or a link): PlantUML source is in `requirements/use-cases.puml`; no rendered image was committed.

---

## 7. Diagram review (Part 4)

| Element | Problem | What I changed |
| --- | --- | --- |
| Student --> Send confirmation | A person does not directly trigger confirmation; the system sends it after booking or cancellation. | Removed the direct actor association and kept include links from Book room and Cancel booking. |
| Diagram direction | Original was readable but less controlled | Added `left to right direction`. |
| Associations | Needed only justified actor associations | Kept Student with UC-01/02/03 and Administrator with UC-04/05. |

**Associations.** The generated direct link from Student to UC-06 Send confirmation was not actually triggered by the student. It is a system response to UC-02 and UC-03.

**Did any screen, database or internal component appear as a use case or an actor?** No.

---

## 8. Traceability (Part 5)

Summarise what the table in `requirements/traceability.md` shows:

- Use cases with **no story** behind them: none
- Stories with **no use case** they belong to: none
- Criteria that test **no rule** from section 1: AC-06, AC-07, AC-08, AC-09, AC-11 support use-case behavior but do not directly test R1-R4.

**What does the largest gap tell you about the generated requirements?** The biggest gap is that only three stories received acceptance criteria. Confirmation and usage review are covered by stories, but they still need criteria before implementation.

---

## 9. Checker runs

```
$ python tests/check_requirements.py
PASS   US-1  user-stories.md         no placeholders left
PASS   US-2  user-stories.md         7 stories, IDs US-01…US-07
PASS   US-3  user-stories.md         every story has the required sentence shape
PASS   US-4  user-stories.md         every story has a priority
PASS   US-5  user-stories.md         every story declares an assumption
PASS   US-6  user-stories.md         only Student and Administrator appear as roles
PASS   US-7  user-stories.md         nothing from the out-of-scope list appears
PASS   AC-1  acceptance-criteria.md  no placeholders left
PASS   AC-2  acceptance-criteria.md  three sections, all naming real stories: US-02, US-03, US-04
PASS   AC-3  acceptance-criteria.md  every section has 3 to 5 uniquely numbered criteria
PASS   AC-4  acceptance-criteria.md  all 11 criteria are complete Given/When/Then
PASS   AC-5  acceptance-criteria.md  every section covers an invalid or boundary case
PASS   AC-6  acceptance-criteria.md  3 assumptions listed before the criteria
PASS   AC-7  acceptance-criteria.md  both open questions are settled in the assumptions
PASS   PU-1  use-cases.puml          valid PlantUML block, no placeholders
PASS   PU-2  use-cases.puml          exactly two actors: Student, Administrator
PASS   PU-3  use-cases.puml          all six use cases present
PASS   PU-4  use-cases.puml          system boundary present
PASS   PU-5  use-cases.puml          no screens, databases or internal components
PASS   PU-6  use-cases.puml          no unjustified actor associations found
PASS   TR-1  traceability.md         all six use cases have a row
PASS   TR-2  traceability.md         every ID in the table resolves
PASS   TR-3  traceability.md         every story appears in the table
------------------------------------------------------------------------
23 PASS · 0 FAIL · 0 ERROR   (23 checks)
Shape is clean. This says nothing about whether the requirements are good.
```

```
$ python tests/validate_submission.py
(run after submission.yml is filled)
```

| | PASS | FAIL | ERROR |
| --- | --- | --- | --- |
| `check_requirements.py` | 23 | 0 | 0 |

Commit these numbers were produced at (`git rev-parse --short HEAD`): 9b01f8d

**Every FAIL, one line each: what it is and what you decided to do about it.** No FAIL or ERROR results.

**Did you run the checks by hand instead of with Python?** No.

---

## 10. Conclusion (150–200 words)

The most wrong generated requirement was the direct Student association with UC-06 Send confirmation. A student can trigger booking or cancellation, but confirmation is a system response after those actions. I would catch this without a checker by asking who actually starts each use case. If the actor does not intentionally request it, the association is probably wrong.

The assistant was useful for quickly producing a complete first pass of stories and criteria. It covered the main Student and Administrator goals, and it remembered the blocked-room and overlap rules. Writing that structure from zero would take longer by hand.

Before handing this to developers, I would rewrite UC-06 and its related stories first. Confirmation is important, but the requirements still do not say exactly what information the confirmation contains or where it appears. Since SMS, push notifications and reminders are out of scope, the wording must be careful. Otherwise developers might build an unsupported notification feature instead of a simple in-system confirmation.
