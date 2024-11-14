from setuptools import setup, find_packages

setup(
    name='translator',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    author='Usmonov Shoxruxmirzo',
    author_email='usmonovshohruxmirzo@gmail.com',
    description='Multi language translator',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/webbro-software/multi-language-translator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)