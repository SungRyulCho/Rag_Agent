# MonoRouter 실습 설정

실제 키는 상위 `Rag_Agent/.env`의 `LLM_API_KEY`에 저장합니다.
`LLM_BASE_URL`을 생략하면 `https://monogpt.kr/api/monorouter/v1`을 사용합니다.
노트북은 실행 디렉터리부터 상위 폴더의 `.env`를 찾습니다.
프로젝트 루트나 해당 노트북 폴더를 작업 디렉터리로 사용하세요.

`ChatOpenAI`는 OpenAI 호환 클라이언트입니다. 실습에서는 키와 주소를
명시하여 MonoRouter의 Chat Completions API를 호출합니다.
OpenAI 계정의 별도 키는 사용하지 않습니다.

변경된 노트북을 다시 열고 커널을 재시작한 뒤 환경 설정 셀부터 실행하세요.
01번 노트북을 먼저 실행할 필요는 없습니다. 각 노트북에서 환경을 읽습니다.
모델 이름은 교육에서 제공한 MonoRouter 지원 목록과 일치해야 합니다.

임베딩 예제도 MonoRouter 주소로 설정했습니다. 다만 제공받은 안내만으로는
`/embeddings` 및 `text-embedding-3-small` 지원 여부를 확인할 수 없습니다.
지원하지 않는 경우 별도 임베딩 모델을 설정해야 합니다.
기존 Ollama 예제는 API 키 없이 Ollama 서버를 호출하는 별도 실습입니다.
