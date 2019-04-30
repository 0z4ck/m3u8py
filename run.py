from m3u8 import MpegTS
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Download and assemble transport-stream file.')
    parser.add_argument('url' ,help='the URL to m3u8 file')
    parser.add_argument('-k','--keep', dest='keep', action='store_true', help='Keep the video file on disk after the post-processing; the video is erased by default')
    parser.add_argument('-v','--verbose', dest='verbose', action='store_true', help='Print various debugging information')
    parser.add_argument('-H','--header', dest='headers', action='append', help='Pass custom header(s) to server')
    
    args = parser.parse_args()
    
    
    headers = [(h.split(":")[0],h[h.index(":")+1:]) for h in args.headers]
    
    
    m = MpegTS(args.keep, args.verbose, args.url, headers=headers)
    
    m._loadTsUrls()
    m._retrieve()
