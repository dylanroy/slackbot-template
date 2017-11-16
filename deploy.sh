GOOGLE_PROJECT=INSTERT_PROJECT_HERE
gcloud auth activate-service-account --key-file=$HOME/$GOOGLE_PROJECT.json
gcloud config set project $GOOGLE_PROJECT
gcloud config set app/cloud_build_timeout 3600
gcloud app deploy -v 0-1-0