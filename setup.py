from setuptools import setup

requirements = []
extra_requirements = {
    "dev": [
        "pre-commit",
        "pytest",
    ]
}

setup(
    name="devcloud",
    version="0.1",
    description="Devcloud utitlies",
    url="http://github.com/rscohn2/devcloud",
    author="Robert Cohn",
    author_email="rscohn2@gmail.com",
    license="MIT",
    packages=["devcloud"],
    entry_points={
        "console_scripts": ["devcloud=devcloud.cli:main"],
    },
    install_requires=requirements,
    extras_require=extra_requirements,
    zip_safe=False,
)
