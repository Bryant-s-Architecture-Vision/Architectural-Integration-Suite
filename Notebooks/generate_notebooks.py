import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
from datetime import datetime

# Project and stage details
project_name = "ArchIntegSuite"
stages = ["Dev", "Test", "Deploy"]

components = [
    "UID Generator", "ML & Infra Domain Classifier", "Azure ML & Terraform Resource Mapper",
    "Integrated Architecture Mapper", "Stereotype Definer", "Resource Descriptor and Validator",
    "Visualization and Access Control Planner", "Interdependency Mapper", "Use Case and Context Analyzer",
    "Profile Mapping and Integration", "Custom Diagram Designer", "Modeling Toolbox Customizer",
    "Starter Model Generator", "MDG Technology File Assembler", "Script and Extension Integrator",
    "Reusable Model Fragment Creator", "MDG Integration Controller", "File Reader", "Data Processor",
    "Data Exporter", "Data Validation", "Diagram Artifact and Pattern Manager", "SQL Architecture Repository Connector",
    "Configuration Manager"
]

# Function to create a basic Jupyter notebook structure
def create_notebook_json(component_name):
    # Notebook cells
    cells = []

    # Add Markdown cells for the notebook overview and sections
    cells.append(new_markdown_cell(f"# {component_name} Notebook\n"))
    cells.append(new_markdown_cell(
        """
        # Notebook Overview
        # -----------------
        # This notebook is a part of the Architectural Integration Suite and focuses on the '{}' component.
        # It guides you through setting up an Azure ML environment, testing the component, and preparing for deployment.

        # Sections:
        # 1. Environment Setup
        # 2. Code Testing
        # 3. Deployment Preparation
        # 4. Additional Information and Best Practices
        """.format(component_name)))

    # Add Markdown cell for Environment Setup
    cells.append(new_markdown_cell(
        """
        # 1. Environment Setup
        # ---------------------
        # This section covers the setup of your Azure ML environment.
        # Ensure that you have your conda specification YAML file (e.g., 'conda-specification.yml') ready.
        """))

    # Add Code cell for importing libraries and setting up Azure ML workspace
    cells.append(new_code_cell(
        """
        # Import required libraries
        from azure.ai.ml import MLClient
        from azure.identity import DefaultAzureCredential
        from azure.ai.ml.entities import Environment

        # Define Azure ML workspace details
        subscription_id = '<SUBSCRIPTION_ID>'
        resource_group = '<RESOURCE_GROUP>'
        workspace_name = '<AZUREML_WORKSPACE_NAME>'

        # Connect to the Azure ML workspace
        ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace_name)

        # Define the environment from the Conda specification
        env_name = "your_environment_name"
        conda_spec_path = "path/to/your/conda-specification.yml"
        env_from_conda = Environment(name=env_name, conda_file=conda_spec_path)

        # Create or update the environment in Azure ML
        ml_client.environments.create_or_update(env_from_conda)
        """
    ))

    # Additional Markdown and Code cells for other sections can be added similarly

    # Create a new notebook
    notebook = new_notebook(cells=cells)

    return notebook

notebooks_dir = "Notebooks"

# Create the main notebooks directory if it doesn't exist
if not os.path.exists(notebooks_dir):
    os.makedirs(notebooks_dir)

# Generate notebook files
for component in components:
    # Create a directory for each component
    component_dir = os.path.join(notebooks_dir, component.replace(' ', '_'))
    if not os.path.exists(component_dir):
        os.makedirs(component_dir)

    for stage in stages:
        formatted_component_name = component.replace(' ', '_')
        version = datetime.now().strftime("%Y%m%d")  # Current date as version
        file_name = f"{project_name}_{formatted_component_name}_{stage}_{version}.ipynb"
        file_path = os.path.join(component_dir, file_name)

        notebook_json = create_notebook_json(component)
        with open(file_path, 'w', encoding='utf-8') as file:
            nbformat.write(notebook_json, file)

print(f"Generated {len(components) * len(stages)} notebook files in organized packages within the '{notebooks_dir}' directory.")