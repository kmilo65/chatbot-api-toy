# Personal AI Chatbot

A modern web-based AI chatbot built with FastAPI and OpenAI's GPT-4, featuring both conversational AI capabilities and AI-powered image generation. This project provides an interactive web interface for users to engage with an AI tutor specialized in Python programming and generate custom images through natural language prompts.

## Features

- **AI-Powered Chat Interface**: Interactive conversation with a Python tutor AI using OpenAI's GPT-4 model
- **Image Generation**: Create custom images from text descriptions using OpenAI's DALL-E model
- **Modern Web UI**: Clean, responsive interface built with Bootstrap 5
- **Real-time Chat History**: View and track conversation history
- **Dual Functionality**: Switch between chat and image generation modes

## Project Description

This chatbot is designed as a Python tutor AI that helps users learn Python programming from scratch. It provides clear instructions on Python concepts, best practices, and syntax, creating a structured learning path for users to develop production-ready Python applications. The system also includes an image generation feature for creating visual content based on text prompts.

## Installation Instructions

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Dependencies

The project requires the following main dependencies:
- `fastapi==0.116.1` - Modern web framework for building APIs
- `openai==1.97.1` - OpenAI API client
- `python-dotenv` - Environment variable management
- `uvicorn==0.35.0` - ASGI server for running FastAPI applications
- `jinja2` - Template engine for HTML rendering
- `python-multipart` - Form data handling

### Setup Instructions

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd openaichatbot
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## How to Run the Chatbot Using Uvicorn

### About Uvicorn

Uvicorn is an ASGI (Asynchronous Server Gateway Interface) server that provides lightning-fast ASGI server implementation, used to run FastAPI applications. It supports HTTP/1.1, WebSockets, and HTTP/2 protocols.

### Installing Uvicorn

If not already installed via requirements.txt:
```bash
pip install uvicorn
```

### Starting the Server

Run the following command from the project root directory:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**Command Parameters Explained:**
- `main:app` - Points to the `app` variable in `main.py`
- `--host 0.0.0.0` - Binds the server to all available network interfaces
- `--port 8000` - Runs the server on port 8000
- `--reload` - Enables auto-reload for development (restarts server when code changes)

### Alternative Commands

For production deployment (without auto-reload):
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

For local development only:
```bash
uvicorn main:app --reload
```

## Usage

Once the server is running, you can access the chatbot through your web browser:

1. **Open your browser** and navigate to: `http://localhost:8000`

2. **Chat Interface** (`/`):
   - Type your Python-related questions in the text area
   - Click "Send" to get AI responses
   - View chat history below the input form

3. **Image Generation** (`/image`):
   - Click the "Image Generator" button in the navigation
   - Describe the image you want to generate
   - Submit to create AI-generated images (512x512 pixels)

### Web Interface Features

- **Responsive Design**: Works on desktop and mobile devices
- **Navigation Bar**: Easy switching between chat and image generation
- **Real-time Updates**: Immediate responses from the AI
- **Chat History**: Persistent conversation tracking during the session

## Project Structure

```
openaichatbot/
├── main.py                 # Main FastAPI application file
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore file
└── templates/            # HTML templates
    ├── layout.html       # Base template with Bootstrap styling
    ├── navbar.html       # Navigation component
    ├── home.html         # Chat interface template
    └── image.html        # Image generation template
```

### Key Files Explained

- **`main.py`**: Contains the FastAPI application with routes for chat and image generation
- **`templates/`**: Jinja2 HTML templates for the web interface
- **`requirements.txt`**: Lists all Python package dependencies
- **`.env`**: Configuration file for API keys (not included in repository)

## Additional Notes

### Environment Variables

The application requires the following environment variable:
- `OPENAI_API_KEY`: Your OpenAI API key for accessing GPT-4 and DALL-E services

### Configuration

- **Model**: Uses GPT-4o-mini for chat responses
- **Temperature**: Set to 0.6 for balanced creativity and consistency
- **Image Size**: Generated images are 512x512 pixels
- **Chat History**: Maintains conversation context during the session

### Security Considerations

- Never commit your `.env` file to version control
- Keep your OpenAI API key secure and private
- Consider implementing rate limiting for production use

### Customization

To customize the chatbot:

1. **Change AI Personality**: Modify the system message in `main.py` (lines 25-29)
2. **Adjust Model Parameters**: Change temperature, model, or other OpenAI parameters
3. **Modify UI**: Edit HTML templates in the `templates/` directory
4. **Add Features**: Extend the FastAPI application with new routes and functionality

### Troubleshooting

- **Port Already in Use**: Change the port number in the uvicorn command
- **API Key Issues**: Ensure your `.env` file is properly configured
- **Template Errors**: Check that all template files are in the `templates/` directory

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## License

This project is open source and available under the [MIT License](LICENSE).
@chenriquez
