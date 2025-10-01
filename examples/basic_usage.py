#!/usr/bin/env python3
"""
Basic usage example for Sheetsight Python client
"""

import os
from sheetsight_py import SheetsightClient, AuthenticationError, APIError

def main():
    # Get API key from environment variable or replace with your key
    api_key = os.getenv("SHEETSIGHT_API_KEY")
    if not api_key:
        print("Please set SHEETSIGHT_API_KEY environment variable or replace with your API key")
        print("Get your API key from: https://sheetsight.ai/dashboard")
        return
    
    try:
        # Initialize client
        with SheetsightClient(api_key=api_key) as client:
            # Example 1: Simple search
            print("🔍 Searching for ESP32 power consumption...")
            results = client.search("ESP32 power consumption", max_results=3)
            
            print(f"\n✅ Found {results['total_results']} results across {results['total_parts']} parts")
            print(f"⏱️  Processing time: {results['processing_time_ms']}ms")
            
            # Display results
            for i, group in enumerate(results['grouped_results'], 1):
                part = group['part']
                manufacturer = group['manufacturer']
                
                print(f"\n📦 {i}. {part['partNumber']} by {manufacturer['displayName']}")
                print(f"   Description: {part.get('description', 'N/A')}")
                print(f"   Matches: {group['matchCount']} (Score: {group['totalRelevanceScore']:.1f})")
                
                # Show best match content preview
                if group['bestMatch']:
                    match = group['bestMatch']
                    content_preview = match['content'][:150].replace('\n', ' ')
                    print(f"   Best match: \"{content_preview}...\"")
                    if match['page_number']:
                        print(f"   Page: {match['page_number']}")
            
            # Example 2: Using custom options
            print("\n\n🔍 Search with custom options...")
            custom_results = client.global_search(
                "STM32 GPIO configuration",
                options={
                    "maxResults": 5,
                    "maxMatchesPerPart": 2,
                    "groupByPart": True
                }
            )
            
            print(f"✅ Custom search found {custom_results['total_results']} results")
            
            # Example 3: Ungrouped search
            print("\n\n🔍 Ungrouped search results...")
            ungrouped_results = client.search(
                "Arduino compatibility", 
                max_results=10,
                group_by_part=False
            )
            
            print(f"✅ Ungrouped search found {ungrouped_results['total_results']} results")
            
    except AuthenticationError:
        print("❌ Authentication failed. Please check your API key.")
    except APIError as e:
        print(f"❌ API error: {e}")
        if hasattr(e, 'status_code'):
            print(f"   Status code: {e.status_code}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
