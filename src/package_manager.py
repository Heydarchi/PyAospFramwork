from adb import *


class PackageManager:
    def __init__(self, adb):
        self.adb = adb

    def _parse_package_list(self, raw_output):
        if raw_output:
            return [
                line.replace("package:", "").strip() for line in raw_output.splitlines()
            ]
        return []

    def list_installed_packages(self):
        raw_output = self.adb._execute_adb_command("shell pm list packages")
        return self._parse_package_list(raw_output)

    def list_system_packages(self):
        raw_output = self.adb._execute_adb_command("shell pm list packages -s")
        return self._parse_package_list(raw_output)

    def list_user_packages(self):
        raw_output = self.adb._execute_adb_command("shell pm list packages -3")
        return self._parse_package_list(raw_output)

    def get_package_path(self, package_name):
        raw_output = self.adb._execute_adb_command(f"shell pm path {package_name}")
        return self._parse_package_list(raw_output)

    def clear_app_data(self, package_name):
        return self.adb._execute_adb_command(f"shell pm clear {package_name}")

    def enable_app(self, package_name):
        result = self.adb._execute_adb_command(f"shell pm enable {package_name}")
        return True if "enabled" in result else False

    def disable_app(self, package_name):
        result = self.adb._execute_adb_command(f"shell pm disable {package_name}")
        return True if "disabled" in result else False

    def grant_permission(self, package_name, permission):
        return self.adb._execute_adb_command(
            f"shell pm grant {package_name} {permission}"
        )

    def revoke_permission(self, package_name, permission):
        return self.adb._execute_adb_command(
            f"shell pm revoke {package_name} {permission}"
        )

    def is_app_installed(self, package_name):
        installed_packages = self.list_installed_packages()
        return package_name in installed_packages if installed_packages else False

    def get_permissions(self, package_name):
        return self.adb._execute_adb_command(
            f"shell dumpsys package {package_name} | grep -A 10 'requested permissions'"
        )

    def force_stop_app(self, package_name):
        return self.adb._execute_adb_command(f"shell am force-stop {package_name}")


if __name__ == "__main__":
    adb = ADB()
    adb.root()
    pm = PackageManager(adb)

    print("List of Installed Packages:")
    installed_packages = pm.list_installed_packages()
    print(installed_packages)

    print("\nList of System Packages:")
    system_packages = pm.list_system_packages()
    print(system_packages)

    print("\nList of User Packages:")
    user_packages = pm.list_user_packages()
    print(user_packages)

    package_name = "com.aospinsight.emptyapp"
    print(f"\nChecking if package '{package_name}' is installed:")
    is_installed = pm.is_app_installed(package_name)
    print(f"Installed: {is_installed}")

    apk_path = "apks/emptyapp.apk"
    print(f"\nInstalling APK from '{apk_path}':")
    install_result = adb.install_apk(apk_path)
    print(install_result)

    print(f"\nGetting path for package '{package_name}':")
    package_paths = pm.get_package_path(package_name)
    print(package_paths)

    print(f"\nClearing data for package '{package_name}':")
    clear_result = pm.clear_app_data(package_name)
    print(clear_result)

    print(f"\nEnabling package '{package_name}':")
    enable_result = pm.enable_app(package_name)
    print(enable_result)

    print(f"\nDisabling package '{package_name}':")
    disable_result = pm.disable_app(package_name)
    print(disable_result)

    permission = "android.permission.CAMERA"
    print(f"\nGranting permission '{permission}' to package '{package_name}':")
    grant_result = pm.grant_permission(package_name, permission)
    print(grant_result)

    print(f"\nRevoking permission '{permission}' from package '{package_name}':")
    revoke_result = pm.revoke_permission(package_name, permission)
    print(revoke_result)

    print(f"\nForce stopping package '{package_name}':")
    force_stop_result = pm.force_stop_app(package_name)
    print(force_stop_result)

    print(f"\nUninstalling package '{package_name}':")
    uninstall_result = adb.uninstall_apk(package_name)
    print(uninstall_result)

    print(f"\nChecking if package '{package_name}' is installed:")
    is_installed = pm.is_app_installed(package_name)
    print(f"Installed: {is_installed}")
