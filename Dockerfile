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

# 포트 설정
EXPOSE 8000

# 명령어 설정
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_project1.wsgi:application"]
