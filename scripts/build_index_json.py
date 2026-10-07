"""Builds templates/index.json and the header/footer group JSON for the Mezzame homepage.

Content is the sample copy from the approved prototype ("Gift Hamper Layout 2") with the
brand spelled Mezzame and designer notes removed. Re-run after editing, then push.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "theme"
IMG = "shopify://shop_images/mezamme-{}".format  # files already uploaded to Shopify Files


def blocks(prefix, items):
    data = {f"{prefix}_{i}": item for i, item in enumerate(items, 1)}
    return {"blocks": data, "block_order": list(data)}


hero = {
    "type": "mzh-hero",
    "settings": {"aria_label": "Mezzame featured celebrations", "autoplay_seconds": 7},
    **blocks("slide", [
        {"type": "slide", "settings": {
            "image": IMG("731116dfeb85.webp"),
            "kicker": "Signature cakes · Crafted in Chennai",
            "heading": "Cakes Worth\nShowing Up For.",
            "text": "Freshly baked celebration cakes and layered desserts—crafted in small batches, finished by hand and made to be remembered.",
            "button_1_label": "Shop Cakes", "button_1_link": "#cakes",
            "button_2_label": "Discover Mezzame", "button_2_link": "#why"}},
        {"type": "slide", "settings": {
            "image": IMG("d88120efe3d9.png"),
            "kicker": "Celebrations, finished beautifully",
            "heading": "Made for\nYour Moment.",
            "text": "Statement cakes, thoughtful hampers and elegant packaging for birthdays, milestones and meaningful celebrations.",
            "button_1_label": "Explore Gift Hampers", "button_1_link": "#gifts",
            "button_2_label": "Shop by Occasion", "button_2_link": "#occasions"}},
    ]),
}

trust = {
    "type": "mzh-trust",
    "settings": {"aria_label": "Why customers choose Mezzame"},
    **blocks("item", [{"type": "item", "settings": {"text": t}} for t in [
        "Freshly Baked Daily", "Premium Ingredients", "Delivery Across Chennai",
        "Eggless Options", "Elegant Gift Packaging", "Custom Celebration Cakes"]]),
}

products = {
    "type": "mzh-products",
    "settings": {
        "anchor": "cakes", "eyebrow": "Easy entry collection", "heading": "Best Sellers Under ₹1,500",
        "text": "Our most-loved cakes, freshly baked in Chennai and ready for your next celebration.",
        "limit": 4, "link_label": "View all cakes ↗"},
    **blocks("card", [
        {"type": "card", "settings": {"label": label, "image": IMG(img), "title": title, "price_text": price}}
        for label, img, title, price in [
            ("Best seller", "1d6f1e28e1eb.webp", "Signature Chocolate Cake", "From ₹1,250"),
            ("Eggless", "e7b5640dccfe.webp", "Fresh Fruit Celebration", "From ₹1,350"),
            ("Celebration", "efa1cdf71aed.webp", "Lace Celebration Cake", "From ₹1,450"),
            ("Popular", "56232ed5661d.webp", "Milestone Vanilla Cake", "From ₹1,400"),
        ]]),
}

occasion_cards = [
    ("occasion", "Celebrate", "Birthdays", "e7b5640dccfe.webp"),
    ("occasion", "Together", "Anniversaries", "efa1cdf71aed.webp"),
    ("occasion", "New beginnings", "Baby Showers", "c73c0bf157ad.webp"),
    ("occasion", "Milestones", "Congratulations", "56232ed5661d.webp"),
    ("occasion", "At work", "Corporate", "50664836b9d6.webp"),
    ("occasion", "Seasonal", "Festive", "1d6f1e28e1eb.webp"),
    ("relation", "For her", "Mom", "e7b5640dccfe.webp"),
    ("relation", "For him", "Dad", "1d6f1e28e1eb.webp"),
    ("relation", "Together", "Partner", "efa1cdf71aed.webp"),
    ("relation", "Always", "Friends", "c73c0bf157ad.webp"),
    ("relation", "At work", "Colleagues", "50664836b9d6.webp"),
    ("relation", "At home", "Family", "56232ed5661d.webp"),
]
occasions = {
    "type": "mzh-occasions",
    "settings": {"anchor": "occasions", "eyebrow": "Shop by intent", "heading": "Made for Every Moment",
                 "tab_occasion": "By Occasion", "tab_relation": "By Relation"},
    **blocks("card", [
        {"type": "card", "settings": {"group": g, "eyebrow": e, "title": t, "image": IMG(img)}}
        for g, e, t, img in occasion_cards]),
}

gifts = {
    "type": "mzh-gifts",
    "settings": {
        "anchor": "gifts", "eyebrow": "Gifting collection", "heading": "Gifts That Feel Considered",
        "text": "Four hamper formats, each packed by hand with tissue, a handwritten note and a ribbon finish.",
        "link_label": "View all hampers ↗",
        "film_status": "Packaging film · 20 sec", "film_eyebrow": "Made to be opened slowly",
        "film_heading": "Watch the Gift Come Together",
        "film_text": "Tissue placement, product arrangement, a handwritten note and the ribbon finish—every hamper is packed to be unwrapped slowly."},
    **blocks("hamper", [
        {"type": "hamper", "settings": {"eyebrow": e, "title": t, "text": d, "price_text": p, "link_label": "Explore"}}
        for e, t, d, p in [
            ("Everyday gifting", "The Classic Box", "A considered mix of signature bakes for birthdays, thank-yous and thoughtful drop-ins.", "From ₹1,499"),
            ("Celebration edit", "The Celebration Hamper", "Layered treats, petite cakes and finishing details designed for milestone gifting.", "From ₹2,299"),
            ("Tea-time selection", "The Afternoon Edit", "Cookies, tea cakes and small-batch savouries curated for relaxed sharing.", "From ₹1,799"),
            ("Corporate & festive", "The Grand Hamper", "A larger-format premium assortment with custom notes and brand-ready packaging.", "From ₹3,499"),
        ]]),
}

offer = {
    "type": "mzh-offer",
    "settings": {"eyebrow": "Gifting offer", "heading": "Complimentary handwritten note",
                 "text": "On selected gift hampers above ₹1,999.", "watermark": "20%",
                 "button_label": "Shop the offer", "button_link": "#gifts"},
}

proof = {
    "type": "mzh-proof",
    "settings": {"anchor": "why", "eyebrow": "Why Mezzame", "heading": "The Proof Is in the Details",
                 "text": "Every Mezzame cake is baked in small batches and finished by hand, so what arrives looks and tastes the way it should."},
    **blocks("block", [
        {"type": "slide", "settings": {"image": IMG("7ce0ad6bdced.webp")}},
        {"type": "slide", "settings": {"image": IMG("1b91ae68aab0.webp")}},
        {"type": "slide", "settings": {"image": IMG("f6c62765d9f4.webp")}},
        {"type": "point", "settings": {"title": "Small-batch craftsmanship", "text": "Real daily production, carefully finished instead of mass-produced."}},
        {"type": "point", "settings": {"title": "Premium ingredients", "text": "Quality chocolate, fresh cream and seasonal fruit chosen for flavour first."}},
        {"type": "point", "settings": {"title": "Packaging worth gifting", "text": "Every touchpoint—from the box to the note—designed to elevate the occasion."}},
    ]),
}

film = {"type": "mzh-film", "settings": {"eyebrow": "Behind every cake", "heading": "See the hands behind the finish."}}

reviews = {
    "type": "mzh-reviews",
    "settings": {"eyebrow": "Customer proof", "heading": "Loved at First Slice"},
    **blocks("review", [
        {"type": "review", "settings": {"rating": 5, "quote": q, "author": a}} for q, a in [
            ("“The cake looked premium, travelled well and tasted even better than it looked.”", "Birthday order"),
            ("“The hamper packaging felt thoughtful enough to gift without adding anything else.”", "Corporate gifting"),
            ("“Ordering was easy and the finish felt genuinely special—not generic.”", "Anniversary cake"),
        ]]),
}

faq = {
    "type": "mzh-faq",
    "settings": {"anchor": "faq", "eyebrow": "Useful answers", "heading": "Before You Order",
                 "text": "Delivery, customisation, eggless options and lead times—answered before you check out."},
    **blocks("question", [
        {"type": "question", "settings": {"question": q, "answer": f"<p>{a}</p>"}} for q, a in [
            ("Do you offer same-day delivery?", "Same-day availability depends on the product, your delivery location and the time you order."),
            ("Can I customise a celebration cake?", "Yes. Custom celebration cakes need advance notice—message us with your design, size and date."),
            ("Are eggless cakes available?", "Yes. Eggless options are marked on each product and can be chosen when you order."),
            ("Which areas do you deliver to?", "We deliver across Chennai. Enter your pincode on any product page to check availability."),
        ]]),
}

cta = {"type": "mzh-cta", "settings": {
    "heading": "Something worth celebrating?",
    "text": "Choose a cake, hamper or custom order and make the moment feel considered.",
    "button_label": "Order Now", "button_link": "#cakes"}}

journal = {
    "type": "mzh-journal",
    "settings": {"anchor": "journal", "eyebrow": "The Mezzame journal", "heading": "Ideas for Better Celebrations",
                 "link_label": "Read all stories ↗"},
    **blocks("story", [
        {"type": "story", "settings": {"category": c, "title": t}} for c, t in [
            ("Celebration guide", "How to choose the right cake for every kind of celebration"),
            ("Gifting", "Five thoughtful hamper ideas"),
            ("Behind the bake", "What makes a premium cake different"),
        ]]),
}

instagram = {
    "type": "mzh-instagram",
    "settings": {"eyebrow": "@mezzame", "heading": "Fresh From Instagram", "link_label": "Follow Mezzame ↗"},
    **blocks("tile", [{"type": "tile", "settings": {}} for _ in range(6)]),
}

sections = {
    "hero": hero, "trust": trust, "cakes": products, "occasions": occasions, "gifts": gifts,
    "offer": offer, "proof": proof, "film": film, "reviews": reviews, "faq": faq,
    "order": cta, "journal": journal, "instagram": instagram,
}
index = {"sections": sections, "order": list(sections)}

header_group = {
    "type": "header",
    "name": "t:names.header",
    "sections": {
        "header_announcements_9jGBFp": {
            "type": "header-announcements",
            "name": "t:names.announcement_bar",
            **blocks("announcement", [{"type": "_announcement", "settings": {
                "text": "Freshly baked in Chennai · Delivery across Chennai",
                "font": "var(--font-body--family)", "font_size": "0.75rem",
                "letter_spacing": "loose", "case": "uppercase"}}]),
            "settings": {"speed": 5, "section_width": "page-width", "background_color": "#17110d",
                         "divider_width": 0, "padding-block-start": 9, "padding-block-end": 9},
        },
        "header_section": {
            "type": "header",
            "blocks": {
                "header-logo": {"type": "_header-logo", "static": True, "settings": {
                    "hide_logo_on_home_page": False, "padding-block-start": 0, "padding-block-end": 0}, "blocks": {}},
                "header-menu": {"type": "_header-menu", "static": True, "settings": {
                    "menu": "mezzame-header", "type_font_primary_size": "0.75rem", "menu_font_style": "inverse",
                    "type_font_primary_link": "body", "type_case_primary_link": "uppercase",
                    "menu_style": "featured_products", "featured_products_aspect_ratio": "4 / 5",
                    "featured_collections_aspect_ratio": "16 / 9", "image_border_radius": 0,
                    "navigation_bar": False, "drawer_accordion": False,
                    "drawer_accordion_expand_first": False, "drawer_dividers": False}, "blocks": {}},
            },
            "settings": {
                "logo_position": "left", "menu_position": "center", "menu_row": "top",
                "show_search": True, "search_position": "right", "search_row": "top",
                "show_country": False, "country_selector_style": False, "show_language": False,
                "localization_font": "heading", "localization_font_size": "0.875rem",
                "localization_position": "right", "localization_row": "top",
                "section_width": "page-width", "section_height": "standard",
                "enable_sticky_header": "scroll-up", "divider_width": 0, "divider_size": "page-width",
                "border_width": 0, "background_color_top": "#f4ede3",
                "enable_transparent_header_home": True, "text_color_transparent_home": "#fffdf9",
                "enable_transparent_header_product": False, "enable_transparent_header_collection": False},
        },
    },
    "order": ["header_announcements_9jGBFp", "header_section"],
}

footer_group = {
    "type": "footer",
    "name": "t:names.footer",
    "sections": {
        "mzh_footer": {
            "type": "mzh-footer",
            "settings": {"text": "Premium cakes, desserts and gifting—made visible, specific and worth showing up for.",
                         "tagline": "Proof, Not Promises."},
            **blocks("column", [
                {"type": "menu", "settings": {"heading": "Shop", "menu": "mezzame-header"}},
                {"type": "menu", "settings": {"heading": "Help", "menu": "mezzame-help"}},
                {"type": "text", "settings": {"heading": "Visit", "text": "<p>Chennai, Tamil Nadu</p>"}},
            ]),
        }
    },
    "order": ["mzh_footer"],
}

for rel, data in [("templates/index.json", index),
                  ("sections/header-group.json", header_group),
                  ("sections/footer-group.json", footer_group)]:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("wrote", rel)
