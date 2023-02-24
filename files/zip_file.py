import zipfile

my_zip = zipfile.ZipFile('files.zip','w')

my_zip.write('test.txt')
my_zip.write('thunbnail.png')

# https: // youtu.be/z0gguhEmWiY?t = 241

# with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.write('test.txt')
#     my_zip.write('thunbnail.png')

# https: // youtu.be/z0gguhEmWiY?t = 353

# with zipfile.ZipFile('files.zip', 'r', compression=zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.extractall('files')
#     # my_zip.write('thunbnail.png')

# https: // youtu.be/z0gguhEmWiY?t = 644


