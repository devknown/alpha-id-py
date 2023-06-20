from setuptools import setup, find_packages

setup(
    name='alpha_id',
    version='0.0.4',
    description='Python library for generating short alphanumeric strings from integers',
    long_description='Python library that allows you to generate short alphanumeric strings from integers. It can be useful for creating compact, unique, and obfuscated identifiers.',
    author='Hassan Azzi',
    author_email='devknown@gmail.com',
    url='https://github.com/devknown/alpha-id-py',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='alpha-id alphanumeric string generator',
    install_requires=[
        # Add your dependencies here
    ],
    python_requires='>=3.6',
)
