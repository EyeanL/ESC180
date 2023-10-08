import gamify as gamify
import unittest

from gradescope_utils.autograder_utils.decorators import weight, number, visibility


class TestTiredRunningStarBasic(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTiredRunningStarBasic, self).__init__(*args, **kwargs)
        self.start_health = 0
        self.start_hedons = 0
        self.long_run = False
        self.star_kind = None
    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        self.start_health += 3
        self.start_hedons += 2
        gamify.offer_star('running')
        self.star_kind = 'r'

    def setUp(self):
        self.prepare()

    @weight(1)
    @visibility("after_due_date")        
    def test_hedons_points_when_running_1min(self):
        gamify.perform_activity('running',1)
        if self.star_kind == 'r':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2+3)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2)

    @weight(1)
    @visibility("after_due_date")
    def test_hedons_points_when_running_11min(self):
        gamify.perform_activity('running',11)
        if self.star_kind == 'r':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2*11+30)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2*11)

    @weight(1)
    @visibility("after_due_date")        
    def test_hedons_points_when_carrying_1min(self):
        gamify.perform_activity('textbooks',1)
        if self.star_kind == 'c':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons -2+3)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2)

    @weight(1)
    @visibility("after_due_date")
    def test_hedons_points_when_carrying_11min(self):
        gamify.perform_activity('textbooks',11)
        if self.star_kind == 'c':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons -2*11+30)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2*11)

    @weight(1)
    @visibility("after_due_date")
    def test_hedons_points_rest_run(self):
        gamify.perform_activity('resting',1)
        gamify.perform_activity('running',1)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons -2)
        
    @weight(1)
    @visibility("after_due_date")
    def test_hedons_points_rest_carry(self):
        gamify.perform_activity('resting',1)
        gamify.perform_activity('textbooks',1)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons -2)
    
    @weight(1)
    @visibility("after_due_date")
    def test_hedons_points_carrying_seq1(self):
        gamify.perform_activity('textbooks',1)
        gamify.perform_activity('textbooks',2)
        if self.star_kind == 'c':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2*3+3)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2*3)
            
    @weight(1)
    @visibility("after_due_date")
    def test_hedon_point_run_seq1(self):
        gamify.perform_activity('running',1)
        gamify.perform_activity('running',2)
        if self.star_kind == 'r':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2*3+3)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2*3)

    @weight(1)
    @visibility("after_due_date")
    def test_hedons_points_carrying_seq2(self):
        gamify.perform_activity('textbooks',1)
        gamify.perform_activity('textbooks',2)
        gamify.perform_activity('textbooks',2)
        if self.star_kind == 'c':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2*5+3)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2*5)
            

    @weight(1)
    @visibility("after_due_date")
    def test_hedon_point_run_seq2(self):
        gamify.perform_activity('running',1)
        gamify.perform_activity('resting',1)
        gamify.perform_activity('running',2)
        if self.star_kind == 'r':
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2*3+3)
        else:
            self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2*3)
        
    @weight(1)
    @visibility("after_due_date")
    def test_most_fun_act(self):
        if self.star_kind == 'r':
            self.assertEqual(gamify.most_fun_activity_minute(), 'running')
        elif self.star_kind == 'c':
            self.assertEqual(gamify.most_fun_activity_minute(), 'textbooks')

    @weight(1)
    @visibility("after_due_date")                
    def test_three_starts_in_2hrs_1(self):
        gamify.perform_activity("running",1)
        self.start_health += 3
        if self.star_kind == 'r':
            self.start_hedons += -2+3
        else:
            self.start_hedons += -2
            
        gamify.offer_star("textbooks")
        gamify.perform_activity("running",1)
        self.start_health += 3
        self.start_hedons += -2
        gamify.offer_star("textbooks")
        gamify.perform_activity("textbooks",1)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2)
        
    @weight(1)
    @visibility("after_due_date")
    def test_three_starts_in_2hrs_2(self):
        gamify.perform_activity("running",1)
        self.start_health += 3
        if self.star_kind == 'r':
            self.start_hedons += -2+3
        else:
            self.start_hedons += -2
            
        gamify.offer_star("textbooks")
        gamify.perform_activity("running",1)
        self.start_health += 3
        self.start_hedons += -2
        gamify.perform_activity("resting",110)
        gamify.offer_star("textbooks")
        gamify.perform_activity("textbooks",1)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2)
        

    @weight(1)
    @visibility("after_due_date")
    def test_three_starts_in_2hrs_3(self):
        gamify.perform_activity("running",1)
        self.start_health += 3
        if self.star_kind == 'r':
            self.start_hedons += -2+3
        else:
            self.start_hedons += -2
         
        gamify.perform_activity("resting",110)    
        gamify.offer_star("textbooks")
        gamify.perform_activity("running",1)
        self.start_health += 3
        self.start_hedons += -2
        gamify.perform_activity("resting",5)
        gamify.offer_star("textbooks")
        gamify.perform_activity("textbooks",1)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2)

    @weight(1)
    @visibility("after_due_date")
    def test_three_starts_in_2hrs_4(self):
        gamify.perform_activity("running",1)
        self.start_health += 3
        if self.star_kind == 'r':
            self.start_hedons += -2+3
        else:
            self.start_hedons += -2
         
        gamify.perform_activity("resting",110)    
        gamify.offer_star("textbooks")
        gamify.perform_activity("running",1)
        self.start_health += 3
        self.start_hedons += -2
        gamify.perform_activity("resting",9)
        gamify.offer_star("textbooks")
        gamify.perform_activity("textbooks",1)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+1)

        
class TestTiredCarryingStarBasic(TestTiredRunningStarBasic):
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity('running',1)
        gamify.offer_star("textbooks")
        self.star_kind = 'c'
        self.start_health = 3
        self.start_hedons = 2
        
if __name__ == '__main__':
    unittest.main()

