import parse as strParse
import re

class ParserNotImplemented(NotImplementedError):
    pass

class FormatNotRecognized(ValueError):
    pass

formats = {'local': [strParse.compile("/local/{uf}/{cidade}/{categoria}/{lbsid}/{titulo}.html"),
                     strParse.compile("/local/{uf}/{cidade}/{categoria}/{lbsid}/{titulo}.html?{headers}")
                    ],
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

def getParsedData(parserobj, path):
    if isinstance(parserobj, list):
        for parser in parserobj:
            parsed = parser.parse(path)
            if parsed is not None:
                return parsed
        raise FormatNotRecognized("Failed to parse this object")
    else:
        parsed = parserobj.parse(path)
        if parsed is None:
            raise FormatNotRecognized("This")
        else:
            return parsed

def parse(path):
    pathType = getPathType(path)
    parser = getCorrectParser(pathType)
    parsedData = getParsedData(parser, path)
    return {k: fixSpaces(v) for k,v in parsedData.named.items()}
