from langchain_openai import ChatOpenAI
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env", override=True)

api_key = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL", "https://monogpt.kr/api/monorouter/v1")

def llm_connect(
    model: str,
    api_key: str = api_key,
    temperature: float = 0,
    max_tokens: int = 512
):
    if not api_key:
        raise ValueError("프로젝트 .env에 LLM_API_KEY를 설정하세요.")
    return ChatOpenAI(
        model=model,
        api_key=api_key,
        base_url=BASE_URL,
        temperature=temperature,
        use_responses_api=False,  # base url로 할 때는 이부분 넣어야 함.(MonoRouter 사용)
        max_tokens=max_tokens,
    )
