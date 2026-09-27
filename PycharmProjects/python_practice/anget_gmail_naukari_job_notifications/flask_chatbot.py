#!/usr/bin/env python3
"""
Gmail Chatbot - Flask Backend
Provides REST API for the chatbot frontend
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from flask import Flask, jsonify, request
from datetime import datetime
import json

app = Flask(__name__)

# Try to import gmail module
try:
    from gmail import get_chatbot_adapter, get_gmail_status, get_gmail_options
    gmail_available = True
except ImportError as e:
    print(f"Warning: Gmail module not available: {e}")
    gmail_available = False

# Routes

@app.route('/')
def index():
    """Serve the chatbot UI"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Naukri Job Chatbot</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 12px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                max-width: 800px;
                width: 100%;
                overflow: hidden;
            }
            
            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 30px;
                text-align: center;
            }
            
            .header h1 {
                font-size: 2rem;
                margin-bottom: 10px;
            }
            
            .header p {
                opacity: 0.9;
                font-size: 0.95rem;
            }
            
            .content {
                padding: 30px;
            }
            
            .controls {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 12px;
                margin-bottom: 20px;
            }
            
            .control-group {
                display: flex;
                gap: 10px;
                align-items: center;
            }
            
            label {
                font-weight: 600;
                color: #333;
                font-size: 0.9rem;
            }
            
            input[type="range"] {
                flex: 1;
            }
            
            .limit-value {
                min-width: 40px;
                background: #f0f0f0;
                padding: 8px 12px;
                border-radius: 6px;
                text-align: center;
                font-weight: 600;
                color: #667eea;
            }
            
            .buttons {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 12px;
                margin-bottom: 20px;
            }
            
            button {
                padding: 12px 20px;
                border: none;
                border-radius: 8px;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s ease;
            }
            
            .btn-primary {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            
            .btn-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
            }
            
            .btn-secondary {
                background: #f0f0f0;
                color: #333;
            }
            
            .btn-secondary:hover {
                background: #e0e0e0;
            }
            
            button:disabled {
                opacity: 0.6;
                cursor: not-allowed;
            }
            
            .status {
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
                display: none;
            }
            
            .status.show {
                display: block;
            }
            
            .status.success {
                background: #d4edda;
                color: #155724;
                border: 1px solid #c3e6cb;
            }
            
            .status.error {
                background: #f8d7da;
                color: #721c24;
                border: 1px solid #f5c6cb;
            }
            
            .status.loading {
                background: #cfe2ff;
                color: #084298;
                border: 1px solid #b6d4fe;
            }
            
            .jobs-container {
                display: grid;
                gap: 15px;
            }
            
            .job-card {
                background: #f8f9fa;
                border-left: 4px solid #667eea;
                padding: 20px;
                border-radius: 8px;
                transition: all 0.3s ease;
            }
            
            .job-card:hover {
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }
            
            .job-card h3 {
                color: #333;
                margin-bottom: 10px;
                font-size: 1.1rem;
            }
            
            .job-card p {
                color: #666;
                line-height: 1.6;
                font-size: 0.95rem;
            }
            
            .job-number {
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 4px 10px;
                border-radius: 20px;
                font-size: 0.85rem;
                margin-right: 10px;
            }
            
            .empty-state {
                text-align: center;
                padding: 40px;
                color: #999;
            }
            
            .empty-state p {
                font-size: 1rem;
                margin: 10px 0;
            }
            
            .loading-spinner {
                display: inline-block;
                width: 20px;
                height: 20px;
                border: 3px solid rgba(102, 126, 234, 0.3);
                border-top-color: #667eea;
                border-radius: 50%;
                animation: spin 1s linear infinite;
            }
            
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>💼 Naukri Job Assistant</h1>
                <p>Fetch and view your latest job notifications</p>
            </div>
            
            <div class="content">
                <div class="controls">
                    <div class="control-group">
                        <label for="limit">Emails to fetch:</label>
                        <input type="range" id="limit" min="1" max="20" value="5">
                        <span class="limit-value" id="limitValue">5</span>
                    </div>
                </div>
                
                <div class="buttons">
                    <button class="btn-primary" id="fetchBtn" onclick="fetchJobs()">
                        🔄 Fetch Jobs
                    </button>
                    <button class="btn-secondary" id="statusBtn" onclick="checkStatus()">
                        ℹ️ Service Status
                    </button>
                </div>
                
                <div class="status" id="status"></div>
                
                <div class="jobs-container" id="jobsContainer">
                    <div class="empty-state">
                        <p>👈 Click "Fetch Jobs" to get started!</p>
                    </div>
                </div>
            </div>
        </div>
        
        <script>
            // Update limit display
            document.getElementById('limit').addEventListener('input', function() {
                document.getElementById('limitValue').textContent = this.value;
            });
            
            function showStatus(message, type) {
                const statusEl = document.getElementById('status');
                statusEl.textContent = message;
                statusEl.className = `status show ${type}`;
            }
            
            function fetchJobs() {
                const limit = document.getElementById('limit').value;
                const fetchBtn = document.getElementById('fetchBtn');
                fetchBtn.disabled = true;
                
                showStatus('⏳ Fetching jobs...', 'loading');
                
                fetch(`/api/fetch?limit=${limit}`)
                    .then(res => res.json())
                    .then(data => {
                        fetchBtn.disabled = false;
                        
                        if (data.success) {
                            showStatus(`✅ Found ${data.count} jobs!`, 'success');
                            displayJobs(data.jobs);
                        } else {
                            showStatus(`❌ ${data.error}`, 'error');
                            document.getElementById('jobsContainer').innerHTML = 
                                '<div class="empty-state"><p>⚠️ No jobs found or error occurred</p></div>';
                        }
                    })
                    .catch(error => {
                        fetchBtn.disabled = false;
                        showStatus(`❌ Error: ${error.message}`, 'error');
                    });
            }
            
            function displayJobs(jobs) {
                const container = document.getElementById('jobsContainer');
                
                if (!jobs || jobs.length === 0) {
                    container.innerHTML = '<div class="empty-state"><p>No jobs to display</p></div>';
                    return;
                }
                
                container.innerHTML = jobs.map((job, idx) => `
                    <div class="job-card">
                        <h3>
                            <span class="job-number">#${idx + 1}</span>
                            ${job.subject || 'No Subject'}
                        </h3>
                        <p>${(job.body || 'No content').substring(0, 300)}...</p>
                    </div>
                `).join('');
            }
            
            function checkStatus() {
                const statusBtn = document.getElementById('statusBtn');
                statusBtn.disabled = true;
                
                fetch('/api/status')
                    .then(res => res.json())
                    .then(data => {
                        statusBtn.disabled = false;
                        const status = data.data;
                        const message = `📧 Email: ${status.email} | Service: ${status.service} | Status: ${status.status}`;
                        showStatus(message, 'success');
                    })
                    .catch(error => {
                        statusBtn.disabled = false;
                        showStatus(`❌ Error: ${error.message}`, 'error');
                    });
            }
        </script>
    </body>
    </html>
    '''

@app.route('/api/fetch')
def api_fetch():
    """API endpoint to fetch jobs"""
    if not gmail_available:
        return jsonify({
            'success': False,
            'error': 'Gmail module not available'
        })

    try:
        limit = request.args.get('limit', 5, type=int)
        adapter = get_chatbot_adapter()
        result = adapter.fetch_jobs(limit=limit)

        return jsonify({
            'success': result['status'] == 'success',
            'count': result.get('count', 0),
            'jobs': result.get('emails', []),
            'error': result.get('message') if result['status'] != 'success' else None
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/status')
def api_status():
    """API endpoint for service status"""
    if not gmail_available:
        return jsonify({
            'success': False,
            'error': 'Gmail module not available'
        })

    try:
        status = get_gmail_status()
        return jsonify({
            'success': True,
            'data': status
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/commands')
def api_commands():
    """API endpoint for available commands"""
    if not gmail_available:
        return jsonify({
            'success': False,
            'error': 'Gmail module not available'
        })

    try:
        options = get_gmail_options()
        return jsonify({
            'success': True,
            'data': options
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Gmail Chatbot Server")
    print("=" * 60)
    print("\n📱 Open your browser to: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server\n")

    app.run(debug=True, port=5000, use_reloader=False)

