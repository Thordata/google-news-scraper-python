"""
Progress indicator utilities
Provides visual feedback for long-running operations
"""
import sys
from typing import Optional

class ProgressBar:
    """
    Simple progress bar for terminal output
    """
    
    def __init__(self, total: int, prefix: str = "Progress", length: int = 40):
        """
        Initialize progress bar.
        
        Args:
            total: Total number of items
            prefix: Prefix text
            length: Length of progress bar in characters
        """
        self.total = total
        self.prefix = prefix
        self.length = length
        self.current = 0
    
    def update(self, n: int = 1):
        """
        Update progress by n items.
        
        Args:
            n: Number of items to increment
        """
        self.current = min(self.current + n, self.total)
        self._display()
    
    def _display(self):
        """Display the progress bar"""
        if self.total == 0:
            percent = 100
        else:
            percent = 100 * (self.current / self.total)
        
        filled = int(self.length * self.current // self.total) if self.total > 0 else self.length
        bar = '=' * filled + '-' * (self.length - filled)
        
        sys.stdout.write(f'\r{self.prefix}: [{bar}] {percent:.1f}% ({self.current}/{self.total})')
        sys.stdout.flush()
    
    def finish(self):
        """Finish the progress bar"""
        self.current = self.total
        self._display()
        print()  # New line after completion

def show_progress(current: int, total: int, prefix: str = "Progress"):
    """
    Simple progress indicator.
    
    Args:
        current: Current item number
        total: Total number of items
        prefix: Prefix text
    """
    percent = 100 * (current / total) if total > 0 else 100
    print(f"\r{prefix}: {current}/{total} ({percent:.1f}%)", end="", flush=True)
    if current >= total:
        print()  # New line when complete
