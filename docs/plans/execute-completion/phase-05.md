# Phase 5: Mobile Application Stack

> **For Claude:** Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Achieve full mobile capability parity — iOS is already expert-grade (23 skills),
Android needs one critical gap closed (`android-ai-ml`), and 4 stale duplicate skills
must be formally deprecated to keep the library clean.

**Architecture:** One new skill, four deprecation markers. The iOS and cross-platform
foundations are world-class. Android reaches parity with iOS in AI/ML after this phase.

**Skills library path:** `C:\Users\Peter\.claude\skills\`

---

## Consultancy Capability This Phase Unlocks

A fully equipped consultant can:

- Build production iOS applications from architecture to App Store submission
- Build production Android applications with AI/ML features (ML Kit, TensorFlow Lite, Gemini Nano)
- Build cross-platform apps with Kotlin Multiplatform (KMP) and Compose Multiplatform
- Implement on-device AI: text recognition, face detection, barcode scanning, language detection
- Stream AI responses (Claude, GPT) into Compose UI with proper loading and error states
- Run custom TensorFlow Lite models on-device for offline-capable inference
- Use MediaPipe for real-time computer vision (pose, face mesh, hand landmarks)
- Apply TDD discipline across iOS (Swift), Android (Kotlin), and cross-platform (KMP)

---

## Current Strengths — Skills Already Built

### iOS (23 Skills — Expert Grade)
- `ios-development` — Swift fundamentals, UIKit, SwiftUI, app lifecycle, Xcode
- `ios-architecture-advanced` — MVVM, TCA, Clean Architecture, dependency injection
- `ios-at-scale` — Modular architecture, micro-features, Swift packages, build optimisation
- `ios-ai-ml` — CoreML, Vision, NaturalLanguage, CreateML, on-device inference
- `ios-biometric-login` — Face ID, Touch ID, LocalAuthentication, keychain integration
- `ios-bluetooth-printing` — CoreBluetooth, thermal receipt printer integration
- `ios-data-persistence` — CoreData, SwiftData, CloudKit sync, keychain, file storage
- `ios-debugging-mastery` — Instruments, memory leaks, thread sanitizer, crash symbolication
- `ios-monetization` — StoreKit 2, in-app purchases, subscriptions, App Store Review guidelines
- `ios-networking-advanced` — URLSession, Combine, async/await networking, certificate pinning
- `ios-pdf-export` — PDFKit, UIGraphics, print to PDF, report generation
- `ios-production-patterns` — Launch screen, background tasks, push notification deep links
- `ios-project-setup` — Xcode project structure, schemes, targets, signing, CI integration
- `ios-push-notifications` — APNs, UserNotifications, rich notifications, notification extensions
- `ios-rbac` — Role-based access control, PermissionGate ViewModifier, secure token storage
- `ios-stability-solutions` — Crash-free rate > 99.5%, ANR prevention, memory management
- `ios-swift-design-patterns` — Factory, Builder, Observer, Command, Strategy in Swift
- `ios-swift-recipes` — UITableView, CollectionView, custom transitions, gestures reference
- `ios-swiftdata` — SwiftData model macros, queries, migrations, CloudKit integration
- `ios-tdd` — XCTest, XCTestCase, mocks, snapshot testing, UI testing
- `ios-uikit-advanced` — Custom views, CALayer, animations, Auto Layout performance
- `ios-app-security` — Data protection, jailbreak detection, SSL pinning, code obfuscation
- `ios-pdf-export` — (already listed; one entry)

### Android (11 Skills — Solid)
- `android-development` — Kotlin, Compose UI, ViewModel, Navigation, Hilt DI
- `android-biometric-login` — BiometricPrompt, EncryptedSharedPreferences, keystore
- `android-data-persistence` — Room, DataStore (Proto + Preferences), file storage
- `android-pdf-export` — PdfDocument API, Apache PDFBox, print service integration
- `android-room` — Room entities, DAOs, migrations, Flow integration, testing
- `android-tdd` — JUnit5, MockK, Robolectric, Espresso, Hilt testing
- `mobile-reports` — Reporting UI for both Android and iOS: tables, charts, exports
- `mobile-report-tables` — Data table components for mobile: sorting, pagination, selection
- `mobile-saas-planning` — SaaS mobile app planning: feature tiers, offline strategy
- `mobile-rbac` — Cross-platform role-based access control patterns
- `mobile-custom-icons` — Custom app icons: adaptive icons (Android), App Icon Sets (iOS)

### Cross-Platform (3 Skills — KMP)
- `kmp-development` — KMP shared business logic: repositories, use cases, networking
- `kmp-compose-multiplatform` — Compose Multiplatform UI: shared screens, platform-specific views
- `kmp-tdd` — KMP testing: shared tests, platform-specific mocks, coroutines testing

### Supplementary
- `android-custom-icons` — **DEPRECATED** (superseded by `mobile-custom-icons`)
- `android-reports` — **DEPRECATED** (superseded by `mobile-reports`)
- `android-saas-planning` — **DEPRECATED** (superseded by `mobile-saas-planning`)
- `android-report-tables` — **DEPRECATED** (superseded by `mobile-report-tables`)

---

## Build Tasks

### Task 1: Mark 4 deprecated Android skills

**Files to modify** (add one line at the very top of each SKILL.md):

1. `C:\Users\Peter\.claude\skills\android-custom-icons\SKILL.md`
   — Add: `> **DEPRECATED:** Use \`mobile-custom-icons\` instead.`

2. `C:\Users\Peter\.claude\skills\android-reports\SKILL.md`
   — Add: `> **DEPRECATED:** Use \`mobile-reports\` instead.`

3. `C:\Users\Peter\.claude\skills\android-saas-planning\SKILL.md`
   — Add: `> **DEPRECATED:** Use \`mobile-saas-planning\` instead.`

4. `C:\Users\Peter\.claude\skills\android-report-tables\SKILL.md`
   — Add: `> **DEPRECATED:** Use \`mobile-report-tables\` instead.`

**Step 1:** Open each file and add the DEPRECATED line at line 1.
**Step 2:** Verify the deprecated file still contains its original content (do not delete).
**Step 3:** Commit: `chore(skills): mark 4 android-* skills as deprecated`

---

### Task 2: Create `android-ai-ml` skill

**File to create:** `C:\Users\Peter\.claude\skills\android-ai-ml\SKILL.md`

**Read first:**
- Android ML Kit Guide — `developers.google.com/ml-kit`
- TensorFlow Lite Android — `tensorflow.org/lite/android`
- MediaPipe documentation — `developers.google.com/mediapipe`
- Gemini Nano documentation — `developer.android.com/ai/gemini-nano`

**Content outline for SKILL.md (target: 380–460 lines):**

1. **Android AI/ML Landscape** — ML Kit vs TFLite vs MediaPipe vs Gemini Nano: when to use which
2. **ML Kit — Text Recognition** — `TextRecognizer`, live camera stream, result parsing
3. **ML Kit — Face Detection** — `FaceDetector`, landmark detection, face mesh, liveness check
4. **ML Kit — Barcode Scanning** — `BarcodeScanner`, camera X integration, QR + EAN + Code128
5. **ML Kit — Language Detection** — `LanguageIdentification`, translation, on-device vs cloud
6. **ML Kit — Entity Extraction** — entity types, annotation span parsing, custom models
7. **TensorFlow Lite — Model Inference** — `.tflite` model loading, interpreter setup, input/output tensors
8. **TensorFlow Lite — Custom Model Training** — BYOM workflow, TFLite converter, quantisation (INT8)
9. **MediaPipe — Pose Landmark Detection** — setup, live video pipeline, landmark normalisation
10. **MediaPipe — Hand Tracking** — hand landmarks, gesture recognition, Compose overlay rendering
11. **Gemini Nano (On-Device)** — AICore API (Android 14+), availability check, text summarisation
12. **Streaming AI Responses in Compose** — Claude/GPT API integration, `LazyColumn` token streaming
13. **Camera Integration Patterns** — CameraX pipeline: preview + analysis + image capture
14. **Performance & Battery** — GPU delegate, NNAPI, background inference, power profiling
15. **Testing AI Features** — unit tests for model inference, mock camera for ML Kit, golden outputs

**Step 1:** Read all four source materials above.
**Step 2:** Create `SKILL.md` following the content outline.
**Step 3:** Every section must include a Kotlin code snippet.
**Step 4:** Run `wc -l SKILL.md` — confirm 350–500 lines.
**Step 5:** Commit: `feat(skills): add android-ai-ml skill`

---

## Phase Completion Checklist

- [ ] 4 deprecated android-* skills have DEPRECATED header line added
- [ ] `android-ai-ml` SKILL.md created — 350–500 lines
- [ ] All 15 sections in the android-ai-ml content outline are present
- [ ] Every section has at least one Kotlin code example
- [ ] `android-ai-ml` cross-references `ios-ai-ml` for parity comparison
- [ ] `android-development` references `android-ai-ml` for AI feature work
- [ ] No skill file exceeds 500 lines
- [ ] Git commit made: `feat(skills): complete phase-5 — mobile application stack`

---

## Reading Material

### Books to Buy

| Priority | Title | Author | Publisher | Price | Why Buy |
|----------|-------|--------|-----------|-------|---------|
| 1 | *Android Programming: The Big Nerd Ranch Guide* (5th ed.) | Philips, Stewart, Hardy | Big Nerd Ranch | ~$50 | The most thorough Android fundamentals book — Kotlin, Compose, Room, navigation, testing. Deepens existing android-* skills. |
| 2 | *Kotlin in Action* (2nd ed.) | Jemerov & Isakova | Manning | ~$50 | Kotlin deep dive — coroutines, flows, sealed classes, inline functions. Essential for advanced Android and KMP. |
| 3 | *AI and Machine Learning for On-Device Development* | Laurence Moroney | O'Reilly | ~$55 | On-device ML for both Android (TFLite) and iOS (CoreML) — directly feeds both `android-ai-ml` and `ios-ai-ml`. |
| 4 | *Programming Android with Kotlin* | Pierre-Olivier Laurence | O'Reilly | ~$55 | Modern Android architecture with Kotlin — ViewModel, Hilt, Room, Compose patterns. |

### Free Resources

- Android ML Kit documentation — `developers.google.com/ml-kit` — authoritative ML Kit guide
- TensorFlow Lite Android guide — `tensorflow.org/lite/android` — model inference patterns
- MediaPipe documentation — `developers.google.com/mediapipe` — real-time vision processing
- Gemini Nano / AICore API — `developer.android.com/ai/gemini-nano` — on-device LLM (Android 14+)
- Google Codelabs (ML) — `codelabs.developers.google.com` — hands-on ML Kit and TFLite labs
- CameraX documentation — `developer.android.com/training/camerax` — camera pipeline integration
- KMP documentation — `kotlinlang.org/docs/multiplatform.html` — KMP shared code patterns

---

*Next phase: [Phase 6 — AI-Differentiated Product Layer](phase-06.md)*
