from setuptools import setup

package_name = 'rqt_sample'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    package_dir={'': 'src'},    # srcから読み込み
    # 各読み込みファイルの指定
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros2user',
    maintainer_email='ikemoto.lab.kyutech@gmail.com',
    # 概要説明
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    # 起動コマンドの設定
    entry_points={
        'console_scripts': [
            'sample = ' + package_name + '.main:main',
        ],
    },
)
