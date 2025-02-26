from tools import pdf_reader_tool

if __name__ == '__main__':
    directory_path = "data"
    documents = pdf_reader_tool.run(directory_path)
    print(documents[0])
