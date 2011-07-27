###############################################################################
##
##  Copyright 2011 Tavendo GmbH
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

from setuptools import setup

setup (
   name = 'autobahn',
   version = '0.1',
   description = 'Autobahn - asynchronous RPC/PubSub over JSON/WebSockets.',
   author = 'Tavendo GmbH',
   url = 'http://www.tavendo.de/autobahn',
   platforms = ('Any',),
   install_requires = ['Twisted>=10.1'],
   packages = ['autobahn'],
   zip_safe = False
)
