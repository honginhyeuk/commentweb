# 베이스 이미지
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 파일 복사
COPY requirements.txt .

# 종속성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY . .

# 정적 파일 수집
RUN python manage.py collectstatic --noinput

# 엔트리포인트 스크립트 복사
COPY entrypoint.sh .

# 엔트리포인트 스크립트 실행 권한 추가
RUN chmod +x /app/entrypoint.sh

# 포트 설정
EXPOSE 8000

# 엔트리포인트 설정
ENTRYPOINT ["/app/entrypoint.sh"]
