import textwrap
import unittest

from parse import parse


class ParserUnitTest(unittest.TestCase):

    def test_parse_result(self):
        expected_output = textwrap.dedent(u"""
        <table border="0" cellpadding="0" cellspacing="0" width="675">
        <tr><td style="text-align: right; vertical-align: top;">trouble</td></tr><tr>
        <td style="text-align: left; vertical-align: top;">email_r1_c1</td>
        </tr>
        <tr>
        <td style="text-align: left; vertical-align: top;">email_r2_c1</td>
        </tr>
        <tr>
        <td style="text-align: left; vertical-align: top;">email_r3_c1</td>
        </tr>
        <tr>
        <td style="text-align: left; vertical-align: top;">email_r4_c1</td>
        </tr>
        <tr>
        <td style="text-align: left; vertical-align: top;">email_r5_c1</td>
        </tr>
        <tr>
        <td style="text-align: left; vertical-align: top;"><table align="left" border="0" cellpadding="0" cellspacing="0" width="675">
        <tr>
        <td style="text-align: left; vertical-align: top;">email_r6_c1</td>
        <td style="text-align: left; vertical-align: top;">email_r6_c2</td>
        <td style="text-align: left; vertical-align: top;">email_r6_c3</td>
        <td style="text-align: left; vertical-align: top;">email_r6_c4</td>
        <td style="text-align: left; vertical-align: top;">email_r6_c5</td>
        <td style="text-align: left; vertical-align: top;">email_r6_c6</td>
        </tr>
        </table></td>
        </tr>
        <tr>
        <td style="text-align: left; vertical-align: top;">email_r7_c1</td>
        </tr>
        </table>
        """).strip('\n')

        output = parse(file_path='test_files/email.html')

        self.assertEqual(output, expected_output,
            "Output did not match expectation. Instead was: \n\n{}".format(
                output))

    def test_bad_file_extension_raises_exception(self):
        self.assertRaises(Exception, parse, file_path='test_files/email.txt')

    def test_non_existent_file_raises_exception(self):
        self.assertRaises(IOError, parse, file_path='foo.txt')


if __name__ == '__main__':
    unittest.main()
