#!/usr/bin/env python3
"""
Email Style Analyzer for CLAUDE.md Generation
Processes MBOX files to extract writing patterns and style characteristics
"""

import mailbox
import email
from email.utils import parsedate_to_datetime
from collections import Counter, defaultdict
import re
import json
from datetime import datetime
import statistics
from html.parser import HTMLParser
import argparse
import html

class EmailStyleAnalyzer:
    def __init__(self):
        self.emails = []
        self.patterns = {
            'greetings': Counter(),
            'closings': Counter(),
            'opening_lines': [],
            'closing_lines': [],
            'sentence_lengths': [],
            'common_phrases': Counter(),
            'email_lengths': [],
            'response_times': [],
            'recipients': defaultdict(int),
            'subjects': [],
            'time_patterns': defaultdict(int),
            'emoticons': Counter(),
            'punctuation_style': Counter(),
        }
        
    def extract_text_from_html(self, html_content):
        """Convert HTML to plain text using regex"""
        # Remove script and style tags and their content
        text = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
        
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)
        
        # Decode HTML entities
        text = html.unescape(text)
        
        # Clean up whitespace
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        
        return text
    
    def parse_mbox(self, mbox_path):
        """Parse MBOX file and extract emails"""
        mbox = mailbox.mbox(mbox_path)
        
        for message in mbox:
            email_data = {
                'subject': message.get('Subject', ''),
                'from': message.get('From', ''),
                'to': message.get('To', ''),
                'date': message.get('Date', ''),
                'body': ''
            }
            
            # Extract body
            body = []
            if message.is_multipart():
                for part in message.walk():
                    if part.get_content_type() == "text/plain":
                        body.append(part.get_payload(decode=True).decode('utf-8', errors='ignore'))
                    elif part.get_content_type() == "text/html":
                        html_content = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                        body.append(self.extract_text_from_html(html_content))
            else:
                content = message.get_payload(decode=True).decode('utf-8', errors='ignore')
                if '<html' in content.lower():
                    body.append(self.extract_text_from_html(content))
                else:
                    body.append(content)
            
            email_data['body'] = '\n'.join(body)
            
            # Only process non-empty emails
            if email_data['body'].strip():
                self.emails.append(email_data)
    
    def extract_greeting(self, body):
        """Extract greeting from email"""
        lines = body.strip().split('\n')
        if not lines:
            return None
            
        first_line = lines[0].strip()
        
        # Common greeting patterns
        greeting_patterns = [
            r'^(Hi|Hello|Hey|Dear|Good morning|Good afternoon|Good evening)\s+\w+',
            r'^(Hi|Hello|Hey|Dear)\s*[,!]?$',
            r'^\w+\s*[,:]',  # Just a name
        ]
        
        for pattern in greeting_patterns:
            if re.match(pattern, first_line, re.IGNORECASE):
                return first_line
        
        return None
    
    def extract_closing(self, body):
        """Extract closing from email"""
        lines = [line.strip() for line in body.strip().split('\n') if line.strip()]
        if len(lines) < 2:
            return None
        
        # Look for common closings in last few lines
        closing_words = ['best', 'regards', 'sincerely', 'thanks', 'thank you', 
                        'cheers', 'respectfully', 'warm', 'kind']
        
        for i in range(min(5, len(lines))):
            line = lines[-(i+1)].lower()
            if any(word in line for word in closing_words):
                return lines[-(i+1)]
        
        return None
    
    def analyze_sentence_structure(self, body):
        """Analyze sentence patterns"""
        # Remove signatures and quotes
        clean_body = re.sub(r'--\s*\n.*', '', body, flags=re.DOTALL)
        clean_body = re.sub(r'>.*\n', '', clean_body)
        
        # Split into sentences
        sentences = re.split(r'[.!?]+', clean_body)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
        
        for sentence in sentences:
            words = sentence.split()
            if words:
                self.patterns['sentence_lengths'].append(len(words))
    
    def extract_common_phrases(self, body):
        """Extract commonly used phrases"""
        # Common business phrases to look for
        phrase_patterns = [
            r'thank you for',
            r'please let me know',
            r'looking forward to',
            r'as discussed',
            r'following up on',
            r'please find attached',
            r'hope this finds you well',
            r'reaching out to',
            r'wanted to',
            r'just wanted to',
            r'quick question',
            r'when you get a chance',
            r'at your earliest convenience',
        ]
        
        lower_body = body.lower()
        for pattern in phrase_patterns:
            if re.search(pattern, lower_body):
                self.patterns['common_phrases'][pattern] += 1
    
    def analyze_emails(self):
        """Perform comprehensive analysis on all emails"""
        print(f"Analyzing {len(self.emails)} emails...")
        
        for email in self.emails:
            body = email['body']
            
            # Extract patterns
            greeting = self.extract_greeting(body)
            if greeting:
                self.patterns['greetings'][greeting.lower()] += 1
            
            closing = self.extract_closing(body)
            if closing:
                self.patterns['closings'][closing.lower()] += 1
            
            # Analyze structure
            self.analyze_sentence_structure(body)
            self.extract_common_phrases(body)
            
            # Email length
            self.patterns['email_lengths'].append(len(body.split()))
            
            # Time patterns
            if email['date']:
                try:
                    dt = parsedate_to_datetime(email['date'])
                    hour = dt.hour
                    if 6 <= hour < 12:
                        self.patterns['time_patterns']['morning'] += 1
                    elif 12 <= hour < 17:
                        self.patterns['time_patterns']['afternoon'] += 1
                    elif 17 <= hour < 22:
                        self.patterns['time_patterns']['evening'] += 1
                    else:
                        self.patterns['time_patterns']['night'] += 1
                except:
                    pass
            
            # Emoticons/emoji
            emoticons = re.findall(r'[:;]-?[)D(P]|(?:^|\s)(?:lol|haha|LOL)', body)
            for emoticon in emoticons:
                self.patterns['emoticons'][emoticon] += 1
    
    def generate_style_report(self):
        """Generate comprehensive style report"""
        report = {
            'total_emails_analyzed': len(self.emails),
            'writing_patterns': {},
            'structure_analysis': {},
            'common_elements': {},
            'communication_style': {}
        }
        
        # Most common greetings
        if self.patterns['greetings']:
            report['common_elements']['top_greetings'] = dict(
                self.patterns['greetings'].most_common(5)
            )
        
        # Most common closings
        if self.patterns['closings']:
            report['common_elements']['top_closings'] = dict(
                self.patterns['closings'].most_common(5)
            )
        
        # Sentence structure
        if self.patterns['sentence_lengths']:
            report['structure_analysis']['avg_sentence_length'] = round(
                statistics.mean(self.patterns['sentence_lengths']), 1
            )
            report['structure_analysis']['sentence_length_range'] = {
                'min': min(self.patterns['sentence_lengths']),
                'max': max(self.patterns['sentence_lengths'])
            }
        
        # Email length
        if self.patterns['email_lengths']:
            report['structure_analysis']['avg_email_length'] = round(
                statistics.mean(self.patterns['email_lengths']), 0
            )
        
        # Common phrases
        if self.patterns['common_phrases']:
            report['common_elements']['frequent_phrases'] = dict(
                self.patterns['common_phrases'].most_common(10)
            )
        
        # Time patterns
        if self.patterns['time_patterns']:
            total_time_emails = sum(self.patterns['time_patterns'].values())
            report['communication_style']['sending_times'] = {
                k: f"{round(v/total_time_emails*100, 1)}%" 
                for k, v in self.patterns['time_patterns'].items()
            }
        
        # Emoticon usage
        report['communication_style']['uses_emoticons'] = len(self.patterns['emoticons']) > 0
        
        return report
    
    def save_sample_emails(self, output_dir, num_samples=5):
        """Save anonymized email samples"""
        samples = []
        for i, email in enumerate(self.emails[:num_samples]):
            # Anonymize email addresses
            anonymized_body = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 
                                    '[EMAIL]', email['body'])
            # Anonymize phone numbers
            anonymized_body = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE]', anonymized_body)
            
            samples.append({
                'sample_id': i + 1,
                'subject': email['subject'],
                'body_preview': anonymized_body[:500] + '...' if len(anonymized_body) > 500 else anonymized_body
            })
        
        with open(f"{output_dir}/email_samples.json", 'w') as f:
            json.dump(samples, f, indent=2)
        
        return samples

def main():
    parser = argparse.ArgumentParser(description='Analyze email writing style from MBOX files')
    parser.add_argument('mbox_file', help='Path to MBOX file')
    parser.add_argument('--output', default='.', help='Output directory for results')
    
    args = parser.parse_args()
    
    analyzer = EmailStyleAnalyzer()
    
    print("Parsing MBOX file...")
    analyzer.parse_mbox(args.mbox_file)
    
    print("Analyzing email patterns...")
    analyzer.analyze_emails()
    
    print("Generating style report...")
    report = analyzer.generate_style_report()
    
    # Save report
    with open(f"{args.output}/email_style_analysis.json", 'w') as f:
        json.dump(report, f, indent=2)
    
    # Save samples
    analyzer.save_sample_emails(args.output)
    
    print(f"\nAnalysis complete!")
    print(f"- Analyzed {report['total_emails_analyzed']} emails")
    print(f"- Style report saved to: {args.output}/email_style_analysis.json")
    print(f"- Sample emails saved to: {args.output}/email_samples.json")
    
    # Print summary
    print("\n--- Quick Summary ---")
    if 'top_greetings' in report['common_elements']:
        print(f"Most common greeting: {list(report['common_elements']['top_greetings'].keys())[0]}")
    if 'avg_email_length' in report['structure_analysis']:
        print(f"Average email length: {report['structure_analysis']['avg_email_length']} words")
    if 'sending_times' in report['communication_style']:
        print(f"Most active time: {max(report['communication_style']['sending_times'], key=report['communication_style']['sending_times'].get)}")

if __name__ == "__main__":
    main()