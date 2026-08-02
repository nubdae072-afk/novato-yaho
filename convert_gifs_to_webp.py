import os
from PIL import Image

def convert_gif_to_webp(gif_path, webp_path):
    """GIF를 WebP로 변환"""
    try:
        with Image.open(gif_path) as img:
            # GIF의 모든 프레임 추출
            frames = []
            durations = []
            
            for frame_num in range(0, img.n_frames):
                img.seek(frame_num)
                frame = img.convert('RGB')
                frames.append(frame)
                durations.append(img.info.get('duration', 100))
            
            # 첫 번째 프레임 저장
            frames[0].save(
                webp_path,
                'WEBP',
                save_all=True,
                append_images=frames[1:] if len(frames) > 1 else [],
                duration=durations,
                loop=0,
                quality=80,
                method=6
            )
            
        print(f"[OK] 변환 완료: {gif_path} -> {webp_path}")
        return True
    except Exception as e:
        print(f"[FAIL] 변환 실패: {gif_path} - {e}")
        return False

# 1Q GIF 변환
print("=== 1Q GIF → WebP 변환 시작 ===")
for i in range(1, 13):
    gif_path = f"{i}.gif"
    webp_path = f"1q_webp/{i}.webp"
    
    if os.path.exists(gif_path):
        os.makedirs("1q_webp", exist_ok=True)
        convert_gif_to_webp(gif_path, webp_path)
    else:
        print(f"[FAIL] 파일 없음: {gif_path}")

# 3Q GIF 변환
print("\n=== 3Q GIF → WebP 변환 시작 ===")
for i in [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
    gif_path = f"3q/{i}.gif"
    webp_path = f"3q_webp/{i}.webp"
    
    if os.path.exists(gif_path):
        os.makedirs("3q_webp", exist_ok=True)
        convert_gif_to_webp(gif_path, webp_path)
    else:
        print(f"[FAIL] 파일 없음: {gif_path}")

print("\n=== 변환 완료 ===")