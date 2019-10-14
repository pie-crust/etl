 ~/py27/bin/pyinstaller --log-level=DEBUG --onefile --nowindow \
 --hidden-import=include.fmt \
 --hidden-import=pysqlite2.dbapi2 \
vcli.py
