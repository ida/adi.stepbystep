# -*- coding: utf-8 -*-
"""
This module contains the tool of adi.stepbystep
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.2dev'

long_description = (read('README.rst'))

tests_require = ['zope.testing']

setup(name='adi.stepbystep',
      version=version,
      description="A stepbystep system for Plone",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['adi', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
      'adi.devgen',
                        'collective.wfcomment'
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='adi.stepbystep.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
