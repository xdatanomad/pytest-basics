from setuptools import setup, find_packages

# Read the requirements from requirements.txt
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='gitallica',
    version='0.1',
    packages=find_packages(include=['gitallica', 'gitallica.*', 'tests']),
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your package',
    url='https://github.com/yourusername/gitallica',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
