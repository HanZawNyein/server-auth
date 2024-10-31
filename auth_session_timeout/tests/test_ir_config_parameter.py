# (c) 2015 ACSONE SA/NV, Dhinesh D

# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests import common


class TestIrConfigParameter(common.TransactionCase):
    def setUp(self):
        super(TestIrConfigParameter, self).setUp()
        self.db = self.env.cr.dbname
        self.param_obj = self.env["ir.config_parameter"]
        self.data_obj = self.env["ir.model.data"]
        self.delay = self.env.ref(
            "auth_session_timeout.inactive_session_time_out_delay"
        )

    def test_check_session_param_delay(self):
        delay = self.param_obj._auth_timeout_get_parameter_delay()
        self.assertEqual(delay, int(self.delay.value))
        self.assertIsInstance(delay, int)

    def test_check_session_param_urls(self):
        urls = self.param_obj._auth_timeout_get_parameter_ignored_urls()
        self.assertIsInstance(urls, list)
