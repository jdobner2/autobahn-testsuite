###############################################################################
##
##  Copyright 2013 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

__all__ = ("TestRun",)


import random
from collections import deque

from twisted.python import log


class Testee:

   ATTRIBUTES = ['name', 'url', 'auth', 'debug']

   def __init__(self, **args):

      for attr in Testee.ATTRIBUTES:
         setattr(self, attr, None)

      self.load(args)


   def load(self, obj):
      for attr in obj.keys():
         if attr in Testee.ATTRIBUTES:
            setattr(self, attr, obj[attr])
         else:
            if self.debug:
               log.msg("Warning: skipping unknown testee attribute '%s'" % attr)



class TestRun:
   """
   A TestRun contains an ordered sequence of test case classes.
   A test runner instantiates tests from these test case classes.
   The test case classes must derive from WampCase or Case.
   """

   def __init__(self, testee, cases, randomize = False):
      self.testee = testee
      _cases = cases[:]
      if randomize:
         random.shuffle(_cases)
      _cases.reverse()
      self._cases = deque(_cases)

   def next(self):
      try:
         return self._cases.pop()
      except IndexError:
         return None

   def remaining(self):
      return len(self._cases)