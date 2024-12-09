import os
import datetime
from CRABClient.UserUtilities import config
config = config()

todaysDate = datetime.date.today().strftime('%Y%m%d')

config.General.requestName = f'ScoutingNano_TTbar_{todaysDate}'
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = '/afs/hep.wisc.edu/home/ekauffma/test-dir/crabWorkArea'

config.JobType.allowUndistributedCMSSW = True
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/ScoutingAnalysisSkims/python/scoutingnano_mc.py'
config.JobType.pluginName = 'Analysis'
config.JobType.maxMemoryMB = 5000

config.Data.inputDataset= '/TT_TuneCP5_13p6TeV_powheg-pythia8/ekauffma-CICADAAnalysis_ZeroBias_Skim_2024G_20241206-324e0bac8106cc6e12d258f344e69f7c/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 5500
config.Data.publication = True
config.Data.outputDatasetTag = f'ScoutingNano_TTbar_{todaysDate}'
config.Data.partialDataset = True

config.Site.storageSite = 'T2_US_Wisconsin'

