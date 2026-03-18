import requests
from bs4 import BeautifulSoup
import csv

# 1. Add your URLs to this list
urls = [
    "https://www.salesforce.com/form/service-cloud/ai-for-customer-service-demo/?d=pb",
    "https://www.salesforce.com/ap/form/service-cloud/ai-for-customer-service-demo/?d=pb",
    "https://www.salesforce.com/au/form/service-cloud/ai-for-customer-service-demo/?d=pb",
    # Add as many as you need...
]

def get_campaign_id(url):
    try:
        # Request with a timeout so the script doesn't hang forever
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.find(attrs={"name": "FormCampaignId"})
        
        if element and element.has_attr('value'):
            return element['value']
        else:
            return "Not Found"
            
    except Exception as e:
        return f"Error: {str(e)}"

# 2. Process the batch and save to CSV
output_file = "campaign_ids.csv"

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the Header Row
    writer.writerow(["URL", "Campaign ID"])
    
    print(f"Starting crawl of {len(urls)} URLs...")
    
    for url in urls:
        print(f"Checking: {url}")
        campaign_id = get_campaign_id(url)
        writer.writerow([url, campaign_id])

print(f"\nDone! Results saved to {output_file}")