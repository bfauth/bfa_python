# Copyright 2018 Artjom Löbsack
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bfa-django",
    version="0.1.2",
    author="Artjom Löbsack",
    author_email="ceigh@pm.me",
    license="",
    description="Using user's browser fingerprint for authentication.",
    long_description=long_description,
    url="https://gitlab.com/bfa/bfa-django",
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
