import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.nano_eras_cff import *

from  PhysicsTools.NanoAOD.common_cff import *

cicadaTable = cms.EDProducer(
    "SimpleCandidateFlatTableProducer",
    src = cms.InputTag("caloLayer1Digis","CICADAScore"),
    cut = cms.string(""),
    name = cms.string("CICADA"),
    singleton = cms.bool(True), # the number of entries is not variable
    extension = cms.bool(False), # this is the main table for cicada
    variables = cms.PSet(
        CICADAScore = Var("", float, doc="emulated CICADA score"),
    )
)
