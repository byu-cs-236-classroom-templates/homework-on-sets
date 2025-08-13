#!/usr/bin/env bash
set -euo pipefail

PATTERN="${1:-test_*}"
FILE="tests/test_integration_tests.py"

pytest -q "$FILE" -k "$PATTERN"
