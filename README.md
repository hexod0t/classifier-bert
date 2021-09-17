# Fake news Classifier v1.0

## Clone Repo
```bash
git lfs install

git clone https://github.com/hexod0t/classifier-bert.git
```

## if you want to clone without large files – just their pointers
## prepend your git clone with the following env var:
GIT_LFS_SKIP_SMUDGE=1

## Build and Deploy to GCP
```bash
# Build image
gcloud builds submit --tag gcr.io/<project_id>/index

# Deploy image
gcloud run deploy --image gcr.io/<project_id>/index --platform managed
```