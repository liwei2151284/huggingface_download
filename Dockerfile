FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY download_from_Artifactory_huggingface.py .

# 声明 build args
ARG HF_REPO_ID
ARG HF_REVISION
ARG HF_LOCAL_DIR

# 让 build arg 变成容器内部的 ENV（可选）
ENV HF_REPO_ID=${HF_REPO_ID}
ENV HF_REVISION=${HF_REVISION}
ENV HF_LOCAL_DIR=${HF_LOCAL_DIR}

# 使用 build arg 运行下载脚本
RUN python download_from_Artifactory_huggingface.py

CMD ["python", "main.py"]
