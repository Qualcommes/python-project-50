from .formats.plain import plain
from .formats.stylish import stylish


def format(diff, format_style='stylish'):
    if format_style == 'stylish':
        return stylish(diff)
    if format_style == 'plain':
        return plain(diff)
    
    raise ValueError(f"Unknown format: {format_style}")