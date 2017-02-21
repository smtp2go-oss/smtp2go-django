from setuptools import setup

setup(name='smtp2go-django',
      version='0.0.1',
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
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries"
      ],
      zip_safe=False)
