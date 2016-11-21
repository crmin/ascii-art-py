# ASCII-ART-PY

사용자의 이미지를 ascii text를 이용한 그림으로 바꾸어줍니다

## 개발환경
본 앱은 아래와 같은 환경에서 개발되었습니다.
* macOS Sierra
* Python 3.5 (with virtualenv)
* Pillow 3.4.2

## 동작환경
아래와 같은 조건을 만족하는 환경에서 제대로 동작합니다.
* Python 3.x (virtualenv를 사용하지 않아도 됨)
* Pillow (버전 의존성 확인 필요)

## USAGE
python art.py IMAGE_FILE_PATH  
e.g. `python art.py rocket.jpg`

이미지 파일의 가로 또는 세로의 길이가 100px을 넘지 않는 경우 ascii art를 생성해도 이미지 판별이 불가능할 가능성이 높으므로 이미지 처리를 제한합니다.


## License
MIT License에 따라 자유롭게 이용 가능합니다