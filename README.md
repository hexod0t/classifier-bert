# Fake news Classifier v1.0
# Build image
gcloud builds submit --tag gcr.io/<project_id>/index

# Deploy service
gcloud run deploy --image gcr.io/<project_id>/index --platform managed