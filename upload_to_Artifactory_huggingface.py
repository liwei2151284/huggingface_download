# download_model.py
import os
from huggingface_hub import HfApi

def main():
    repo_id = os.getenv("HF_REPO_ID", "test")
    revision_id = os.getenv("HF_RVERSION", "main")
  

    print(f"Start uploading model: {repo_id}")

    api = HfApi()
    api.upload_folder(
        folder_path = os.getenv("HF_LOCAL_DIR", f"./models/{repo_id}") ,
        repo_id=repo_id, # defines the name under which model will be saved in the local repo. (models--${model_name})
        revision=revision_id, # represents git revision under which files are stored (main by default) (snapshots/${revision}/...files)
        repo_type="model"
    )
    print("Model upload finished!")

if __name__ == "__main__":
    main()
