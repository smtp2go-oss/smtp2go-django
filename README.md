[![Build Status](https://travis-ci.org/smtp2go-oss/smtp2go-django.svg?branch=master)](https://travis-ci.org/smtp2go-oss/smtp2go-django)
[![Coverage Status](https://coveralls.io/repos/github/smtp2go-oss/smtp2go-django/badge.svg?branch=master)](https://coveralls.io/github/smtp2go-oss/smtp2go-django?branch=master)
[![PyPI version](https://badge.fury.io/py/smtp2go.svg)](https://badge.fury.io/py/smtp2go)
[![Dependency Status](https://gemnasium.com/badges/github.com/smtp2go-oss/smtp2go-django.svg)](https://gemnasium.com/github.com/smtp2go-oss/smtp2go-django)
[![Code Climate](https://codeclimate.com/github/smtp2go-oss/smtp2go-django/badges/gpa.svg)](https://codeclimate.com/github/smtp2go-oss/smtp2go-django)
[![Issue Count](https://codeclimate.com/github/smtp2go-oss/smtp2go-django/badges/issue_count.svg)](https://codeclimate.com/github/smtp2go-oss/smtp2go-django)
[![license](https://img.shields.io/github/license/smtp2go-oss/smtp2go-django.svg)]()

# smtp2go-django

Python/Django wrapper for interfacing with the [smtp2go](https://www.smtp2go.com) API

You may not need this library at all! If you want to use the SMTP server directly, simply set the following in your settings.py:

    
    EMAIL_HOST = 'smtp.smtp2go.com'
    EMAIL_HOST_USER = '<your registered email>'
    EMAIL_HOST_PASSWORD = '<Your password>'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

    # Django defaults to this backend, but if you'd like to be explicit:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

## Installation

Add this line to your application's requirements.txt:

    smtp2go-django

Or install it yourself with pip:

    $ pip install smtp2go-django

## Usage

Sign up for a free account [here](https://www.smtp2go.com/pricing) and get an API key. At your shell, run:

    $ export API_KEY="<your_API_key>"

  In settings.py, set:

    EMAIL_BACKEND = 'mailer.email_backend.SMTP2GoEmailBackend'
Then you can hook into Django's inbuilt email sending:


    from django.core.mail import send_mail

    send_mail(
        subject='Trying out smtp2go',
        message='Test Message',
        from_email='dave@example.com',
        recipient_list=['matt@example.com']
    )

Full API documentation can be found [here](https://apidoc.smtp2go.com/documentation/#/README) and for your convenience, here are [Django's email docs](https://docs.djangoproject.com/en/1.10/topics/email/)


## Development

Clone repo and install requirements into a virtualenv. Run tests with `pytest`.

## Contributing

Bug reports and pull requests are welcome on GitHub [here](https://github.com/smtp2go-oss/smtp2go-django)

## License

The package is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
