from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='dashactyl.py',
    version='0.0.3',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/Mystik-Lukas/dashactyl.py',  
    author='Lukas Canter',
    author_email='lukascanter07@outlook.com',
    license='MIT', 
    classifiers=classifiers,
    keywords='dahsactyl', 
    packages=find_packages(),
    install_requires=['requests'] 
)