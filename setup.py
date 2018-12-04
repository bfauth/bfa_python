import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bfa",
    version="0.1.10",
    author="Artjom Löbsack",
    author_email="ceigh@pm.me",
    license="2.0",
    description="Using user's browser fingerprint for authentication.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://gitlab.com/bfa/bfa_django",
    keywords="django fingerprint auth",
    packages=setuptools.find_packages(),
    project_urls={
        "BFA": "https://gitlab.com/bfa"
    },
    classifiers=[
        "Programming Language :: Python 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
