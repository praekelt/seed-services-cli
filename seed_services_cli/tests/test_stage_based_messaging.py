""" Tests for seed_services_cli.stage_based_messaging """

from unittest import TestCase
from click.testing import CliRunner
from seed_services_cli.main import cli


class TestStageBasedMessagingCommands(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def tearDown(self):
        pass

    def test_identity_search_help(self):
        result = self.runner.invoke(cli, ['sbm-schedules', '--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(
            "List all schedules"
            in result.output)
