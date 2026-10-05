# Acceptance criteria — three selected stories

## Assumptions

- **Overlap:** a booking that ends exactly when another begins is allowed under R3, because the two students do not occupy the room at the same time.
- **Duration:** a booking of exactly two hours is allowed under R2, because the rule says "at most two hours".
- **Blocked rooms:** a blocked room cannot receive new bookings until an Administrator unblocks it.

---

## US-02 — Book room

### AC-01
- **Given** a Student selects an unblocked room with no overlapping booking
- **When** the Student requests a future booking lasting one hour
- **Then** the system creates the booking and records the selected time slot

### AC-02
- **Given** a Student selects any room
- **When** the Student requests a booking that starts in the past
- **Then** the system rejects the booking because it violates R1

### AC-03
- **Given** a Student selects an available room
- **When** the Student requests a booking longer than two hours
- **Then** the system rejects the booking because it violates R2

### AC-04
- **Given** a room already has a booking from 14:00 to 15:00
- **When** the Student requests the same room from 14:30 to 15:30
- **Then** the system rejects the booking because it overlaps under R3

### AC-05
- **Given** a room is blocked by an Administrator
- **When** the Student requests a new booking for that room
- **Then** the system rejects the booking because blocked rooms cannot be booked under R4

---

## US-03 — Cancel booking

### AC-06
- **Given** a Student has an existing booking
- **When** the Student cancels that booking
- **Then** the system releases the room for the cancelled time slot

### AC-07
- **Given** a Student tries to cancel a booking made by another student
- **When** the cancellation is requested
- **Then** the system rejects the cancellation

### AC-08
- **Given** a Student has cancelled a booking successfully
- **When** another Student views availability for the same room and time
- **Then** the released slot is shown as available

---

## US-04 — Block or unblock room

### AC-09
- **Given** an Administrator selects an active room
- **When** the Administrator blocks the room
- **Then** the system marks the room unavailable for new bookings

### AC-10
- **Given** a room is blocked
- **When** a Student attempts to book it
- **Then** the system rejects the booking under R4

### AC-11
- **Given** an Administrator selects a blocked room
- **When** the Administrator unblocks the room
- **Then** the system allows future valid booking requests for that room
