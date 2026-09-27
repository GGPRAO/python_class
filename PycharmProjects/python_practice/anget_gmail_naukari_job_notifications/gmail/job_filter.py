"""
Job Filter Module
Intelligent job filtering and extraction based on keywords and criteria.
"""

import re
from typing import List, Dict, Any


class JobFilter:
    """Filter and extract job information from emails."""

    # Keywords for extracting job details
    SALARY_PATTERNS = [
        r'₹?(\d+(?:,\d+)*)\s*-\s*₹?(\d+(?:,\d+)*)\s*(?:lpa|lac|p\.a\.)',
        r'salary[:\s]*₹?(\d+(?:,\d+)*)\s*-\s*₹?(\d+(?:,\d+)*)',
        r'(\d+(?:,\d+)*)\s*-\s*(\d+(?:,\d+)*)\s*lpa',
    ]

    EXPERIENCE_PATTERNS = [
        r'(\d+)\s*-\s*(\d+)\s*years?',
        r'experience[:\s]*(\d+)\s*-\s*(\d+)',
        r'(\d+)\s*(?:\+\s*)?yrs?\.?',
    ]

    LOCATION_KEYWORDS = [
        'location', 'city', 'based', 'cities', 'places', 'area', 'regions'
    ]

    def __init__(self):
        """Initialize the job filter."""
        self.extracted_jobs = []

    def extract_salary_range(self, text: str) -> Dict[str, Any]:
        """Extract salary information from text."""
        text_lower = text.lower()
        for pattern in self.SALARY_PATTERNS:
            matches = re.finditer(pattern, text_lower, re.IGNORECASE)
            for match in matches:
                try:
                    min_sal = int(match.group(1).replace(',', ''))
                    max_sal = int(match.group(2).replace(',', ''))
                    return {
                        'min': min_sal,
                        'max': max_sal,
                        'currency': '₹',
                        'unit': 'lpa'
                    }
                except (IndexError, ValueError):
                    continue
        return None

    def extract_experience(self, text: str) -> Dict[str, Any]:
        """Extract experience requirements from text."""
        text_lower = text.lower()
        for pattern in self.EXPERIENCE_PATTERNS:
            matches = re.finditer(pattern, text_lower)
            for match in matches:
                try:
                    if len(match.groups()) == 2:
                        min_exp = int(match.group(1))
                        max_exp = int(match.group(2))
                        return {
                            'min': min_exp,
                            'max': max_exp,
                            'unit': 'years'
                        }
                    elif len(match.groups()) == 1:
                        exp = int(match.group(1))
                        return {
                            'min': exp,
                            'max': exp,
                            'unit': 'years'
                        }
                except (IndexError, ValueError):
                    continue
        return None

    def extract_job_role(self, text: str) -> str:
        """Extract job role/title from text."""
        text = text[:500]  # Limit to first 500 chars for efficiency

        # Common job role patterns
        patterns = [
            r'(?:position|role|job|title)[:\s]*([\w\s&]+?)(?:\.|,|\n|apply)',
            r'hiring\s+(?:for\s+)?(?:a\s+)?([\w\s&]+?)(?:\s+(?:role|position))?(?:\s+in|\s+at|\.|,|\n)',
            r'^([\w\s&]+?)\s+(?:role|position|job)',
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                role = match.group(1).strip()
                if role and len(role) < 100:  # Sanity check
                    return role

        # Fallback: extract from subject
        return None

    def extract_company(self, email: Dict) -> str:
        """Extract company name from email."""
        subject = email.get('subject', '').lower()
        body = email.get('body', '').lower()[:1000]

        # Try to find company in subject first
        if 'naukri' in subject or 'naukri.com' in subject:
            # Extract from patterns like "Job Opportunity at CompanyName"
            match = re.search(r'(?:at|from|by)\s+([\w\s&]+?)(?:\s+-|\s+|$|:)', subject, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        # Check body
        patterns = [
            r'company[:\s]*([\w\s&]+?)(?:\.|,|\n)',
            r'about\s+([\w\s&]+?)(?:\s+jobs?|\s+-)',
        ]

        for pattern in patterns:
            match = re.search(pattern, body, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return "Unknown Company"

    def extract_location(self, text: str) -> List[str]:
        """Extract location(s) from text."""
        locations = []
        text_lower = text.lower()

        # Common Indian cities and locations
        common_locations = [
            'bangalore', 'bengaluru', 'mumbai', 'delhi', 'new delhi', 'hyderabad',
            'pune', 'chennai', 'kolkata', 'ahmedabad', 'jaipur', 'lucknow',
            'indore', 'chandigarh', 'gurgaon', 'noida', 'surat', 'vadodara',
            'kochi', 'coimbatore', 'visakhapatnam', 'nagpur', 'pune', 'remote',
            'work from home', 'wfh', 'hybrid', 'onsite', 'pan-india'
        ]

        for location in common_locations:
            if location in text_lower:
                locations.append(location.title())

        return locations if locations else ["Not Specified"]

    def extract_job_details(self, email: Dict) -> Dict[str, Any]:
        """Extract all job details from an email."""
        subject = email.get('subject', '')
        body = email.get('body', '')
        full_text = f"{subject}\n{body}"

        job_details = {
            'subject': subject,
            'company': self.extract_company(email),
            'role': self.extract_job_role(full_text),
            'salary': self.extract_salary_range(full_text),
            'experience': self.extract_experience(full_text),
            'locations': self.extract_location(full_text),
            'body_preview': body[:300] if body else "No description"
        }

        return job_details

    def filter_jobs(self, jobs: List[Dict], **criteria) -> List[Dict]:
        """
        Filter jobs based on criteria.

        Args:
            jobs: List of job dictionaries
            **criteria: Filter criteria
                - role: Job role keyword
                - company: Company name
                - location: Location
                - min_salary: Minimum salary (lpa)
                - max_salary: Maximum salary (lpa)
                - min_experience: Minimum experience required
                - max_experience: Maximum experience required

        Returns:
            Filtered list of jobs
        """
        filtered = jobs

        # Filter by role
        if 'role' in criteria and criteria['role']:
            role_query = criteria['role'].lower()
            filtered = [
                j for j in filtered
                if j.get('role') and role_query in j['role'].lower()
            ]

        # Filter by company
        if 'company' in criteria and criteria['company']:
            company_query = criteria['company'].lower()
            filtered = [
                j for j in filtered
                if company_query in j.get('company', '').lower()
            ]

        # Filter by location
        if 'location' in criteria and criteria['location']:
            location_query = criteria['location'].lower()
            filtered = [
                j for j in filtered
                if any(location_query in loc.lower() for loc in j.get('locations', []))
            ]

        # Filter by salary range
        if 'min_salary' in criteria and criteria['min_salary']:
            min_sal = criteria['min_salary']
            filtered = [
                j for j in filtered
                if j.get('salary') and j['salary'].get('min', 0) >= min_sal
            ]

        if 'max_salary' in criteria and criteria['max_salary']:
            max_sal = criteria['max_salary']
            filtered = [
                j for j in filtered
                if j.get('salary') and j['salary'].get('max', 0) <= max_sal
            ]

        # Filter by experience
        if 'max_experience' in criteria and criteria['max_experience']:
            max_exp = criteria['max_experience']
            filtered = [
                j for j in filtered
                if j.get('experience') and j['experience'].get('min', 0) <= max_exp
            ]

        return filtered

    def parse_query(self, query: str) -> Dict[str, Any]:
        """
        Parse natural language query to extract filter criteria.

        Args:
            query: Natural language query

        Returns:
            Dictionary of extracted criteria
        """
        query_lower = query.lower()
        criteria = {}

        # Extract salary first (it's most distinct)
        salary_match = re.search(r'(\d+)\s*(?:-\s*(\d+))?\s*(?:lpa|lac|l\.p\.a)', query_lower)
        if salary_match:
            min_sal = int(salary_match.group(1))
            max_sal = int(salary_match.group(2)) if salary_match.group(2) else min_sal
            criteria['min_salary'] = min_sal
            criteria['max_salary'] = max_sal

        # Extract experience (years)
        exp_match = re.search(r'(\d+)\s*(?:-\s*(\d+))?\s*(?:\+)?\s*(?:yrs?|years?)', query_lower)
        if exp_match:
            min_exp = int(exp_match.group(1))
            max_exp = int(exp_match.group(2)) if exp_match.group(2) else min_exp
            if max_exp == min_exp:
                criteria['max_experience'] = min_exp
            else:
                criteria['max_experience'] = max_exp

        # Extract location - look for city keywords
        location_keywords = [
            'bangalore', 'bengaluru', 'mumbai', 'delhi', 'new delhi', 'hyderabad',
            'pune', 'chennai', 'kolkata', 'ahmedabad', 'jaipur', 'lucknow',
            'indore', 'chandigarh', 'gurgaon', 'noida', 'surat', 'vadodara',
            'kochi', 'coimbatore', 'visakhapatnam', 'nagpur', 'remote', 'hybrid'
        ]

        for loc in location_keywords:
            if loc in query_lower:
                criteria['location'] = loc
                break

        # Extract role/title - look for job-related keywords
        role_keywords = [
            'python', 'java', 'javascript', 'developer', 'engineer', 'manager',
            'architect', 'lead', 'backend', 'frontend', 'full stack', 'fullstack',
            'data scientist', 'devops', 'qa', 'analyst', 'admin', 'tester',
            'designer', 'product', 'scrum'
        ]

        # Find all matching roles in query
        matched_roles = []
        for role in role_keywords:
            if role in query_lower:
                matched_roles.append(role)

        # Combine matched roles (e.g., "python" + "developer" = "python developer")
        if matched_roles:
            # Sort by length (descending) to prioritize longer matches
            matched_roles.sort(key=len, reverse=True)

            # Remove substrings (e.g., if "full stack" exists, remove "fullstack")
            unique_roles = []
            for r in matched_roles:
                skip = False
                for ur in unique_roles:
                    if r in ur or ur in r:
                        skip = True
                        break
                if not skip:
                    unique_roles.append(r)

            criteria['role'] = ' '.join(unique_roles[:3])  # Limit to top 3 keywords

        # Extract company name - look for common company names
        companies = [
            'tcs', 'infosys', 'accenture', 'wipro', 'cognizant', 'tech mahindra',
            'hcl', 'capgemini', 'ibm', 'oracle', 'deloitte', 'pwc', 'ey',
            'google', 'amazon', 'microsoft', 'apple', 'facebook', 'uber',
            'flipkart', 'myntra', 'paytm', 'olx', 'zomato', 'swiggy'
        ]

        for company in companies:
            if company in query_lower:
                criteria['company'] = company
                break

        return criteria


# Helper function
def extract_and_filter_jobs(emails: List[Dict], query: str = None) -> tuple:
    """
    Extract job details from emails and optionally filter by query.

    Args:
        emails: List of email dictionaries
        query: Optional query to filter jobs

    Returns:
        Tuple of (extracted_jobs, filter_criteria, filtered_jobs)
    """
    filter_obj = JobFilter()

    # Extract all jobs
    extracted_jobs = [filter_obj.extract_job_details(email) for email in emails]

    # Parse query and filter if provided
    filter_criteria = {}
    filtered_jobs = extracted_jobs

    if query:
        filter_criteria = filter_obj.parse_query(query)
        filtered_jobs = filter_obj.filter_jobs(extracted_jobs, **filter_criteria)

    return extracted_jobs, filter_criteria, filtered_jobs

