import gamify as gamify
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility


class TestNotTiredBasic(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestNotTiredBasic, self).__init__(*args, **kwargs)
        self.start_health = 0
        self.start_hedons = 0
    
    def prepare(self):
        gamify.initialize()

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
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+2)
    @weight(1)
    @visibility("after_due_date")         
    def test_hedon_points_when_carrying_1min(self):
        gamify.perform_activity('textbooks',1)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+1)
    @weight(1)
    @visibility("after_due_date")         
    def test_most_fun_act(self):
        self.assertEqual(gamify.most_fun_activity_minute(), 'running')

    @weight(1)
    @visibility("after_due_date")     
    def test_hedons_10min_run(self):
        gamify.perform_activity("running",10)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+20)    

    @weight(1)
    @visibility("after_due_date") 
    def test_hedons_20min_carry(self):
        gamify.perform_activity("textbooks",20)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+20)

    @weight(1)
    @visibility("after_due_date") 
    def test_hedons_11min_run(self):
        gamify.perform_activity("running",11)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+18)

    @weight(1)
    @visibility("after_due_date") 
    def test_hedons_21min_carry(self):
        gamify.perform_activity("textbooks",21)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons+19)
        
    @weight(1)
    @visibility("after_due_date") 
    def test_health_long_run1(self):
        gamify.perform_activity("running",180)
        self.assertEqual(gamify.get_cur_health(), self.start_health + 3*180)
        
    @weight(1)
    @visibility("after_due_date") 
    def test_health_long_run2(self):
        gamify.perform_activity("running",190)
        self.assertEqual(gamify.get_cur_health(), self.start_health + 3*180+10)

    @weight(1)
    @visibility("after_due_date") 
    def test_hedon_long_run1(self):
        gamify.perform_activity("running",180)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons + 20-2*170)
        
    @weight(1)
    @visibility("after_due_date") 
    def test_hedon_long_run2(self):
        gamify.perform_activity("running",190)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons + 20-2*180)


class TestNotTiredAfterRest1(TestNotTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        gamify.perform_activity("resting",240)
        self.start_health = 3
        self.start_hedons = 2

class TestNotTiredAfterRest2(TestNotTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        gamify.perform_activity("resting",100)
        gamify.perform_activity("resting",140)
        self.start_health = 3
        self.start_hedons = 2
    
class TestNotTiredAfterRest2(TestNotTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        gamify.perform_activity("resting",100)
        gamify.perform_activity("resting",140)
        self.start_health = 3
        self.start_hedons = 2

class TestTiredRunningStarRest1(TestNotTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        gamify.offer_star("running")
        gamify.perform_activity("running",1)
        gamify.perform_activity("resting",240)
        self.start_health = 6
        self.start_hedons = 2 + 1

class TestTiredRunningStarRest2(TestNotTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        gamify.offer_star("running")
        gamify.perform_activity("resting",240)
        self.start_health = 3
        self.start_hedons = 2

class TestTiredCarryingStarRest1(TestNotTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        gamify.offer_star("textbooks")
        gamify.perform_activity("textbooks",1)
        gamify.perform_activity("resting",240)
        self.start_health = 3+2
        self.start_hedons = 2 + (3-2)

class TestTiredCarryingStarRest2(TestNotTiredBasic):  
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        gamify.offer_star("textbooks")
        gamify.perform_activity("resting",240)
        self.start_health = 3
        self.start_hedons = 2

if __name__ == '__main__':
    unittest.main()
