from .formats.json import render_json
from .formats.plain import plain
from .formats.stylish import stylish


def format(diff, format_style='stylish'):
    if format_style == 'stylish':
        return stylish(diff)
    if format_style == 'plain':
        return plain(diff)
    if format_style == 'json':
        return render_json(diff)
    
    raise ValueError(f"Unknown format: {format_style}")