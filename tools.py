from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.schema.document import Document
from typing import List, Type


# First method
class PDFReaderToolInput(BaseModel):
    directory_path: str = Field(..., description="The path to the directory containing PDF files.")

class PDFReaderTool(BaseTool):
    name: str = "pdf_loader_tool"
    description: str = "Reads PDFs from a specified directory and loads them with metadata."
    args_schema: Type[BaseModel] = PDFReaderToolInput

    def _run(self, directory_path: str) -> List[Document]:
        document_loader = PyPDFDirectoryLoader(path=directory_path)
        documents = document_loader.load()
        return documents

pdf_reader_tool = PDFReaderTool()


# Second method
# from crewai.tools import tool
# from langchain_community.document_loaders import PyPDFDirectoryLoader
# from langchain.schema.document import Document
# from typing import List

# @tool("pdf_loader_tool")
# def pdf_loader_tool(directory_path: str) -> List[Document]:
#     """Reads PDFs from the specified directory and loads them with metadata."""
#     document_loader = PyPDFDirectoryLoader(path=directory_path)
#     documents = document_loader.load()
#     return documents
