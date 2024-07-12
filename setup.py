from setuptools import setup

package_name = 'rqt_sample'

setup(
    name=package_name,
    version='2.0.3',
    packages=[package_name],
    package_dir={'': 'src'},　# srcから読み込み
    # 各読み込みファイルの指定
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),　
        ('share/' + package_name, ['plugin.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Your Name',
    maintainer='Your Name',
    maintainer_email='yourmail@hoge.com',
    keywords=['ROS'],
    # 任意の説明を追加
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    # 概要説明
    description=(
        'sample_pkg provides a GUI sample plugin.'
    ),
    license='Hoge',
    entry_points={
        'console_scripts': [
            'sample = ' + package_name + '.main:main'
        ],
    },
)