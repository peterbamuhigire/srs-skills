# Section 2: Android App Installation

BIRDC ERP includes 6 Android apps. Each app is intended for a specific staff role. Apps are distributed through Firebase App Distribution or the BIRDC internal download link — they are not on Google Play Store.

---

## 2.1 The 6 Android Apps

| App Name | Who Uses It | Offline Capable |
|---|---|---|
| Sales Agent App | Field Sales Agents (Samuel) | Yes |
| Warehouse App | Store Manager (David) | Yes |
| Farmer Delivery App | Collections Officers (Patrick) | Yes |
| Factory Floor App | Production Supervisors (Moses) | Yes |
| HR Self-Service App | All staff | Partial |
| Executive Dashboard App | Director | No (requires internet) |

---

## 2.2 Downloading and Installing an App

*These steps apply to all 6 Android apps. Do them once for each app you need.*

**Method A — Firebase App Distribution link (IT Administrator sends this):**

1. On your Android phone, open the email or WhatsApp message from the IT Administrator containing the app download link.
2. Tap the link. Your browser opens and asks you to download the APK file.
3. Tap **Download**.
4. When the download is complete, tap **Open** or find the file in your Downloads folder and tap it.
5. Android may ask "Do you want to install apps from unknown sources?" Tap **Settings**, enable **Install unknown apps** for your browser, then go back and tap the APK file again.
6. Tap **Install**.
7. Tap **Open** when installation is complete.

**Method B — Internal download link:**

1. On your Android phone, open the browser and go to the internal download page: `http://erp.birdc.local/apps`
2. Tap the name of the app you need.
3. Tap **Download APK**.
4. Follow steps 4–7 from Method A above.

*You need to be on the BIRDC Wi-Fi network to use Method B. If you are outside the office, use Method A.*

---

## 2.3 First Login on the App

1. Open the installed app.
2. On the login screen, enter the **Server URL**: `http://erp.birdc.local` (the IT Administrator will confirm the correct address).
3. Enter your **Username** and **Password** (the same credentials you use for the web application).
4. Tap **Login**.
5. The app downloads your initial data (product list, price list, customer list, your agent record). This may take 1–2 minutes on the first login. Stay connected to Wi-Fi.
6. When the download is complete, the app takes you to your home screen.

---

## 2.4 Syncing Initial Data

After first login, the app stores all necessary data on your phone so you can work offline. If you are given a new phone or reinstall the app:

1. Connect to Wi-Fi.
2. Open the app and log in.
3. The app automatically starts a full data sync. A progress bar is shown.
4. Wait for the sync to complete before going to the field.

---

## 2.5 Pairing a Bluetooth Thermal Printer (Sales Agent App and Farmer Delivery App)

The Sales Agent App and Farmer Delivery App can print 80mm thermal receipts using a Bluetooth printer.

1. Switch on the Bluetooth printer. The power light comes on.
2. On your Android phone, open **Settings**, then **Bluetooth**.
3. Make sure Bluetooth is turned on.
4. Tap **Pair new device**. Your phone searches for nearby Bluetooth devices.
5. Tap the printer name in the list (for example, "POS58" or the model name of your printer).
6. If asked for a pairing code, enter `0000` (four zeros) or `1234` — check your printer's manual if neither works.
7. The printer name appears under **Paired devices**.
8. Open the Sales Agent App or Farmer Delivery App.
9. Tap **Settings** (gear icon).
10. Tap **Printer Settings**.
11. Tap **Select Printer** and choose the printer you just paired.
12. Tap **Test Print** to confirm the connection is working. A test receipt prints.

*Keep the printer close to your phone (within 10 metres) for a reliable Bluetooth connection.*
