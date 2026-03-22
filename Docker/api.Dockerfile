# 1. base image
FROM python:3.13-slim

# 2. set the working dir inside the container
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Install system deps if needed (optional)
# RUN apt-get update && apt-get install -y build-essential

# 4.1 copy dependencies file
COPY pyproject.toml .

# 4.2
RUN pip install uv && uv pip install --system .


# 6. copy project files
COPY . .

# 7. expose a port
EXPOSE 8000

# 8. run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
