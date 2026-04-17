# Technology Stack

## Backend
- **Language:** PHP 8.2+
- **Framework:** Chwezi Core (custom framework shared with Academia Pro and Medic8)
- **Database:** MySQL 8.x
- **API:** RESTful JSON API with JWT authentication (mobile) and session-based auth (web)
- **Server:** Apache/Nginx on Linux (Ubuntu)

## Web Frontend
- **UI Framework:** Bootstrap 5 / Tabler admin template
- **JavaScript:** jQuery (consistent with Chwezi Core)
- **Maps:** Google Maps JavaScript API + OpenStreetMap offline fallback
- **Charts:** Chart.js for dashboards and reports
- **Tables:** DataTables for data grids
- **Alerts:** SweetAlert2
- **Date Picker:** Flatpickr

## Android App
- **Language:** Kotlin
- **UI:** Jetpack Compose (Material 3)
- **Architecture:** MVVM + Clean Architecture
- **DI:** Hilt
- **Local DB:** Room (SQLCipher encryption)
- **Networking:** Retrofit + OkHttp
- **Maps:** Google Maps SDK for Android
- **Image Loading:** Coil
- **Background Sync:** WorkManager

## iOS App
- **Language:** Swift
- **UI:** SwiftUI
- **Architecture:** MVVM + Clean Architecture
- **Local DB:** SwiftData (encrypted)
- **Networking:** URLSession + async/await
- **Maps:** MapKit + Google Maps SDK
- **Background Sync:** BGTaskScheduler

## Optional Edge Services
- **IoT Gateway:** WebSocket server (PHP Swoole or Node.js) for real-time Jaguza/sensor data
- **Camera Proxy:** mediamtx + ffmpeg for RTSP-to-HLS stream conversion
- **GPS Tracker Receiver:** Lightweight TCP/MQTT daemon for tracker protocols

## External Integrations
- **Weather:** Open-Meteo API (free)
- **SMS/USSD:** Africa's Talking
- **Mobile Money:** MTN MoMo API, Airtel Money API
- **Push Notifications:** Firebase Cloud Messaging
- **Maps:** Google Maps SDK, OpenStreetMap/Mapbox (offline tiles)
- **Satellite Imagery:** Sentinel-2 via Google Earth Engine
- **AI:** Claude API (Anthropic) for pest/disease ID and farm advisory
- **IoT:** Jaguza API (OAuth)
- **Cameras:** Hik-Connect, Dahua DMSS, Reolink Open API, generic RTSP/ONVIF
- **Payments (international):** Flutterwave / Paystack

## Infrastructure
- **Hosting:** Africa-based cloud (same infrastructure as Academia Pro/Medic8)
- **CDN:** For static assets and offline map tiles
- **File Storage:** S3-compatible object storage for photos, receipts, certificates
- **SSL:** Let's Encrypt
