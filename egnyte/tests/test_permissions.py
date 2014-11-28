from egnyte import exc

from unittest.case import skip
from egnyte.tests.config import IntegrationCase


class TestPermissions(IntegrationCase):
    def test_permissions(self):
        folder = self.root_folder.folder("permissions_1").create(True)
        permissions = folder.get_permissions()

    @skip('Does not work yet')
    def test_effective(self):
        folder = self.root_folder.folder("permissions_1").create(True)
        effective = folder.get_effective_permissions(self.config['login'])