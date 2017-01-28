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

from keystone.common import resource_options


USER_OPTIONS_REGISTRY = resource_options.ResourceOptionRegistry('USER')
IGNORE_CHANGE_PASSWORD_OPT = (
    resource_options.ResourceOption('1000',
                                    'ignore_change_password_upon_first_use'))
IGNORE_PASSWORD_EXPIRY_OPT = (
    resource_options.ResourceOption('1001',
                                    'ignore_password_expiry'))


# NOTE(notmorgan): wrap this in a function for testing purposes.
# This is called on import by design.
def register_user_options():
    for opt in [
        IGNORE_CHANGE_PASSWORD_OPT,
        IGNORE_PASSWORD_EXPIRY_OPT,
    ]:
        USER_OPTIONS_REGISTRY.register_option(opt)


register_user_options()
