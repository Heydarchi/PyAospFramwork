import unittest
from unittest.mock import patch, MagicMock
from package_manager import PackageManager
from adb import *

PACKAGE_NAME = "com.aospinsight.emptyapp"


class TestPackageManager(unittest.TestCase):

    @patch("ADB._execute_adb_command")
    def test_list_installed_packages(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "package:com.example.app1\npackage:com.example.app2"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.list_installed_packages()
        self.assertEqual(result, ["com.example.app1", "com.example.app2"])
        mock_execute_adb_command.assert_called_once_with("shell pm list packages")
    
    @patch("ADB._execute_adb_command")
    def test_list_system_packages(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "package:com.android.systemui\npackage:com.android.settings"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.list_system_packages()
        self.assertEqual(result, ["com.android.systemui", "com.android.settings"])
        mock_execute_adb_command.assert_called_once_with("shell pm list packages -s")

    @patch("ADB._execute_adb_command")
    def test_list_user_packages(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "package:com.example.userapp1\npackage:com.example.userapp2"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.list_user_packages()
        self.assertEqual(result, ["com.example.userapp1", "com.example.userapp2"])
        mock_execute_adb_command.assert_called_once_with("shell pm list packages -3")

    @patch("ADB._execute_adb_command")
    def test_get_package_path(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "package:/data/app/com.example.app1-1/base.apk"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.get_package_path(PACKAGE_NAME)
        self.assertTrue("/base.apk" in result)
        mock_execute_adb_command.assert_called_once_with("shell pm path " + PACKAGE_NAME)

    @patch("ADB._execute_adb_command")
    def test_clear_app_data(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "Success"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.clear_app_data("com.example.app1")
        self.assertEqual(result, "Success")
        mock_execute_adb_command.assert_called_once_with("shell pm clear com.example.app1")

    @patch("ADB._execute_adb_command")
    def test_enable_app(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "Enabled"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.enable_app("com.example.app1")
        self.assertTrue(result)
        mock_execute_adb_command.assert_called_once_with("shell pm enable com.example.app1")

    @patch("ADB._execute_adb_command")
    def test_disable_app(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "Disabled"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.disable_app("com.example.app1")
        self.assertTrue(result)
        mock_execute_adb_command.assert_called_once_with("shell pm disable com.example.app1")

    @patch("ADB._execute_adb_command")
    def test_grant_permission(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "Success"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.grant_permission("com.example.app1", "android.permission.CAMERA")
        self.assertEqual(result, "Success")
        mock_execute_adb_command.assert_called_once_with(
            "shell pm grant com.example.app1 android.permission.CAMERA"
        )

    @patch("ADB._execute_adb_command")
    def test_revoke_permission(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "Success"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.revoke_permission("com.example.app1", "android.permission.CAMERA")
        self.assertEqual(result, "Success")
        mock_execute_adb_command.assert_called_once_with(
            "shell pm revoke com.example.app1 android.permission.CAMERA"
        )

    @patch("ADB._execute_adb_command")
    def test_is_app_installed(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "package:com.example.app1\npackage:com.example.app2"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.is_app_installed("com.example.app1")
        self.assertTrue(result)
        mock_execute_adb_command.assert_called_once_with("shell pm list packages")

    @patch("ADB._execute_adb_command")
    def test_get_permissions(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "permission: android.permission.CAMERA"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.get_permissions("com.example.app1")
        self.assertEqual(result, "permission: android.permission.CAMERA")
        mock_execute_adb_command.assert_called_once_with(
            "shell dumpsys package com.example.app1 | grep -A 10 'requested permissions'"
        )

    @patch("ADB._execute_adb_command")
    def test_force_stop_app(self, mock_execute_adb_command):
        mock_execute_adb_command.return_value = "Success"
        adb_mock = MagicMock()
        pm = PackageManager(adb_mock)
        result = pm.force_stop_app("com.example.app1")
        self.assertEqual(result, "Success")
        mock_execute_adb_command.assert_called_once_with("shell am force-stop com.example.app1")


if __name__ == "__main__":
    unittest.main()
