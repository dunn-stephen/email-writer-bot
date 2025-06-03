#!/usr/bin/env python3
"""
Claude Style Analyzer - Prepares email data for Claude analysis
Creates structured prompts and data packages for Claude to analyze writing style
"""

import json
import random
import os

class ClaudeStylePreparer:
    def __init__(self, analysis_file, samples_file):
        with open(analysis_file, 'r') as f:
            self.analysis = json.load(f)
        
        with open(samples_file, 'r') as f:
            self.samples = json.load(f)
    
    def prepare_claude_prompt(self):
        """Create a comprehensive prompt for Claude to analyze writing style"""
        
        prompt = f"""You are analyzing Stephen Dunn's email writing style based on {self.analysis['total_emails_analyzed']} emails. 
Please provide a detailed analysis of the writing style characteristics to populate a CLAUDE.md file that will help an AI assistant write emails in Stephen's style.

## Statistical Analysis from {self.analysis['total_emails_analyzed']} emails:

### Greeting Patterns:
Most common greetings:
{self._format_dict(self.analysis['common_elements']['top_greetings'])}

### Closing Patterns:
Most common closings:
{self._format_dict(self.analysis['common_elements']['top_closings'])}

### Common Phrases Used:
{self._format_dict(self.analysis['common_elements']['frequent_phrases'])}

### Writing Metrics:
- Average sentence length: {self.analysis['structure_analysis']['avg_sentence_length']} words
- Average email length: {self.analysis['structure_analysis']['avg_email_length']} words
- Most active sending time: {self._get_most_active_time()}
- Uses emoticons: {self.analysis['communication_style']['uses_emoticons']}

### Email Samples:
{self._format_samples()}

## Based on this data, please analyze and describe:

1. **Tone & Voice Characteristics**:
   - What is the overall formality level? (casual, professional, formal)
   - What personality traits come through in the writing?
   - What is the energy level of the emails?

2. **Communication Patterns**:
   - How does Stephen typically structure his emails?
   - What opening strategies does he use?
   - How does he transition between topics?
   - How does he close emails?

3. **Language Style**:
   - What vocabulary level does he use?
   - How does he balance technical terms with plain language?
   - What punctuation patterns are notable?

4. **Context Adaptations**:
   - How might his style differ for internal vs external emails?
   - What adjustments might he make for different audiences?

5. **Unique Style Elements**:
   - What makes his email style distinctive?
   - What patterns should be replicated to sound authentic?

6. **Do's and Don'ts**:
   - What should an AI always do when writing in his style?
   - What should an AI avoid doing?

Please provide specific examples and actionable guidelines that an AI can follow to replicate this writing style accurately.
"""
        return prompt
    
    def _format_dict(self, d, max_items=10):
        """Format dictionary for prompt"""
        items = list(d.items())[:max_items]
        return '\n'.join([f"- {k}: {v}" for k, v in items])
    
    def _get_most_active_time(self):
        """Get most active sending time"""
        times = self.analysis['communication_style']['sending_times']
        return max(times, key=lambda x: float(times[x].rstrip('%')))
    
    def _format_samples(self):
        """Format email samples for analysis"""
        formatted = []
        for sample in self.samples[:3]:  # Use first 3 samples
            formatted.append(f"""
Email {sample['sample_id']}:
Subject: {sample['subject']}
Body Preview:
{sample['body_preview']}
""")
        return '\n'.join(formatted)
    
    def save_claude_ready_file(self, output_file):
        """Save the prompt to a file ready for Claude"""
        prompt = self.prepare_claude_prompt()
        with open(output_file, 'w') as f:
            f.write(prompt)
        
        print(f"Claude-ready analysis saved to: {output_file}")
        
    def create_batch_prompts(self, output_dir):
        """Create multiple focused prompts for different aspects of style"""
        
        # Prompt 1: Greeting and Closing Analysis
        prompt1 = f"""Analyze Stephen's email greeting and closing patterns:

Top Greetings:
{self._format_dict(self.analysis['common_elements']['top_greetings'])}

Top Closings:
{self._format_dict(self.analysis['common_elements']['top_closings'])}

Based on these patterns, describe:
1. When does he use "Hi" vs "Hey"?
2. How does he personalize greetings?
3. What's his preferred closing style?
4. How formal or casual are his greetings?
"""
        
        # Prompt 2: Phrase and Expression Analysis
        prompt2 = f"""Analyze Stephen's common phrases and expressions:

Most Frequent Phrases:
{self._format_dict(self.analysis['common_elements']['frequent_phrases'])}

Describe:
1. What do these phrases reveal about his communication style?
2. How does he make requests?
3. How does he express gratitude?
4. What transitional phrases does he favor?
"""
        
        # Prompt 3: Email Structure Analysis
        prompt3 = f"""Analyze Stephen's email structure based on these samples:

{self._format_samples()}

Writing Metrics:
- Average email length: {self.analysis['structure_analysis']['avg_email_length']} words
- Average sentence length: {self.analysis['structure_analysis']['avg_sentence_length']} words

Describe:
1. How does he structure multi-topic emails?
2. How does he use formatting (bullets, bold, etc.)?
3. What's his paragraph structure like?
4. How does he handle action items?
"""
        
        # Save prompts
        prompts = {
            'greeting_closing_analysis.txt': prompt1,
            'phrase_expression_analysis.txt': prompt2,
            'structure_analysis.txt': prompt3
        }
        
        for filename, content in prompts.items():
            with open(os.path.join(output_dir, filename), 'w') as f:
                f.write(content)
        
        print(f"Batch prompts saved to: {output_dir}")

def main():
    # Initialize preparer
    preparer = ClaudeStylePreparer(
        'email_style_analysis.json',
        'email_samples.json'
    )
    
    # Create comprehensive prompt
    preparer.save_claude_ready_file('claude_comprehensive_prompt.txt')
    
    # Create batch prompts
    preparer.create_batch_prompts('.')
    
    print("\nNext steps:")
    print("1. Copy the content from 'claude_comprehensive_prompt.txt'")
    print("2. Paste it into Claude and ask for the analysis")
    print("3. Use the response to update CLAUDE.md")
    print("\nAlternatively, use the individual prompt files for focused analysis")

if __name__ == "__main__":
    main()