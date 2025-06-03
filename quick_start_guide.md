# Quick Start: Setting Up Your Claude Email Project

## 🚀 5-Minute Setup

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
You are Stephen Dunn's email writing assistant. Always write emails matching his style from CLAUDE.md.

Quick Rules:
• Greetings: "Hi [Name]," (default) or "Hey [Name]," (familiar contacts)
• Sign-off: Always "Thank you," + signature
• Tone: Professional but approachable
• Structure: Short paragraphs, bullets for multiple topics
• Common phrases: "Please let me know", "Thanks for", "Following up on"

Signature:
Thank you,

Stephen Dunn
Sr. Product Consultant | blueshift.com
```

### Step 4: Test It!
Try these prompts:
- "Write an email to Alex confirming our 2pm meeting"
- "Draft a follow-up email about the API integration issue"
- "Create a friendly reminder email about the pending invoice"

## 📱 Pro Tips

### Save Time with Templates
Ask Claude to create templates:
- "Create a template for welcoming new clients"
- "Make a template for technical issue responses"

### Quick Style Checks
- Paste any draft and ask: "Rewrite this in my style"
- "Make this email more like how I usually write"

### Mobile Usage
The Claude mobile app maintains your project settings - perfect for drafting emails on the go!

## 🔧 Maintenance

**Monthly**: Export new sent emails and run:
```bash
python3 email_analyzer.py [new-mbox-file] --output .
```

Then update your project files with any new patterns.

---

That's it! Your email assistant is ready. Just open your project and start drafting.