import gamify as gamify
import unittest

from gradescope_utils.autograder_utils.decorators import weight, number, visibility


class TestTiredBasic(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTiredBasic, self).__init__(*args, **kwargs)
        self.start_health = 0
        self.start_hedons = 0
        self.long_run = False
    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        self.start_health += 3
        self.start_hedons += 2

    def setUp(self):
        self.prepare()

    @weight(1)
    @visibility("after_due_date")        
    def test_health_points_when_running_1min(self):
        if not self.long_run:
            gamify.perform_activity("running",1)
            self.assertEqual(gamify.get_cur_health(), self.start_health + 3)
        else:
            gamify.perform_activity("running",1)
            self.assertEqual(gamify.get_cur_health(), self.start_health + 1)
            
    @weight(1)
    @visibility("after_due_date")                
    def test_health_points_when_carrying_1min(self):
        gamify.perform_activity("textbooks",1)
        self.assertEqual(gamify.get_cur_health(), self.start_health + 2)

    @weight(1)
    @visibility("after_due_date")                
    def test_hedons_points_when_running_1min(self):
        gamify.perform_activity('running',1)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons-2)

    @weight(1)
    @visibility("after_due_date")                
    def test_hedons_points_when_carrying_1min(self):
        gamify.perform_activity('textbooks',1)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons -2)

    @weight(1)
    @visibility("after_due_date")                
    def test_health_points_run_seq_not_long(self):
        gamify.perform_activity('resting',1)
        gamify.perform_activity('running',1)
        gamify.perform_activity('running',2)
        gamify.perform_activity('running',3)
        gamify.perform_activity('running',4)
        self.assertEqual(gamify.get_cur_health(), self.start_health + 3*10)

    @weight(1)
    @visibility("after_due_date")            
    def test_health_points_carrying_seq_not_long(self):
        gamify.perform_activity('resting',1)
        gamify.perform_activity('textbooks',1)
        gamify.perform_activity('textbooks',2)
        gamify.perform_activity('textbooks',3)
        gamify.perform_activity('textbooks',4)
        self.assertEqual(gamify.get_cur_health(), self.start_health + 2*10)

    @weight(1)
    @visibility("after_due_date")        
    def test_hedons_points_run_seq_not_long(self):
        gamify.perform_activity('resting',1)
        gamify.perform_activity('running',1)
        gamify.perform_activity('running',2)
        gamify.perform_activity('running',3)
        gamify.perform_activity('running',4)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons -2*10)

    @weight(1)
    @visibility("after_due_date")            
    def test_hedons_points_carrying_seq_not_long(self):
        gamify.perform_activity('resting',1)
        gamify.perform_activity('textbooks',1)
        gamify.perform_activity('textbooks',2)
        gamify.perform_activity('textbooks',3)
        gamify.perform_activity('textbooks',4)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons -2*10)
        
    @weight(1)
    @visibility("after_due_date")        
    def test_health_point_run_seq_long1(self):
        gamify.perform_activity('resting',1)
        gamify.perform_activity('running',100)
        gamify.perform_activity('running',100)
        self.assertEqual(gamify.get_cur_health(), self.start_health + 3*180+20)

    @weight(1)
    @visibility("after_due_date")        
    def test_hedon_point_run_seq_long1(self):
        gamify.perform_activity('resting',1)
        gamify.perform_activity('running',100)
        gamify.perform_activity('running',100)
        self.assertEqual(gamify.get_cur_hedons(), self.start_hedons - 2*200)
    
    @weight(1)
    @visibility("after_due_date")        
    def test_health_point_run_seq_long2(self):
        gamify.perform_activity('resting',1)
        gamify.perform_activity('running',100)
        gamify.perform_activity('running',100)
        gamify.perform_activity('resting',1)
        gamify.perform_activity('running',100)
        self.assertEqual(gamify.get_cur_health(), self.start_health + 280*3+20)

    @weight(1)
    @visibility("after_due_date")        
    def test_health_point_run_seq_long3(self):
        gamify.perform_activity('resting',1)
        gamify.perform_activity('running',100)
        gamify.perform_activity('running',100)
        gamify.perform_activity('running',200)
        self.assertEqual(gamify.get_cur_health(), self.start_health + 3*180 + 220)

    @weight(1)
    @visibility("after_due_date")        
    def test_health_point_long_run(self):
        gamify.perform_activity('resting',1)
        gamify.perform_activity('running',190)
        self.assertEqual(gamify.get_cur_health(), self.start_health + 3*180+10)

    @weight(1)
    @visibility("after_due_date")                
    def test_most_fun_act(self):
        self.assertEqual(gamify.most_fun_activity_minute(), 'resting')

class TestSimpleTired(TestTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",170)
        self.start_health = 3*170
        self.start_hedons = 20 + -2*160    

class TestTiredRestGap(TestTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",170)
        gamify.perform_activity("resting",118)
        self.start_health = 3*170
        self.start_hedons = 20 - 2*160  

class TestTiredRestGap2(TestTiredBasic):
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        gamify.perform_activity("resting",118)
        self.start_health = 3
        self.start_hedons = 2

class TestTiredRestGapEasy(TestTiredBasic):
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        gamify.perform_activity("resting",1)
        self.start_health = 3
        self.start_hedons = 2

class TestTiredRestGapEasy(TestTiredBasic):
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",1)
        gamify.perform_activity("resting",1)
        self.start_health = 3
        self.start_hedons = 2

class TestCarryingStarTired1(TestTiredBasic):
    def prepare(self):
        gamify.initialize()
        gamify.offer_star("textbooks")
        gamify.perform_activity("textbooks",1)
        self.start_health = 2
        self.start_hedons = 1+3

class TestCarryingStarTired2(TestTiredBasic):
    def prepare(self):
        gamify.initialize()
        gamify.offer_star("textbooks")
        gamify.perform_activity("running",1)
        self.start_health = 3
        self.start_hedons = 2

class TestRunningStarTired1(TestTiredBasic):
    def prepare(self):
        gamify.initialize()
        gamify.offer_star("running")
        gamify.perform_activity("running",1)
        self.start_health = 3
        self.start_hedons = 2+3

class TestRunningStarTired2(TestTiredBasic):
    def prepare(self):
        gamify.initialize()
        gamify.offer_star("running")
        gamify.perform_activity("textbooks",1)
        self.start_health = 2
        self.start_hedons = 1

class TestSimpleTiredRunningStarTired1(TestTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",170)
        self.start_health = 3*170
        self.start_hedons = 20 + -2*160            
        gamify.offer_star("running")
        gamify.perform_activity("running",1)
        self.start_hedons += (-2+3)*1
        self.start_health += 3
        
class TestSimpleTiredRunningStarTired2(TestTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",170)
        self.start_health = 3*170
        self.start_hedons = 20 + -2*160            
        gamify.offer_star("running")
        gamify.perform_activity("textbooks",1)
        self.start_hedons -= 2 #(-2)*1
        self.start_health += 2

class TestSimpleTiredCarryingStarTired1(TestTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",170)
        self.start_health = 3*170
        self.start_hedons = 20 + -2*160            
        gamify.offer_star("textbooks")
        gamify.perform_activity("textbooks",1)
        self.start_hedons += (-2+3)*1
        self.start_health += 2
        
class TestSimpleTiredCarryingStarTired2(TestTiredBasic):    
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",170)
        self.start_health = 3*170
        self.start_hedons = 20 + -2*160            
        gamify.offer_star("textbooks")
        gamify.perform_activity("running",1)
        self.start_hedons += (-2)*1
        self.start_health += 3
        
class TestLongRunningStarTired(TestTiredBasic):
    def prepare(self):
        gamify.initialize()
        gamify.perform_activity("running",180)
        self.start_health += 3*180
        self.start_hedons += 20-170*2
        self.long_run = True

if __name__ == '__main__':
    unittest.main()
