import shutil

# shutil.make_archive('another', 'zip', 'files')
# salveaza al doilea file  ca another

shutil.unpack_archive('another.zip', 'another')
# extract!
# formats
# zip: ZIP file
# tar: Uncompresed tar file
# gztar: gzip`ed tar-file
# bztar: bzip2`ed tar-file
# xztar: xzed tar-file

# unpaking
# shutil.make_archive('another', 'gztar', 'files')

#