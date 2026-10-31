from setuptools import setup, find_packages

setup(
    name="l4z4n3t-ai",
    version="1.0.0",
    author="L4z4n3T",
    description="Advanced Cyber Pentesting Platform & Autonomous Red Teaming Engine",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/L4z4n3T-AI",
    packages=find_packages(),
    py_modules=["client", "server", "subdomain_enum", "reporter"],
    install_requires=[
        "mcp",
        "rich",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "l4z4n3t=client:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security",
    ],
    python_requires=">=3.10",
)
