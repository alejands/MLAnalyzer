import os
from glob import glob
import re
import argparse

parser = argparse.ArgumentParser(description='Run RHAnalyzer')
parser.add_argument('-d','--decay', required=True, help='Decay:Single*Pt50',type=str)
args = parser.parse_args()

eosDir='/eos/uscms/store/user/mba2012'
#eosDir='/eos/cms/store/user/mandrews'
xrootd='root://cmsxrootd.fnal.gov' # FNAL
#xrootd='root://eoscms.cern.ch' # CERN
#decay='%s_FEVTDEBUG'%args.decay
decay=args.decay

cfg='RecHitAnalyzer/python/ConfFile_cfg.py'
#inputFiles_ = ['file:%s'%path for path in glob('%s/FEVTDEBUG/%s/*/*/step*root'%(eosDir,decay))]
#inputFiles_ = ['file:%s'%path for path in glob('%s/AODSIM/%s/*/*/step*root'%(eosDir,decay))]
inputFiles_ = ['%s/%s'%(xrootd,path) for path in glob('%s/AODSIM/%s/*/*/step*root'%(eosDir,decay))]

listname = 'list_%s.txt'%decay
with open(listname, 'w') as list_file:
    for inputFile in inputFiles_:
        list_file.write("%s\n" % inputFile)

maxEvents_=-1
skipEvents_=0

decay=decay.replace('_AODSIM','')
#cmd="cmsRun %s inputFiles=%s maxEvents=%d skipEvents=%d"%(cfg,inputFiles_,maxEvents_,skipEvents_)
cmd="cmsRun %s inputFiles_load=%s maxEvents=%d skipEvents=%d outputFile=%s/IMGs/%s_IMG.root"%(cfg,listname,maxEvents_,skipEvents_,eosDir,decay)
#print '%s'%cmd
os.system(cmd)

#os.system('mv cEB*.eps %s/'%(inputTag))
