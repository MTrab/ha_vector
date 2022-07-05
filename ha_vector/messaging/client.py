# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: skip-file

"""
Protobuf messages exposed to the Vector Python SDK.
"""
import sys
import inspect

from ha_vector.messaging.alexa_pb2_grpc import *
from ha_vector.messaging.behavior_pb2_grpc import *
from ha_vector.messaging.cube_pb2_grpc import *
from ha_vector.messaging.messages_pb2_grpc import *
from ha_vector.messaging.nav_map_pb2_grpc import *
from ha_vector.messaging.response_status_pb2_grpc import *
from ha_vector.messaging.settings_pb2_grpc import *
from ha_vector.messaging.shared_pb2_grpc import *
from ha_vector.messaging.external_interface_pb2_grpc import *

__all__ = [obj.__name__ for _, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isclass(obj)]
