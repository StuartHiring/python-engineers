### Python Engineer Assessment

TASKS: These tasks are designed to test your python 🐍 skills, with a particular focus on OOP, validations and error handling. For each task we expect you to follow engineering best practices.

DURATION: You should be spending 1.5 to 3 hours to finish this assessment.

DISCLAIMER: Whilst this task is broadly based around the topic of logistics, please note this challenge has been generated purely for the purpose of this test and none of this code or logic represents code used at Stuart.

TECH STACK

- We recommend using Python 3.7 or above.
- We recommend having the following Python libraries installed: pandas, datetime, pytest.
  - Please feel free to use any additional libraries you think are useful.
- We use PyTest for our unit tests.
  - These tests are found in the /tests/ folder.
  - Each \_test.py should include a fixture that could be useful in any unit test you create.
- The /utils/ folder contains useful mappings that could be useful during the assessment

SUBMISSION

- Once you have finished the assessment, please zip all the files.
- Attach the zipped folder to an email and send the finished assessment to us as instructed.
- Please let us know any additional information we might need before reviewing your assessment.
- We're always looking to improve our assessments, please share with us any feedback you might have.
- Next steps? The assessment will be reviewed by our engineering team. Should you pass the assessment, we will send you an invitation for a technical interview to discuss the assessment directly with our team.

NOTES

- Show off! We love TDD. We love unit tests. We love design patterns. We love engineering!
- If you have further questions, don't hesitate asking.

# GOOD LUCK!

## Task 1

DURATION: ~ 1 hour

Create a Courier class in courier.py with the following:

Arguments

- courier_id: integer between 0 - 10,000 (required)
- first_name: string less than or equal to 50 characters long (required)
- surname: string less than or equal to 50 characters long (required)
- country: string (must be valid country found in utils.city_mapping.py)
- city: string (must be a valid city as recorded in utils.city_mapping.py)
- valid_from: datetime courier was registered (required)
- valid_to: datetime courier is valid to (not required):
  - set to 1 year from valid from if not specified
- vehicle: string from valid vehicle options (specified in vehicle_mapping.py)

Methods

- valid_at:
  - Returns if courier is valid at given date (between valid_from -> valid_to)
    Note - A courier is valid at the same time as valid_from, but not valid at the same time as valid_to.
    - Inputs:
      - date: date to check against (optional):
        - Use current date if not specified
    - Returns:
      - bool: True if courier is valid at given date, else False.

## Task 2

DURATION: ~ 30 minutes

Review the classes and methods in delivery.py:

- Produce technical documentation for delivery.py, this should be written in DeliveryDocumentation.md
- Refactor the code in delivery.py to improve performance and readability where required.

## Task 3

DURATION: ~ 1 hour

Create a function called find_courier in validate.py, which takes an list of Courier instances and an instance of a delivery class from delivery.py. The find_courier function:

- returns the delivery class instance which is updated with the following:

  - in_progress set to True if any Courier instance is validated
  - courier_id is set to first valid courier in list.
    - Optional: If multiple couriers are able to deliver to the courier, order first by green vehicles, and secondly by the vehicles top_speed.

- A courier is valid if:

  - ⏰ Courier is_valid at delivery date
  - 🌎 Courier is linked to the same city as the delivery
  - 🏃‍♀️ Vehicle must be capable of traveling distance of delivery

- If no courier is valid, Raise NoCourierFoundError.

Tests

- We have provided basic tests to help develop this function.
