#!/usr/bin/env python
"""
_Cosmics_

Test for Cosmics Scenario implementation

"""


import unittest
import FWCore.ParameterSet.Config as cms
from Configuration.DataProcessing.GetScenario import getScenario



def writePSetFile(name, process):
    """
    _writePSetFile_

    Util to dump the process to a file

    """
    handle = open(name, 'w')
    handle.write(process.dumpPython())
    handle.close()


class cosmicsScenarioTest(unittest.TestCase):
    """
    unittest for cosmics scenario

    """

    def testA(self):
        """get the scenario"""

        try:
            scenario = getScenario("cosmics")
        except Exception, ex:
            msg = "Failed to get cosmics scenario\n"
            msg += str(ex)
            self.fail(msg)


    def testPromptReco(self):
        """test promptReco method"""

        
        
        scenario = getScenario("cosmics")
        try:
            process = scenario.promptReco("GLOBALTAG::ALL", ['RECO'])
            writePSetFile("testPromptReco.py", process)
        except Exception, ex:
            msg = "Failed to create Prompt Reco configuration\n"
            msg += "for cosmics Scenario\n"
            msg += str(ex)
            self.fail(msg)

        
        


    def testDQMHarvesting(self):
        """test dqmHarvesting  method"""


        scenario = getScenario("cosmics")

        try:
            process = scenario.dqmHarvesting("dataset", 123456,
                                             "GLOBALTAG::ALL")
            
            writePSetFile("testDQMHarvesting.py", process)
        except Exception, ex:
            msg = "Failed creating DQM Harvesting configuration "
            msg += "for cosmics scenario:\n"
            msg += str(ex)
            self.fail(msg)

    def testExpressProcessing(self):
        """ test expressProcessing method"""
        scenario = getScenario("cosmics")

        try:
            process = scenario.expressProcessing("GLOBALTAG::ALL",
                                                 ['RECO', 'RAW'],
                                                 ['Dataset1'],)
            writePSetFile("testExpressProcessing.py", process)
        except Exception, ex:
            msg = "Error calling cosmics.expressProcessing:\n"
            msg += str(ex)
            self.fail(msg)

        
            
            

            
    def testAlcaReco(self):
        """ test alcaReco method"""
        scenario = getScenario("cosmics")
        try:
            process = scenario.alcaReco("ALCARECOStreamMuAlStandAloneCosmics")
            writePSetFile("testAlcaReco.py", process)
        except Exception, ex:
            msg = "Error preparing Alca Reco configuration\n"
            msg += str(ex)
            self.fail(msg)
                              

    
if __name__ == '__main__':
    unittest.main()