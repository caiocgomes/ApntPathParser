import unittest
import yaml
import PathParser


class TestApntURLParser(unittest.TestCase):
    def setUp(self):
        confs = yaml.load(open('data.yml', 'r'))
        self.localPaths = confs['localPaths']
        self.emPaths = confs['emPaths']

    def testPathType(self):
        for case in self.localPaths:
            pathType = PathParser.getPathType(case['path'])
            self.assertTrue(pathType, 'local')
        for case in self.emPaths:
            pathType = PathParser.getPathType(case['path'])
            self.assertTrue(pathType, 'em')

    def testParse(self):
        for case in self.localPaths:
            parsed = PathParser.parse(case['path'])
            self.assertEqual(parsed['uf'], case['uf'])
            self.assertEqual(parsed['lbsid'], case['lbsid'])
            self.assertEqual(parsed['cidade'], case['cidade'])
            self.assertEqual(parsed['categoria'], case['categoria'])

        for case in self.emPaths:
            parsed = PathParser.parse(case['path'])
            self.assertEqual(parsed['uf'], case['uf'])
            self.assertEqual(parsed['cidade'], case['cidade'])
            self.assertEqual(parsed['categoria'], case['categoria'])
            self.assertEqual(parsed['em'], case['em'])
