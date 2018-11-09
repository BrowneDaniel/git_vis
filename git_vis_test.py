import git_vis
import unittest

class git_vis_test(unittest.TestCase):

    def test_bad_pass(self):
        test = git_vis.get_login_direct("bad", "login")
        self.assertTrue(test == "prompt user to retry login")
