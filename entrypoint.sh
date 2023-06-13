#!/bin/bash
set -e

# Function to start Gunicorn with dynamic reload-extra-file options
start_gunicorn() {
    # Generate the reload-extra-file options dynamically
    extra_files=$(find /app/templates -name "*.html" -printf "--reload-extra-file %p ")

    # Start Gunicorn
    echo "Starting Gunicorn..."
    gunicorn --config gunicorn-cfg.py --reload --reload-engine=poll $extra_files core.wsgi
}

# Start Gunicorn
start_gunicorn
