from setuptools import setup

setup(name='smtp2go-django',
      version='1.0.0',
      description='Library for interacting with the SMTP2Go API via Django.',
      url='https://github.com/smtp2go-oss/smtp2go-django',
      author='SMTP2Go',
      author_email='devs@smtp2go.com',
      license='MIT',
      packages=['smtp2go_django'],
      install_requires=[
          'smtp2go'
      ],
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Topic :: Communications :: Email",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      zip_safe=False)
