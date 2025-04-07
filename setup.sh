#!/bin/bash
# Create the main project folder
mkdir -p taksoai-hvac-parser && cd taksoai-hvac-parser

# Create backend directories and files
mkdir -p backend/app backend/data backend/scripts
echo "# Backend for TaksoAi HVAC Parser" > backend/README.md
echo "fastapi\nuvicorn\nlangchain\npypdf2\npdfplumber\nPyMuPDF" > backend/requirements.txt

# Create frontend directories and files
mkdir -p frontend/public frontend/src
echo "# Frontend for TaksoAi HVAC Parser" > frontend/README.md
echo "{\n  \"name\": \"taksoai-hvac-parser-frontend\",\n  \"version\": \"1.0.0\",\n  \"private\": true,\n  \"dependencies\": {}\n}" > frontend/package.json

# Create root level README.md and LICENSE
echo "# TaksoAi HVAC Product Brochure Parser" > README.md
echo "MIT License" > LICENSE

# Create a .gitignore file with Python and Node ignores
cat <<EOL > .gitignore
# Python
venv/
__pycache__/
*.py[cod]

# Node
node_modules/
dist/
build/

# VSCode settings
.vscode/
EOL

echo "Repository structure created successfully!"
