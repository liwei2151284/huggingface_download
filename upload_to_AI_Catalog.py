
import frogml
import os

def main():

    repo_id = os.getenv("HF_REPO_ID", "test")
    revision_id = os.getenv("HF_RVERSION", "main")

    base_projects_directory = os.getenv("HF_LOCAL_DIR", f"./models/{repo_id}") 
    frogml.huggingface.log_model(   
        model= finetuned_model,
        tokenizer= tokenizer,
        repository="kk-huggingface-dev-local",    # The JFrog repository to upload the model to.
        model_name=repo_id,     # The uploaded model name
        version=revision_id,     # Optional. The uploaded model version
    )
    print("--- Model Logged Successfully ---")

if __name__ == "__main__":
    main()
