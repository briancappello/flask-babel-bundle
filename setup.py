from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='Flask Babel Bundle',
    version='0.1.0',
    description='Adds support for translations to Flask Unchained',
    long_description=long_description,
    url='https://github.com/briancappello/flask-babel-bundle',
    author='Brian Cappello',
    license='MIT',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'flask-unchained>=0.2.1',
        'flask-babelex>=0.9.3',
    ],
    extras_require={
        'dev': [
            'coverage',
            'pytest',
            'pytest-flask',
            'tox',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
