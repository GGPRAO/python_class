# 🤖 Quick Start: Enhanced Naukri Job Assistant

## What's New?

✨ **No more hardcoded limits!** The chatbot can now search ANY number of emails (1-50) and intelligently filter them based on natural language queries.

## Start Using It

### 1️⃣ Run the Chatbot
```bash
streamlit run chatbot_ui.py
```

### 2️⃣ Try These Queries

Copy & paste any of these to see it in action:

```
1. "Show me Python developer jobs"
2. "Find jobs in Bangalore"
3. "Jobs with 10-15 lpa salary"
4. "Backend engineer roles for 5+ years"
5. "Remote work positions"
6. "TCS jobs"
7. "Bangalore Python developer 15-20 lpa"
8. "Remote backend engineer 3-5 years experience"
9. "Frontend developer roles in Mumbai"
10. "Data scientist positions with 10-15 lpa"
```

### 3️⃣ Adjust Settings
- **Change email limit**: Use sidebar slider (1-50)
- **View search history**: Click recent searches in sidebar
- **Clear chat**: Click "Clear Chat" button

## How It Works

```
Your Query (Natural Language)
    ↓
Chatbot understands what you want
    ↓
Searches through selected # of emails
    ↓
Extracts job details (role, salary, location, company, experience)
    ↓
Filters jobs based on your criteria
    ↓
Shows matching jobs with all details
```

## Example Interactions

### Scenario 1: Role-Based Search
**You:** "Show me Python developer jobs"
**Chatbot:** 
✅ Found 3 matching job(s)!

1. **Python Developer**
   🏢 Company: TechCorp
   📍 Location: Bangalore
   💰 Salary: ₹12,00,000 - ₹15,00,000 LPA
   📊 Experience: 2-5 years

[... more jobs ...]

### Scenario 2: Complex Filter
**You:** "Remote backend engineer jobs with 15-20 lpa for 3-5 years"
**Chatbot:**
✅ Found 2 matching job(s)!

Filters Applied:
• Role: backend engineer
• Location: remote
• Salary: 15-20 lpa
• Experience: 3-5 years

1. **Backend Engineer**
   🏢 Company: CloudTech
   📍 Location: Remote
   💰 Salary: ₹15,00,000 - ₹20,00,000 LPA
   📊 Experience: 3-5 years

### Scenario 3: Refine Results
**You:** "Can you show me backend jobs in Bangalore?"
**Chatbot:**
✅ Found 1 matching job(s)!

[Shows matching job]

**You:** "Do you have any with 20+ lpa?"
**Chatbot:**
❌ No jobs found matching your criteria!

I searched through 15 recent job notifications, but couldn't find matches for...

💡 Try:
- Being less specific with filters
- Searching for different roles
- Increasing the email limit in settings

## Supported Keywords

### Roles/Positions
- Developer, Engineer, Manager, Lead, Architect
- Python, Java, JavaScript, Full Stack, Backend, Frontend
- Data Scientist, DevOps, QA, etc.

### Locations
- Bangalore, Mumbai, Delhi, Hyderabad, Pune
- Chennai, Kolkata, Ahmedabad, Jaipur, Lucknow
- Indore, Chandigarh, Gurgaon, Noida, Surat
- Vadodara, Kochi, Coimbatore, Remote, Hybrid

### Salary (Automatic Recognition)
- "10-15 lpa"
- "20 lpa"
- "₹10 lakh - ₹15 lakh"
- "15-20 package"

### Experience (Automatic Recognition)
- "5+ years"
- "2-4 years"
- "3 yrs"
- "fresher"

### Companies
- Company names automatically recognized
- "Jobs at TCS"
- "Roles from Infosys"

## Natural Language Examples

The chatbot understands these natural ways of asking:

```
✅ "Show me Python jobs"
✅ "Find backend developer roles"
✅ "Get jobs with 15 lpa salary"
✅ "Jobs in Bangalore for 5+ years"
✅ "Remote Python developer positions"
✅ "Backend engineer + Mumbai + 10-15 lpa"
✅ "Can I see frontend jobs at TCS?"
✅ "What about data science roles?"
✅ "Filter by salary 20 lpa"
✅ "Jobs for fresher candidates"
```

## Tips & Tricks

### ⚡ Tip 1: Increase Search Range
- Default searches 15 emails
- Want more results? Increase to 30-50 in sidebar
- More emails = more chances to find matches

### ⚡ Tip 2: Combine Multiple Filters
- Role + Location: "Python in Bangalore"
- Role + Salary: "Developer 15 lpa"
- Role + Location + Salary: "Python in Mumbai 20 lpa"
- All 4 criteria: "Backend engineer in Bangalore 15-20 lpa 3-5 years"

### ⚡ Tip 3: Be Flexible
- If no results with specific filters
- Remove one filter and try again
- "Show me all Python jobs" (remove location)
- "Show me all Bangalore jobs" (remove role)

### ⚡ Tip 4: Use History
- Sidebar shows your recent searches
- Click to run again quickly
- Great for refining searches

### ⚡ Tip 5: Ask for Help
- Type "help" to see command list
- Type "what can you do?" for examples
- Chatbot will guide you

## What Gets Extracted From Emails?

The chatbot automatically extracts:

| Item | Example | Pattern |
|------|---------|---------|
| Role | "Python Developer" | Keywords like developer, engineer |
| Company | "TechCorp" | Company names in subject/body |
| Location | "Bangalore" | City names |
| Salary | "₹10-15 LPA" | Numbers + "lpa" |
| Experience | "5 years" | Numbers + "years/yrs" |

## Common Queries & Results

### Q1: "Show me Python jobs"
Searches for: Role contains "python"
Returns: All Python-related positions

### Q2: "Bangalore jobs"
Searches for: Location = Bangalore
Returns: All jobs in Bangalore

### Q3: "10-15 lpa"
Searches for: Salary between 10-15 LPA
Returns: Jobs in that salary range

### Q4: "5+ years"
Searches for: Experience requirement >= 5 years
Returns: Jobs for experienced professionals

### Q5: "Python developer Bangalore 15-20 lpa 3-5 years"
Searches for: ALL of the above
Returns: Jobs matching ALL criteria

## Troubleshooting

### Problem: "No jobs found"
**Solution:**
1. Increase email limit to 30-50
2. Remove one filter condition
3. Try more general search (just role, just location)

### Problem: "Salary not showing"
**Solution:**
- Not all emails have salary info
- Try role + location search instead

### Problem: "Can't find specific company"
**Solution:**
- Try searching by role + location
- Company names must match exactly

### Problem: Chatbot not responding
**Solution:**
1. Check Gmail is connected (green dot)
2. Click Refresh in sidebar
3. Try simpler query

## Performance Tips

- **Faster results**: Search 15-20 emails instead of 50
- **More options**: Search 40-50 emails for more matches
- **Balanced**: 20-30 emails is usually best

## What Happens Behind the Scenes?

1. **You type query**: "Python developer in Bangalore 15 lpa"
2. **Parse query**: Extract Python + Bangalore + 15 lpa
3. **Fetch emails**: Get 15 recent Naukri emails
4. **Extract jobs**: Parse each email for role, salary, location, etc.
5. **Filter**: Keep only jobs matching all criteria
6. **Display**: Show matching jobs with details

## Keyboard Shortcuts

- **Enter**: Send query
- **Ctrl+L**: Focus on input
- Use sidebar buttons for quick actions

## Getting Help

For issues:
1. Check sidebar status (should be 🟢 Connected)
2. Try simpler queries first
3. Check INTELLIGENT_CHATBOT_GUIDE.md for details
4. Review examples above

## Next Steps

1. ✅ Start the chatbot
2. ✅ Try 2-3 example queries
3. ✅ Adjust email limit in sidebar
4. ✅ Experiment with your own queries
5. ✅ Use search history to refine searches

---

**Happy job hunting! 🚀**

*The chatbot learns your preferences over time. The more you search, the better it understands what you want.*

