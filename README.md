# PDF Summarizer using OpenAI

A Streamlit-based web application that automatically summarizes PDF documents using OpenAI's GPT models and LangChain for document processing.

## Features

- 📄 Upload PDF documents through a user-friendly web interface
- 🤖 AI-powered summarization using OpenAI's GPT-3.5-turbo model
- 📊 Text chunking and embedding for better processing of large documents
- 🔍 Vector similarity search using FAISS for relevant content extraction
- 💰 Cost tracking for OpenAI API usage
- ⚡ Fast processing with HuggingFace embeddings

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   cd Pdf-summarizer-using-open-ai
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create an `openai.env` file in the project root directory:
   ```bash
   touch openai.env
   ```

4. Add your OpenAI API key to the `openai.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run utils.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

3. Upload a PDF document using the file uploader

4. The application will automatically:
   - Extract text from the PDF
   - Split the text into manageable chunks
   - Create embeddings and a knowledge base
   - Generate a 3-5 sentence summary of the document

## How It Works

1. **PDF Processing**: Uses PyPDF2 to extract text from uploaded PDF files
2. **Text Chunking**: Splits large documents into smaller chunks using LangChain's CharacterTextSplitter
3. **Embeddings**: Creates vector embeddings using HuggingFace's sentence-transformers model
4. **Knowledge Base**: Builds a FAISS vector store for similarity search
5. **Summarization**: Uses OpenAI's GPT-3.5-turbo model to generate concise summaries

## Dependencies

- `streamlit` - Web application framework
- `langchain` - Framework for developing applications with LLMs
- `openai` - OpenAI API client
- `pypdf` - PDF processing library
- `python-dotenv` - Environment variable management
- `langchain-community` - Community extensions for LangChain

## Configuration

The application uses the following default settings:
- **Model**: GPT-3.5-turbo-16k
- **Temperature**: 0.1 (for consistent outputs)
- **Chunk Size**: 1000 characters
- **Chunk Overlap**: 200 characters
- **Embedding Model**: sentence-transformers/all-MiniLM-L6-v2

## Environment Variables

| Variable | Description | Required |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

## Troubleshooting

**Issue**: "Unable to retrieve OPENAI_API_KEY" error
- **Solution**: Ensure your `openai.env` file exists and contains a valid OpenAI API key

**Issue**: Application doesn't start
- **Solution**: Make sure all dependencies are installed with `pip install -r requirements.txt`

**Issue**: PDF upload fails
- **Solution**: Ensure the PDF file is not password-protected and is a valid PDF format

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- OpenAI for providing the GPT models
- LangChain for the document processing framework
- Streamlit for the web application framework
- HuggingFace for the embedding models
