# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import ServiceBusManagementClientConfiguration
from .operations import Operations
from .operations import NamespacesOperations
from .operations import DisasterRecoveryConfigsOperations
from .operations import MigrationConfigsOperations
from .operations import QueuesOperations
from .operations import TopicsOperations
from .operations import SubscriptionsOperations
from .operations import RulesOperations
from .operations import RegionsOperations
from .operations import PremiumMessagingRegionsOperations
from .operations import EventHubsOperations
from .. import models


class ServiceBusManagementClient(object):
    """Azure Service Bus client.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.servicebus.aio.operations.Operations
    :ivar namespaces: NamespacesOperations operations
    :vartype namespaces: azure.mgmt.servicebus.aio.operations.NamespacesOperations
    :ivar disaster_recovery_configs: DisasterRecoveryConfigsOperations operations
    :vartype disaster_recovery_configs: azure.mgmt.servicebus.aio.operations.DisasterRecoveryConfigsOperations
    :ivar migration_configs: MigrationConfigsOperations operations
    :vartype migration_configs: azure.mgmt.servicebus.aio.operations.MigrationConfigsOperations
    :ivar queues: QueuesOperations operations
    :vartype queues: azure.mgmt.servicebus.aio.operations.QueuesOperations
    :ivar topics: TopicsOperations operations
    :vartype topics: azure.mgmt.servicebus.aio.operations.TopicsOperations
    :ivar subscriptions: SubscriptionsOperations operations
    :vartype subscriptions: azure.mgmt.servicebus.aio.operations.SubscriptionsOperations
    :ivar rules: RulesOperations operations
    :vartype rules: azure.mgmt.servicebus.aio.operations.RulesOperations
    :ivar regions: RegionsOperations operations
    :vartype regions: azure.mgmt.servicebus.aio.operations.RegionsOperations
    :ivar premium_messaging_regions: PremiumMessagingRegionsOperations operations
    :vartype premium_messaging_regions: azure.mgmt.servicebus.aio.operations.PremiumMessagingRegionsOperations
    :ivar event_hubs: EventHubsOperations operations
    :vartype event_hubs: azure.mgmt.servicebus.aio.operations.EventHubsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ServiceBusManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.namespaces = NamespacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.disaster_recovery_configs = DisasterRecoveryConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.migration_configs = MigrationConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.queues = QueuesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.topics = TopicsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscriptions = SubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.rules = RulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.regions = RegionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.premium_messaging_regions = PremiumMessagingRegionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.event_hubs = EventHubsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ServiceBusManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
