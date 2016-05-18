# Copyright 2016 Network Intelligence Research Center, 
# Beijing University of Posts and Telecommunications
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import ConfigParser

logging.basicConfig(filename='/tmp/agent.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')
Log = logging.getLogger(__name__)

def getApiServer():
	config = ConfigParser.RawConfigParser()
	config.read('agent.conf')
	try:
		api_server = config.get('DEFAULT','api_server')
		Log.info(api_server)
		return api_server
	except:
		Log.debug('No api_server')
		return None

