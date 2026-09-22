import subprocess
import re

# Get all saved Wi-Fi profiles
result = subprocess.run(
    ["netsh", "wlan", "show", "profiles"],
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="ignore"
)

profiles = re.findall(r"All User Profile\s*:\s*(.*)", result.stdout)

for profile in profiles:
    profile = profile.strip()

    # Get details including the saved key
    details = subprocess.run(
        ["netsh", "wlan", "show", "profile", f"name={profile}", "key=clear"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    ).stdout

    match = re.search(r"Key Content\s*:\s*(.*)", details)
    password = match.group(1).strip() if match else "No saved password"

    print(f"Wi-Fi: {profile}")
    print(f"Password: {password}")
    print("-" * 40)