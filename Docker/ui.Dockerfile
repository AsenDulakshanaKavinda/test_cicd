# 1. base image
FROM python:3.13-slim

# 2. set the working  dir inside the container
WORKDIR /app

# 3.1 copy dependencies file
COPY pyproject.toml .

# 3.2 install the dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN pip install uv && uv pip install --system .

# 4. copy project files
COPY . .

# 5. expose a post
EXPOSE 8501

# 6. run
CMD ["streamlit", "run", "UI/interface.py", "--server.port=8501", "--server.address=0.0.0.0"]