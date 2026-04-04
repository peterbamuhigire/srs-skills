# Feature: Camera Surveillance

## Description
Farm camera registration and live video surveillance system supporting major IP camera brands and generic RTSP/ONVIF protocols. Provides RTSP proxy streaming via HLS for browser playback, single and multi-camera grid views, PTZ control, zone-based motion detection with multi-channel alerts, and time-limited share access for security personnel or farm managers.

## Standard Capabilities
- Camera registration with brand support (Hikvision, Dahua, Reolink, generic RTSP/ONVIF)
- RTSP proxy streaming (mediamtx or ffmpeg transcoding to HLS) for browser-based playback
- Single camera full-screen view with stream quality selector (low, medium, high)
- Multi-camera grid view (2x2, 3x3, custom layout)
- PTZ (Pan-Tilt-Zoom) control for supported cameras
- Night mode and infrared toggle
- Zone-based motion detection with configurable sensitivity per zone
- Motion alert delivery via push notification, SMS, and WhatsApp
- Alert scheduling (active hours, silent hours, weekend overrides)
- False alarm reduction through motion zone exclusion and sensitivity tuning
- Two-way audio for supported cameras
- Time-limited share access (generate expiring link for third-party viewers)
- Event clip recording and storage with timestamp search

## Regulatory Hooks
- Uganda Data Protection and Privacy Act 2019: surveillance consent notices required; data retention policies must be disclosed; third-party access must be logged

## Linked NFRs
- AG-008 (System Availability and Uptime)
- AG-009 (Data Privacy and Consent)
