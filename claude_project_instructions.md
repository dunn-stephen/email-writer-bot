# How to Create a Claude Project for Stephen's Email Bot

## Overview
Claude Projects allow you to create a dedicated workspace with custom instructions and knowledge that Claude will use for all conversations within that project.

## Step-by-Step Setup

### 1. Create a New Claude Project
1. Go to claude.ai
2. Click on your name/profile in the bottom left
3. Select "Projects" 
4. Click "Create project"
5. Name it something like "Stephen's Email Assistant" or "Email Bot"

### 2. Add Project Knowledge
In the project settings, you'll see a "Project knowledge" section where you can add documents:

1. **Add the CLAUDE.md file** - This is your primary style guide
2. **Add email_samples.json** - Provides real examples of your writing
3. **Add email_style_analysis.json** - Contains statistical patterns

### 3. Set Custom Instructions
In the "Custom instructions" field, paste the following:

```
You are Stephen Dunn's email writing assistant. Your role is to draft emails that match Stephen's writing style exactly.

## Core Instructions:
1. ALWAYS refer to the CLAUDE.md style guide for writing patterns
2. Match Stephen's tone: professional yet approachable
3. Use his common phrases naturally
4. Follow his email structure patterns
5. Maintain his signature format

## When drafting emails:
- Start with "Hi [Name]," for most emails (70% of the time)
- Use "Hey [Name]," for familiar contacts (20% of the time)
- Keep sentences concise (average 8 words)
- Use bullet points for multiple topics
- Always end with "Thank you," followed by the signature block

## Stephen's Signature:
Thank you,

Stephen Dunn
Sr. Product Consultant | blueshift.com

## Key Phrases to Use:
- "Thanks for..." (when acknowledging)
- "Please let me know" (for responses)
- "Feel free to reach out" (offering help)
- "Following up on..." (for continuity)
- "I wanted to..." (soft introductions)

## Email Types I Handle:
1. Client onboarding
2. Technical support responses
3. Status updates
4. Follow-ups
5. Meeting requests

## Important Style Notes:
- Average email length: ~100-200 words for simple responses
- No excessive exclamation points
- Technical terms explained simply
- Patient and helpful tone with client issues
- Proactive in offering next steps

When asked to write an email, I will:
1. Ask for context if needed (recipient, purpose, key points)
2. Draft in Stephen's style
3. Include appropriate formatting
4. Suggest subject lines that match his patterns
```

### 4. Using the Project

Once set up, every conversation in this project will have access to your style guide. You can:

1. **Quick Email Drafts**: 
   ```
   "Write an email to John about the delayed shipment"
   ```

2. **Email Revisions**:
   ```
   "Make this email sound more like me: [paste draft]"
   ```

3. **Template Creation**:
   ```
   "Create a template for onboarding new clients"
   ```

4. **Style Checks**:
   ```
   "Does this email match my usual style?"
   ```

## Advanced Integration Options

### Option 1: API Integration
Create a simple script that uses Claude's API with your project:

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

def generate_email(prompt):
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[{
            "role": "user",
            "content": f"Write an email: {prompt}"
        }],
        system="You are Stephen Dunn's email assistant. [Include full instructions here]"
    )
    return response.content[0].text

# Example usage
email = generate_email("to Sarah thanking her for the meeting and confirming next steps")
print(email)
```

### Option 2: Browser Extension
Consider using Claude browser extensions that can:
- Access your project settings
- Draft emails directly in Gmail/Outlook
- Suggest responses based on your style

### Option 3: Workflow Automation
Integrate with tools like:
- **Zapier/Make**: Auto-draft responses to specific email types
- **Gmail Add-ons**: Add a "Draft with Claude" button
- **Slack Integration**: Draft email responses from Slack messages

## Best Practices

1. **Regular Updates**: Update your CLAUDE.md quarterly with new patterns
2. **Feedback Loop**: When Claude drafts something not quite right, provide specific feedback
3. **Context Matters**: Always provide recipient name and context for best results
4. **Review Before Sending**: Claude drafts should be reviewed, especially for sensitive communications

## Example Prompts for Your Project

### Basic Email Request:
"Write an email to Jennifer about rescheduling our Thursday meeting to Friday"

### Technical Support:
"Draft a response to a client who's having login issues with their dashboard"

### Follow-up:
"Create a follow-up email for the onboarding session we had with Acme Corp last week"

### Status Update:
"Write a status update email about the API integration project - we're 75% complete"

## Maintaining Your Style Guide

Run the email analyzer monthly to capture any style evolution:
```bash
cd /Users/stephendunn/Desktop/email_bot
python3 email_analyzer.py Sent-001.mbox --output .
```

Then update the project knowledge with new patterns.