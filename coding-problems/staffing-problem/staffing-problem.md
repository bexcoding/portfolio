# Problem Prompt 

At the end of every 12 hour shift at the hospital, one of the nurses creates an assignment for the coming shift. An assignment is a list of nurses who are scheduled and the patients that are assigned to those nurses. Each unit of the hospital has different requirements for how many patients can be assigned to any given nurse. You must create a solution that returns an assignment for the ICU (Intensive Care Unit). The following limitations and specifications apply:
- Input:
    - Ask the user of the program what nurses are scheduled and what their skill levels are.
    - Ask the user what patients are currently present and what their acuity levels are.
    - There may be 0 to infinity patients or nurses present.
- Nurse to Patient Ratio:
    - Each unit in the hospital has its own ratio of nurses to patients. In the particular ICU in this problem, the ratio is either two patients to one nurse or one patient to one nurse. This means every nurse will have two patients OR one patient OR no patients.
- Nurse Skill:
    - Nurses can have one of two levels of skill - advanced or beginner. 
    - Only advanced nurses can take care of high acuity level patients.
    - Advanced nurses can take care of any patient while beginner nurses can only take care of low acuity patients.
- Patient Acuity (Difficulty):
    - There are two types of patients - high acuity and low acuity.
    - Patient acuity refers to the difficulty and complexity of a patient's medical needs.
    - High acuity patients must be taken care of by advanced nurses.
- Other Staffing Rules:
    - The maximum number of patients that a single nurse can have is two.
    - High acuity patients need their own individual nurse but low acuity patients can share their nurse with one other patient.
    - There must always be at least two nurses on the floor at any given time, even if there are no patients. This is to account for emergencies and for new patients to come to the ICU.
- Expected Output:
    - If there are less than two nurses present, print a message stating the rule of having at least two nurses present at all times.
    - If there are not enough nurses to take care of the patients, print a message saying so.
    - If there are enough nurses to take care of the patients, return and print a dictionary where the keys are the nurses names and the values are tuples of what patients the nurse is assigned to, if any. 
    
# Implementation Notes

These are some notes about why I wrote my solution the way I did.

### File Naming

One might notice that both the explanation/prompt file and the test file follow the typical naming convention of GitHub files - "xxx-xxxxx-xxxxxx.filetype". However, my solution file is the only file in my portfolio (at the time of this writing) to have the "xxx_xxxxx_xxxxxx.filetype" format with underscores instead of dashes. This was not a mistake. When writing my tests for this code, I kept trying to import my solution to the test file so that I could use the functions in the tests. It wasn't working and ended up causing some frustration. With a little bit of experimentation, I came to realize that my environment did not want to import a file with dashes instead of underscores. As far as I can tell, python modules like to be named with either underscores or no separating characters but cannot be named using dashes if you want them to actually import. 

### Why Tuples

In my solution to the staffing problem, I use tuples in several places where they may not be expected. First, I use them in `check_nurse_quantity()`. I could have just returned `True` or `False` but I wanted my `False` message to include a string stating whether the staffing failed because of the minimum nurse rule or if it failed because of the mismatch of skill and acuity. To return two things simultaneously in Python, you have to wrap them together in some object like a dictionary or tuple. The tuple is the easiest and most common way to return a couple of values at one time. Because I returned a tuple with the `False` branch and I wanted to keep the code parallel, I returned the `True` branch as a one item tuple, which looks like `(True)` in Python with a trailing comma.
This same search for parallel code brought me to use tuples again in `match_nurse_to_patient()`. While my assignment dictionary could have used tuples for pairing two patients together and strings if there was just one patient, I wanted the result to be a string attached to a tuple. Inside the tuple could be either 0, 1, or 2 strings. I have not always use this technique of parallel code but it is one of the recommendations I have read about recently to make code more professional.

### Ordering of the Matching Function 

In my `match_nurse_to_patient()` function, I go in a very specific order when matching nurses in patients using several `while` loops. First, I assign all of the high acuity patients because they are the most restrictive element. Then, I add together any remaining advanced nurses with the beginner nurses and assign the rest of the low acuity patients. Finally, I assign an empty assignment to all remaining nurses so that they don't fall off the list and get forgotten.
The naive approach would be to assign the first nurse to either one or two patients based off of skill and acuity, but then you might end up with advanced patients getting assigned to beginner nurses. The only solution is to ensure that the high acuity patients are addressed first. To address them, they have to be assigned to advanced nurses and, to pull this off, I had to separate the dictionaries into high acuity, low acuity, advanced nurse, and beginner nurse lists. While this takes up extra space, this was the only way I could find to work with each category separately.

# Testing

This assignment was the first time I've used the automated tests included in the `unittest` Python module. I've read about it several times recently and have heard that it is well worth the effort. While it did take quite a bit of time setting up, I think that it was valuable to learn how to use this tool. I think that I may try the technique of writing the tests first in the future. This would help find some issues in the future instead of spending time searching for errors with print statements.
In this tests file, I tried to test each function but I could not test the functions that I wrote to get the user input for the nurse and patient lists. This is because there is no guarenteed input for these functions. I also tried to test each component of the functions that I could think might have errors.

# Improvements

If I were to make improvements or suggestions of how to extend this staffing solution problem, I would do any or all of the following:
- More levels of nurses and patients: I simplified the levels of acuity and skill for this problem to make it easier to solve. In the ICU where I worked, there were three levels of nurses - advanced, intermediate, and beginner. The patients were also split into three categories of difficulty. To make this work, each level of nurse could do the corresponding level of difficulty of patient or easier but this led to many challenging extra elements to the problem that I did not want to implement. 
- Maximum patient count: In this implementation I allowed any number of patients from 0 to infinity. The code would be better if the total number of patients had a maximum value. For most standard floors except for the emergency room, there is no possible way to have more patients than there are rooms. If I were to cap the number of patients, I would set the upper limit at 15 to represent a small ICU.
- Input type: Another improvement that would lend to usability is to provide both an option for manual insertion of the patient and nurse list and for inserting the lists from a file. For example, in real life there would be a list of nurses available usually a month ahead of time. It would also be common to have patients for several days so it would be nice to have the patient list stored elsewhere and only make adjustments for when patients arrive, leave, or change acuity level.
- Nurse Skill Database: It would be ideal to store the skill level of a particular nurse in a separate file. The skill level of any given nurse might take several months to change, so it would be redundant to enter their skill level every day they are scheduled. Ideally, the user would just enter the name and the code would be able to look up the nurse and retrieve their skill level. This would also reduce errors that would arrive from entering the wrong skill level.
- Input Error: I did not account for input error from users in this solution. This means that the input does not check that a nurse gets an 'a' or 'b' and it does not check that a patient gets an 'h' or 'l'. This would probably be the first component to fix before allowing non computer savvy users work with the program. Entering the wrong type of skill or acuity would affect the entire solution.
- Float Nurses: A real unit in a hospital would be affected by other units. If there were no patients, it would be likely that the extra nurses would be sent to other floors (this is called floating). I would always keep a minimum of two nurses on the floor and always have at least one nurse capable of taking more patients. Any extra nurses beyond this could be offered to be sent to other hospital units.
