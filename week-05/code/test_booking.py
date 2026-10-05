import unittest

from booking import can_book


BASE_NOW = 540
BASE_EXISTING = [(600, 660)]


class BookingTests(unittest.TestCase):
    def test_touching_end_is_allowed(self):
        self.assertIs(can_book(660, 720, BASE_NOW, False, BASE_EXISTING), True)

    def test_exactly_two_hours_is_allowed(self):
        self.assertIs(can_book(720, 840, BASE_NOW, False, BASE_EXISTING), True)

    def test_overlap_is_rejected(self):
        self.assertIs(can_book(630, 690, BASE_NOW, False, BASE_EXISTING), False)

    def test_over_two_hours_is_rejected(self):
        self.assertIs(can_book(720, 841, BASE_NOW, False, BASE_EXISTING), False)

    def test_blocked_room_is_rejected(self):
        self.assertIs(can_book(660, 720, BASE_NOW, True, BASE_EXISTING), False)

    def test_starts_now_is_rejected(self):
        self.assertIs(can_book(540, 570, BASE_NOW, False, BASE_EXISTING), False)

    def test_zero_length_is_rejected(self):
        self.assertIs(can_book(700, 700, BASE_NOW, False, BASE_EXISTING), False)

    def test_reversed_times_are_rejected(self):
        self.assertIs(can_book(720, 700, BASE_NOW, False, BASE_EXISTING), False)

    def test_day_lower_bound_is_rejected(self):
        self.assertIs(can_book(-1, 30, BASE_NOW, False, []), False)

    def test_day_upper_bound_allows_1440(self):
        self.assertIs(can_book(1380, 1440, BASE_NOW, False, []), True)

    def test_day_upper_bound_rejects_after_1440(self):
        self.assertIs(can_book(1380, 1441, BASE_NOW, False, []), False)

    def test_empty_existing_allows_valid_request(self):
        self.assertIs(can_book(600, 660, BASE_NOW, False, []), True)

    def test_multiple_existing_checks_second_booking(self):
        existing = [(600, 660), (700, 760)]
        self.assertIs(can_book(720, 780, BASE_NOW, False, existing), False)

    def test_unsorted_existing_is_checked(self):
        existing = [(900, 960), (600, 660)]
        self.assertIs(can_book(610, 650, BASE_NOW, False, existing), False)

    def test_inside_existing_is_rejected(self):
        self.assertIs(can_book(615, 645, BASE_NOW, False, BASE_EXISTING), False)

    def test_contains_existing_is_rejected(self):
        self.assertIs(can_book(570, 690, BASE_NOW, False, BASE_EXISTING), False)

    def test_touches_existing_start_is_allowed(self):
        self.assertIs(can_book(570, 600, BASE_NOW, False, BASE_EXISTING), True)

    def test_between_two_touching_bookings_is_allowed(self):
        existing = [(600, 660), (720, 780)]
        self.assertIs(can_book(660, 720, BASE_NOW, False, existing), True)

    def test_inputs_are_unchanged_on_accept(self):
        existing = [(900, 960), (600, 660), (700, 760)]
        snapshot = list(existing)
        self.assertIs(can_book(780, 840, BASE_NOW, False, existing), True)
        self.assertEqual(existing, snapshot)

    def test_inputs_are_unchanged_on_reject(self):
        existing = [(900, 960), (600, 660), (700, 760)]
        snapshot = list(existing)
        self.assertIs(can_book(610, 650, BASE_NOW, False, existing), False)
        self.assertEqual(existing, snapshot)


if __name__ == "__main__":
    unittest.main()
