from fastapi import FastAPI, status, HTTPException
from agent.my_agent import my_agent
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    text: str

@app.get("/health")
def health():
    return {
        "message": "API running"
    }


@app.post("/chat")
def reply(request: ChatRequest):
    try:
        response = my_agent.invoke({
            "messages": [{
                "role": "user",
                "content": request.text
            }]
        })

        return {
            "result": response["messages"][-1].content,
            "status_code": status.HTTP_201_CREATED
        }

    except Exception as e:
        raise HTTPException(detail=f"Error while reply: {str(e)}", status_code=500)
