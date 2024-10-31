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


class TestIrConfigParameterCaching(common.TransactionCase):
    def setUp(self):
        super(TestIrConfigParameterCaching, self).setUp()
        self.db = self.env.cr.dbname
        self.param_obj = self.env["ir.config_parameter"]
        self.get_param_called = False
        test = self

        def get_param(*args, **kwargs):
            test.get_param_called = True
            return orig_get_param(*args[1:], **kwargs)

        orig_get_param = self.param_obj.get_param
        self.param_obj._patch_method("get_param", get_param)

    def tearDown(self):
        super(TestIrConfigParameterCaching, self).tearDown()
        self.param_obj._revert_method("get_param")
