"""
Integration Guide for Gmail Module with Chatbot
Shows how to integrate the gmail module into your main chatbot application.
"""

# ============================================================================
# EXAMPLE 1: Simple Integration in Streamlit App
# ============================================================================

# import streamlit as st
# from gmail import get_chatbot_adapter
#
# def gmail_chatbot_page():
#     """Display Gmail chatbot interface."""
#     st.header("📧 Gmail Naukri Jobs Assistant")
#
#     # Get adapter
#     adapter = get_chatbot_adapter()
#
#     # Get available options
#     options = adapter.get_options()
#
#     # Display status
#     status = adapter.get_status()
#     st.sidebar.write(f"📧 Connected: {status['email']}")
#
#     # Create tabs for different commands
#     tab1, tab2, tab3 = st.tabs(["Fetch Jobs", "Status", "Options"])
#
#     with tab1:
#         col1, col2 = st.columns([3, 1])
#         with col1:
#             limit = st.slider("Number of jobs to fetch", 1, 20, 5)
#         with col2:
#             if st.button("🔄 Fetch"):
#                 result = adapter.execute_command('fetch_jobs', limit=limit)
#                 if result['status'] == 'success':
#                     st.success(result['message'])
#                     for i, email in enumerate(result['emails'], 1):
#                         st.write(f"{i}. {email['subject']}")
#                 else:
#                     st.error(result['message'])
#
#     with tab2:
#         st.json(adapter.get_status())
#
#     with tab3:
#         st.json(adapter.get_options())


# ============================================================================
# EXAMPLE 2: Chatbot Menu Integration
# ============================================================================

# from gmail import get_chatbot_adapter, get_gmail_options
#
# def display_gmail_menu():
#     """Display Gmail options in main chatbot menu."""
#     options = get_gmail_options()
#
#     print("📧 Available Gmail Commands:")
#     for i, option in enumerate(options['options'], 1):
#         print(f"{i}. {option['name']} - {option['description']}")
#
#     choice = input("Select option (number): ")
#
#     adapter = get_chatbot_adapter()
#
#     if choice == '1':  # Fetch jobs
#         limit = int(input("How many emails? (default: 5): ") or 5)
#         result = adapter.execute_command('fetch_jobs', limit=limit)
#         print(result['message'])
#     elif choice == '2':  # Status
#         result = adapter.execute_command('get_status')
#         print(f"Status: {result['status']}")
#     elif choice == '3':  # Options
#         result = adapter.execute_command('get_options')
#         print(result)


# ============================================================================
# EXAMPLE 3: Discord Bot Integration
# ============================================================================

# import discord
# from discord.ext import commands
# from gmail import get_chatbot_adapter
#
# bot = commands.Bot(command_prefix='!')
#
# @bot.command(name='jobs')
# async def fetch_jobs(ctx, limit: int = 5):
#     """Fetch Naukri jobs from Gmail."""
#     async with ctx.typing():
#         adapter = get_chatbot_adapter()
#         result = adapter.execute_command('fetch_jobs', limit=limit)
#
#         if result['status'] == 'success':
#             embed = discord.Embed(
#                 title="📧 Naukri Jobs",
#                 description=result['message'],
#                 color=discord.Color.blue()
#             )
#             for i, email in enumerate(result['emails'][:5], 1):
#                 embed.add_field(
#                     name=f"{i}. {email['subject'][:50]}",
#                     value=f"{email['body'][:100]}...",
#                     inline=False
#                 )
#             await ctx.send(embed=embed)
#         else:
#             await ctx.send(f"❌ Error: {result['message']}")


# ============================================================================
# EXAMPLE 4: Telegram Bot Integration
# ============================================================================

# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes
# from gmail import get_chatbot_adapter
#
# async def jobs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Fetch Naukri jobs command."""
#     adapter = get_chatbot_adapter()
#
#     try:
#         limit = int(context.args[0]) if context.args else 5
#     except (ValueError, IndexError):
#         limit = 5
#
#     result = adapter.execute_command('fetch_jobs', limit=limit)
#
#     if result['status'] == 'success':
#         message = result['message'] + "\n\n"
#         for i, email in enumerate(result['emails'], 1):
#             message += f"{i}. {email['subject']}\n"
#         await update.message.reply_text(message)
#     else:
#         await update.message.reply_text(f"❌ {result['message']}")


# ============================================================================
# EXAMPLE 5: REST API Integration (FastAPI)
# ============================================================================

# from fastapi import FastAPI, HTTPException
# from gmail import get_chatbot_adapter
#
# app = FastAPI()
#
# @app.get("/api/gmail/jobs")
# async def get_jobs(limit: int = 5):
#     """Get Naukri jobs from Gmail."""
#     adapter = get_chatbot_adapter()
#     result = adapter.execute_command('fetch_jobs', limit=limit)
#
#     if result['status'] == 'error':
#         raise HTTPException(status_code=500, detail=result['message'])
#
#     return result
#
# @app.get("/api/gmail/status")
# async def get_status():
#     """Get Gmail service status."""
#     adapter = get_chatbot_adapter()
#     return adapter.get_status()
#
# @app.get("/api/gmail/options")
# async def get_options():
#     """Get available commands."""
#     adapter = get_chatbot_adapter()
#     return adapter.get_options()


# ============================================================================
# EXAMPLE 6: Class-Based Chatbot Integration
# ============================================================================

# from gmail import get_chatbot_adapter
#
# class ChatbotManager:
#     """Main chatbot manager with Gmail integration."""
#
#     def __init__(self):
#         self.gmail_adapter = get_chatbot_adapter()
#         self.modules = {
#             'gmail': self.gmail_adapter
#         }
#
#     def handle_command(self, module: str, command: str, **kwargs):
#         """Route commands to appropriate module."""
#         if module == 'gmail':
#             return self.gmail_adapter.execute_command(command, **kwargs)
#         else:
#             return {"status": "error", "message": f"Unknown module: {module}"}
#
#     def get_available_modules(self):
#         """Get list of available modules."""
#         return list(self.modules.keys())
#
#     def get_module_options(self, module: str):
#         """Get options for a specific module."""
#         if module == 'gmail':
#             return self.gmail_adapter.get_options()
#         else:
#             return {"error": f"Module {module} not found"}
#
# # Usage
# chatbot = ChatbotManager()
# result = chatbot.handle_command('gmail', 'fetch_jobs', limit=5)
# print(result)


# ============================================================================
# EXAMPLE 7: Async Integration
# ============================================================================

# import asyncio
# from gmail import fetch_jobs_for_chatbot, get_gmail_status
#
# async def async_fetch_jobs(limit: int = 5):
#     """Fetch jobs asynchronously using thread pool."""
#     loop = asyncio.get_event_loop()
#     result = await loop.run_in_executor(None, fetch_jobs_for_chatbot, limit)
#     return result
#
# async def main():
#     """Main async function."""
#     print("Fetching jobs...")
#     result = await async_fetch_jobs(5)
#     print(f"Found {result['count']} jobs")
#
# # Run
# asyncio.run(main())


# ============================================================================
# EXAMPLE 8: Error Handling & Logging
# ============================================================================

# import logging
# from gmail import get_chatbot_adapter
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# def fetch_jobs_safely(limit: int = 5):
#     """Fetch jobs with error handling and logging."""
#     try:
#         adapter = get_chatbot_adapter()
#         logger.info(f"Fetching {limit} Naukri jobs...")
#
#         result = adapter.execute_command('fetch_jobs', limit=limit)
#
#         if result['status'] == 'success':
#             logger.info(f"Successfully fetched {result['count']} jobs")
#             return result
#         else:
#             logger.error(f"Failed to fetch jobs: {result['message']}")
#             return result
#
#     except Exception as e:
#         logger.exception(f"Unexpected error: {e}")
#         return {"status": "error", "message": str(e), "emails": []}


# ============================================================================
# QUICK START TEMPLATE
# ============================================================================

"""
Basic template for chatbot integration:

from gmail import get_chatbot_adapter

# Initialize
adapter = get_chatbot_adapter()

# Get available commands
options = adapter.get_options()

# Check status
status = adapter.get_status()

# Execute commands
result = adapter.execute_command('fetch_jobs', limit=5)

# Handle response
if result['status'] == 'success':
    print(f"✅ {result['message']}")
    for email in result['emails']:
        print(f"  - {email['subject']}")
else:
    print(f"❌ {result['message']}")
"""

print("Integration Guide Loaded!")
print("\nAvailable integration examples:")
print("1. Streamlit App Integration")
print("2. Chatbot Menu Integration")
print("3. Discord Bot Integration")
print("4. Telegram Bot Integration")
print("5. FastAPI REST Integration")
print("6. Class-Based Chatbot Integration")
print("7. Async Integration")
print("8. Error Handling & Logging")
print("\nUncomment the examples in this file to use them!")

