# APK 패키징 가이드

이 문서는 PWA로 빌드된 노바토 야호팀 웹앱을 Android APK로 패키징하는 방법을 설명합니다.

## 방법 1: Bubblewrap (권장)

### 1. 환경 설정

```bash
# Java Development Kit (JDK) 11 이상 설치
# Android SDK 설치
# Node.js 설치

# Bubblewrap CLI 설치
npm install -g @bubblewrap/cli
```

### 2. 프로젝트 초기화

```bash
# 프로젝트 폴더에서 실행
bubblewrap init --manifest=./manifest.json
```

### 3. APK 빌드

```bash
# 디버그 APK 빌드
bubblewrap build --type=apk

# 또는 릴리즈 AAB 빌드 (Google Play Store용)
bubblewrap build --type=aab
```

### 4. 출력 파일

- `build/outputs/apk/debug/app-debug.apk` - 디버그 APK
- `build/outputs/bundle/release/app-release.aab` - 릴리즈 AAB

## 방법 2: PWABuilder (온라인 서비스)

### 1. PWABuilder 접속
- https://www.pwabuilder.com 접속

### 2. URL 입력
- 사이트 URL 입력: `https://novato-yaho.netlify.app`

### 3. 빌드 및 다운로드
- "Build" 버튼 클릭
- Android APK 다운로드
- iOS IPA 다운로드 (선택사항)

### 4. Play Store 배포 (선택사항)
- "Publish" 탭에서 Google Play Store 업로드 가이드 확인

## 방법 3: Cordova/PhoneGap

### 1. Cordova 설치

```bash
npm install -g cordova
```

### 2. 프로젝트 생성

```bash
cordova create novato-yaho-app com.novato.yaho "노바토 야호팀"
cd novato-yaho-app
```

### 3. 플랫폼 추가

```bash
cordova platform add android
```

### 4. 설정 파일 수정

`config.xml` 파일 수정:
```xml
<?xml version='1.0' encoding='utf-8'?>
<widget id="com.novato.yaho" version="1.0.0"
    xmlns="http://www.w3.org/ns/widgets"
    xmlns:cdv="http://cordova.apache.org/ns/1.0">
    <name>노바토 야호팀</name>
    <description>노바토 야호팀 코칭 영상 분석 앱</description>
    <author email="coach@novato-yaho.com" href="https://novato-yaho.netlify.app">
      노바토 야호팀
    </author>
    <content src="https://novato-yaho.netlify.app" />
    <access origin="*" />
    <allow-intent href="http://*/*" />
    <allow-intent href="https://*/*" />
    <allow-navigation href="https://novato-yaho.netlify.app/*" />
    <preference name="Fullscreen" value="false" />
    <preference name="Orientation" value="any" />
    <preference name="SplashScreen" value="screen" />
    <icon src="res/icon.png" />
    <splash src="res/screen.png" />
</widget>
```

### 5. 빌드

```bash
# 디버그 빌드
cordova build android

# 릴리즈 빌드 (서명 필요)
cordova build android --release
```

### 6. APK 위치
- `platforms/android/app/build/outputs/apk/debug/app-debug.apk`

## 방법 4: TWA (Trusted Web Activity) - 가장 권장

### TWA 장점
- 최신 Android 기능 지원
- Google Play Store 배포 가능
- 오프라인 캐싱 자동 지원
- PWA 기능 완전 지원

### 설정 단계

1. **Android Studio 설치**
   - https://developer.android.com/studio

2. **TWA 프로젝트 생성**
   - Android Studio에서 "Trusted Web Activity" 프로젝트 템플릿 사용
   - 또는 Bubblewrap 사용 (방법 1 참고)

3. **Digital Asset Links 설정**
   - 도메인에 `assetlinks.json` 파일 배포
   - Google Play Console에 SHA256 지문 등록

4. **빌드 및 배포**
   ```bash
   ./gradlew assembleRelease
   ```

## 배포 방법

### 1. 직접 배포 (APK)
- 빌드된 APK를 팀원들에게 직접 전달
- "알 수 없는 소스" 허용 후 설치

### 2. Google Play Store (권장)
1. Google Play Console 가입
2. 앱 등록 및 스토어 정보 작성
3. AAB (Android App Bundle) 업로드
4. 심사 대기 (보통 1-3일)

### 3. Firebase App Distribution (테스트용)
- Firebase Console에서 앱 배포
- 테스터 초대 및 피드백 수집

## 주의사항

1. **HTTPS 필수**
   - PWA는 HTTPS에서만 작동
   - Netlify는 자동으로 HTTPS 제공

2. **manifest.json 확인**
   - `start_url`, `display`, `icons` 필수 필드 확인
   - 이미지 크기 및 해상도 권장사항 준수

3. **오프라인 지원**
   - Service Worker로 오프라인 캐싱 구현 완료
   - 주요 리소스 사전 캐싱 확인

4. **성능 최적화**
   - 이미지 압축 (WebP, AVIF)
   - MP4 비디오 사용 (GIF 대신)
   - Lazy Loading 적용

## 테스트 체크리스트

- [ ] 앱 설치 성공
- [ ] 홈 화면 아이콘 표시
- [ ] 오프라인에서도 작동
- [ ] 비디오 재생 정상
- [ ] YouTube 연동 작동
- [ ] AI 기능 작동 (API 키 입력 시)
- [ ] 모바일 가로모드 대응
- [ ] 터치 제스처 (스와이프) 작동

## 문제 해결

### "앱이 설치되지 않습니다"
- Android 설정 > 보안 > 알 수 없는 소스 활성화
- 디버그 모드인 경우 USB 디버깅 허용

### "Service Worker가 작동하지 않습니다"
- HTTPS 사용 확인
- Chrome DevTools > Application > Service Workers 확인

### "PWA 설치 프롬프트가 나타나지 않습니다"
- Chrome 68+ 사용 확인
- manifest.json 유효성 검사
- HTTPS 사용 확인

## 참고 자료

- [PWA Builder](https://www.pwabuilder.com)
- [Bubblewrap](https://github.com/nicedoc/bubblewrap)
- [TWA Documentation](https://developer.chrome.com/docs/android/trusted-web-activity/)
- [WebAPK](https://web.dev/samsung-internet-web-apk/)

---

**노바토 야호팀** 🏀
Novato Yaho Basketball Team