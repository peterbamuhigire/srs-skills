# Section 4: ZKTeco Biometric Device Connection

BIRDC uses ZKTeco biometric fingerprint devices to record employee attendance. The ERP imports attendance data directly from the device — no manual data entry is needed.

---

## 4.1 Network Setup for the ZKTeco Device

The ZKTeco device must be connected to the BIRDC local area network (LAN) so the ERP server can reach it.

1. Connect the ZKTeco device to the BIRDC network switch using a network cable (RJ45).
2. On the ZKTeco device, go to **Menu** → **Communication** → **Ethernet**.
3. Set the following network parameters (confirm the values with the IT Administrator):
   - **IP Address:** assign a static IP on the BIRDC LAN (for example, `192.168.1.50`)
   - **Subnet Mask:** `255.255.255.0`
   - **Gateway:** the BIRDC router IP (for example, `192.168.1.1`)
4. Set the **Device Port** to `4370` (the ZKTeco default SDK port).
5. Save the settings on the device.
6. From a computer on the BIRDC network, open a command prompt and type: `ping 192.168.1.50` (use the IP you assigned). If you see reply messages, the device is reachable on the network.

---

## 4.2 Test Connection from the ERP

1. Log in as IT Administrator.
2. Click **System Administration** then **Biometric Devices**.
3. Click **New Device**.
4. Enter:
   - **Device Name** (for example, "Main Entrance — ZKTeco K40")
   - **IP Address** (as set in Section 4.1)
   - **Port:** `4370`
   - **Location** (for example, "Factory Entrance")
5. Click **Test Connection**.
6. If the connection is successful, a green message appears: "Device online. Found X enrolled users."
7. If the connection fails, recheck the IP address and port. Confirm the device and the ERP server are on the same network.
8. Click **Save Device**.

---

## 4.3 Run Initial Attendance Import

On first setup, import historical attendance records stored on the ZKTeco device:

1. Click **System Administration** then **Biometric Devices**.
2. Click on the device you registered.
3. Click **Import Attendance Records**.
4. Select the **Date Range** for the records you want to import.
5. Click **Import Now**. The ERP pulls all punch-in and punch-out records from the device.
6. A confirmation message shows the number of records imported.
7. Navigate to **HR** → **Attendance** to verify the imported records appear correctly.

*Going forward, the ERP imports attendance records from the device automatically every 30 minutes. Manual import is only needed for historical data or to recover after a connectivity interruption.*
