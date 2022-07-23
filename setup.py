from setuptools import setup

setup(
    name='fast_api_test',
    version='0.0.1',
    author='Andrew',
    author_email='andrewdragowork@gmail.com',
    description='test fastAPI application',
    install_requires=['fastapi==0.79.0',
                      'uvicorn==0.18.2',
                      'SQLAlchemy==1.4.39',
                      'pytest==7.1.2',
                      'requests==2.28.1'
                      ],
    scripts=['app/main.py', 'scripts/create_db.py']

)
# -------Activate environment pip install -e . for add setup to environment ---
