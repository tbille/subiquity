# Copyright 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging

from subiquitycore.controller import BaseController

from subiquity.models import IscsiDiskModel

log = logging.getLogger("subiquitycore.controller.iscsi")


class IscsiDiskController(BaseController):
    signals = [
        ('iscsi:show',                         'iscsi'),
        ('iscsi:finish',                       'iscsi_handler'),
        ('iscsi:discover-volumes',             'discover_volumes'),
        ('iscsi:custom-discovery-credentials', 'custom_discovery_credentials'),
        ('iscsi:manual-volume-details',        'manual_volume_details'),
    ]

    def __init__(self, common):
        super().__init__(common)
        self.model = IscsiDiskModel()

    def iscsi(self):
        pass

    def iscsi_handler(self):
        pass

    def discover_volumes(self):
        pass

    def custom_discovery_credentials(self):
        pass

    def manual_volume_details(self):
        pass
