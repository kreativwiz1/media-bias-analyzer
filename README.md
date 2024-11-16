# Media Bias Analyzer 📊

A sophisticated Streamlit web application that leverages AI to analyze media bias and polarization in YouTube content. Using advanced natural language processing and OpenAI's GPT-3.5, this tool provides comprehensive bias analysis through transcript and comment processing.

## ✨ Features

### Content Analysis
- **Video Processing**
  - YouTube URL input handling
  - Transcript extraction
  - Comment collection
  - Metadata analysis

### AI Analysis
- **Bias Detection**
  - OpenAI GPT-3.5 integration
  - Natural language processing
  - Sentiment analysis
  - Context understanding

### Scoring Metrics
- **Bias Categories**
  - Objectivity Score (0-100)
  - Balance Rating (0-100)
  - Neutrality Index (0-100)
  - Engagement Analysis (0-100)

### Visualization
- **Interactive Reports**
  - Bias distribution graphs
  - Temporal analysis
  - Comparative metrics
  - Trend identification

## 🛠️ Technical Requirements

### Software
- Python 3.10+
- Poetry dependency manager

### API Keys
- OpenAI API key
- YouTube Data API v3 key

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/kreativwiz1/media-bias-analyzer.git
cd media-bias-analyzer
```

2. Install dependencies:
```bash
poetry install
```

3. Configure environment variables:
```bash
# .env file
OPENAI_API_KEY=your_openai_key_here
YOUTUBE_API_KEY=your_youtube_key_here
```

## 💻 Usage

1. Start the application:
```bash
streamlit run main.py
```

2. Access the web interface:
```
http://localhost:8501
```

3. Analyze content:
   - Enter YouTube URL
   - Click "Analyze"
   - View detailed results

## 📊 Analysis Metrics

### Objectivity Score
- Fact-based content assessment
- Source verification
- Claims analysis
- Citation checking

### Balance Rating
- Perspective diversity
- Argument representation
- Source variety
- Opinion distribution

### Neutrality Index
- Language analysis
- Tone evaluation
- Emotional content
- Bias indicators

### Engagement Analysis
- Comment sentiment
- User interaction patterns
- Discussion quality
- Community polarization

## ⚙️ Configuration

### Environment Variables
```python
# config.py
OPENAI_MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 2000
TEMPERATURE = 0.7
```

### API Settings
```python
# settings.py
YOUTUBE_COMMENT_LIMIT = 100
TRANSCRIPT_CHUNK_SIZE = 1500
CACHE_DURATION = 3600  # 1 hour
```

## 📈 Performance Optimization

### Caching Strategy
- Transcript caching
- Analysis results storage
- API response caching
- Resource optimization

### Rate Limiting
```python
MAX_REQUESTS_PER_MINUTE = 60
MAX_TOKENS_PER_REQUEST = 4000
COOLDOWN_PERIOD = 60  # seconds
```

## 🔒 Security Features

- API key protection
- Input sanitization
- Rate limiting
- Error handling

## 🧪 Testing

Run tests:
```bash
poetry run pytest
```

Example test:
```python
def test_bias_analysis():
    url = "https://youtube.com/watch?v=example"
    result = analyze_bias(url)
    assert "objectivity_score" in result
    assert 0 <= result["objectivity_score"] <= 100
```

## 📱 Deployment

### Local Development
```bash
streamlit run main.py
```

### Cloud Run Deployment
```yaml
# app.yaml
runtime: python310
env_variables:
  PORT: "8501"
```

### Port Configuration
- Main application: 8501 → 80
- Secondary service: 8502 → 3000

## 📦 Dependencies

```toml
[tool.poetry.dependencies]
python = "^3.10"
streamlit = "^1.24.0"
openai = "^0.27.0"
youtube-transcript-api = "^0.6.0"
google-api-python-client = "^2.86.0"
python-dotenv = "^1.0.0"
textblob = "^0.17.1"
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Submit pull request

### Development Guidelines
- Follow PEP 8
- Add unit tests
- Document features
- Update README

## 🐛 Troubleshooting

### Common Issues

1. **API Rate Limits**
   - Implement exponential backoff
   - Use API key rotation
   - Cache responses

2. **Memory Usage**
   - Chunk large transcripts
   - Stream responses
   - Clean up resources

3. **Analysis Errors**
   - Validate input
   - Handle API timeouts
   - Log errors

## 📮 Support

For assistance:
- Open GitHub issue
- Check documentation
- Contact maintainers

## 🙏 Acknowledgments

- OpenAI team
- YouTube API team
- Streamlit community
- Project contributors