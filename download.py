import urllib.request

print('Beginning file download with urllib2...')

url = 'http://bioinfo.wilmer.jhu.edu/tiger/download/tss_spf_rsc.txt'
urllib.request.urlretrieve(url, '/Users/darrenchang/Desktop/ONCOGX/TIGER-parser/tss_spf_rsc.txt')