from parsers.containermanager import ContainerManagerParser
from tests import SysdiagnoseTestCase
import unittest
import os


class TestParsersContainermanager(SysdiagnoseTestCase):

    def test_parsecontainermanager(self):
        for case_id, case in self.sd.cases().items():
            p = ContainerManagerParser(self.sd.config, case_id=case_id)
            files = p.get_log_files()
            self.assertTrue(len(files) > 0)

            p.save_result(force=True)
            self.assertTrue(os.path.isfile(p.output_file))

            result = p.get_result()
            for item in result:
                self.assertTrue('timestamp' in item)
                self.assertTrue('loglevel' in item)
                self.assertTrue('hexID' in item)
                self.assertTrue('loglevel' in item)
                self.assertTrue('msg' in item)


if __name__ == '__main__':
    unittest.main()
