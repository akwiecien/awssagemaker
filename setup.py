import setuptools


version = '1.0.0'

setuptools.setup(
    name="awssagemaker",
    version=version,
    description="Utils for AWS SageMaker Ground Truth",
    url="https://main.gitlab.in.here.com/here-places/places-ingestion/places-discovery/places-discovery-annotation/awssagemaker.git",
    author="CLANA team",
    author_email="DBE_Cloud_Analytics_Team@here.com",
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=[
        'boto3'
    ]
)
