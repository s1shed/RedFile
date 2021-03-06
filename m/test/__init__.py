# Part of RedFile
#
# Author: Outflank B.V. / Mark Bergman / @xychix
#
# License : BSD3
import shelve
import codecs
import os

## usage:
# /m/test/
# /test/FILE.EXT_MIMETYPE/CHOSENFILE.EXT
# http://lab.outflank.nl:18080/test/aap.jpg_jpg/x.jpg
# http://lab.outflank.nl/~mark/downloader.wsgi/test/aap.jpg_jpg/x.jpg
# basic url or redirector.....................|modname|key.....|notused
class f():
  def __init__(self,key,h,req={}):
    self.key = key.encode("utf-8",'ignore')
    cwd = os.path.dirname(os.path.realpath(__file__))
    self.folder = cwd

  def fileContent(self):
    ff = self.key.split('_')[0]
    with open("%s/%s"%(self.folder,ff), 'rb') as f:
      return f.read()

  def fileType(self):
    ff = self.key.split('_')[1]
    dd =  { "a": "application/octet-stream",
    "ai": "application/postscript",
    "aif": "audio/x-aiff",
    "aifc": "audio/x-aiff",
    "aiff": "audio/x-aiff",
    "au": "audio/basic",
    "avi": "video/x-m    svideo",
    "bat": "text/plain",
    "bin": "application/octet-stream",
    "bmp": "image/x-ms-bmp",
    "c": "text/plain",
    "cdf": "application/x-cdf",
    "csh": "application/x-csh",
    "css": "text/css",
    "dll": "application/octet-stream",
    "doc": "application/msword",
    "dot": "application/msword",
    "dvi": "application/x-dvi",
    "eml": "message/rfc822",
    "eps": "application/postscript",
    "etx": "text/x-setext",
    "exe": "application/octet-stream",
    "gif": "image/gif",
    "gtar": "application/x-gtar",
    "h": "text/plain",
    "hdf": "application/x-hdf",
    "htm": "text/html",
    "html": "text/html",
    "jpe": "image/jpeg",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "js": "application/x-javascript",
    "json": "application/json",
    "ksh": "text/plain",
    "latex": "application/x-latex",
    "m1v": "video/mpeg",
    "man": "application/x-troff-man",
    "me": "application/x-troff-me",
    "mht": "message/rfc822",
    "mhtml": "message/rfc822",
    "mif": "application/x-mif",
    "mov": "video/quicktime",
    "movie": "video/x-sgi-movie",
    "mp2": "audio/mpeg",
    "mp3": "audio/mpeg",
    "mp4": "video/mp4",
    "mpa": "video/mpeg",
    "mpe": "video/mpeg",
    "mpeg": "video/mpeg",
    "mpg": "video/mpeg",
    "ms": "application/x-troff-ms",
    "nc": "application/x-netcdf",
    "nws": "message/rfc822",
    "o": "application/octet-stream",
    "obj": "application/octet-stream",
    "oda": "application/oda",
    "pbm": "image/x-portable-bitmap",
    "pdf": "application/pdf",
    "pfx": "application/x-pkcs12",
    "pgm": "image/x-portable-graymap",
    "png": "image/png",
    "pnm": "image/x-portable-anymap",
    "pot": "application/vnd.ms-powerpoint",
    "ppa": "application/vnd.ms-powerpoint",
    "ppm": "image/x-portable-pixmap",
    "pps": "application/vnd.ms-powerpoint",
    "ppt": "application/vnd.ms-powerpoint",
    "pptx": "application/vnd.ms-powerpoint",
    "ps": "application/postscript",
    "pwz": "application/vnd.ms-powerpoint",
    "py": "text/x-python",
    "pyc": "application/x-python-code",
    "pyo": "application/x-python-code",
    "qt": "video/quicktime",
    "ra": "audio/x-pn-realaudio",
    "ram": "application/x-pn-realaudio",
    "ras": "image/x-cmu-raster",
    "rdf": "application/xml",
    "rgb": "image/x-rgb",
    "roff": "application/x-troff",
    "rtx": "text/richtext",
    "sgm": "text/x-sgml",
    "sgml": "text/x-sgml",
    "sh": "application/x-sh",
    "shar": "application/x-shar",
    "snd": "audio/basic",
    "so": "application/octet-stream",
    "src": "application/x-wais-source",
    "swf": "application/x-shockwave-flash",
    "t": "application/x-troff",
    "tar": "application/x-tar",
    "tcl": "application/x-tcl",
    "tex": "application/x-tex",
    "texi": "application/x-texinfo",
    "texinfo": "application/x-texinfo",
    "tif": "image/tiff",
    "tiff": "image/tiff",
    "tr": "application/x-troff",
    "tsv": "text/tab-separated-values",
    "txt": "text/plain",
    "ustar": "application/x-ustar",
    "vcf": "text/x-vcard",
    "wav": "audio/x-wav",
    "wiz": "application/msword",
    "wsdl": "application/xml",
    "xbm": "image/x-xbitmap",
    "xlb": "application/vnd.ms-excel",
    "xls": "application/vnd.ms-e    xcel",
    "xlsx": "application/vnd.ms-excel",
    "xml": "text/xml",
    "xpdl": "application/xml",
    "xpm": "image/x-xpixmap",
    "xsl": "application/xml",
    "xwd": "image/x-xwindowdump",
    "zip": "application/zip"}

    if dd.has_key(ff):
      return(dd[ff])
    else:
      return('plain/unknown')
