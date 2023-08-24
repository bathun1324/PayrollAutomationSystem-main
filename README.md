# oams server

<br />

## 개발환경 구성
<br />

### ✅Python & Virtual environment setup from GitHub

- [Python 3.10.x](https://www.python.org/downloads/) 설치
  
> 환경변수 설정
```
(Windows PATH에 추가)
{Python root}
{Python root}\Python Scripts
```

- pipenv (Virtual env & Package Manager) 설치
파이썬에서 공식으로 권장하는 패키지 관리 툴로써 무엇보다 편리하고 안정적으로 패키지 관리가 가능하기 때문에 가상환경 사용 시 가장 추천하는 툴
    
> 설치
```
pip install pipenv
```

- 가상환경 생성 방법
```
mkdir {폴더이름} 
cd {폴더이름}
pipenv –python 3.10
```
    
- 패키지 설치 방법
```
가상환경 실행
pipenv install
```

<br />

### ✅How to use app
   
> **Step 1** - Download the code from the GH repository (using `GIT`) 
```txt
# Get the code
git clone https://github.com/FORELINK/oams_front.git
cd oams_front
```

<br />

> **Step 2** - Install modules via `VENV`
```txt
cd oams_front\venv
pipenv shell
pipenv install
```

<br />

> **Step 3** - Set Up Database
```txt
cd oams_front
python manage.py makemigrations
python manage.py migrate
```

<br />

> **Step 4** - Start the app

```txt
python manage.py runserver
```

the app runs at `http://127.0.0.1:8000/`

<br />
