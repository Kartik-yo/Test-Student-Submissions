#!/bin/bash

# Exit immediately if any command fails
set -e

# Navigate to project directory
cd "$(dirname "$0")/.."

# Clean and build the project
echo "Building the project..."
mvn clean install

# Run tests
echo "Running tests..."
mvn test

# Output results
echo "Test results available in target/surefire-reports/"
