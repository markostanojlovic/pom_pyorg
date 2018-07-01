import unittest
from HomePageTCs import TestPyOrgHomePage
from AboutPageTCs import TestPyOrgAboutPage

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPyOrgHomePage('test_TC001_py3_doc_butt_after_doc_hover'))
    suite.addTest(TestPyOrgHomePage('test_TC002_pass_mismatch_message'))
    suite.addTest(TestPyOrgAboutPage('test_TC003_verify_upcoming_events_section_present'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    runner.run (test_suite)
