# RAG Agent 실습

LangChain의 기본 구성 요소부터 문서 검색과 답변 생성까지 익히는 Python 실습 저장소입니다. Jupyter Notebook에서 코드를 실행하고, 검색 결과와 답변을 원문과 비교하며 개선한 내용을 기록합니다.

## 실습 구성

| 폴더 | 내용 |
|---|---|
| `course/1.langchain_basic/` | 채팅 모델, 프롬프트, 출력 파서, Runnable, Tool, Agent |
| `course/2.naive_rag/` | 문서 로딩, 청킹, 임베딩, FAISS, Retriever, RAG 파이프라인 |
| `course/toy_pjt1/` | 금융사기 보고서 기반 질의응답 |

`course/common_config.py`에서 답변 생성 모델의 연결 설정을 관리합니다.

## Toy Project 1 — 금융사기 보고서 QA

「진화하는 금융사기, 모두의 경계가 필요한 시점」 PDF를 검색해 질문에 답하고 근거 페이지를 표시합니다.

```text
PDF → 텍스트 추출·공백 정리 → 청킹 → 임베딩 → FAISS 저장
질문 → 관련 청크 검색 → 문서와 질문을 LLM에 전달 → 답변·출처 반환
```

- PDF 15페이지를 로딩하고, 연속된 공백을 정리한 뒤 27개 청크로 분할
- `chunk_size=800`, `chunk_overlap=120`으로 청킹
- `text-embedding-3-small`로 임베딩하고 FAISS 인덱스를 로컬에 저장
- 질문과 관련된 청크 4개를 검색해 `gpt-4.1`에 전달
- 답변과 검색된 문서의 페이지·청크 번호를 함께 출력

[실습 노트북](course/toy_pjt1/data/1_faiss_naive_rag_financial_fraud_pdf.ipynb)

### 확인한 내용

전기통신금융사기와 투자사기의 차이를 질문하고, 답변 내용을 검색된 원문과 비교했습니다. 문서에 없는 2026년 6월 기준 피해 금액을 물었을 때는 확인할 수 없다고 답하는 것을 확인했습니다.

예방 시스템에 관한 답변에서는 원문의 “네트워크 구축이 요구된다”는 권고를 이미 시행 중인 사실처럼 표현하는 문제가 있었습니다. 프롬프트에 시행·계획·권고를 구분하도록 추가한 뒤 해당 표현이 빠졌습니다. 수정 전후 프롬프트 차이와 답변 비교는 노트북 마지막에 정리했습니다.

출처가 표시돼도 답변이 원문을 정확히 반영하는지 별도로 확인해야 합니다. 위 결과는 실습한 질문에 대한 확인 기록입니다. 근거 페이지는 보고서에 인쇄된 쪽수가 아닌 PDF 파일의 페이지 순서입니다.

## 실행 방법

Python 3.12 이상과 `uv`를 사용합니다. 아래 명령은 저장소 루트에서 실행합니다.

```bash
uv venv --python 3.12
uv pip install --python .venv/bin/python -r course/pyproject.toml
uv pip install --python .venv/bin/python langchain-community langchain-text-splitters pypdf faiss-cpu pandas
```

Toy Project에 필요한 일부 패키지는 현재 `course/pyproject.toml`에 없어 별도로 설치합니다. 이미 `.venv`가 있다면 생성 명령은 생략합니다.

루트의 `.env.example`을 `.env`로 복사하고 발급받은 키를 입력합니다. 기존 `.env`가 있다면 그대로 사용합니다.

```dotenv
LLM_API_KEY=your_monorouter_api_key
LLM_BASE_URL=https://monogpt.kr/api/monorouter/v1
```

이 실습은 MonoRouter를 통해 모델을 호출하므로 해당 서비스의 키와 모델 접근 권한이 필요합니다. 실제 키가 들어 있는 `.env`는 Git에서 제외합니다.

```bash
.venv/bin/python -m ipykernel install --user --name rag-agent --display-name "RAG Agent (Python 3.12)"
.venv/bin/python -m jupyterlab
```

노트북에서 위 커널을 선택하고 셀을 위에서부터 실행합니다. Toy Project의 PDF 상대 경로는 노트북이 있는 `course/toy_pjt1/data/` 폴더를 기준으로 합니다.

## 인덱스 재사용

FAISS 인덱스는 처음 실행할 때 생성하고 이후에는 저장된 파일을 불러옵니다. PDF, 전처리, 청킹 설정 또는 임베딩 모델을 바꾸면 인덱스도 다시 생성해야 합니다.

생성된 인덱스와 IDE 설정은 Git에서 제외합니다. 인덱스를 불러올 때는 직접 생성한 신뢰할 수 있는 파일만 사용합니다.
