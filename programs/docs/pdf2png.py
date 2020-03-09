from loguru import logger
import fitz


doc = fitz.Document("腾讯区块链方案白皮书.pdf")
doc_info = doc.metadata
logger.info(doc_info.get("title"))
logger.info(doc_info.get("format"))

for page in doc:
    page_number = page.number + 1
    png_filename = "%03d.png" % page_number
    logger.info("-" * 20)
    logger.info("Page: %s" % page_number)
    pix = page.getPixmap()
    pix.writePNG(png_filename)
    logger.info("File: %s" % png_filename)

logger.info("-" * 20)
logger.info("Done!")

