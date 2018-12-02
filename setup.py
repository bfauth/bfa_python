import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bfa_django",
    version="0.1.3",
    author="Artjom Löbsack",
    author_email="ceigh@pm.me",
    license="Apache 2.0",
    description="Using user's browser fingerprint for authentication.",
    long_description=long_description,
    url="https://gitlab.com/bfa/bfa_django",
    keywords="django fingerprint auth",
    packages=setuptools.find_packages(),
    project_urls={
        "BFA": "https://gitlab.com/bfa"
    },
    python_requires='>=3.6, <4',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
