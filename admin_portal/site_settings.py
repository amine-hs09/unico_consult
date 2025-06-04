from dataclasses import dataclass

@dataclass
class SiteSettings:
    """Stores basic SEO metadata and social links for the site."""
    seo_title: str = "Default Site Title"
    seo_description: str = "Default description of the site for SEO purposes."
    facebook_url: str = "https://facebook.com/your-page"
    linkedin_url: str = "https://linkedin.com/your-page"
    twitter_url: str = "https://twitter.com/your-page"
    instagram_url: str = "https://instagram.com/your-page"
