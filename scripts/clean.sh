#!/bin/sh
echo "Очистка артефактов сборки..."
rm -rf dist build *.egg-info
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type d -name '*_cache' -exec rm -rf {} +
echo "Очищено."