import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tidy import tidy


class TidyTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def touch(self, name):
        path = self.tmp / name
        path.write_text("x")
        return path

    def test_moves_files_into_categories(self):
        self.touch("photo.jpg")
        self.touch("notes.txt")
        self.touch("clip.mp4")
        moved = tidy(self.tmp)
        self.assertEqual(moved, 3)
        self.assertTrue((self.tmp / "Images" / "photo.jpg").exists())
        self.assertTrue((self.tmp / "Documents" / "notes.txt").exists())
        self.assertTrue((self.tmp / "Videos" / "clip.mp4").exists())

    def test_dry_run_moves_nothing(self):
        self.touch("video.mp4")
        tidy(self.tmp, dry_run=True)
        self.assertTrue((self.tmp / "video.mp4").exists())
        self.assertFalse((self.tmp / "Videos").exists())

    def test_unknown_extension_goes_to_others(self):
        self.touch("data.xyz123")
        tidy(self.tmp)
        self.assertTrue((self.tmp / "Others" / "data.xyz123").exists())

    def test_does_not_overwrite_same_name(self):
        (self.tmp / "Images").mkdir()
        (self.tmp / "Images" / "a.jpg").write_text("old")
        self.touch("a.jpg")
        tidy(self.tmp)
        self.assertEqual((self.tmp / "Images" / "a.jpg").read_text(), "old")
        self.assertTrue((self.tmp / "Images" / "a (1).jpg").exists())


if __name__ == "__main__":
    unittest.main()
