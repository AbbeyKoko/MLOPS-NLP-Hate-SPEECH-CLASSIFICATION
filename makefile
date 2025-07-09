# Makefile for ML Project environment

# Variables
PROJECT_NAME := hate_classifier
AUTHOR := "Tumelo Koko"
AUTHOR_EMAIL := "u11046644@tuks.co.za"
TEMP_PY ?= template.py
GITHUB_REPO ?= "MLOPS-NLP-Hate-SPEECH-CLASSIFICATION"
CONDA_ENV ?= "Py-NLP-Hate"
PYTHON ?= "3.10"
REQUIREMENTS ?= "requirements.in"
TERRAFORM_DIR := terraform
ANSIBLE_DIR := ansible

# Don't produce files
.PHONY: project github create dvc  dvc-run terraform terraform-destroy automate full-install 


# describe what each target does.
help:
	@echo "Makefile commands:"
	@echo "make project				- Create project structure"
	@echo "make github				- Create GITHUB repo, intialise git and push to remote"
	@echo "make full-project			- Create project structure and initialise git with remote repo"
	@echo "make create				- Creates conda environment and installs pip"
	@echo "make install				- Creates requirements.txt using pip-compile"
	@echo "make dvc				- Install and initialise DVC"
	@echo "make automate				- Install Terraform and Ansible globally"
	@echo "make terraform				- Create resources using terraform"
	@echo "make terraform-destroy				- Destroy resources using terraform"
	@echo "make full-install			- Create  project, repo, conda environment and install packages"


project:
	@if [ -f "$(TEMP_PY)" ]; then \
		echo "Creating project structure for ${PROJECT_NAME}"; \
		PROJECT_NAME=$(PROJECT_NAME) python $(TEMP_PY); \
	else \
		echo "No template.py found"; \
	fi


github:
	echo "Initailise git"
	git init || true
	git add . || true
	git commit -m "Create project structure" || true

	@if [ -n "$(GITHUB_REPO)" ]; then \
		echo "Creating repo : $(GITHUB_REPO)"; \
		gh repo create $(GITHUB_REPO) --public --source=. --remote=origin --push; \
	else \
		echo "Github repo not created, skipping remote repo creation"; \
	fi

full-project: project github

create:
	@if [ -n "$(CONDA_ENV)" ] && [ -n "$(PYTHON)" ]; then \
		conda create --name $(CONDA_ENV) python=$(PYTHON).* -y -q; \
		conda run -n $(CONDA_ENV) pip install -U pip pip-tools; \
	else \
		echo "Missing Conda environment name and or Python version"; \
	fi

install:
	@if [ -n "$(REQUIREMENTS)" ] && [ -f "$(REQUIREMENTS)" ] && [ "$(REQUIREMENTS)" = "requirements.in" ]; then \
		echo "Creating requirements.txt from $(REQUIREMENTS)"; \
		conda run -n $(CONDA_ENV) pip-compile -r $(REQUIREMENTS); \
		echo "Installing from requirements.txt"; \
		conda run -n $(CONDA_ENV) pip install -r requirements.txt; \
	elif [ -f "$(REQUIREMENTS)" ] && [ "$(REQUIREMENTS)" = "requirements.txt" ]; then \
		echo "Installing from $(REQUIREMENTS)"; \
		conda run -n $(CONDA_ENV) pip install -r $(REQUIREMENTS); \
	else \
		echo "No file exists"; \
	fi
	@if [ -f "setup.py" ]; then \
		echo "Creating project as package using setup"; \
		PROJECT_NAME=$(PROJECT_NAME) AUTHOR=$(AUTHOR) AUTHOR_EMAIL=$(AUTHOR_EMAIL) conda run -n $(CONDA_ENV) pip install -e .; \
	fi

full-install: full-project create install

dvc:
	conda run -n $(CONDA_ENV) pip install dvc
	conda run -n $(CONDA_ENV) dvc init --force
	echo "DVC initialised."

dvc-run:
	# conda run -n $(CONDA_ENV) dvc repro


automate:
	echo "Installing terraform"
	brew install terraform || true
	echo "Installing ansible"
	brew install ansible || true

terraform:
	cd $(TERRAFORM_DIR) && \
	terraform init && \
	terraform plan -out=secure.tfplan && \
	terraform apply -auto-approve secure.tfplan && \
	terraform output -json > tf_outputs.json

terraform-destroy:
	@read -p "Really destroy all infrastructure? [y/N] " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		cd $(TERRAFORM_DIR) && \
		terraform destroy -auto-approve; \
	else \
		echo "Destroy cancelled."; \
	fi

