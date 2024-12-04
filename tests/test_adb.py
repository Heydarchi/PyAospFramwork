import sys
import os
import unittest
from mock import patch, MagicMock
from lib.adb import *


class TestADB(unittest.TestCase):

    @patch("subprocess.run")
    def test_check_devices(self, mock_run):
        mock_run.return_value = MagicMock(
            stdout="device1\ndevice2", stderr="", returncode=0
        )
        adb = ADB()
        result = adb.check_devices()
        self.assertEqual(result, "device1\ndevice2")

        mock_run.return_value = MagicMock(stdout="", stderr="", returncode=1)
        result = adb.check_devices()
        self.assertEqual(result, "No devices connected.")

    @patch("subprocess.run")
    def test_install_apk(self, mock_run):
        mock_run.return_value = MagicMock(stdout="Success", stderr="", returncode=0)
        adb = ADB()
        result = adb.install_apk("path/to/app.apk")
        self.assertEqual(result, "Success")

        mock_run.return_value = MagicMock(stdout="Failure", stderr="", returncode=1)
        result = adb.install_apk("path/to/app.apk")
        self.assertEqual(result, "Failure")

    @patch("subprocess.run")
    def test_uninstall_apk(self, mock_run):
        mock_run.return_value = MagicMock(stdout="Success", stderr="", returncode=0)
        adb = ADB()
        result = adb.uninstall_apk("com.example.app")
        self.assertEqual(result, "Success")

        mock_run.return_value = MagicMock(stdout="Failure", stderr="", returncode=1)
        result = adb.uninstall_apk("com.example.app")
        self.assertEqual(result, "Failure")

    @patch("subprocess.run")
    def test_get_device_info(self, mock_run):
        mock_run.return_value = MagicMock(stdout="device_info", stderr="", returncode=0)
        adb = ADB()
        result = adb.get_device_info()
        self.assertEqual(result, "device_info")

        mock_run.return_value = MagicMock(stdout="", stderr="Error", returncode=1)
        result = adb.get_device_info()
        self.assertEqual(result, "")

    @patch("subprocess.run")
    def test_reboot_device(self, mock_run):
        mock_run.return_value = MagicMock(stdout="Rebooting", stderr="", returncode=0)
        adb = ADB()
        result = adb.reboot_device()
        self.assertEqual(result, "Rebooting")

        mock_run.return_value = MagicMock(stdout="Error", stderr="", returncode=1)
        result = adb.reboot_device()
        self.assertEqual(result, "Error")

    @patch("subprocess.run")
    def test_push_file(self, mock_run):
        mock_run.return_value = MagicMock(stdout="File pushed", stderr="", returncode=0)
        adb = ADB()
        result = adb.push_file("local/file.txt", "/sdcard/remote/file.txt")
        self.assertEqual(result, "File pushed")

        mock_run.return_value = MagicMock(stdout="Error", stderr="", returncode=1)
        result = adb.push_file("local/file.txt", "/sdcard/remote/file.txt")
        self.assertEqual(result, "Error")

    @patch("subprocess.run")
    def test_pull_file(self, mock_run):
        mock_run.return_value = MagicMock(stdout="File pulled", stderr="", returncode=0)
        adb = ADB()
        result = adb.pull_file("/sdcard/remote/file.txt", "local/file.txt")
        self.assertEqual(result, "File pulled")

        mock_run.return_value = MagicMock(stdout="Error", stderr="", returncode=1)
        result = adb.pull_file("/sdcard/remote/file.txt", "local/file.txt")
        self.assertEqual(result, "Error")


if __name__ == "__main__":
    unittest.main()
