"""Copyright 2019 Artjom Löbsack

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="bfa",
    version="1.2.1",
    author="Artjom Löbsack",
    author_email="ceigh@pm.me",
    license="Apache 2.0",
    description="Using user's browser fingerprint \
for authentication in your web application.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://gitlab.com/bfa/bfa_python",
    keywords="browser fingerprint authentication flask django",
    packages=setuptools.find_packages(),
    install_requires=['django>=1.6', 'werkzeug'],
    python_requires='>=3.5, <4',
    project_urls={
        "BFA project": "https://gitlab.com/bfa",
        "BFA demo site": "https://bfa.pythonanywhere.com"
    },
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
