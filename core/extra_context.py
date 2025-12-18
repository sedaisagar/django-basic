def my_context(request):
    footer_links = [
        "Home",
        "About Us",
        "Our Services",
        "Meet The Team",
        "Latest Blog",
        "Contact Us",
    ]
    return {
        "our_info":"Our Clinic Is Best In Market",
        "quick_links": footer_links,
    }