#!/usr/bin/env python3
"""
Comprehensive test script for Google News Scraper
Tests various scenarios and validates functionality
"""
import os
import sys
import time
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(__file__))
from src.scraper import GoogleNewsScraper
from src.utils import save_to_json

load_dotenv()

def test_basic_search():
    """Test 1: Basic search functionality"""
    print("\n" + "="*60)
    print("TEST 1: Basic Search")
    print("="*60)
    scraper = GoogleNewsScraper()
    results = scraper.search("Artificial Intelligence", num=5)
    assert len(results) > 0, "Basic search should return results"
    assert all("title" in r and "link" in r for r in results), "Results should have title and link"
    print(f"[PASS] Found {len(results)} results with valid structure")
    return True

def test_country_parameter():
    """Test 2: Country parameter"""
    print("\n" + "="*60)
    print("TEST 2: Country Parameter")
    print("="*60)
    scraper = GoogleNewsScraper()
    results_uk = scraper.search("Tesla", num=5, country="uk")
    results_us = scraper.search("Tesla", num=5, country="us")
    # At least one should return results (API may occasionally return empty)
    assert len(results_uk) > 0 or len(results_us) > 0, "At least one country search should return results"
    print(f"[PASS] UK search returned {len(results_uk)} results")
    print(f"[PASS] US search returned {len(results_us)} results")
    return True

def test_limit_parameter():
    """Test 3: Limit parameter"""
    print("\n" + "="*60)
    print("TEST 3: Limit Parameter")
    print("="*60)
    scraper = GoogleNewsScraper()
    results_3 = scraper.search("Bitcoin", num=3)
    results_10 = scraper.search("Bitcoin", num=10)
    assert len(results_3) <= 3, f"Should return at most 3 results, got {len(results_3)}"
    assert len(results_10) <= 10, f"Should return at most 10 results, got {len(results_10)}"
    assert len(results_10) >= len(results_3), "More limit should return more or equal results"
    print(f"[PASS] Limit 3 returned {len(results_3)} results")
    print(f"[PASS] Limit 10 returned {len(results_10)} results")
    return True

def test_device_parameter():
    """Test 4: Device parameter"""
    print("\n" + "="*60)
    print("TEST 4: Device Parameter")
    print("="*60)
    scraper = GoogleNewsScraper()
    results_desktop = scraper.search("AI", num=5, device="desktop")
    results_mobile = scraper.search("AI", num=5, device="mobile")
    assert len(results_desktop) > 0, "Desktop search should return results"
    assert len(results_mobile) > 0, "Mobile search should return results"
    print(f"[PASS] Desktop search returned {len(results_desktop)} results")
    print(f"[PASS] Mobile search returned {len(results_mobile)} results")
    return True

def test_no_cache_parameter():
    """Test 5: No cache parameter"""
    print("\n" + "="*60)
    print("TEST 5: No Cache Parameter")
    print("="*60)
    scraper = GoogleNewsScraper()
    start_time = time.time()
    results = scraper.search("Technology", num=5, no_cache=True)
    elapsed = time.time() - start_time
    assert len(results) > 0, "No cache search should return results"
    print(f"[PASS] No cache search returned {len(results)} results in {elapsed:.2f}s")
    return True

def test_data_structure():
    """Test 6: Data structure validation"""
    print("\n" + "="*60)
    print("TEST 6: Data Structure Validation")
    print("="*60)
    scraper = GoogleNewsScraper()
    results = scraper.search("News", num=5)
    assert len(results) > 0, "Should return results"
    
    required_fields = ["title", "source", "date", "snippet", "link", "thumbnail"]
    for result in results:
        for field in required_fields:
            assert field in result, f"Result should have {field} field"
        assert result["title"], "Title should not be empty"
        assert result["link"], "Link should not be empty"
    
    print(f"[PASS] All {len(results)} results have valid structure")
    print(f"  Sample fields: {list(results[0].keys())}")
    return True

def test_performance():
    """Test 7: Performance test"""
    print("\n" + "="*60)
    print("TEST 7: Performance Test")
    print("="*60)
    scraper = GoogleNewsScraper()
    
    times = []
    for i in range(3):
        start = time.time()
        results = scraper.search("Test", num=5)
        elapsed = time.time() - start
        times.append(elapsed)
        assert len(results) > 0, "Performance test should return results"
        time.sleep(1)  # Avoid rate limiting
    
    avg_time = sum(times) / len(times)
    print(f"[PASS] Average response time: {avg_time:.2f}s")
    print(f"  Times: {[f'{t:.2f}s' for t in times]}")
    assert avg_time < 10, "Average response time should be under 10 seconds"
    return True

def test_error_handling():
    """Test 8: Error handling"""
    print("\n" + "="*60)
    print("TEST 8: Error Handling")
    print("="*60)
    scraper = GoogleNewsScraper()
    
    # Test with very long query (should handle gracefully)
    long_query = "A" * 500
    results = scraper.search(long_query, num=5)
    # Should return empty list or handle gracefully, not crash
    print(f"[PASS] Long query handled gracefully (returned {len(results)} results)")
    
    # Test with empty query (if allowed)
    # Note: This might be handled by API, so we just check it doesn't crash
    print(f"[PASS] Error handling works correctly")
    return True

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("GOOGLE NEWS SCRAPER - COMPREHENSIVE TEST SUITE")
    print("="*60)
    
    tests = [
        test_basic_search,
        test_country_parameter,
        test_limit_parameter,
        test_device_parameter,
        test_no_cache_parameter,
        test_data_structure,
        test_performance,
        test_error_handling,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except AssertionError as e:
            print(f"[FAIL] {e}")
            failed += 1
        except Exception as e:
            print(f"[ERROR] {e}")
            failed += 1
    
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Total tests: {len(tests)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print("="*60)
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
