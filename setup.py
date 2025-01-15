from setuptools import setup, find_packages

setup(
    name='ML-CODE FROM SCRATCH',                #  package name
    version='0.1.0',                         #  package version
    description='Python implementations of some of the fundamental Machine Learning models and algorithms from scratch.',
    #author='Your Name',                      #  name
    #author_email='your_email@example.com',    #  email address
    #url='https://github.com/yourusername/your_project',  # GitHub repository or project URL
    packages=find_packages(),                # Automatically find all the packages in the directory
    install_requires=[                       # List of dependencies your package needs
        'numpy>=1.18',
        'scikit-learn',
        'matplotlib',
        # Add any other dependencies here
    ],
    classifiers=[                            # Classifiers that tell PyPI about your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                  # Minimum Python version required
)
