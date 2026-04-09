# you are building a smart thermostat system.
# if the device_status is "active"
# and temperature > 35 -> Warn High Temperature Alert
# else "Temprature normal"
# if device is off --> device is offline


device_status = "inactive"
temperature = 30

if device_status == "active":
    if temperature > 35:
        print("Warn High Temperature Alert")
    else:
        print("Temperature normal")
else:
    print("Device is offline")