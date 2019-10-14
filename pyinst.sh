 ~/py27/bin/pyinstaller --log-level=DEBUG --onefile --nowindow --hidden-import=include.fmt \
 --hidden-import=include.cli.common.Cli \
 --hidden-import=email.mime.application \
 --hidden-import=include.extractor.common.Extractor \
 --hidden-import=scandir \
 --hidden-import=pysqlite2 \
 --hidden-import=pysqlite2.dbapi2 \
cli.py
