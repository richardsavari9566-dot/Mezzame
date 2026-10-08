# 03 Verification

| Check | Result |
|---|---|
| Liquid accepted by Shopify on upload (syntax) | Pass |
| Remote checksumMd5 equals local for 18 liquid/css/js files + layout | Pass |
| JSON templates/groups/settings accepted; settings read back with new fonts/palette | Pass |
| Theme role still UNPUBLISHED; live theme untouched | Pass |
| Storefront render, desktop + mobile | **Pending — human** (sandbox cannot reach mezzame.co.in) |
| Header transparency over hero, cart drawer opens | **Pending — human** |
| Tabs, hero slider, gallery, packing toggle, film | **Pending — human** |

## UAT script for Richard
1. Online Store → Themes → "Copy of Copy of Horizon" → … → Preview.
2. Check each section against the prototype at desktop width, then a phone.
3. Click Bag and Search in the header; open a menu link (should scroll to the section).
4. Customize → confirm every text, image and link is editable in the side panel.
