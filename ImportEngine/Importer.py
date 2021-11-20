from typing import List

from .ImportInterface import ImportInterface
from .Cat import Cat
from .XlsxImporter import XlsxImporter
from .CSVImporter import CSVImporter
from .TxtImporter import TxtImporter
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter

class Importer(ImportInterface):
    importers = [CSVImporter, XlsxImporter, TxtImporter, DocxImporter, PDFImporter]
    
    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
