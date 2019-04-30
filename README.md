# m3u8py
stream video downloader

## Usage

```
python run.py [-h] [-k] [-v] [-H HEADERS] url

Download and assemble transport-stream file.

positional arguments:
  url                   the URL to m3u8 file

optional arguments:
  -h, --help                         show this help message and exit
  -k, --keep                         Keep the video file on disk after the post-processing;
                                     the video is erased by default
  -v, --verbose                      Print various debugging information
  -H HEADERS, --header HEADERS       Pass custom header(s) to server
  ```
 ### Example
 ```
 python run.py -k -v https://example.com/stream.m3u8 -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" -H "Referer: https://example.com/" -H "Origin: https://example.com"
 ```
