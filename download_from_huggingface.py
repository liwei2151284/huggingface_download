from huggingface_hub import snapshot_download
snapshot_download(
    repo_id="<model_name>", revision="<model_revision>", etag_timeout=86400
)
