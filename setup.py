from distutils.core import setup

setup(
    name='tasveer',
    packages=['tasveer'],
    version='0.1',
    license='MIT',
    description='Download test images from Google',
    author='Abhinav Srivastava',
    author_email='atg271@gmail.com',
    url='https://abhinavmir.github.io',
    download_url='https://github.com/AbhinavMir/tasvir/archive/0.1.tar.gz',
    keywords=['test', 'google', 'images', 'download'],
    install_requires=[
        'google_images_download'
    ],
    extras_require={
        'dev': ['pylint', 'autopep8']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
