import os
import sys

def create_project_structure():
    """Create the basic project structure."""
    # Directories to create
    directories = [
        'data',
        'src',
        'visualizations',
    ]
    
    # Create directories
    for dir_name in directories:
        os.makedirs(dir_name, exist_ok=True)
        # Create .gitkeep files
        if dir_name in ['data', 'visualizations']:
            with open(os.path.join(dir_name, '.gitkeep'), 'w') as f:
                pass

    # Create __init__.py in src
    with open(os.path.join('src', '__init__.py'), 'w') as f:
        pass

    # Create requirements.txt
    requirements = [
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'jupyter',
        'plotly',
    ]
    
    with open('requirements.txt', 'w') as f:
        f.write('\n'.join(requirements))

    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()