#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from apisix.runner.plugin.base import Base
from apisix.runner.http.request import Request
from apisix.runner.http.response import Response


class Example(Base):

    def __init__(self):
        super(Example, self).__init__(self.__class__.__name__)

    def filter(self, request: Request, response: Response):

        # Get plugin configuration information through `self.config`
        # print(self.config)

        # deny by query parameter
        # conf_args = self.config.get("args") or {}
        # req_args = request.args or {}
        #
        # if req_args.get("deny") == conf_args.get("deny"):
        #     response.status_code = 403
        #     self.stop()

        # deny by header parameter
        conf_headers = self.config.get("headers") or {}
        req_headers = request.headers or {}

        if req_headers.get("x-deny") == conf_headers.get("x-deny"):
            response.status_code = 403
            self.stop()
