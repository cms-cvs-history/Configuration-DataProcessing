#!/usr/bin/env python
"""
_Cosmics_

Test for Cosmics Scenario implementation

"""


import unittest
import FWCore.ParameterSet.Config as cms
from Configuration.DataProcessing.GetScenario import getScenario



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

        proc = cms.Process("RECO")
        proc.writeReco = cms.OutputModule("writeReco")
        
        
        scenario = getScenario("Cosmics")
        try:
            scenario.promptReco(proc, proc.writeReco)
        except Exception, ex:
            msg = "Failed to create Prompt Reco configuration\n"
            msg += "for Cosmics Scenario\n"
            msg += str(ex)
            self.fail(msg)

    def testDQMHarvesting(self):
        """test dqmHarvesting  method"""


        scenario = getScenario("Cosmics")

        try:
            scenario.dqmHarvesting("dataset", 123456, "GLOBALTAG::ALL",
                                   "file1", "file2", "file3")
        except Exception, ex:
            msg = "Failed creating DQM Harvesting configuration "
            msg += "for Cosmics scenario:\n"
            msg += str(ex)
            self.fail(msg)

    def testExpressProcessing(self):
        """ test expressProcessing method"""
        scenario = getScenario("Cosmics")

        try:
            scenario.expressProcessing()
        except Exception, ex:
            msg = "Error calling Cosmics.expressProcessing:\n"
            msg += str(ex)
            self.fail(msg)

            
    def testAlcaReco(self):
        """ test alcaReco method"""
        scenario = getScenario("Cosmics")
        try:
            scenario.alcaReco("ALCARECOStreamMuAlStandAloneCosmics")
        except Exception, ex:
            msg = "Error preparing Alca Reco configuration\n"
            msg += str(ex)
            self.fail(msg)
                              

    
if __name__ == '__main__':
    unittest.main()
