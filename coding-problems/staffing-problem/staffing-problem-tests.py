'''
Title: ICU Nurse Staffing Problem Tests
Description: Tests of functions in staffing solution source code
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


import unittest
import staffing_problem_solution as sps

class TestCheckNurseQuantity(unittest.TestCase):
    
    def test_zero_nurses(self):
        self.assertEqual(
            sps.check_nurse_quantity(0, 0, 2, 1), 
            (False, "At least two nurses are needed at all times."))
        self.assertEqual(
            sps.check_nurse_quantity(1, 1, 0, 0), 
            (False, "At least two nurses are needed at all times."))
        
        
    def test_insufficient_advanced(self):
        self.assertEqual(
            sps.check_nurse_quantity(5, 1, 2, 1), 
            (False, "There are not enough nurses for the patient acuity."))
        self.assertEqual(
            sps.check_nurse_quantity(4, 2, 4, 0), 
            (False, "There are not enough nurses for the patient acuity."))
        
        
    def test_too_many_patients(self):
        self.assertEqual(
            sps.check_nurse_quantity(2, 2, 0, 5), 
            (False, "There are not enough nurses for the patient acuity."))
        self.assertEqual(
            sps.check_nurse_quantity(5, 5, 0, 15), 
            (False, "There are not enough nurses for the patient acuity."))
        
    
    def test_sufficient_staffing(self):
        self.assertEqual(sps.check_nurse_quantity(10, 5, 5, 10), (True,))
        self.assertEqual(sps.check_nurse_quantity(8, 0, 0, 15), (True,))
        

class TestMatchNurses(unittest.TestCase):
    
    def test_extra_assign_slot(self):
        self.assertEqual(
            sps.match_nurse_to_patient(
                {"Sara": "A", "Tom": "A"}, {"K.A.": "H", "A.M.": "L"}), 
                {"Sara": ("K.A.",), "Tom": ("A.M.",)})
        self.assertEqual(
            sps.match_nurse_to_patient(
                {"Sara": "A", "Tom": "A", "Kiara": "L"}, 
                {"K.A.": "H", "A.M.": "L", "T.T.": "L", "N.R.": "L" }), 
                {"Sara": ("K.A.",), "Tom": ("A.M.", "T.T."), "Kiara": ("N.R.",)})


    def test_exact_amount(self):
        self.assertEqual(
            sps.match_nurse_to_patient(
                {"Sara": "A", "Tom": "A", "Kiara": "L"}, 
                {"K.A.": "H", "A.M.": "L", "T.T.": "L", "N.R.": "L", "F.Y.": "L"}), 
                {"Sara": ("K.A.",), "Tom": ("A.M.", "T.T."), "Kiara": ("N.R.", "F.Y.")})
    
    
    def test_no_patients(self):
        self.assertEqual(
            sps.match_nurse_to_patient(
                {"Sara": "A", "Tom": "A", "Kiara": "L"}, {}), 
                {"Sara": (), "Tom": (), "Kiara": ()})
    
    
class TestCheckAndMatch(unittest.TestCase):
    
    def test_full_assignment(self):
        self.assertEqual(sps.check_then_match(
            {"Helen": "A", "Troy": "B", "Charles": "A", "Dixson": "B", 
             "Shawn": "B", "Hector": "B", "Xena": "A"},
            {"A.B.": "H", "C.D.": "L", "E.F.": "H", "G.H.": "L", "I.J.": "L", 
             "K.L.": "L", "M.N.": "L", "O.P.": "L", "Q.R.": "H"}),
            {"Helen": ("A.B.",), "Charles": ("E.F.",), "Xena": ("Q.R.",),
             "Troy": ("C.D.", "G.H."), "Dixson": ("I.J.", "K.L."), "Shawn": ("M.N.", "O.P."),
             "Hector": ()})

if __name__ == "__main__":
    unittest.main()