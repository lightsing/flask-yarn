"""
Flask-yarn
-------------

Flask yarn setup file
"""
from setuptools import setup


setup(
    name='Flask-yarn',
    version='1.0',
    url='https://github.com/lightsing/flask-yarn',
    license='MIT',
    author='lightsing',
    author_email='light.tsing@gmail.com',
    description='serve yarn package with pretty',
    long_description=__doc__,
    py_modules=['flask_yarn'],
    zip_safe=True,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)