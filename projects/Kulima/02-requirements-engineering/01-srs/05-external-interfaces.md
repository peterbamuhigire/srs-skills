# 5 External Interface Requirements

## 5.1 User Interfaces

### 5.1.1 Web Dashboard

- **Framework:** Bootstrap 5 / Tabler admin template
- **Browser support:** Chrome 90+, Firefox 90+, Safari 14+, Edge 90+
- **Layout:** Responsive 3-panel layout (sidebar navigation, main content, contextual detail panel). Collapses to single-column on mobile browsers
- **Components:** DataTables for data grids, Chart.js for dashboards and reports, Flatpickr for date selection, SweetAlert2 for confirmations and alerts, Google Maps JavaScript API for map views
- **Screens:** Farm dashboard, plot management, crop season management, livestock register, financial records, task board (Kanban + calendar), inventory, weather, marketplace, traceability, cooperative management, IoT dashboard, camera grid, GPS tracking map, AI advisor, director dashboard, settings

### 5.1.2 Android App (Farmer)

- **Framework:** Kotlin, Jetpack Compose (Material 3)
- **Minimum SDK:** Android 10 (API 29), Android Go edition supported
- **Target device:** Tecno Spark (2GB RAM, 32GB storage) as reference device
- **Architecture:** MVVM + Clean Architecture, Hilt DI, Room with SQLCipher for local storage
- **Offline-first:** All core screens function identically offline and online
- **Navigation:** Bottom navigation bar (Home, Crops, Livestock, Finances, More). Farm switcher in top app bar
- **Touch targets:** Minimum 48x48dp
- **Font size:** Minimum 14sp body text
- **Languages:** English, Luganda, Swahili (Phase 1); French, Portuguese, Kinyarwanda (Phase 2)

### 5.1.3 iOS App (Farmer)

- **Framework:** Swift, SwiftUI
- **Minimum OS:** iOS 16+
- **Architecture:** MVVM + Clean Architecture, SwiftData for local storage (encrypted)
- **Offline-first:** Same offline-first architecture as Android
- **Navigation:** Tab bar matching Android bottom navigation structure
- **Phase:** 2

### 5.1.4 Worker Simplified App

- **Description:** A simplified interface within the Android app activated by the "Worker" role
- **Screens:** Task list (assigned tasks only), task detail with "Start" and "Complete" actions, daily work log, pay history
- **Constraints:** Reduced menu options; no access to farm management, financial records, or settings beyond language and profile
- **Target device:** Entry-level Android (Itel A18, Android Go, 16GB storage)

### 5.1.5 Buyer Portal

- **Description:** A read-only web interface accessible via QR code scan without authentication
- **Screens:** Batch traceability view (origin, chain of custody, certifications, input history, deforestation check, farmer profile, GPS polygon map)
- **Constraints:** No write operations. No sensitive data (exact GPS, financials, contact details) exposed
- **Phase:** 2

### 5.1.6 Director App

- **Description:** A dedicated mobile app (or mode within the main app) for directors/investors
- **Screens:** Consolidated farm overview, financial summary, livestock health dashboard, harvest forecast, approval workflow, inter-farm transfer
- **Phase:** 4

### 5.1.7 USSD Interface

- **Description:** USSD short code for basic transaction recording on feature phones
- **Functions:** Record income, record expense, check balance, view task list
- **Provider:** Africa's Talking USSD API
- **Constraints:** Text-only, menu-driven navigation, maximum 160 characters per screen
- **Phase:** 4

## 5.2 Hardware Interfaces

### 5.2.1 GPS Module

- **Interface:** Android LocationManager / Google Fused Location Provider; iOS CoreLocation
- **Function:** Farm and plot boundary capture (GeoJSON polygon), animal tracker position, farm location for weather API
- **Accuracy requirement:** $\leq$ 5 metres positional accuracy
- **Data format:** GeoJSON (RFC 7946)

### 5.2.2 IP Cameras (RTSP/ONVIF)

- **Protocols:** RTSP (Real-Time Streaming Protocol), ONVIF (Open Network Video Interface Forum)
- **Supported brands:** Hikvision (Hik-Connect API), Dahua (DMSS API), Reolink (Open API), generic RTSP/ONVIF compliant cameras
- **Function:** Live video streaming, PTZ control, motion detection events
- **Data flow:** Camera → RTSP → mediamtx/ffmpeg proxy → HLS stream → client
- **Phase:** 3

### 5.2.3 IoT Ear Tags (Jaguza)

- **Interface:** Jaguza REST API (OAuth 2.0)
- **Function:** Animal activity monitoring, temperature sensing, GPS location, fertility index, disease early warning
- **Data frequency:** 10-minute polling + real-time webhook alerts
- **Phase:** 3

### 5.2.4 GPS Animal Trackers

- **Protocols:** TCP (proprietary tracker protocols), MQTT, HTTP
- **Function:** Real-time animal/vehicle position reporting
- **Data fields:** IMEI, timestamp, latitude, longitude, speed, heading, battery level
- **Phase:** 3

### 5.2.5 Soil Sensors

- **Interface:** MQTT or HTTP webhook to Kulima IoT gateway
- **Function:** Soil moisture, soil temperature, soil pH reporting per plot
- **Phase:** 3

### 5.2.6 Weather Stations

- **Interface:** MQTT or HTTP webhook
- **Function:** Local rainfall, temperature, wind speed, humidity overriding API weather with actual readings
- **Phase:** 3

### 5.2.7 RFID Readers

- **Interface:** Bluetooth Low Energy (BLE) to Android/iOS app
- **Function:** Animal tag scanning for identification during health events, weighing, and movement recording
- **Phase:** 1

## 5.3 Software Interfaces

### 5.3.1 MySQL 8.x

- **Interface type:** Database driver (PHP PDO)
- **Function:** Primary relational data store for all application data
- **Data:** Tenant records, farm data, crop data, livestock data, financial records, user accounts, reference data, GeoJSON (JSON columns with spatial indexing)
- **Constraints:** Multi-tenant data isolation enforced at query level via tenant_id scoping

### 5.3.2 Chwezi Core Framework

- **Interface type:** Internal PHP framework
- **Function:** Provides authentication, RBAC, tenant management, billing, notification dispatch, audit logging, and director platform infrastructure
- **Shared with:** Academia Pro, Medic8

### 5.3.3 Open-Meteo API

- **Interface type:** REST API (HTTPS)
- **Endpoint:** `https://api.open-meteo.com/v1/forecast`
- **Authentication:** None (free tier)
- **Function:** Weather forecast retrieval (3-day free, 8-day paid), historical weather data
- **Data format:** JSON
- **Rate limit:** [CONTEXT-GAP: Open-Meteo rate limits not documented in context files]

### 5.3.4 Africa's Talking API

- **Interface type:** REST API (HTTPS)
- **Function:** SMS delivery (notifications, alerts, OTP), USSD session management
- **Authentication:** API key + username
- **Data format:** JSON

### 5.3.5 MTN MoMo API

- **Interface type:** REST API (HTTPS)
- **Function:** Subscription payment collection, worker wage disbursement, cooperative bulk payment
- **Authentication:** OAuth 2.0 (API user + API key)
- **Data format:** JSON
- **Operations:** Collection (receive payment), Disbursement (send payment), Transfer

### 5.3.6 Airtel Money API

- **Interface type:** REST API (HTTPS)
- **Function:** Subscription payment collection, worker wage disbursement
- **Authentication:** OAuth 2.0
- **Data format:** JSON
- **Operations:** Collection, Disbursement

### 5.3.7 Firebase Cloud Messaging (FCM)

- **Interface type:** REST API (HTTPS)
- **Function:** Push notification delivery to Android and iOS devices
- **Authentication:** Server key / Service account
- **Data format:** JSON
- **Notification types:** Weather alerts, task reminders, low stock alerts, expiry alerts, payment confirmations, IoT alerts, geofence breaches, motion detection

### 5.3.8 Google Maps SDK

- **Interface type:** JavaScript API (web), Android SDK, iOS SDK
- **Function:** Farm/plot boundary mapping, satellite imagery, geofence visualization, GPS tracking live map
- **Authentication:** API key
- **Fallback:** OpenStreetMap / Mapbox for offline tile caching

### 5.3.9 Sentinel-2 via Google Earth Engine

- **Interface type:** REST API / Python client
- **Function:** NDVI crop health analysis from satellite imagery
- **Authentication:** Google Cloud service account
- **Data format:** GeoTIFF imagery, JSON metadata
- **Phase:** 2

### 5.3.10 Jaguza API

- **Interface type:** REST API (HTTPS)
- **Authentication:** OAuth 2.0
- **Function:** IoT device data retrieval (animal activity, temperature, GPS, fertility), webhook registration for real-time alerts
- **Data format:** JSON
- **Phase:** 3

### 5.3.11 Hik-Connect / Dahua DMSS / Reolink APIs

- **Interface type:** REST API (HTTPS) for cloud-managed cameras; ONVIF for local cameras
- **Function:** Camera discovery, stream URL retrieval, PTZ control, motion event subscription
- **Authentication:** API key or OAuth (varies by manufacturer)
- **Phase:** 3

### 5.3.12 Claude API (Anthropic)

- **Interface type:** REST API (HTTPS)
- **Endpoint:** `https://api.anthropic.com/v1/messages`
- **Authentication:** API key (x-api-key header)
- **Function:** Natural language farm Q&A, photo-based pest/disease diagnosis (Vision API), personalised recommendations
- **Models:** Claude with vision capability for photo diagnosis
- **Data format:** JSON
- **Phase:** 3

### 5.3.13 mediamtx / ffmpeg

- **Interface type:** Local service (process)
- **Function:** RTSP-to-HLS stream conversion for camera proxy
- **Data flow:** RTSP input → transcode/remux → HLS output served via HTTP
- **Phase:** 3

### 5.3.14 Flutterwave / Paystack

- **Interface type:** REST API (HTTPS)
- **Function:** International payment processing for non-African subscribers
- **Authentication:** Secret key
- **Data format:** JSON
- **Phase:** 4

## 5.4 Communication Interfaces

### 5.4.1 REST API (JSON over HTTPS)

- **Protocol:** HTTPS (TLS 1.2+)
- **Data format:** JSON (application/json)
- **Authentication:** JWT Bearer token (mobile/API clients), session cookie (web client)
- **Versioning:** URL-based (`/api/v1/`)
- **Rate limiting:** 100 requests/minute per authenticated user; 20 requests/minute for unauthenticated endpoints
- **Error format:** Standardised JSON error responses with error code, message, and field-level validation details

### 5.4.2 WebSocket (IoT Gateway)

- **Protocol:** WSS (WebSocket Secure)
- **Function:** Real-time IoT data ingestion from Jaguza webhooks and sensor data
- **Runtime:** PHP Swoole or Node.js
- **Phase:** 3

### 5.4.3 TCP/MQTT (GPS Trackers)

- **Protocol:** TCP (proprietary GPS tracker protocols), MQTT 3.1.1
- **Function:** GPS tracker position data ingestion
- **Data fields:** IMEI, timestamp, latitude, longitude, speed, heading, battery, satellite count
- **Phase:** 3

### 5.4.4 HLS (Camera Streams)

- **Protocol:** HTTP Live Streaming (HLS) over HTTPS
- **Function:** Delivery of proxied camera streams to web and mobile clients
- **Segment duration:** 2 seconds (configurable)
- **Quality levels:** High (1080p), Medium (720p), Low (360p), Auto (adaptive)
- **Phase:** 3

### 5.4.5 SMS

- **Provider:** Africa's Talking
- **Function:** Alert delivery (weather, geofence breach, motion detection), OTP verification, USSD fallback
- **Encoding:** GSM 7-bit (160 characters) or UCS-2 (70 characters for non-Latin scripts)

### 5.4.6 USSD

- **Provider:** Africa's Talking
- **Function:** Feature phone fallback for basic transaction recording
- **Session management:** Menu-driven interactive text sessions
- **Phase:** 4
