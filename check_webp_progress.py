import os

print("=== WebP 변환 상태 확인 ===")
print("\n[1q_webp]")
if os.path.exists("1q_webp"):
    files = os.listdir("1q_webp")
    print(f"  총 {len(files)}개 파일 생성됨")
    for f in sorted(files)[:5]:
        print(f"    {f}")
    if len(files) > 5:
        print(f"    ... 외 {len(files)-5}개")
else:
    print("  폴더 없음")

print("\n[3q_webp]")
if os.path.exists("3q_webp"):
    files = os.listdir("3q_webp")
    print(f"  총 {len(files)}개 파일 생성됨")
    if files:
        for f in sorted(files)[:5]:
            print(f"    {f}")
else:
    print("  폴더 없음")

print("\n=== 완료 ===")