#!/usr/bin/env/python

from jnpr.junos import Device

from jnpr.junos.exception import LockError

from jnpr.junos.utils.config import Config

from jnpr_devices import srx2

device_object = Device(**srx2)
device_object.open()

device_config_object = Config(device_object)

#Now we'll lock the config in an unprotected manner

device_config_object.lock()

#And try again to lock it, but with some sanity check

try:
    device_config_object.lock()
    print("Successfully locked the device config for editing")
except LockError:
    print("The device was already locked; failed to get a new lock")

#Set the hostname with a one-liner

device_config_object.load("set system host-name some-fake-hostname", format="set", merge=True)

#Now verify that we actually sent some config (but didn't apply it)
print("The following config is waiting to apply on the device")
print(device_config_object.diff())

device_config_object.rollback(0)

print("Now see if we have any config waiting to apply")
print(device_config_object.diff())
