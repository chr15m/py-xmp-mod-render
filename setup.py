from setuptools import setup

setup(
    name='modrender',
    version='0.0.1',
    url='https://github.com/chr15m/py-xmp-mod-render.git',
    author='Chris McCormick',
    author_email='chris@mccormick.cx',
    description='Render tracker modules with XMP.',
    py_modules=['modrender'],
    install_requires=[],
    entry_points='''
        [console_scripts]
        modrender=modrender:modrender
    '''
)
