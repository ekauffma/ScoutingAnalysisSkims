import FWCore.ParameterSet.Config as cms

CICADANtuplizer = cms.EDAnalyzer(
    'CICADANtuplizer',
    caloLayer1CICADAScore = cms.InputTag("caloLayer1Digis", "CICADAScore"),
)
