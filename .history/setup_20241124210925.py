import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "1.0.0"

REPO_NAME = "textSummarization"
AUTHOR_USER_NAME = "chan"
SRC_REPO = f"https://github.com/SOFTENGIC/{REPO_NAME}.git"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email="chan@github.com",
    description="A simple text summarization tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/SOFTENGIC/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
