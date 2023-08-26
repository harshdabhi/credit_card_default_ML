from setuptools import find_packages,setup

def get_requirements():
    with open('requirements.txt','r+') as f:
        p=f.read()
        list_req=p.split('\n')
    return list_req


setup(

    name='credit_card_default',
    version='1.0.0',
    author='harsh_dabhi',
    author_email='harshdabhi67@gmail.com',
    packages=find_packages(),
    install_require=get_requirements()
    

)