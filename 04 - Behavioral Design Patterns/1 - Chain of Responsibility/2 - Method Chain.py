"""
1 - Scenario: Logging System
Imagine you are developing a logging system where log messages can be handled differently depending on 
their severity level(e.g., DEBUG, INFO, WARNING, ERROR). 
You want the system to try handling a message starting from the highest priority handler (ERROR) 
down to the lowest one (DEBUG) until it finds the appropriate handler.
"""


class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if not self._successor:
            raise NotImplementedError("Must provide an implementation in subclass")
        self._successor.handle(request)


class ErrorHandler(Handler):
    def handle(self, request):
        if request == "ERROR":
            print("ErrorHandler: Handling error")
        else:
            super().handle(request)


class WarningHandler(Handler):
    def handle(self, request):
        if request == "WARNING":
            print("WarningHandler: Handling warning")
        else:
            super().handle(request)


class InfoHandler(Handler):
    def handle(self, request):
        if request == "INFO":
            print("InfoHandler: Handling info")
        else:
            super().handle(request)


# Broker Chain
class DebugHandler(Handler):
    def handle(self, request):
        if request == "DEBUG":
            print("DebugHandler: Handling debug")
        else:
            print("Unhandled request: ", request)


debug_handler = DebugHandler()
info_handler = InfoHandler(debug_handler)
warning_handler = WarningHandler(info_handler)
error_handler = ErrorHandler(warning_handler)

requests = ["DEBUG", "INFO", "WARNING", "ERROR", "UNKNOWN"]
for request in requests:
    print("\nSending request:", request)
    error_handler.handle(request)

"""
2 - Scenario: Document File Reader
Imagine you are tasked with designing a file processing system that can read and interpret documents in various formats, 
such as PDF, DOCX, and TXT. 
The system should attempt to open a document in each of the supported formats, one at a time, 
until it finds a reader that can handle the document successfully. If a document format is not supported, the system should notify the user.
"""
from abc import ABC, abstractmethod


class DocumentReaderABC(ABC):
    @abstractmethod
    def read(self, files_path: str): ...


class DucmentReader(DocumentReaderABC):

    def __init__(self, reader: DocumentReaderABC = None) -> None:
        self.__reader = reader

    def read(self, files_path: str):
        if not self.__reader:
            raise NotImplementedError("Must provide an implementation of reader")
        self.__reader.read(files_path)

    def _get_extension(self, file_path: str):
        *_, extension = file_path.split(".")
        return extension.lower()


class PDFReader(DucmentReader):
    def read(self, files_path: str):
        if self._get_extension(files_path) == "pdf":
            print("reading PDF file")
            return
        return super().read(files_path)


class DOCXReader(DucmentReader):
    def read(self, files_path: str):
        if self._get_extension(files_path) == "docx":
            print("reading DOCX file")
            return
        return super().read(files_path)


class TXTReader(DucmentReader):
    def read(self, files_path: str):
        if self._get_extension(files_path) == "txt":
            print("reading TXT file")
        else:
            print("can not read this file format")


text_reader = TXTReader()
docs_reader = DOCXReader(text_reader)
pdf_reader = PDFReader(docs_reader)

pdf_reader.read("file.pdf")
