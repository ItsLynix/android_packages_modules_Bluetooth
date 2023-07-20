# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Security grpc interface."""

from typing import AsyncGenerator
from typing import AsyncIterator

from google.protobuf import empty_pb2
from google.protobuf import wrappers_pb2
import grpc
from pandora import security_pb2
from pandora import security_grpc_aio


class SecurityService(security_grpc_aio.SecurityServicer):
    """Service to trigger Bluetooth Host security pairing procedures.

    This class implements the Pandora bluetooth test interfaces,
    where the meta class definition is automatically generated by the protobuf.
    The interface definition can be found in:
    https://cs.android.com/android/platform/superproject/+/main:external
    /pandora/bt-test-interfaces/pandora/security.proto
    """

    async def OnPairing(self, request: AsyncIterator[security_pb2.PairingEventAnswer],
                        context: grpc.ServicerContext) -> AsyncGenerator[security_pb2.PairingEvent, None]:
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)  # type: ignore
        context.set_details("Method not implemented!")  # type: ignore
        raise NotImplementedError("Method not implemented!")
        yield security_pb2.PairingEvent()  # no-op: to make the linter happy

    async def Secure(self, request: security_pb2.SecureRequest,
                     context: grpc.ServicerContext) -> security_pb2.SecureResponse:
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)  # type: ignore
        context.set_details("Method not implemented!")  # type: ignore
        raise NotImplementedError("Method not implemented!")

    async def WaitSecurity(self, request: security_pb2.WaitSecurityRequest,
                           context: grpc.ServicerContext) -> security_pb2.WaitSecurityResponse:
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)  # type: ignore
        context.set_details("Method not implemented!")  # type: ignore
        raise NotImplementedError("Method not implemented!")


class SecurityStorageService(security_grpc_aio.SecurityStorageServicer):
    """Service to trigger Bluetooth Host security persistent storage procedures.

    This class implements the Pandora bluetooth test interfaces,
    where the meta class definition is automatically generated by the protobuf.
    The interface definition can be found in:
    https://cs.android.com/android/platform/superproject/+/main:external
    /pandora/bt-test-interfaces/pandora/security.proto
    """

    async def IsBonded(self, request: security_pb2.IsBondedRequest,
                       context: grpc.ServicerContext) -> wrappers_pb2.BoolValue:
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)  # type: ignore
        context.set_details("Method not implemented!")  # type: ignore
        raise NotImplementedError("Method not implemented!")

    async def DeleteBond(self, request: security_pb2.DeleteBondRequest,
                         context: grpc.ServicerContext) -> empty_pb2.Empty:
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)  # type: ignore
        context.set_details("Method not implemented!")  # type: ignore
        raise NotImplementedError("Method not implemented!")
