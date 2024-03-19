# Chicken-Disease-Classification--Project

## Workflows
1. Update `config.yaml`
2. Update `secrets.yaml` (Optional)
3. Update `params.yaml`
4. Update the entity
5. Update the configuration manager in `src/config`
6. Update the components
7. Update the pipeline 
8. Update `main.py`
9. Update `dvc.yaml`

## How to run?
1. Clone the repository
2. Create a conda environment after opening the repository
   ```bash
   conda create -n cnncls python=3.8 -y
   conda activate cnncls
   ```
3. Install the requirements
   ```bash
   pip install -r requirements.txt
   ```
4. Run the following command
   ```bash
   python app.py
   ```
5. Open up your localhost and port

## DVC cmd
1. `dvc init`
2. `dvc repro`
3. `dvc dag`

## AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment
3. Create ECR repo to store/save docker image
4. Create EC2 machine (Ubuntu) 
5. Install Docker in EC2 Machine
6. Configure EC2 as self-hosted runner
7. Setup GitHub secrets

## AZURE-CICD-Deployment-with-Github-Actions
1. Save pass
2. Run from terminal: Docker build, login, and push
3. Deployment Steps

These instructions provide a comprehensive guide on how to set up, run, and deploy your project using various services and tools. If you have any specific questions or need further assistance with any of the steps, feel free to ask!