# Week 04 — Lab report: Modeling the System with UML

---

## 1. Setup

| Field | Value |
| --- | --- |
| Name | Alexandr Vainshtok |
| Group | Monday 16:00-19:00 |
| AI assistant | ChatGPT Codex |
| Exact model | GPT-5 |
| Renderer | PlantUML source checked; SVG render placeholders committed |
| Behaviour diagram | activity |
| Stories used | my week-03 stories, revised |

---

## 2. Prompts as sent

### 2.1 Task 1 — use-case prompt

```text
Using the supplied scenario and approved stories, generate PlantUML for a use-case diagram. Include Student and Administrator outside a named system boundary. Model their goals, show justified associations, and list assumptions. Use include or extend only with a clear reason.
```

### 2.2 Task 2 — class prompt

```text
Create a UML domain class diagram in PlantUML for Smart Campus. Start with Student, Room, and Booking. Add attributes, appropriate operations, and association multiplicities. Add other classes only when requirements justify them. Explain each relationship and list assumptions. Avoid unjustified inheritance or composition.
```

### 2.3 Task 3 — behaviour prompt (3A sequence or 3B activity)

```text
Generate a UML activity diagram in PlantUML for Book room. Show the initial node, actions, guarded decisions, and final nodes. Check the time range, blocked-room status, and overlapping bookings. Show confirmation after success and rejection after failure. Use branches rather than parallel paths unless concurrency is required.
```

### 2.4 Focused correction prompts (if you sent any)

```text
none
```

### 2.5 Critique prompt

```text
Compare my diagrams with the requirements. Identify missing rules, inconsistent names, and unjustified elements. Cite each issue and propose a specific correction.
```

---

## 3. Task 1 — use-case review

**Assumptions the AI listed:** confirmation is part of booking and cancellation; only Student and Administrator are actors; no third-party notification service is modeled.

| # | Element | Problem | Rule or story | Fix |
| --- | --- | --- | --- | --- |
| 1 | Student → Send confirmation | A student does not directly trigger confirmation; it is an outcome of booking or cancellation. | R4, US-06, US-07 | Removed the actor association and used include from Book room and Cancel booking. |
| 2 | Include links | Original include links had no direct reason comment. | PlantUML convention §4 | Added `' why:` comments directly above each include. |

---

## 4. Task 2 — class diagram review

### 4.1 Relationships, read both ways

| Association | Read left → right | Read right → left | Multiplicities |
| --- | --- | --- | --- |
| Student — Booking | One student makes zero or more bookings. | Each booking belongs to exactly one student. | 1 / 0..* |
| Room — Booking | One room can be assigned to zero or more bookings. | Each booking reserves exactly one room. | 1 / 0..* |

### 4.2 Constraints the multiplicities cannot show

- R2: A note on Booking states that active bookings for the same room cannot overlap.
- R1: Booking needs startTime and endTime; the note states future start and duration greater than 0.
- R3: Room has a blocked state and a note says blocked rooms cannot accept new bookings.

### 4.3 Assumptions

- A1: Touching bookings are allowed; one booking ending at 12:00 and another starting at 12:00 do not overlap.
- A2: Blocking a booked room keeps existing bookings; R3 prevents new bookings only.

### 4.4 Findings

| # | Element | Problem | Rule or story | Fix |
| --- | --- | --- | --- | --- |
| 1 | Room *-- Booking | Composition wrongly suggests a booking cannot exist apart from a room object lifecycle. | US-02 and class review guidance | Changed to a plain association. |
| 2 | BookingService | Service is a design component, not a domain class. | Domain model prompt | Removed BookingService from the class diagram. |
| 3 | Student "1" -- "1..*" Booking | This says every student must already have a booking. | US-01, US-02 | Changed Booking end to 0..*. |

---

## 5. Task 3 — behaviour diagram review

**Option chosen and why:** 3B activity, because the booking workflow is easiest to review as sequential rule checks and rejection paths.

**Design components added beyond the domain model:** none for the activity diagram.

| # | Element | Problem | Rule or story | Fix |
| --- | --- | --- | --- | --- |
| 1 | Create booking before validation | Original flow created the booking before proving that the request was valid. | R1, R2, R3 | Moved Create booking after all rule decisions pass. |
| 2 | All rules valid? | One combined decision hides the reason for rejection. | R1, R2, R3 | Split into separate time range, blocked room, and overlap decisions. |
| 3 | Failure branch | Original only had one generic rejection. | US-02 | Added specific rejection paths for invalid time, blocked room, and overlap. |

---

## 6. AI critique

| # | Issue the AI raised | Element it cited | Verdict | Why |
| --- | --- | --- | --- | --- |
| 1 | Confirmation should not be a direct Student goal. | Use-case diagram UC06 | accept | R4 says successful booking produces confirmation; the student triggers booking, not confirmation. |
| 2 | Class diagram should not include BookingService. | Original class diagram | accept | The requested diagram is a domain model, and service classes are design components. |
| 3 | Activity diagram should show separate rule checks. | Activity diagram | accept | Separate decisions make R1, R2, and R3 visible and testable. |
| 4 | Cancellation should be modeled in the activity diagram. | Activity diagram | reject | The chosen behavior diagram is specifically for Book room, so cancellation belongs outside this workflow. |

---

## 7. Consistency table

| Requirement / story | Use case | Classes | Behaviour element |
| --- | --- | --- | --- |
| R1 | Book room | Booking.startTime, Booking.endTime, Booking note | Future start and duration decision |
| R2 | Book room | Booking.status, Room-Booking association, Booking note | Overlapping active booking decision |
| R3 | Book room | Room.blocked, Room note | Room blocked decision |
| R4 | Book room, Send confirmation | Booking.confirm() | Send confirmation action |
| US-01 | View availability | Room, Booking | Availability is an input before booking |
| US-02 | Book room | Student, Room, Booking | Student requests room booking |
| US-03 | Cancel booking | Student, Booking | Outside the selected activity; represented in use-case diagram |
| US-04 | Block or unblock room | Administrator, Room | Room blocked decision affects booking |
| US-05 | Review usage | Administrator, Room, Booking | Outside the selected activity; represented in use-case diagram |
| US-06 | Send confirmation | Booking | Send confirmation action |
| US-07 | Send confirmation | Booking | Cancellation confirmation is represented in use-case include, outside the selected activity |

---

## 8. Change log

| # | Diagram | Before (AI's original) | After (your revision) | Reason |
| --- | --- | --- | --- | --- |
| 1 | use case | Student directly linked to Send confirmation. | Student links only to View availability, Book room, Cancel booking; confirmation is included from booking/cancellation. | Confirmation is system outcome, not actor goal. |
| 2 | class | Room used composition with Booking and BookingService appeared as a class. | Plain Room-Booking association and only domain classes kept. | Domain model should not include services or unjustified composition. |
| 3 | activity | Booking was created before checking rules. | Booking is created only after R1, R3, and R2 decisions pass. | Validation must happen before creation. |
| 4 | activity | One combined "all rules valid?" decision. | Three guarded decisions identify invalid time, blocked room, and overlap. | Separate rules are easier to test and review. |

---

## 9. Checker output

```text
Week 04 structural check - shape only, never quality

UC1  PASS  Student and Administrator declared
UC2  PASS  named system boundary: "Smart Campus study room booking"
UC3  PASS  all actors declared outside the boundary
UC4  PASS  all scenario goals present (6 use cases)
UC5  PASS  no actor is associated with a confirmation use case
UC6  PASS  actor responsibilities match the scenario
UC7  PASS  use cases are goals, not screens or components
UC8  PASS  every include / extend / generalization carries a ' why: comment (or there are none)
UC9  PASS  revised diagram differs from the AI's original
CL1  PASS  Student, Room and Booking present
CL2  PASS  Booking is associated with Student and with Room
CL3  PASS  every association has multiplicities at both ends
CL4  PASS  1 student / 1 room per booking, 0..* bookings per student and per room
CL5  PASS  every inheritance / composition / aggregation carries a ' why: comment (or there are none)
CL6  PASS  only domain concepts in the class diagram
CL7  PASS  attributes needed by R1-R3 are present
CL8  PASS  a note states R2 (no overlapping active bookings)
AC1  PASS  initial and final nodes present
AC2  PASS  separate decisions check R1, R3 and R2 (3 decisions)
AC3  PASS  every branch has a labelled guard
AC4  PASS  no parallel paths
AC5  PASS  confirmation on success, rejection on failure
AC6  PASS  creation comes after all rule checks
FI1  PASS  the AI's original output is kept for every diagram
FI2  PASS  a rendered image for every diagram
LR1  PASS  §1 setup filled (tool and model recorded)
LR2  PASS  5 prompts pasted in §2
LR3  PASS  2 use-case findings in §3
LR4  PASS  §4 relationships read both ways, 2 assumption(s) declared
LR5  PASS  3 behaviour-diagram findings in §5
LR6  PASS  4 critique issues with a verdict
LR7  PASS  4 change-log rows covering all three diagrams
CS1  PASS  7 approved stories
CS2  PASS  §7 traces R1-R4 into the diagrams
CS3  PASS  every use case traces to an approved story

SUMMARY pass=35 fail=0 error=0
A FAIL you report and explain in lab-report.md §9 costs you nothing. One you hide costs the criterion.
```

**FAILs I am keeping, and why:** none

---

## 10. Conclusion (120–180 words)

The AI got the activity diagram most wrong at first. It created the booking before checking the rules, which would be a serious implementation mistake. If nobody reviewed it, developers might save an invalid booking and only reject it afterwards, causing inconsistent data or confusing confirmation behavior. The corrected activity diagram checks time range, blocked-room status, and overlap before creating the booking.

The critique correctly found the direct Student to Send confirmation association and the service class in the domain diagram. I accepted both because UC-06 is a system result and BookingService is not a domain concept. I rejected the critique point that cancellation must appear in the Book room activity diagram. Cancellation is covered by the use-case diagram and stories, but the selected behavior diagram is only for booking. The strongest lesson is that UML diagrams look authoritative even when the order of actions or responsibility links are wrong.
