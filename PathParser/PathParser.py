import parse as strParse
import re

formats = {'local': strParse.compile("/local/{uf}/{cidade}/{categoria}/{lbsid}/{titulo}.html"),
           'em':    strParse.compile("/em/{uf}_{cidade}/{categoria}/em_{em}")}

def fixSpaces(string):
    return re.sub('[_|-]', ' ', string)

def getPathType(path):
    return path.split('/')[1]

def parse(path):
    pathType = getPathType(path)
    parser = formats[pathType]
    parsedData = parser.parse(path)
    return {k: fixSpaces(v) for k,v in parsedData.named.items()}
