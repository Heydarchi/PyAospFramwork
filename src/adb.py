import subprocess


class ADB:
    def __init__(self, device_id=None, enable_root=True):
        self.device_id = device_id

    def _execute_adb_command(self, command):
        adb_command = ["adb"]
        if self.device_id:
            adb_command.extend(["-s", self.device_id])
        adb_command.extend(command.split(" "))

        try:
            result = subprocess.run(
                adb_command, capture_output=True, text=True, check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error executing command {adb_command}: {e.stderr}")
            return None

    def check_devices(self):
        result = self._execute_adb_command("devices")
        if result:
            return result
        return "No devices connected."

    def install_apk(self, apk_path):
        command = f"install {apk_path}"
        return self._execute_adb_command(command)

    def uninstall_apk(self, package_name):
        command = f"uninstall {package_name}"
        return self._execute_adb_command(command)

    def get_device_info(self):
        command = "shell getprop"
        return self._execute_adb_command(command)

    def reboot_device(self):
        return self._execute_adb_command("reboot")

    def push_file(self, local_file_path, remote_file_path):
        command = f"push {local_file_path} {remote_file_path}"
        return self._execute_adb_command(command)

    def pull_file(self, remote_file_path, local_file_path):
        command = f"pull {remote_file_path} {local_file_path}"
        return self._execute_adb_command(command)

    def root(self):
        command = "root"
        return self._execute_adb_command(command)

    def unroot(self):
        command = "unroot"
        return self._execute_adb_command(command)

    def kill_server(self):
        command = "kill-server"
        return self._execute_adb_command(command)

    def start_server(self):
        command = "start-server"
        return self._execute_adb_command(command)


if __name__ == "__main__":
    adb = ADB()

    # Check connected devices
    devices = adb.check_devices()
    print("Connected devices:")
    print(devices)

    # Install an APK (adjust the APK path for your setup)
    apk_path = "apks/emptyapp.apk"
    install_result = adb.install_apk(apk_path)
    print(f"Install APK result: {install_result}")

    # Uninstall an app by package name
    package_name = "com.aospinsight.emptyapp"
    uninstall_result = adb.uninstall_apk(package_name)
    print(f"Uninstall APK result: {uninstall_result}")

    # Get device info
    device_info = adb.get_device_info()
    print("Device info:")
    print(device_info)

    # Push a file to the device
    push_result = adb.push_file("apks/local_file.txt", "/sdcard/remote_file.txt")
    print(f"Push file result: {push_result}")

    # Pull a file from the device
    pull_result = adb.pull_file("/sdcard/remote_file.txt", "local_file.txt")
    print(f"Pull file result: {pull_result}")

    # Reboot the device
    reboot_result = adb.reboot_device()
    print(f"Reboot result: {reboot_result}")
