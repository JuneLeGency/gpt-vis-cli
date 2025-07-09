from setuptools import setup, find_packages

setup(
    name="gpt-vis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pydantic>=1.9.1,<2.0.0",
    ],
    entry_points={
        'console_scripts': [
            'gpt-vis = gpt_vis:main',
        ],
    },
)
