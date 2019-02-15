from setuptools import setup, find_packages

version = '1.0.0'

requires = [
    'systemd-python',
]

test_requires = requires + [
    'circus',
    'circus-web',
]

setup(name='ExtendedJournalHandler',
      version=version,
      description="Python logging handler extending functionality of basic journal handler from systemd-python",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='ktarasz',
      author_email='ktarasz@quintagroup.com',
      url='',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require={
          'test': test_requires,
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
