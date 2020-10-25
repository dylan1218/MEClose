
approvalChoicesAccountRec = (
        ('Not Started', 'Not Started'),
        ('Rejected', 'In-Progress'),
        ('Approved', 'Completed'), 
)

approvalChoices = (
    ('Not Started', 'Not Started'),
    ('Waiting on Support', 'Waiting on Support Upload'),
    ('Rejected', 'In-Progress'),
    ('Reverted', 'In-Progress'),
    ('Approved', 'Completed'), 
)

statusChoices = (
    ('NS', 'Not Started'),
    ('WT', 'Waiting on Preceding Task'),
    ('IP', 'In-Progress'),
    ('CT', 'Completed'), 
)

#this choice field should go away after creating attributes based off of date field
periodChoices = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
)

periodChoices = (
    ("Opened", "Opened"),
    ("Closed", "Closed"),
    ("Late Entry", "Late Entry"),
)

binaryChoice = (
    ("Yes", "Yes"),
    ("No", "No"),
)