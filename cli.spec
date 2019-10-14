# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['cli.py'],
             pathex=['/home/s_dev_racct/ab_gtx'],
             binaries=[],
             datas=[],
             hiddenimports=['include.fmt', 'include.cli.common.Cli', 'email.mime.application', 'include.extractor.common.Extractor', 'include.loader.common.Loader', 'scandir', 'pysqlite2.dbapi2'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='cli',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
