# To-do list Web Application (Flask + MongoDB + Nginx + Docker Compose)

이 프로젝트는 **Flask 백엔드**, **MongoDB 데이터베이스**, **Nginx 웹 서버**, 그리고 **Docker Compose**를 이용하여 구성된 간단한 웹 기반 To-do List 애플리케이션입니다.

---

##  프로젝트 구조

```
todo_project/
├── app
│   ├── app.py              # Flask 백엔드 애플리케이션
│   ├── Dockerfile          # Flask 컨테이너용 Dockerfile
│   └── requirements.txt    # Flask 의존성 목록
├── nginx
│   └── index.html          # 사용자 입력을 위한 웹 UI
├── data/                   # MongoDB 데이터 저장 디렉토리 (volume 연결용)
├── docker-compose.yml      # 전체 시스템 구성
└── .gitignore              # Git 제외 파일 목록
```

---

##  실행 방법

Docker와 Docker Compose가 설치된 환경에서 아래 명령어를 실행하세요.

```bash
docker-compose up --build
```

### 접속 주소

- **웹 UI (Nginx)**: [http://localhost:8080](http://localhost:8080)
- **Flask API**:
  - Add: `POST http://localhost:5000/add`
  - List: `GET http://localhost:5000/list`
- **Mongo Express (MongoDB 관리자 웹 UI)**: [http://localhost:8081](http://localhost:8081)  
  - 로그인: `admin` / `pass`

---

## 주요 기능

-  사용자로부터 날짜, 할 일, 만나는 사람, 마감일을 입력받아 MongoDB에 저장
-  저장된 항목을 JSON 형태로 조회 (`/list` endpoint)
-  Nginx를 통한 정적 웹 UI 제공
-  Docker Compose를 통한 멀티 컨테이너 구성 (Flask + MongoDB + Nginx)

---

## 주의 사항

- Flask 개발 서버는 `개발용`이며, 운영 환경에서는 **Gunicorn**, **uWSGI** 같은 WSGI 서버 사용을 권장합니다.
- MongoDB 데이터는 `data/` 디렉토리에 영속 저장됩니다.
- `.gitignore`를 통해 `.pyc`, `__pycache__`, `.DS_Store`, `*.swp` 등은 Git에서 제외됩니다.

---

## 작성자

- Taejoon Kong  
- GitHub: [@tkong88](https://github.com/tkong88)  
- Email: taejoonkong@gmail.com

