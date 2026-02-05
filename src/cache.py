"""
Simple in-memory cache for API responses
Reduces redundant API calls and improves performance
"""
import time
import hashlib
import json
from typing import Dict, Optional, Any
from functools import wraps

class SimpleCache:
    """
    Simple in-memory cache with TTL (Time To Live) support
    """
    
    def __init__(self, default_ttl: int = 300):
        """
        Initialize cache with default TTL in seconds.
        
        Args:
            default_ttl: Default time-to-live in seconds (default: 5 minutes)
        """
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.default_ttl = default_ttl
    
    def _make_key(self, *args, **kwargs) -> str:
        """Create a cache key from function arguments"""
        # Create a hash of the arguments
        key_data = json.dumps({"args": args, "kwargs": kwargs}, sort_keys=True)
        return hashlib.md5(key_data.encode()).hexdigest()
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get value from cache if not expired.
        
        Args:
            key: Cache key
        
        Returns:
            Cached value or None if not found/expired
        """
        if key not in self.cache:
            return None
        
        entry = self.cache[key]
        if time.time() > entry["expires_at"]:
            # Expired, remove it
            del self.cache[key]
            return None
        
        return entry["value"]
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        """
        Store value in cache with TTL.
        
        Args:
            key: Cache key
            value: Value to cache
            ttl: Time-to-live in seconds (uses default if None)
        """
        ttl = ttl or self.default_ttl
        self.cache[key] = {
            "value": value,
            "expires_at": time.time() + ttl
        }
    
    def clear(self):
        """Clear all cached entries"""
        self.cache.clear()
    
    def size(self) -> int:
        """Get number of cached entries"""
        return len(self.cache)

# Global cache instance
_cache = SimpleCache(default_ttl=300)  # 5 minutes default

def cached(ttl: Optional[int] = None):
    """
    Decorator to cache function results.
    
    Args:
        ttl: Time-to-live in seconds (uses cache default if None)
    
    Usage:
        @cached(ttl=600)  # Cache for 10 minutes
        def my_function(arg1, arg2):
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key
            cache_key = _cache._make_key(func.__name__, *args, **kwargs)
            
            # Try to get from cache
            cached_result = _cache.get(cache_key)
            if cached_result is not None:
                return cached_result
            
            # Call function and cache result
            result = func(*args, **kwargs)
            _cache.set(cache_key, result, ttl)
            
            return result
        
        return wrapper
    return decorator

def clear_cache():
    """Clear the global cache"""
    _cache.clear()

def get_cache_size() -> int:
    """Get the number of cached entries"""
    return _cache.size()
