import os, sys, requests, re, argparse
from pathlib import Path
from requests_html import HTMLSession

#%%
def scrape_links(url, pat = None):
    """
    Scrapes all links on page, optionally accepts filename pattern
    """
    session = HTMLSession()
    r = session.get(url)
    parsed_html = r.html
    links = [e for e in parsed_html.absolute_links]
    if pat:
        links = [e for e in links if re.search(pat, e)]
    return links

# %%
def download(url):
    """
    downloads URL to binary using requests
    """
    try:
        fn = url.rsplit('/', 1)[-1]
        r = requests.get(url)
        with open(fn,'wb') as f:
            f.write(r.content)
        print(url.rsplit('/', 1)[-1] + ' download successful.')
    except:
        print(url.rsplit('/', 1)[-1] + ' failed to download.')
        pass

# %%
def writelist(filelist, targetpath):
    """
    writes list to plaintext file specified in targetpath
    """
    with open(targetpath, "w") as outfile:
        outfile.write("\n".join(filelist))

# %%
def download_files(filelist, targetdir):
    """
    creates output folder and calls download to dl files from list
    to specified location
    """
    cwd = os.getcwd()
    # create folder
    Path(targetdir).mkdir(parents = True, exist_ok = True)
    os.chdir(targetdir)
    for f in filelist:
        download(f)
    os.chdir(cwd)

# %%
def unwebsitifier(link):
    """
    removes website prefixes / shortens URL to conform to windows' folder
    name limits
    """
    folder = re.sub(r'http|https|.edu|.org|[^\w]', '', link)
    return (folder[-20:])

# %%
