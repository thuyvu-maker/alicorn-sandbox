import pathlib
import unittest

README = pathlib.Path(__file__).resolve().parent.parent / "README.md"


class ReadmeTest(unittest.TestCase):
    def setUp(self):
        self.text = README.read_text(encoding="utf-8")

    def test_has_title(self):
        self.assertTrue(self.text.startswith("# alicorn-sandbox"))

    def test_documents_project_creation_flow(self):
        self.assertIn("## Project creation flow", self.text)
        self.assertIn("ABCT-2", self.text)

    def test_has_task_log_entry_for_abct_1(self):
        self.assertIn("## Task log", self.text)
        self.assertIn("- ABCT-1:", self.text)

    def test_documents_how_to_run_tests(self):
        self.assertIn("python3 -m unittest discover -s tests", self.text)


if __name__ == "__main__":
    unittest.main()
