import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

with open(os.path.join(here, 'pyshop', '__init__.py')) as v_file:
    version = re.compile(r".*__version__ = '(.*?)'",
                         re.S).match(v_file.read()).group(1)

requires = [
    'pyramid',
    'waitress',
    'SQLAlchemy',
#    'pyramid_debugtoolbar',
    'pyramid_scss',
    'pyramid_jinja2',
    'pyramid_xmlrpc',

    'pyramid_tm',
    'zope.sqlalchemy',

    'cryptacular',
    'requests',
    'docutils',

    'IPython',
]


if 'VIRTUAL_ENV' in os.environ:
    venv = os.environ['VIRTUAL_ENV']
    data_files = [(venv, ['development.ini',
                          ])]
else:
    data_files = []


setup(name='pyshop',
      version=version,
      description='pyshop',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.7',
      'Development Status :: 4 - Beta',
      'Environment :: Web Environment',
      'Framework :: Pyramid',
      'Topic :: Internet :: WWW/HTTP',
      'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
      'Topic :: Software Development',
      'Topic :: System :: Archiving :: Mirroring',
      'Topic :: System :: Archiving :: Packaging',
      'Intended Audience :: Developers',
      'Intended Audience :: System Administrators',
      'License :: OSI Approved :: BSD License',
      ],
      author='Guillaume GAUVRIT',
      author_email='ggauvrit@laposte.net',
      url='https://github.com/mardiros/pyshop',
      keywords='web wsgi pyramid cheeseshop pypi packaging',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pyshop',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = pyshop:main
      [console_scripts]
      pyshop_install = pyshop.bin.install:main
      pyshop_shell = pyshop.bin.shell:main
      """,
      paster_plugins=['pyramid'],
      data_files=data_files,
      )
