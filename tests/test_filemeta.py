#!/usr/bin/python3
import unittest
import unittest.mock as mock
import ampnadoo.filemeta

class TestFileMetaTestCase(unittest.TestCase):
	def setUp(self):	
		self.fm = ampnadoo.filemeta.GetFileMeta()
		self.bogus = '/bogus/path/to/file/boo.ogg'
		self.bogus1 = {'filename': self.bogus}
		self.bogus_dir = '/bogus/path/to/file'
	
	def tearDown(self):
		self.fm = None
		self.bogus = None
		self.bogus1 = None
		self.bogus_dir = None

	def test_size(self):
		self.assertEqual(self.fm.size(self.bogus), '001')

	def test_dirpath(self):
		self.assertEqual(self.fm.dirpath(self.bogus), self.bogus_dir)

	def test_split_lower(self):
		self.assertEqual(self.fm.split_lower(self.bogus), '.ogg')

	def test_uuidd(self):
		uuid1 = self.fm.uuidd()
		uuid2 = self.fm.uuidd()
		self.assertNotEqual(uuid1, uuid2)

	def test_get_file_meta(self):
		boo = self.fm.get_file_meta(self.bogus1)
		self.assertEqual(boo['filesize'], '001')
		self.assertEqual(boo['dirpath'], self.bogus_dir)
		self.assertEqual(boo['filetype'], '.ogg')
		self.assertNotEqual(boo['songid'], '456456')

	def suite(self):
		TestFileMetaTestSuite = unittest.TestSuite()
		TestFileMetaTestSuite.addTest(TestFileMetaTestCase('test_size', 'test_dirpath',
			'test_split_lower', 'test_uuidd', 'test_get_file_meta',
		))		
		return TestFileMetaTestSuite