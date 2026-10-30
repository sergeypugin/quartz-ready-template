"""Regression tests for shared normalization behavior."""
import tempfile
import unittest
from pathlib import Path

from scripts.check_math import Formatter
from scripts.convert_links import LinkConverter
from scripts.ensure_blank_after_embed import rewrite
from scripts import utils


class SharedBehaviorTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def write(self, relative, text="x\n"):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        return path

    def test_markdown_traversal_is_case_insensitive(self):
        self.write("Keep.MD")
        self.write("Sub/also.Md")
        self.write("NODE_MODULES/ignored.MD")
        self.write(".OBSidian/ignored.md")
        self.write("_IGNORE/ignored.md")
        self.write(".GIT/ignored.md")
        files = [path.relative_to(self.root).as_posix() for path in utils.markdown_files(self.root)]
        self.assertEqual(files, ["Keep.MD", "Sub/also.Md"])

    def test_attachment_stem_lookup_and_joined_alias(self):
        self.write("Attachments/cover image.png")
        self.write("topic.md")
        self.write("page.md", "![[cover image]] [[topic|first|second]]\n")
        converted, issues = LinkConverter(self.root).convert_text("![[cover image]] [[topic|first|second]]\n", Path("page.md"))
        self.assertEqual(issues, [(1, "![[cover image]]", "wikilink can be converted", set(), "change"), (1, "[[topic|first|second]]", "wikilink can be converted", set(), "change")])
        self.assertEqual(converted, "![cover image.png](<Attachments/cover image.png>) [first|second](topic)\n")

    def test_angle_bracket_markdown_destination_with_parentheses(self):
        self.write("docs/a (copy).md")
        converter = LinkConverter(self.root)
        converted, issues = converter.convert_text("[doc](<docs/a (copy).md>)\n", Path("notes/page.md"))
        self.assertEqual(issues[0][2], "can be made relative")
        self.assertEqual(converted, "[doc](<../docs/a (copy)>)\n")

    def test_bom_and_bom_frontmatter_are_preserved(self):
        self.write("topic.md")
        source = "\ufeff---\ntitle: page\n---\n\n[[topic]]\n"
        converted, _ = LinkConverter(self.root).convert_text(source, Path("page.md"))
        self.assertEqual(converted, "\ufeff---\ntitle: page\n---\n\n[topic](topic)\n")

    def test_inline_math_ignores_escaped_dollars_and_code_spans(self):
        text = r"\$5 and $ x + y $ and `$ z $`" + "\n"
        formatter = Formatter()
        self.assertEqual(formatter.format(text), r"\$5 and $x + y$ and `$ z $`" + "\n")
        self.assertEqual(formatter.warnings, [])

    def test_inline_math_uses_backslash_parity(self):
        escaped = r"\$ x \$" + "\n"
        even_backslashes = r"\\$ x $" + "\n"

        escaped_formatter = Formatter()
        self.assertEqual(escaped_formatter.format(escaped), escaped)
        self.assertEqual(escaped_formatter.warnings, [])
        self.assertEqual(Formatter().format(even_backslashes), r"\\$x$" + "\n")

    def test_display_math_uses_backslash_parity(self):
        escaped = r"\$$x\$$" + "\n"
        even_backslashes = r"\\$$x$$" + "\n"

        escaped_formatter = Formatter()
        self.assertEqual(escaped_formatter.format(escaped), escaped)
        self.assertEqual(escaped_formatter.warnings, [])
        self.assertEqual(Formatter().format(even_backslashes), "\\\\\n$$\nx\n$$\n")

    def test_math_preserves_bom_and_frontmatter(self):
        text = "\ufeff---\ntitle: '$ x $'\n---\n$ x $\n"
        self.assertEqual(Formatter().format(text), "\ufeff---\ntitle: '$ x $'\n---\n$x$\n")

    def test_embed_spacing_keeps_blockquote_and_bom_frontmatter(self):
        text = "\ufeff---\ntitle: page\n---\n> ![x](<a b.png>)\n> next\n"
        rewritten, changed = rewrite(text)
        self.assertTrue(changed)
        self.assertEqual(rewritten, "\ufeff---\ntitle: page\n---\n> ![x](<a b.png>)\n>\n> next\n")

    def test_blue_bible_has_no_template_special_case(self):
        _, issues = LinkConverter(self.root).convert_text("[[blue_bible.pdf]]\n", Path("page.md"))
        self.assertEqual(issues[0][2], "target not found")


if __name__ == "__main__":
    unittest.main()
