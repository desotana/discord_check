import setuptools
requirements = []
setuptools.setup(
    name='discord_check',
    version='0.0.1',
    install_requires=requirements,
    packages=setuptools.find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
