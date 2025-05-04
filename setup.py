from setuptools import setup, find_packages

setup(
    name="fast-sso",
    version="0.1.0",
    description="Simplify the way to integrate Google SSO within your fastapi project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Saif A",
    author_email="you@example.com",
    url="https://github.com/yourusername/fastapi-library",  # Update with your repo URL
    license="MIT",
    packages=find_packages(),  # Automatically find sub-packages
    install_requires=[
        "fastapi>=0.100.0",
        "aiohttp>=3.8.0",
        "requests>=2.31.0",
        "python-jose>=3.3.0",
        "pydantic>=1.10.11"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",  # Specify the minimum Python version
)