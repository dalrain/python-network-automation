def test_prompt(netmiko_connect):
    """Look for a command prompt, make sure the connection was successful"""
    assert netmiko_connect.find_prompt() == "arista1#"

def test_show_version(netmiko_connect):
    """Get show version from the device"""
    assert "4.20.10M" in netmiko_connect.send_command("show version")
