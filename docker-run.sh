#!/bin/bash
celery -A tasks worker --loglevel=info &
flask run --host=0.0.0.0