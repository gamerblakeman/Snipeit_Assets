from modulefinder import test
import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

tester = None
serial = None

tests = []
class flukeTest:
  def __init__(self, outdata = []):
    self.outdata = outdata
  def parse(self, fielename):
    with open(fielename) as t:
      self.ls = t.readlines()
      self.tester = re.findall("MODEL *(.*) *?", self.ls[1])[0]
      self.serial = re.findall("SN *(.*) *?", self.ls[2])[0]
      self.testdata = ''.join(self.ls[4:-2])
      self.testdata = self.testdata.split('\n\n')
      print(f"Found {len(self.testdata)} tests.")
      for self.test in self.testdata:
        self.test = [l.rstrip() for l in self.test.split('\n')]
        try:
          self.data = self.parsetest(self.test)
          
        except Exception as e:
          print("---")
          print("ERROR: malformed entry. Unable to parse test.")
          print(e)
          print(self.test)
        if self.data:
          #print(self.data)
          self.outdata.append(self.data)
    return self.outdata
  def parsetest(self, test, obj = None):
    #print(obj)
    if obj == None:
      obj = {
        'tests': {}
      }
    #print(len(test))
    #print(test)
    while len(test) > 0:
      # handle each possible data block:
      if 'TEST NUMBER' in test[0]:
        obj['testnum'] = re.findall(r'TEST NUMBER\s+(\d+)', test[0])[0]
        test = test[1:]
      
      elif 'DATE' in test[0]:
        obj['date'] = re.findall(r'DATE\s+(\d\d-\w\w\w-\d\d)', test[0])[0]
        test = test[1:]
      
      elif 'APP NO' in test[0]:
        obj['appno'] = re.findall(r'APP NO +([a-zA-Z0-9]+)\s*', test[0])[0]
        test = test[1:]
      
      elif 'TEST MODE' in test[0]:
        obj['testmode'] = re.findall(r'TEST MODE *(.+) *', test[0])[0]
        test = test[1:]
      
      elif 'SITE' in test[0]:
        obj['site'] = re.findall(r'SITE *(.*)', test[0])[0]
        obj['site1'] = re.findall(r'SITE1 *(.*)', test[1])[0]
        obj['site2'] = re.findall(r'SITE2 *(.*)', test[2])[0]
        test = test[3:]
      
      elif 'USER' in test[0]:
        obj['user'] = re.findall(r'USER *(.*)', test[0])[0]
        test = test[1:]
      
      elif 'VISUAL CHECK' in test[0]:
        obj['visual'] = re.findall(r'VISUAL CHECK *([PF])', test[0])[0]
        test = test[1:]

      elif 'LEAD CONTINUITY' in test[0]:
        t = {}
        t['continuity'] = re.findall(r'LEAD CONTINUITY *([PF])', test[0])[0]
        ex = re.findall(r'EARTH *(.*?) *([PF])', test[1])
        t['earth'] = ex[0][0]
        t['earthpass'] = ex[0][1]
        t['earthlimit'] = re.findall(r'LIMIT *(.*)', test[2])[0]
        obj['tests']['iectest'] = t
        test = test[3:]
      
      elif 'INS' in test[0]:
        # for some reason my tester adds an extra entry for insulation tests
        if 'INS 1' in test[1]:
          obj['tests']['ins1'] = {'testvoltage': re.findall(r'INS *(.*)', test[1])[0]}
        elif 'INS 2' in test[1]:
          obj['tests']['ins2'] = {'testvoltage': re.findall(r'INS *(.*)', test[1])[0]}
        test = test[1:]

      elif 'INS 1' in test[0]:
        #print("Parsing INS 1")
        ex = re.findall(r'INS 1 *(.*?) *([PF])', test[0])
        t = {}
        t['res'] = ex[0][0]
        t['pass'] = ex[0][1]
        t['limit'] = re.findall(r'LIMIT *(.*)', test[1])[0]
        if 'ins1' in obj['tests']:
          t['testvoltage'] = obj['tests']['ins1']['testvoltage']
        obj['tests']['ins1'] = t
        #print(obj)
        test = test[2:]

      elif 'INS 2' in test[0]:
        ex = re.findall(r'INS 2 *(.*?) *([PF])', test[0])
        t = {}
        t['res'] = ex[0][0]
        t['pass'] = ex[0][1]
        t['limit'] = re.findall(r'LIMIT *(.*)', test[1])[0]
        if 'ins2' in obj['tests']:
          t['testvoltage'] = obj['tests']['ins2']['testvoltage']
        obj['tests']['ins2'] = t
        test = test[2:]
      
      elif 'PN CONTINUITY' in test[0]:
        if 'TOUCH' in test[1]:
          ex = re.findall(r'TOUCH *(.*?) *([PF])', test[1])
          t = {}
          t['current'] = ex[0][0]
          t['pass'] = ex[0][1]
          t['limit'] = re.findall(r'LIMIT *(.*)', test[2])[0]
          t['pncontinuity'] = re.findall(r'PN CONTINUITY *([PF])', test[0])[0]
          obj['tests']['touch'] = t
          test = test[3:]
        elif 'LOAD' in test[1]:
          ex = re.findall(r'LOAD *(.*?) *([PF])', test[1])
          t = {}
          t['load'] = ex[0][0]
          t['pass'] = ex[0][1]
          t['limit'] = re.findall(r'LIMIT *(.*)', test[2])[0]
          t['pncontinuity'] = re.findall(r'PN CONTINUITY *([PF])', test[0])[0]
          obj['tests']['load'] =  t
          test = test[3:]

      elif 'CURRENT' in test[0]:
        ex = re.findall(r'CURRENT *(.*?) *([PF])', test[0])
        t = {}
        t['current'] = ex[0][0]
        t['pass'] = ex[0][1]
        t['limit'] = re.findall(r'LIMIT *(.*)', test[1])[0]
        obj['tests']['current'] = t
        test = test[2:]
      
      elif 'LKGE' in test[0]:
        ex = re.findall(r'LKGE *(.*?) *([PF])', test[0])
        t = {}
        t['current'] = ex[0][0]
        t['pass'] = ex[0][1]
        t['limit'] = re.findall(r'LIMIT *(.*)', test[1])[0]
        obj['tests']['leakage'] = t
        test = test[2:]
      
      elif 'BOND RANGE' in test[0]:
        t = {}
        t['testcurrent'] = re.findall(r'BOND RANGE *(.*)', test[0])[0]
        ex = re.findall(r'EARTH *(.*?) *([PF])', test[1])
        t['resistance'] = ex[0][0]
        t['pass'] = ex[0][1]
        t['limit'] = re.findall(r'LIMIT *(.*)', test[2])[0]
        obj['tests']['earthbond'] = t
        test = test[3:]
      
      elif 'SUBST 1' in test[0]:
        ex = re.findall(r'SUBST 1 *(.*?) *([PF])', test[0])
        t = {}
        t['current'] = ex[0][0]
        t['pass'] = ex[0][1]
        t['limit'] = re.findall(r'LIMIT *(.*)', test[1])[0]
        obj['tests']['subst1'] = t
        test = test[2:]
      
      elif 'SUBST 2' in test[0]:
        ex = re.findall(r'SUBST 2 *(.*?) *([PF])', test[0])
        t = {}
        t['current'] = ex[0][0]
        t['pass'] = ex[0][1]
        t['limit'] = re.findall(r'LIMIT *(.*)', test[1])[0]
        obj['tests']['subst2'] = t
        test = test[2:]
      
      elif 'PROBE PELV' in test[0]:
        ex = re.findall(r'PROBE PELV *([PF])', test[0])
        t = {}
        t['pass'] = ex[0]
        t['currentlimit'] = re.findall(r'LIMIT *(.*)', test[1])[0]
        obj['tests']['probepelv'] = t
        test = test[2:]

      elif 'LOC1' in test[0]:
        obj['loc'] = re.findall(r'LOC1 *(.*)', test[0])[0] + re.findall(r'LOC2 *(.*)', test[1])[0]
        test = test[2:]
      
      elif 'DES1' in test[0]:
        obj['des1'] = re.findall(r'DES1 *(.*)', test[0])[0]
        obj['des2'] = re.findall(r'DES2 *(.*)', test[1])[0]
        obj['des3'] = re.findall(r'DES3 *(.*)', test[2])[0]
        test = test[3:]
      
      elif 'TEXT1' in test[0]:
        obj['note'] = re.findall(r'TEXT1 *(.*)', test[0])[0] + re.findall(r'TEXT2 *(.*)', test[1])[0]
        test = test[2:]

      else:
        # unknown entry type, skip this line?
        #print("-----")
        #print("Unknown entry type, skipping line:")
        
        #print(test)
        #print(obj)
        test = test[1:]
    if len(test) == 0:
      #print("Returing obj")
      return obj



