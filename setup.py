from setuptools import setup

setup(
    name='xs',
    version='0.0.1',
    description='A module for creation of endpoint of the open-sourced LLMs like Meta LLaMA3, Mistral, NeoGPT, and more...',
    url='https://github.com/xprabhudayal/xs.git',
    author='Prabhudayal Vaishnav',
    author_email='pradachan@tuta.io',
    license='MIT',
    py_modules=['xs'],
    install_requires=[
        'flask',
        'pyngrok',
        'transformers'
    ],
    zip_safe=False
)
