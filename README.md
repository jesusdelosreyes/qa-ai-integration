# QA Agent Generator (LangChain + Pytest)

This project allows you to automatically generate and run tests using AI (OpenAI, LangChain), integrating Selenium for web testing and requests for API testing.

## How to use

1. Install the dependencies:
```bash
pip install -r requirements.txt
```
2. Remove .example from the .env file and add your API Key:
```
 OPENAI_API_KEY=sk-xxxxxx
```
3. Run the app:
```bash
streamlit run app.py
```
4. Write a prompt such as:
> "Test that the API https://jsonplaceholder.typicode.com/posts returns 200"

## Author
Jesus De Los Reyes

## ----------------------------------------------------------------------------------

## 🤖 AI Model Selection Strategy

This QA Agent uses OpenAI's LLMs via LangChain. Depending on use case (cost, speed, or intelligence), you can switch models in `test_generator.py`.

### 🔍 Why GPT-4.1 Mini?

- ✅ Balanced cost vs quality ($0.40 input / $1.60 output per 1M tokens)
- 🚀 Fast generation for tests (Web/API) under 1s
- 🧠 Smart enough to generate valid Selenium, Requests, and Pytest code

### 🧪 Token Primer

- **Tokens** are chunks of words (≈ 750 tokens ≈ 1 page of text)
- You pay for **input + output**
- **Cached inputs** (reused prompts) are cheaper

### 💰 Estimated Cost per Test Prompt

| Model         | Input (100t) | Output (500t) | Total Cost  |
|---------------|--------------|----------------|-------------|
| GPT-4.1 mini  | $0.00004     | $0.0008        | ~$0.00084   |
| o4-mini       | $0.00011     | $0.0022        | ~$0.0023    |

Switching to `gpt-4.1-nano` can reduce cost further for low-stakes tests.

### ⚙️ Model configuration (in `test_generator.py`)

```python
llm = OpenAI(
    temperature=0,
    model="gpt-4.1-mini",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)



