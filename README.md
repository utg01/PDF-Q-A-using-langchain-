# 📄 PDF Q&A Chat Application

A powerful Streamlit-based application that allows you to upload PDF documents and ask questions about their content using Google's Gemini AI. The application uses advanced natural language processing to provide accurate answers based on the uploaded PDF content.

## ✨ Features

- **PDF Upload**: Upload any PDF document through an intuitive web interface
- **AI-Powered Q&A**: Ask questions about your PDF content using Google Gemini AI
- **Vector Search**: Uses FAISS vector database for efficient document retrieval
- **Chunk-based Processing**: Intelligently splits documents for better context understanding
- **Real-time Responses**: Get instant answers to your questions
- **User-friendly Interface**: Clean and simple Streamlit-based UI

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd pdf-qa-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   
   Create a `.env` file in the project root and add your Google Gemini API key:
   ```
   GOOGLE_GEMINI_API_KEY=your_api_key_here
   ```
   
   To get a Google Gemini API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key to your `.env` file

6. **Run the application**
   ```bash
   streamlit run pdf_q_a.py
   ```

7. **Access the application**
   
   Open your browser and navigate to `http://localhost:8501`

## 📋 Usage

1. **Upload a PDF**: Click on the file uploader and select a PDF document
2. **Wait for Processing**: The application will process your PDF (this may take a moment)
3. **Ask Questions**: Type your question in the text input field
4. **Get Answers**: The AI will provide answers based on the PDF content

### Example Questions

- "What is the main topic of this document?"
- "Summarize the key points"
- "What are the conclusions mentioned?"
- "Explain the methodology used"
- "What data is presented in the document?"

## ⚠️ Important Note

**The application may show an error when you first start it, but this is normal!** The error occurs because the application tries to process the PDF before one is uploaded. Simply upload a PDF file and ask your question - the application will work perfectly after that.

## 🛠️ Technical Details

### Architecture

- **Frontend**: Streamlit web interface
- **PDF Processing**: PyPDF2 for text extraction
- **Text Splitting**: CharacterTextSplitter for document chunking
- **Embeddings**: Google Generative AI embeddings
- **Vector Store**: FAISS for similarity search
- **LLM**: Google Gemini 2.0 Flash model
- **Chain**: LangChain QA chain for question answering

### Dependencies

- `streamlit`: Web application framework
- `langchain`: LLM application framework
- `langchain_google_genai`: Google Gemini integration
- `PyPDF2`: PDF text extraction
- `faiss-cpu`: Vector similarity search
- `python-dotenv`: Environment variable management
- `google`: Google AI SDK

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_GEMINI_API_KEY` | Your Google Gemini API key | Yes |

### Model Settings

- **Embedding Model**: `models/embedding-001`
- **Chat Model**: `gemini-2.0-flash`
- **Temperature**: 0 (for consistent responses)
- **Chunk Size**: 500 characters
- **Chunk Overlap**: 100 characters
- **Similarity Search**: Top 10 most relevant chunks

## 📁 Project Structure

```
pdf-qa-app/
├── pdf_q_a.py          # Main application file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── README.md          # This file
└── venv/              # Virtual environment (created after setup)
```

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your `.env` file is in the project root
   - Verify your Google Gemini API key is correct
   - Make sure the API key has proper permissions

2. **PDF Upload Issues**
   - Ensure the PDF is not password-protected
   - Check that the PDF contains extractable text (not just images)
   - Try with a different PDF file

3. **Memory Issues**
   - For large PDFs, the application may take longer to process
   - Consider splitting very large documents

4. **Import Errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Verify your virtual environment is activated

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [LangChain](https://langchain.com/) for the LLM framework
- [Google Gemini](https://ai.google.dev/) for the AI capabilities
- [FAISS](https://faiss.ai/) for vector search

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information about your problem

---

**Happy PDF Questioning! 🎉**
