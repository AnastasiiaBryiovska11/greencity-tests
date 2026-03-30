# Test Case ID: 4

## Title
Verify Event Filter functionality for Health events

## Priority
Medium

## Preconditions
1. The user is logged in
2. Click the "Event" button

---

## Test Steps

| Step | Step Description | Test Data | Expected Result |
|------|-----------------|-----------|----------------|
| 1 | Click the "Event time/Past" button | - | Display only past events. |
| 2 | Click the "Event time/Past" and "Event time/Upcoming" button | — | Display past and upcoming events. |
| 3 | Test all Event time buttons sequentially | - | All filters work correctly and display the corresponding events. |
| 4 | Click Type → All types filter | - | All event types are displayed; filters are applied correctly. |

---

## Postconditions
Events are displayed according to the selected filters.
