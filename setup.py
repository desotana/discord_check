import setuptools

setuptools.setup(
    name='discord_check',
    version='0.0.1',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)