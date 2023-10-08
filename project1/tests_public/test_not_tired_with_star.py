import gamify as gamify
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility


class TestNotTiredRunningStarBasic(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestNotTiredRunningStarBasic, self).__init__(*args, **kwargs)
        self.start_health = 0
        self.start_hedons = 0
        self.star_kind = None
    
    def prepare(self):
        gamify.initialize()
        gamify.offer_star("running")
        self.star_kind = 'r'

    def setUp(self):
        self.prepare()

    @weight(1)
    @visibility("after_due_date") 
    def test_health_points_when_running_1min(self):
        gamify.perform_activity("running",1)
        self.assertEqual(gamify.get_cur_health(), self.start_health + 3)

    @weight(1)
    @visibility("after_due_date")         
    def test_health_points_when_carrying_1min(self):
        gamify.perform_activity("textbooks",1)
        self.assertEqual(gamify.get_cur_health(), self.start_health + 2)

    @weight(1)
    @visibility("after_due_date")         
    def test_hedon_points_when_running_1min(self):
        gamify.perform_activity('running',1)
        if self.star_kind == 'r':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+2+3)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+2)        
    @weight(1)
    @visibility("after_due_date")             
    def test_hedon_points_when_carrying_1min(self):
        gamify.perform_activity('textbooks',1)
        if self.star_kind == 'c':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+1+3)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+1)  

    @weight(1)
    @visibility("after_due_date")             
    def test_most_fun_act(self):
        if self.star_kind == 'r':
            self.assertEqual(gamify.most_fun_activity_minute(), 'running')
            print("p")
        elif self.star_kind == 'c':
                self.assertEqual(gamify.most_fun_activity_minute(), 'textbooks')
                print("t")

    @weight(1)
    @visibility("after_due_date") 
    def test_hedons_10min_run(self):
        gamify.perform_activity("running",10)
        if self.star_kind == 'r':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+20+30)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+20)

    @weight(1)
    @visibility("after_due_date") 
    def test_hedons_20min_carry(self):
        gamify.perform_activity("textbooks",20)
        if self.star_kind == 'c':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+20+3*10)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+20)
            
    @weight(1)
    @visibility("after_due_date") 
    def test_hedons_11min_run(self):
        gamify.perform_activity("running",11)
        if self.star_kind == 'r':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+18+30)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+18)

    @weight(1)
    @visibility("after_due_date") 
    def test_hedons_21min_carry(self):
        gamify.perform_activity("textbooks",21)
        if self.star_kind == 'c':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+19+10*3)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+19)

class TestNotTiredCarryingStarBasic(TestNotTiredRunningStarBasic):
    def prepare(self):
        gamify.initialize()
        gamify.offer_star("textbooks")
        self.star_kind = 'c'
        
if __name__ == '__main__':
    unittest.main()
