# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_policy import policy

from keystone.common.policies import base

region_policies = [
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'get_region',
        check_str='',
        description='Show region details.',
        operations=[{'path': '/v3/regions/{region_id}',
                     'method': 'GET'},
                    {'path': '/v3/regions/{region_id}',
                     'method': 'HEAD'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'list_regions',
        check_str='',
        description='List regions.',
        operations=[{'path': '/v3/regions',
                     'method': 'GET'},
                    {'path': '/v3/regions',
                     'method': 'HEAD'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'create_region',
        check_str=base.RULE_ADMIN_REQUIRED,
        description='Create region.',
        operations=[{'path': '/v3/regions',
                     'method': 'POST'},
                    {'path': '/v3/regions/{region_id}',
                     'method': 'PUT'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'update_region',
        check_str=base.RULE_ADMIN_REQUIRED,
        description='Update region.',
        operations=[{'path': '/v3/regions/{region_id}',
                     'method': 'PATCH'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'delete_region',
        check_str=base.RULE_ADMIN_REQUIRED,
        description='Delete region.',
        operations=[{'path': '/v3/regions/{region_id}',
                     'method': 'DELETE'}])
]


def list_rules():
    return region_policies
