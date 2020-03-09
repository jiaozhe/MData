from loguru import logger
from PyPDF2 import PdfFileReader, PdfFileWriter


pdf_input = PdfFileReader(open("腾讯区块链方案白皮书.pdf", "rb"))
logger.info(pdf_input.getNumPages())

