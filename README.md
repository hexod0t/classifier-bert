# classifier-fake-news-bert
# Cloud build & Deploy
gcloud builds submit --tag gcr.io/<project_id>/index
gcloud run deploy --image gcr.io/<project_id>/index --platform managed