# Email Writer Bot

An AI-powered email assistant that learns and replicates your personal writing style using Claude AI.

## 🎯 Overview

This project analyzes your email history to create a personalized AI assistant that can draft emails matching your unique writing style, tone, and patterns. It's built to work with Claude AI and includes tools for analyzing email patterns and creating a comprehensive style guide.

## 📁 Project Structure

```
email-writer-bot/
├── CLAUDE.md                  # Main style guide with comprehensive writing patterns
├── setup_guide.md            # Complete setup instructions (quick start + advanced)
├── email_templates.json      # Consolidated email examples by category
├── email_style_analysis.json # Statistical analysis of writing patterns
├── email_analyzer.py         # Python script to analyze email patterns
├── claude_style_analyzer.py  # Script to prepare prompts for Claude analysis
└── analysis/                 # Analysis output files (intermediate data)
```

## 🚀 Quick Start

1. **Clone this repository**
   ```bash
   git clone git@github.com:bsft-stephen-dunn/email-writer-bot.git
   cd email-writer-bot
   ```

2. **Create a Claude Project**
   - Go to [claude.ai](https://claude.ai)
   - Create a new project named "Email Assistant"
   - Upload `CLAUDE.md`, `email_templates.json`, and `email_style_analysis.json` to Project Knowledge

3. **Start using your assistant**
   - Ask Claude to draft emails in your style
   - Example: "Write an email to John about rescheduling our meeting"

For detailed setup instructions, see [setup_guide.md](setup_guide.md).

## 🛠️ Analyzing Your Own Emails

To create a style guide from your email history:

1. **Export your emails** as an MBOX file from your email client
2. **Run the analyzer**:
   ```bash
   python3 email_analyzer.py your-emails.mbox --output ./
   ```
3. **Generate the style guide**:
   ```bash
   python3 claude_style_analyzer.py
   ```
4. **Upload to Claude** to create your personalized assistant

## 📊 Features

- **Style Analysis**: Identifies greeting patterns, closing styles, common phrases, and sentence structures
- **Email Templates**: Categorized templates for different email types (onboarding, technical support, follow-ups, etc.)
- **Statistical Insights**: Data-driven analysis of writing patterns based on thousands of emails
- **Easy Integration**: Works with Claude AI web interface and API

## 🔧 Requirements

- Python 3.7+
- `mailbox` module (standard library)
- `anthropic` package (for API integration)
- Claude AI account

## 📝 Example Use Cases

- **Client Communications**: Draft professional responses maintaining consistent tone
- **Technical Support**: Create helpful, patient responses to technical questions
- **Project Updates**: Generate status updates with appropriate detail level
- **Meeting Coordination**: Schedule and reschedule meetings professionally
- **Follow-ups**: Create timely follow-up emails with context

## 🔄 Maintenance

Update your style guide quarterly:
1. Export recent sent emails
2. Re-run the analyzer
3. Update project files in Claude
4. Review and adjust as needed

## 📚 Additional Resources

- [Claude AI Documentation](https://docs.anthropic.com)
- [Email Best Practices](https://www.grammarly.com/blog/email-writing/)
- [Python Email Processing](https://docs.python.org/3/library/mailbox.html)

## 🤝 Contributing

Feel free to fork this repository and adapt it for your own email style analysis needs.

## 📄 License

This project is for personal use. Please respect privacy when analyzing email data.