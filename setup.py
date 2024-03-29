import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="indigo_utils",
    version="0.0.3",
    author="Pandaaaa906",
    author_email="ye.pandaaaa906@gmail.com",
    description="A small useful tools for epam.indigo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pandaaaa906/indigo_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'epam.indigo',
    ]
)
