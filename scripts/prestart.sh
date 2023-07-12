#! /usr/bin/env bash

# Run migrations
echo "RUNNING MIGRATIONS"

alembic upgrade head

echo "MIGRATION APPLIED"