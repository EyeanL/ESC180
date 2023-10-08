import gamify as gamify
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, number


class TestBasicCases(unittest.TestCase):

    def setUp(self):
        gamify.initialize()
    
    @weight(1)
    @visibility("visible")
    def test_function_names(self):
        gamify.get_cur_hedons()
        gamify.get_cur_health()
        gamify.offer_star("running")
        gamify.perform_activity("running", 10)
        gamify.star_can_be_taken("running")
        gamify.most_fun_activity_minute()
 
	
    
    @weight(1)
    @visibility("visible")    
    def test1(self):
        gamify.perform_activity("running", 30)
        self.assertEqual(gamify.get_cur_health(), 90)
    
    @weight(1)
    @visibility("visible")        
    def test2(self):
        gamify.perform_activity("running", 30)
        self.assertEqual(gamify.get_cur_hedons(), -20)

    @weight(1)
    @visibility("visible")        
    def test3(self):
        gamify.perform_activity("running", 30)
        self.assertEqual(gamify.most_fun_activity_minute(),"resting")

    @weight(1)
    @visibility("after_due_date")                
    def test4(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        self.assertEqual(gamify.most_fun_activity_minute(),"running")
    
    @weight(1)
    @visibility("after_due_date")                
    def test5(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        self.assertEqual(gamify.get_cur_health(), 150)

    
    @weight(1)
    @visibility("after_due_date")        
    def test6(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        self.assertEqual(gamify.get_cur_hedons(), -80)        
    
    @weight(1)
    @visibility("after_due_date")            
    def test7(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        gamify.offer_star("running")
        gamify.perform_activity("running", 20)
        self.assertEqual(gamify.get_cur_health(), 210)

    @weight(1)
    @visibility("after_due_date")        
    def test8(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        gamify.offer_star("running")
        gamify.perform_activity("running", 20)
        self.assertEqual(gamify.get_cur_hedons(), -90)

    @weight(1)
    @visibility("after_due_date")        
    def test9(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        gamify.offer_star("running")
        gamify.perform_activity("running", 20)
        gamify.perform_activity("running", 170)
        self.assertEqual(gamify.get_cur_health(), 700)

    @weight(1)
    @visibility("after_due_date")        
    def test10(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        gamify.offer_star("running")
        gamify.perform_activity("running", 20)
        gamify.perform_activity("running", 170)
        self.assertEqual(gamify.get_cur_hedons(), -430)
    
if __name__ == '__main__':
    unittest.main()
