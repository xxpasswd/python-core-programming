from setuptools import setup

setup(
    name='module_name',
    version='1.0',
    py_modules=['which_module'],
    include_package_data=True,
    install_requires=[
        'require_module',
    ],
    # 
    entry_points='''
        [console_scripts]
        command_name = your_module:function
    ''',
)