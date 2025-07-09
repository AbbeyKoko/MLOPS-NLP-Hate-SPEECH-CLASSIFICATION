import os
from pathlib import Path

project_name = os.getenv("PROJECT_NAME", "src")

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_training.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_deployment.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/stage_01_data_ingestion_train_pipeline.py",
    f"{project_name}/pipeline/stage_02_data_validation_train_pipeline.py",
    f"{project_name}/pipeline/stage_03_data_transformation_train_pipeline.py",
    f"{project_name}/pipeline/stage_04_model_training_train_pipeline.py",
    f"{project_name}/pipeline/stage_05_model_evaluation_train_pipeline.py",
    f"{project_name}/pipeline/stage_06_model_deployment_train_pipeline.py",
    f"{project_name}/pipeline/inference_pipeline.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",
    "README.md",
    "app.py",
    "demo.py",
    "setup.py",
    "install_requirements.sh",
    "requirements.in",
    "Dockerfile" ".dockerignore",
    "config/schema.yaml",
    "config/model.yaml",
    ".env",
    "dvc.yaml",
    "static/css/style.css",
    "templates/index.html",
    "bootstrap.sh",
    "terraform/main.tf",
    "terraform/variables.tf",
    "terraform/outputs.tf",
    "terraform/secret.auto.tfvars",
    "terraform/modules/new/main.tf",
    "terraform/modules/new/variables.tf",
    "terraform/modules/new/outputs.tf",
    "ansible/bootstrap.sh",
    "ansible/group_secrets/secrets.yml",
    "ansible/inventory/inventory.ini",
    "ansible/roles/new/tasks/main.yml",
    "ansible/roles/new/templates/test.json.j2",
    "ansible/bootstrap.yml",
    "ansible/deployment.yml",
    "ansible/ansible.cfg",
    "ansible/requirements.yml",
    "ansible/vault_pass.txt",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File is already present at {filepath}")
