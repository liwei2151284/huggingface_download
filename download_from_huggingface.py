# download_model.py
import os
from huggingface_hub import snapshot_download

def main():
    repo_id = os.getenv("HF_REPO_ID", "bert-base-uncased")
    revision_id = os.getenv("HF_RVERSION", "main")

    print(f"Start downloading model: {repo_id}")
    print(f"Target dir: {local_dir}")

    snapshot_download(
        repo_id=repo_id, 
        revision=revision_id, 
        etag_timeout=86400
    )

    print("Model download finished!")

if __name__ == "__main__":
    main()
