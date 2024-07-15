#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import socket

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connexion fictive à une adresse externe
        local_ip_address = s.getsockname()[0]
        s.close()
        return local_ip_address
    except socket.error:
        return None



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xender.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    ip = get_local_ip()
    
    execute_from_command_line(['manage.py', 'migrate'])
    if ip : 

        execute_from_command_line(['manage.py', 'runserver', f'0.0.0.0:8000'])
    else :
        execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000'])



if __name__ == '__main__':
    
    main()
