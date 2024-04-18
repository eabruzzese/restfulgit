# coding=utf-8
import os
from datetime import timedelta

# base path for repositories that should be exposed
RESTFULGIT_REPO_BASE_PATH = os.getenv("RESTFULGIT_REPO_BASE_PATH")
# default number of commits that should be returned by /repos/<repo_key>/git/commits/
RESTFULGIT_DEFAULT_COMMIT_LIST_LIMIT = os.getenv("RESTFULGIT_DEFAULT_COMMIT_LIST_LIMIT", 50)

# Cross-Origin Resource Sharing
RESTFULGIT_ENABLE_CORS = os.getenv("RESTFULGIT_ENABLE_CORS", "False").lower() == "true"
RESTFULGIT_CORS_ALLOWED_ORIGIN = os.getenv("RESTFULGIT_CORS_ALLOWED_ORIGIN", "*")
RESTFULGIT_CORS_ALLOW_CREDENTIALS = os.getenv("RESTFULGIT_CORS_ALLOW_CREDENTIALS", "False").lower() == "true"
RESTFULGIT_CORS_ALLOWED_HEADERS = os.getenv("RESTFULGIT_CORS_ALLOWED_HEADERS", "").split(",")
RESTFULGIT_CORS_MAX_AGE = timedelta(days=int(os.getenv("RESTFULGIT_CORS_MAX_AGE", 30)))
