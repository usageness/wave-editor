# wave-editor

물리적 환경 및 녹음 장비로 인해 오디오 파일에 포함되는 노이즈를 제거하는 작업을 수행하는 오디오 처리 소프트웨어입니다.

## 사용 방법

1. 먼저 필요한 라이브러리를 설치합니다.

```python
$ pip install librosa matplotlib spleeter pydub
```

2. `main.py` 파일을 실행합니다.

```bash
$ main.py
```

3. 노이즈를 제거할 음성 파일을 입력합니다.

4. 작업이 종료되면 `./output` 경로에 파일이 저장되고, 스펙트럼을 통해 작업 전/후 결과를 비교할 수 있습니다.

![image](/result.png)

### License

[MIT License](https://opensource.org/license/mit/)

- **librosa**
  - ISC License
- **spleeter**
  - MIT License
- **pydub**
  - MIT License
