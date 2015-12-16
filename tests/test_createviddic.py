#!/usr/bin/python3
import unittest
import unittest.mock as mock
import ampnadoo.createviddic

class TestCreateVidDictTestCase(unittest.TestCase):
	def setUp(self):
		self.CreateVidDict = ampnadoo.createviddic.CreateVidDict()
		self.opt = {'catname':'cat1'}
		self.avlist5 = [
			"/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4",
			"/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4",
			"/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4",
			"/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4",
			'/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4',
			'/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4', 
			'/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4', 
			'/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4']
		self.avlist6 = [
			('/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4', 'cat1'),
			('/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4', 'cat1'), 
			('/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4', 'cat1'), 
			('/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4', 'cat1'), 
			('/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4', 'cat1'), 
			('/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4', 'cat1'), 
			('/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4', 'cat1'), 
			('/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4', 'cat1')]
		self.cvvd = {
			'filesize': 1328562128, 
			'vid_playpath': 'Music/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4', 
			'vid_id': '140508252572584',
			'catname': 'cat1', 
			'vid_name': 'Avengers Grimm', 
			'dirpath': '/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video', 
			'filename': '/usr/share/ampnado/static/MUSIC/cat1/0994c6c991284a99a9d26e28d85d8057/Video/Avengers.Grimm.mp4'}

	def tearDown(self):
		self.CreateVidDict = None
		self.avlist5 = None
		self.avlist6 = None
		self.cvvd = None

	def test_add_catname(self):
		z = self.CreateVidDict.add_catname(self.avlist5, self.opt)
		self.assertEqual(z, self.avlist6)

	@mock.patch('ampnadoo.createviddic.CreateVidDict.insert', return_value='inserted')
	@mock.patch('os.path.getsize', return_value=1328562128)
	@mock.patch('ampnadoo.createviddic.CreateVidDict.uuidd', return_value='140508252572584')
	def test_create_vid_dict(self, ins_function, osgs_function, uuid_function):
		ccvd = self.CreateVidDict._create_vid_dict(self.avlist6[0])
		self.assertEqual(ccvd, self.cvvd)

	def suite(self):
		TestCreateVidDictTestSuite = unittest.TestSuite()
		TestCreateVidDictTestSuite.addTest(TestCreateVidDictTestCase('test_add_catname', 'test_create_vid_dict'))
		return TestCreateVidDictTestSuite