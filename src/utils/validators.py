class URLValidator:
    def validate_vtt_url(self, url):
        if not url:
            raise ValueError("URL cannot be empty")
        
        if not url.strip():
            raise ValueError("URL cannot be whitespace")
            
        if not url.endswith('.vtt'):
            raise ValueError("The provided URL does not point to a .vtt file.")