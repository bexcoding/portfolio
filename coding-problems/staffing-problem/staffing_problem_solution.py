'''
Title: ICU Nurse Staffing Problem
Description: Checks if ICU nurse staffing and creates a shift assignment
Developer: Alexander Beck
Email: beckhv2@gmail.com
Github: https://github.com/bexcoding

.....//\\......//\\......//\\......//\\......//\\......//\\......//\\....../
....//  \\....//  \\....//  \\....//  \\....//  \\....//  \\....//  \\....//
\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..//
\\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /
 || | <> | || | <> |                                     > | || | <> | || |
 || | <> | || | <> | ||                          ||   // > | || | <> | || |
 /\  \  /  /\  \  /  ||                          ||  //   /  /\  \  /  /\  \
/  \  \/  /  \  \/   ||____       ___      ___   || //   /  /  \  \/  /  \
 <> | || | <> | ||   ||    \\   //   \\  //   \\ ||||    | | <> | || | <> |
 <> | || | <> | ||   ||     || ||____|| ||       || \\   | | <> | || | <> |
\  /  ||  \  /  ||   ||     || ||       ||       ||  \\  |  \  /  ||  \  /
 \/  //\\  \/  //\\  ||____//   \\___//  \\___// ||   \\ \\  \/  //\\  \/  /
    //..\\    //..\\                                      \\    //..\\    //
\  //....\\  //....\\  //....\\  //....\\  //....\\  //....\\  //....\\  //.
\\//......\\//......\\//......\\//......\\//......\\//......\\//......\\//..

'''

import math


def check_nurse_quantity(nurses, adv_nurses, h_patients, l_patients):
    """
    int, int, int, int -> tuple (boolean, string)
    returns a tuple that tells if there are enough nurses
    
    nurses: total number of nurses
    adv_nurses: number of nurses marked as advanced
    h_patients: number of high acuity patients
    l_patients: number of low acuity patients
    
    assume all integer inputs are non-negative
    """
    
    if nurses >= 2:
        if nurses >= math.ceil(
                h_patients + (l_patients * 0.5)) and adv_nurses >= h_patients:
            return (True,)
        else:
            return (False, 
                    "There are not enough nurses for the patient acuity.")
    else:
        return (False, "At least two nurses are needed at all times.")


def match_nurse_to_patient(nurses, patients):
    """
    dict, dict -> dict
    returns a dictionary of nurses assigned to patients
    
    nurses: dictionary of scheduled nurses {name of nurse: skill level}
    patients: dictionary of current patients {initials: acuity (difficulty)}
    """
    # split nurses into "A" and "B" and patients into "H" and "L"
    advanced_nurses = [n for n in nurses if nurses.get(n) == "A"]
    basic_nurses = [n for n in nurses if n not in advanced_nurses]
    high_acuity_patients = [p for p in patients if patients.get(p) == "H"]
    low_acuity_patients = [
        p for p in patients if p not in high_acuity_patients]
    nurse_assignments = {}
    # assign high level patients first
    while len(high_acuity_patients) > 0:
        nurse_assignments.update(
            {advanced_nurses.pop(0): (high_acuity_patients.pop(0),)})
    combined_nurses = advanced_nurses + basic_nurses
    # assign the rest of the patients two at a time if possible
    while len(low_acuity_patients) > 0:
        if len(low_acuity_patients) == 1:
            nurse_assignments.update(
                {combined_nurses.pop(0): (low_acuity_patients.pop(0),)})
        else: 
            nurse_assignments.update(
                {combined_nurses.pop(0): (low_acuity_patients.pop(0), 
                                          low_acuity_patients.pop(0))})
    # add all unassigned nurses to the end of the assignment
    while len(combined_nurses) > 0:
        nurse_assignments.update(
            {combined_nurses.pop(0): ()})  
    return nurse_assignments


def check_then_match(scheduled_nurses, current_patients):
    """
    dict, dict -> dict or print message
    if the numer of nurses scheduled is sufficient, returns a dictionary of
    assignments. Otherwise prints an error message
    
    nurses: dictionary of scheduled nurses {name of nurse: skill level}
    patients: dictionary of current patients {initials: acuity (difficulty)}
    """
    count_of_high = list(current_patients.values()).count("H")
    count_of_low = list(current_patients.values()).count("L")
    advanced_nurse_count = list(scheduled_nurses.values()).count("A")
    result_of_quantity_check = check_nurse_quantity(len(scheduled_nurses), 
            advanced_nurse_count, count_of_high, count_of_low)
    if result_of_quantity_check[0] is True:
        return match_nurse_to_patient(scheduled_nurses, current_patients)
    else:
        print(f"Error: staff shortage. {result_of_quantity_check[1]}")
        
        
def get_nurses():
    """
    none -> dict (str:str)
    prompts user to enter names of scheduled nurse, and returns a dictionary
    """
    new_nurse_dict = {}
    print("""
Enter the names of the nurses for the next shift and enter 'x' when done
listing names. After entering the name, type 'a' for advanced nurses and
'b' for beginners.\n""")
    temp_name = ""
    while temp_name != "x":
        temp_name = input("Who is the next nurse? (type 'x' to quit)\n")
        if temp_name != "x":
            temp_skill_level = input(
                f"What is {temp_name}'s skill level? A or B?\n")
            new_nurse_dict.update({temp_name: temp_skill_level.upper()})
    return new_nurse_dict
            
            
def get_patients():
    """
    none -> dict (str:str)
    prompts user to enter names of current patients, and returns a dictionary
    """
    new_patient_dict = {}
    print("""
Enter the names of the patients that are currently on the unit and enter 'x'
when done listing names. After entering the name, type 'h' for high acuity
patients and 'l' for low acuity patients.\n""")
    temp_patient_name = ""
    while temp_patient_name != "x":
        temp_patient_name = input(
            "Who is the next patient? (type 'x' to quit)\n")
        if temp_patient_name != "x":
            temp_acuity_level = input(
                f"What is {temp_patient_name}'s acuity level? H or L?\n")
            new_patient_dict.update(
                {temp_patient_name: temp_acuity_level.upper()})
    return new_patient_dict

    
if __name__ == "__main__":
    print(check_then_match(get_nurses(), get_patients()))