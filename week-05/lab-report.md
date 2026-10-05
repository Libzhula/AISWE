# Week 05 — Lab report

**Name:** Alexandr Vainshtok
**Group:** Monday 16:00-19:00
**Date:** 2026-10-05

---

## 1. Setup

| | |
| --- | --- |
| Assistant (tool) | ChatGPT Codex |
| **Exact** model name | GPT-5 |
| Language and version | Python 3 |
| Path | A |
| My Week 04 declaration for touching bookings | allowed |

Week 04 and AC4 agree that touching endpoints are allowed, so no model assumption had to change.

---

## 2. Task 1 — the plan

**The assistant's plan, pasted unedited:**

```text
Implementation plan:
1. Check AC1 first: start and end must be inside the day, start must be before end, and start must be after now.
2. Check AC2: reject any request longer than 120 minutes.
3. Check AC3: reject immediately when blocked is True.
4. Check AC4: compare the request with every existing active booking. Use start < booked_end and end > booked_start; this rejects real overlap and allows touching endpoints.
5. If all checks pass, return True. Otherwise return False. Do not mutate existing.

Boundary cases: touching at the end, touching at the start, exactly 120 minutes, 121 minutes, starts now, zero-length, reversed times, end after 1440, empty existing list, multiple bookings, unsorted bookings, and unchanged input.
```

**What the plan invented or changed.**

| # | What the plan said | What the contract or the AC says | What I did |
| --- | --- | --- | --- |
| 1 | Check AC1, AC2, AC3, AC4, then return by AC5. | AC1-AC5 require exactly those checks and a Boolean result. | Kept the plan; it invented no extra rule. |

**Boundary cases the assistant suggested that I kept as tests:**

- touching at the end and at the start
- exactly 120 minutes and 121 minutes
- zero-length and reversed times
- end after 1440
- empty, multiple, and unsorted existing bookings
- unchanged input after accept and reject

---

## 3. Task 2 — the first version (v1), read before it was run

v1 is saved as `code/original/booking_v1.py`, exactly as the assistant returned it: yes

**AC map.**

| # | Line in v1 | AC it implements | Correct as written? If not, why |
| --- | --- | --- | --- |
| 1 | `if not (0 <= start < end <= 1440):` | AC1 | Correct; checks day bounds and time order. |
| 2 | `if start <= now:` | AC1 | Correct; start must be greater than now. |
| 3 | `if end - start > 120:` | AC2 | Correct; exactly 120 is allowed. |
| 4 | `if blocked:` | AC3 | Correct; blocked room rejects all requests. |
| 5 | `if start < booked_end and end > booked_start:` | AC4 | Correct; real overlap is rejected and touching endpoints pass. |
| 6 | `return True` after all checks | AC5 | Correct; True only when AC1-AC4 hold. |

**Anything in v1 that no AC asks for**:

- Nothing beyond the contract.

---

## 4. Task 3 — my tests

Base input for every row unless the row says otherwise: `now=540, blocked=False, existing=[(600, 660)]`.

| # | Test name | Request (start, end) | What differs from the base input | Expected | AC | Result on v1 | Result on final |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | touching_end_is_allowed | (660, 720) | none | True | AC4 | PASS | PASS |
| 2 | exactly_two_hours_is_allowed | (720, 840) | none | True | AC2 | PASS | PASS |
| 3 | overlap_is_rejected | (630, 690) | none | False | AC4 | PASS | PASS |
| 4 | over_two_hours_is_rejected | (720, 841) | none | False | AC2 | PASS | PASS |
| 5 | blocked_room_is_rejected | (660, 720) | blocked=True | False | AC3 | PASS | PASS |
| 6 | starts_now_is_rejected | (540, 570) | none | False | AC1 | PASS | PASS |
| 7 | zero_length_is_rejected | (700, 700) | none | False | AC1 | PASS | PASS |
| 8 | reversed_times_are_rejected | (720, 700) | none | False | AC1 | PASS | PASS |
| 9 | day_lower_bound_is_rejected | (-1, 30) | existing=[] | False | AC1 | PASS | PASS |
| 10 | day_upper_bound_allows_1440 | (1380, 1440) | existing=[] | True | AC1 | PASS | PASS |
| 11 | day_upper_bound_rejects_after_1440 | (1380, 1441) | existing=[] | False | AC1 | PASS | PASS |
| 12 | empty_existing_allows_valid_request | (600, 660) | existing=[] | True | AC4 | PASS | PASS |
| 13 | multiple_existing_checks_second_booking | (720, 780) | existing=[(600,660),(700,760)] | False | AC4 | PASS | PASS |
| 14 | unsorted_existing_is_checked | (610, 650) | existing=[(900,960),(600,660)] | False | AC4 | PASS | PASS |
| 15 | inside_existing_is_rejected | (615, 645) | none | False | AC4 | PASS | PASS |
| 16 | contains_existing_is_rejected | (570, 690) | none | False | AC4 | PASS | PASS |
| 17 | touches_existing_start_is_allowed | (570, 600) | none | True | AC4 | PASS | PASS |
| 18 | between_two_touching_bookings_is_allowed | (660, 720) | existing=[(600,660),(720,780)] | True | AC4 | PASS | PASS |
| 19 | inputs_are_unchanged_on_accept | (780, 840) | unsorted existing | True | AC5 | PASS | PASS |
| 20 | inputs_are_unchanged_on_reject | (610, 650) | unsorted existing | False | AC5 | PASS | PASS |

---

## 5. Task 4 — debugging with evidence

| # | Input (the full call) | Expected | Actual | Cause (quote the line) | Fix | Who proposed the fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `can_book(660, 720, 540, False, [(600, 660)])` plus the rest of the suite | True and all suite cases pass | True; v1 passed all 20 tests and all F checks | `if start < booked_end and end > booked_start:` handled overlap correctly | No code fix needed; kept v1 unchanged | I decided after test evidence |

**The debug prompt I sent, and the assistant's answer**:

```text
No debug prompt was sent because v1 passed the complete suite and checker behavior checks.
```

---

## 6. Task 5 — the critique

**The assistant's critique, pasted unedited:**

```text
1. The overlap condition is correct for half-open intervals. The line `if start < booked_end and end > booked_start:` rejects actual overlap and allows touching endpoints, matching AC4.
2. The function returns False rather than raising errors for invalid time ranges. This matches AC5 because the contract asks for a Boolean decision.
3. The implementation does not mutate existing. It only iterates over it, which supports AC5.
4. The function assumes inputs follow the contract, including integer times and valid existing tuples. That is acceptable because the contract says those inputs are valid.
```

| # | Suggestion | accept / reject | Reason — cite the AC or the contract line | Suite after the change |
| --- | --- | --- | --- | --- |
| 1 | Keep overlap condition | accept | AC4 says touching endpoints are allowed; half-open comparison is right. | 20 tests OK |
| 2 | Return False for invalid ranges | accept | AC5 says return True only when AC1-AC4 hold; otherwise False. | 20 tests OK |
| 3 | No mutation issue | accept | AC5 says never alter existing; tests 19 and 20 verify it. | 20 tests OK |
| 4 | Contract-valid existing tuples | accept | Contract says existing contains valid active booking tuples. | 20 tests OK |

---

## 7. Change log — v1 to final

| # | What changed (the line, before → after) | Why | Evidence: the test or check that moved |
| --- | --- | --- | --- |
| 1 | No code change; `booking_v1.py` and final `booking.py` stayed identical. | v1 satisfied AC1-AC5 and the expanded tests. | 20 unit tests OK; checker F1-F10 and M1-M10 passed. |

---

## 8. Evidence — real output

### 8.1 My suite, final run

```text
test_between_two_touching_bookings_is_allowed (test_booking.BookingTests.test_between_two_touching_bookings_is_allowed) ... ok
test_blocked_room_is_rejected (test_booking.BookingTests.test_blocked_room_is_rejected) ... ok
test_contains_existing_is_rejected (test_booking.BookingTests.test_contains_existing_is_rejected) ... ok
test_day_lower_bound_is_rejected (test_booking.BookingTests.test_day_lower_bound_is_rejected) ... ok
test_day_upper_bound_allows_1440 (test_booking.BookingTests.test_day_upper_bound_allows_1440) ... ok
test_day_upper_bound_rejects_after_1440 (test_booking.BookingTests.test_day_upper_bound_rejects_after_1440) ... ok
test_empty_existing_allows_valid_request (test_booking.BookingTests.test_empty_existing_allows_valid_request) ... ok
test_exactly_two_hours_is_allowed (test_booking.BookingTests.test_exactly_two_hours_is_allowed) ... ok
test_inputs_are_unchanged_on_accept (test_booking.BookingTests.test_inputs_are_unchanged_on_accept) ... ok
test_inputs_are_unchanged_on_reject (test_booking.BookingTests.test_inputs_are_unchanged_on_reject) ... ok
test_inside_existing_is_rejected (test_booking.BookingTests.test_inside_existing_is_rejected) ... ok
test_multiple_existing_checks_second_booking (test_booking.BookingTests.test_multiple_existing_checks_second_booking) ... ok
test_over_two_hours_is_rejected (test_booking.BookingTests.test_over_two_hours_is_rejected) ... ok
test_overlap_is_rejected (test_booking.BookingTests.test_overlap_is_rejected) ... ok
test_reversed_times_are_rejected (test_booking.BookingTests.test_reversed_times_are_rejected) ... ok
test_starts_now_is_rejected (test_booking.BookingTests.test_starts_now_is_rejected) ... ok
test_touches_existing_start_is_allowed (test_booking.BookingTests.test_touches_existing_start_is_allowed) ... ok
test_touching_end_is_allowed (test_booking.BookingTests.test_touching_end_is_allowed) ... ok
test_unsorted_existing_is_checked (test_booking.BookingTests.test_unsorted_existing_is_checked) ... ok
test_zero_length_is_rejected (test_booking.BookingTests.test_zero_length_is_rejected) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.001s

OK
```

### 8.2 The checker, final run

```text
Week 05 - can_book: the function, your tests, the evidence   (Path A)

PASS   F1   the six cases from the task table           6 of 6 cases
PASS   F2   AC1 time order and day bounds               5 of 5 cases
PASS   F3   AC1 the start is in the future              5 of 5 cases
PASS   F4   AC2 at most 120 minutes                     3 of 3 cases
PASS   F5   AC3 a blocked room accepts nothing          2 of 2 cases
PASS   F6   AC4 every kind of overlap is rejected       5 of 5 cases
PASS   F7   AC4 touching endpoints are allowed          3 of 3 cases
PASS   F8   AC4 every existing booking is checked       4 of 4 cases
PASS   F9   AC5 the result is a real Boolean            3 of 3 cases
PASS   F10  AC5 the inputs are left unchanged           2 of 2 cases
PASS   O1   the assistant's first version is kept       v1 kept (16 lines)
PASS   S1   your suite has at least 11 tests            20 tests
PASS   S2   your suite is green on your own code        20 tests, OK
PASS   M1   your tests catch a fault in AC1             caught by test_starts_now_is_rejected
PASS   M2   your tests catch a fault in AC1             caught by test_day_upper_bound_rejects_after_1440
PASS   M3   your tests catch a fault in AC1             caught by test_zero_length_is_rejected
PASS   M4   your tests catch a fault in AC2             caught by test_exactly_two_hours_is_allowed
PASS   M5   your tests catch a fault in AC3             caught by test_blocked_room_is_rejected
PASS   M6   your tests catch a fault in AC4             caught by test_between_two_touching_bookings_is_allowed, test_touches_existing_start_is_allowed, test_touching_end_is_allowed
PASS   M7   your tests catch a fault in AC4             caught by test_inputs_are_unchanged_on_reject, test_multiple_existing_checks_second_booking, test_unsorted_existing_is_checked
PASS   M8   your tests catch a fault in AC4             caught by test_contains_existing_is_rejected
PASS   M9   your tests catch a fault in AC5             caught by test_inputs_are_unchanged_on_accept
PASS   M10  your tests catch a fault in AC5             caught by test_inputs_are_unchanged_on_accept, test_inputs_are_unchanged_on_reject
PASS   L1   report 1: tool, model and language          tool, model and language recorded
PASS   L2   report 2: the plan, and what you corrected  plan pasted, 1 row(s) on what you corrected or verified
PASS   L3   report 3: v1 mapped to AC1-AC4              6 conditions mapped, AC1-AC4 all present
PASS   L4   report 4: at least 11 of your tests listed  20 tests listed
PASS   L5   report 5: debugging evidence                1 row(s) of input / expected / actual
PASS   L6   report 6: the critique, each point judged   critique pasted, 4 points judged
PASS   L7   report 7: change log                        1 change-log row(s)
PASS   L8   report 8.1: real output of your suite       suite output pasted
PASS   L9   report 10: conclusion of 120-180 words      146 words
------------------------------------------------------------------------------
v1 (code/original/booking_v1.py): passes F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 - fails nothing - identical to your final: yes
SUMMARY pass=32 fail=0 error=0   (32 checks)
Behaviour and shape are clean. This says nothing about the quality of your review.
```

### 8.3 Path B only — three faults I planted myself

| # | Line I changed (before → after) | AC it breaks | Test that failed |
| --- | --- | --- | --- |

The three failing runs (Path A students leave this block empty):

```text
```

---

## 9. What still fails, and what the contract does not say

### 9.1 Checks I am keeping as FAIL or ERROR

| Check | Why it stays |
| --- | --- |
| none | The final checker run is clean. |

### 9.2 Outside the contract

The contract says times are integers, so my function does not add separate type validation. With `600.5`, Python comparisons and subtraction work, so the function may return a Boolean based on the numeric value. With `"600"`, Python raises a `TypeError` during comparison. I declare this as not-handled because non-integer times are outside the supplied contract.

### 9.3 A bound that never decides

The bound `start < end` means `end <= 1440` can never be the only reason when `end` is too low; for example, zero-length or reversed intervals already fail the ordering part. For upper-day validation, `end <= 1440` still matters because `(1380, 1441)` has valid order but is outside the day.

---

## 10. Conclusion (120–180 words)

The final overlap condition is `start < booked_end and end > booked_start`. Both comparisons are strict because the assignment says intervals include the start and exclude the end. If a requested booking starts exactly when an existing one ends, `start < booked_end` is false, so it is allowed. If it ends exactly when an existing one starts, `end > booked_start` is false, so it is also allowed.

The tests did not miss a code fault for long because v1 already passed the checker, but the most important risk was testing only the six table cases. Those cases include one overlap and one touching endpoint, but not every overlap shape. I added inside, contains, unsorted, second-booking, and both-touching tests to cover AC4 properly.

The decision I had to make was outside the contract: non-integer times. I left them not-handled because the contract says times are integer minutes.
