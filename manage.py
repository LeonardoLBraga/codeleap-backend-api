#!/usr/bin/env python
"""
Command-line utility for administrative tasks in a Django project.

This script sets up the environment and executes management commands,
such as running the development server, applying migrations, or creating superusers.

It also loads environment variables from a .env file using python-dotenv,
allowing for secure and configurable deployment.
"""
import os
import sys

from dotenv import load_dotenv
load_dotenv()

def main():
    """
    Set the default Django settings module and execute command-line tasks.

    This function initializes the Django application environment and
    delegates execution to Django's management command system.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeleap_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django..."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
