# Claude Email Assistant Setup Guide

## 🚀 Quick Start (5-Minute Setup)

### Step 1: Create the Project
1. Go to [claude.ai](https://claude.ai)
2. Click your profile (bottom left) → "Projects" → "Create project"
3. Name it: "Stephen's Email Assistant"

### Step 2: Upload Your Style Files
Drag and drop these 3 files into the "Project knowledge" section:
- `CLAUDE.md` (your main style guide)
- `email_samples.json` (example emails)
- `email_style_analysis.json` (writing patterns)

### Step 3: Add Instructions
Copy and paste this into "Custom instructions":

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

### Step 4: Test It!
Try these prompts:
- "Write an email to Alex confirming our 2pm meeting"
- "Draft a follow-up email about the API integration issue"
- "Create a friendly reminder email about the pending invoice"

## 📱 Using Your Email Assistant

### Basic Email Drafts
```
"Write an email to John about the delayed shipment"
```

### Email Revisions
```
"Make this email sound more like me: [paste draft]"
```

### Template Creation
```
"Create a template for onboarding new clients"
```

### Style Checks
```
"Does this email match my usual style?"
```

## 💡 Pro Tips

### Save Time with Templates
Ask Claude to create reusable templates:
- "Create a template for welcoming new clients"
- "Make a template for technical issue responses"
- "Build a template for project status updates"

### Quick Style Conversions
- Paste any draft and ask: "Rewrite this in my style"
- "Make this email more like how I usually write"

### Mobile Usage
The Claude mobile app maintains your project settings - perfect for drafting emails on the go!

### Example Prompts for Common Scenarios

**Basic Email Request:**
"Write an email to Jennifer about rescheduling our Thursday meeting to Friday"

**Technical Support:**
"Draft a response to a client who's having login issues with their dashboard"

**Follow-up:**
"Create a follow-up email for the onboarding session we had with Acme Corp last week"

**Status Update:**
"Write a status update email about the API integration project - we're 75% complete"

## 🔧 Advanced Configuration

### API Integration
Create a script that uses Claude's API with your project:

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

### Browser Extensions
Consider using Claude browser extensions that can:
- Access your project settings
- Draft emails directly in Gmail/Outlook
- Suggest responses based on your style

### Workflow Automation
Integrate with tools like:
- **Zapier/Make**: Auto-draft responses to specific email types
- **Gmail Add-ons**: Add a "Draft with Claude" button
- **Slack Integration**: Draft email responses from Slack messages

## 🔄 Maintenance & Best Practices

### Regular Updates
**Monthly**: Export new sent emails and run:
```bash
cd /Users/stephendunn/Desktop/email_bot
python3 email_analyzer.py Sent-001.mbox --output .
```
Then update your project files with any new patterns.

### Best Practices
1. **Regular Updates**: Update your CLAUDE.md quarterly with new patterns
2. **Feedback Loop**: When Claude drafts something not quite right, provide specific feedback
3. **Context Matters**: Always provide recipient name and context for best results
4. **Review Before Sending**: Claude drafts should be reviewed, especially for sensitive communications

### Maintaining Your Style Guide
- Run the email analyzer monthly to capture any style evolution
- Update the project knowledge with new patterns
- Add new common phrases or email types as they emerge

---

That's it! Your email assistant is ready. Just open your project and start drafting. The more you use it and provide feedback, the better it becomes at matching your style.