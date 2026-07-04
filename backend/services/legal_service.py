# backend/services/legal_service.py

def fetch_privacy_policy():
    """
    Returns the dynamic content for the Privacy Policy page.
    In a real app, this could be fetched from a database so admins can update it without code changes.
    """
    return {
        "last_updated": "July 4, 2026",
        "hero": {
            "title": "Privacy Policy",
            "subtitle": "Transparency • Security • Trust"
        },
        "sections": [
            {
                "id": "1",
                "title": "1. Introduction",
                "content": "Weather Intelligence Pro values your privacy and is committed to protecting your personal information. This policy explains how we collect, use, and safeguard your data."
            },
            {
                "id": "2",
                "title": "2. Information We Collect",
                "content": "<ul style='padding-left: 20px; list-style-type: disc;'><li>Account profile and authentication data</li><li>Search history (Cities, Locations, Maps)</li><li>Device information and Usage analytics</li></ul>"
            },
            {
                "id": "3",
                "title": "3. How We Use Your Data",
                "content": "The collected data is exclusively used to provide personalized AI insights, accurate weather forecasting, and to trigger targeted emergency alerts for your saved locations."
            },
            {
                "id": "4",
                "title": "4. Data Security",
                "content": "All sensitive data is encrypted using the AES-256 standard. Our infrastructure is monitored 24/7 to prevent unauthorized access, and we are fully GDPR compliant."
            }
        ],
        "stats": [
            {"value": "100%", "label": "Secure Storage"},
            {"value": "24/7", "label": "Monitoring"},
            {"value": "GDPR", "label": "Compliant"},
            {"value": "AES", "label": "Encryption"}
        ],
        "contact": {
            "title": "Contact Information",
            "email": "support@weatherintelligencepro.com",
            "phone": "+91 9876543210",
            "address": "Haldwani, Uttarakhand, India"
        }
    }