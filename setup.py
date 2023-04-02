import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="curriculum_module_generator",
    version="0.0.1",
    author="Nathan Laundry",
    author_email="nathan.laundry@gmail.com",
    description="Generates a jupyter notebook and markdown file for a topic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheAcademicsFieldGuideToWritingCode/Tutorials-Generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "openai",
        "nbformat",
        "markdown2",
        "markdownify",
        "tqdm"
    ],
    entry_points={
        "console_scripts": [
            "curriculum_module_generator=curriculum_module_generator.main:cli",
        ],
    },
)
