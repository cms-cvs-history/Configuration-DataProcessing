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


class CosmicsScenarioTest(unittest.TestCase):
    """
    unittest for cosmics scenario

    """

    def testA(self):
        """get the scenario"""

        try:
            scenario = getScenario("Cosmics")
        except Exception, ex:
            msg = "Failed to get Cosmics scenario\n"
            msg += str(ex)
            self.fail(msg)


    def testPromptReco(self):
        """test promptReco method"""

        
        
        scenario = getScenario("Cosmics")
        try:
            process = scenario.promptReco("GLOBALTAG::ALL", ['RECO'])
            writePSetFile("testPromptReco.py", process)
        except Exception, ex:
            msg = "Failed to create Prompt Reco configuration\n"
            msg += "for Cosmics Scenario\n"
            msg += str(ex)
            self.fail(msg)

        
        


    def testDQMHarvesting(self):
        """test dqmHarvesting  method"""


        scenario = getScenario("Cosmics")

        try:
            process = scenario.dqmHarvesting("dataset", 123456,
                                             "GLOBALTAG::ALL")
            
            writePSetFile("testDQMHarvesting.py", process)
        except Exception, ex:
            msg = "Failed creating DQM Harvesting configuration "
            msg += "for Cosmics scenario:\n"
            msg += str(ex)
            self.fail(msg)

    def testExpressProcessing(self):
        """ test expressProcessing method"""
        scenario = getScenario("Cosmics")

        try:
            process = scenario.expressProcessing("GLOBALTAG::ALL",
                                                 ['RECO', 'RAW'],
                                                 ['Dataset1'],)
            writePSetFile("testExpressProcessing.py", process)
        except Exception, ex:
            msg = "Error calling Cosmics.expressProcessing:\n"
            msg += str(ex)
            self.fail(msg)

        
            
            

            
    def testAlcaReco(self):
        """ test alcaReco method"""
        scenario = getScenario("Cosmics")
        try:
            process = scenario.alcaReco("ALCARECOStreamMuAlStandAloneCosmics")
            writePSetFile("testAlcaReco.py", process)
        except Exception, ex:
            msg = "Error preparing Alca Reco configuration\n"
            msg += str(ex)
            self.fail(msg)
                              

    
if __name__ == '__main__':
    unittest.main()
