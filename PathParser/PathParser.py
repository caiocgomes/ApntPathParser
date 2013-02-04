import parse as strParse
import re

class ParserNotImplemented(NotImplementedError):
    pass

formats = {'local': strParse.compile("/local/{uf}/{cidade}/{categoria}/{lbsid}/{titulo}.html"),
           'em':    strParse.compile("/em/{uf}_{cidade}/{categoria}/em_{em}")}

def fixSpaces(string):
    return re.sub('[_|-]', ' ', string)

def getPathType(path):
    return path.split('/')[1]

def getCorrectParser(pathType):
    try:
        parser = formats[pathType]
        return parser
    except KeyError:
        raise ParserNotImplemented("There's no parser implemented for this kind of url")

def parse(path):
    pathType = getPathType(path)
    parser = getCorrectParser(pathType)
    parsedData = parser.parse(path)
    return {k: fixSpaces(v) for k,v in parsedData.named.items()}
