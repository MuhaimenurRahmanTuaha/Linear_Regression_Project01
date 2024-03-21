from setuptools import setup,find_packages

def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name = "Linear_Regression_AI_Setup",
    version = "0.0.1",
    author = "Muhaimenur Rahman Tuaha",
    author_email = "muhaimenurrahmantuaha@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)