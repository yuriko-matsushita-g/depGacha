from setuptools import setup

APP = ['gacha_for_build.py']
DATA_FILES = ['members.csv', 'gacha.gif']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'PIL', 'pandas', 'random'],
    'plist': {
        'CFBundleName': 'GachaGachaApplication',
        'CFBundleDisplayName': 'GachaGachaApplication',
        'CFBundleGetInfoString': "Random person display",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0"
    },
    # 'iconfile': 'app_icon.icns',  # アイコンファイルがある場合、ここにパスを指定
    'resources': DATA_FILES,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
