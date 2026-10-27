
from reportlab.lib.utils import open_for_read
from utils.pdf_generator import generate_pdf


def test_pdf_generates_with_special_characters(tmp_path):
    output_file = tmp_path / "analysis_report.pdf"

    generate_pdf(
        filename=str(output_file),
        topic="Python <Basics> & Functions",
        transcript="I learned x < y and x > 0; A & B.",
        similarity=85.5,
        overall=85.5,
        concept=85,
        quality=80,
        level="Good",
        feedback="Good explanation.\nReview A & B.",
    )

    assert output_file.exists()
    assert output_file.stat().st_size > 0

    # A PDF file begins with the PDF signature.
    with open(output_file, "rb") as pdf_file:
        assert pdf_file.read(5) == b"%PDF-"
