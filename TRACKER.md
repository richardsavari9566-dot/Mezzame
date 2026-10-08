# Project Tracker: Mezzame Launch (Home, Product Page, Purchase Journey)
Last updated: 08 Oct 2026, 07:30 IST

## Summary
Sprint: 0 of 4 (in progress), S3 homepage pulled forward | Done: 0 | In test: 5 | Failed: 0 | Blocked: 0

Phase: Gate 1 APPROVED · Gate 2 APPROVED · **Sprint 0 running**

## Tasks
| Task ID | Sprint | Description | Agent / Model | Status | Test result | Proof | Updated |
|---|---|---|---|---|---|---|---|
| T-0-1 | S0 | Apply approved brand spelling across store | Builder / sonnet | To do | | Q1 answered: Mezzame. Homepage done; product, policy and email copy still to apply | 08 Oct |
| T-0-2 | S0 | Create 8 launch products with variants and metafields | Builder / sonnet | To do | | Needs client catalogue (Q5). Store confirmed at 0 products incl. drafts. | 07 Oct |
| T-0-3 | S0 | Create occasion, Cakes and Hampers collections | Builder / haiku | To do | | | 07 Oct |
| T-0-4 | S0 | Shortlist 3 delivery date apps, recommend 1 | Researcher / sonnet | In test | Awaiting human approval | See proof log T-0-4 | 07 Oct |
| T-0-5 | S0 | Install and configure delivery app | Builder / sonnet | To do | | Needs F03 operating rules | 07 Oct |
| T-0-6 | S0 | Payment gateway in test mode | Human | To do | | | 07 Oct |
| T-0-7 | S0 | Write and publish 4 policy pages | Builder / sonnet | To do | | | 07 Oct |
| T-1-1 | S1 | Product template: gallery, H1, breadcrumbs | Builder / sonnet | To do | | | 07 Oct |
| T-1-2 | S1 | Buy box: variants, price, sticky Add to bag | Builder / sonnet | To do | | | 07 Oct |
| T-1-3 | S1 | Pincode check and date/slot picker | Builder / sonnet | To do | | | 07 Oct |
| T-1-4 | S1 | Message on cake and gift note | Builder / sonnet | To do | | | 07 Oct |
| T-1-5 | S1 | Fact table and description blocks | Builder / sonnet | To do | | | 07 Oct |
| T-1-6 | S1 | Product descriptions and fact data (8 products) | Builder / sonnet | To do | | | 07 Oct |
| T-1-7 | S1 | Product, Offer, Brand, BreadcrumbList JSON-LD | Builder / opus | To do | | | 07 Oct |
| T-2-1 | S2 | Restyle inner templates to design system | Builder / sonnet | To do | | | 07 Oct |
| T-2-2 | S2 | Cart lines with date, slot, message; fee display | Builder / sonnet | To do | | | 07 Oct |
| T-2-3 | S2 | Zone, cut-off, blackout validation | Builder / sonnet | To do | | | 07 Oct |
| T-2-4 | S2 | Checkout settings and notification templates | Builder / sonnet | To do | | | 07 Oct |
| T-2-5 | S2 | GA4 and Meta Pixel/CAPI tracking | Builder / opus | To do | | | 07 Oct |
| T-3-1 | S3 | Static hero and trust strip | Builder / sonnet | In test | Uploaded; awaiting visual check in preview | See proof log T-3 | 08 Oct |
| T-3-2 | S3 | Best sellers, occasions, hampers bound to real data | Builder / sonnet | In test | Collection/product pickers built; sample cards until catalogue (Q5) | See proof log T-3 | 08 Oct |
| T-3-3 | S3 | Custom cake enquiry | Builder / haiku | To do | | | 07 Oct |
| T-3-4 | S3 | Remove placeholders, hide empty blocks | Builder / haiku | In test | Wireframe notes removed; empty Instagram/journal/offer hide | See proof log T-3 | 08 Oct |
| T-3-5 | S3 | FAQ and footer with schema | Builder / sonnet | In test | FAQPage JSON-LD; footer with menus + policy links | See proof log T-3 | 08 Oct |
| T-3-6 | S3 | Performance pass | Builder / opus | To do | | | 07 Oct |
| T-4-x | S4 | Good-to-haves by impact, then nice-to-haves | Builder / sonnet, haiku | To do | | | 07 Oct |

Status values: To do, In progress, In test, Pass, Fail, Blocked

## Proof log
### Store connection check (orchestrator)
get-shop-info: Shop "Mezzame" (mezzame.co.in), Plan Advanced, Currency INR, Timezone IST, Country India.
search_products (all statuses): productsCount = 0 (EXACT). Confirms audit A2.

### T-3 Homepage rebuild (Builder) — 08 Oct
Target: theme "Copy of Copy of Horizon" (gid 180412842177, role UNPUBLISHED). Not published. Live theme "Copy of Horizon" untouched.
Source of truth: repo branch claude/mezzame-shopify-connect-tdn6w5, commit d884e25, folder theme/.
- Uploaded via themeFilesUpsert (URL bodies pinned to the commit). 18 liquid/css/js files: remote checksumMd5 == local md5 for all 18.
- layout/theme.liquid checksum matches local (c5994112…). index.json, header-group.json, footer-group.json, settings_data.json accepted.
- settings_data read back: fonts DM Sans / Playfair Display, palette #f4ede3 / #1f1812 / #5f422f / #e8dccd.
- Menus created: mezzame-header (Cakes, Occasions, Gifting, Our Proof, Journal), mezzame-help (Contact, Delivery, FAQs, Search). Main menu unchanged.
- Shopify accepted all Liquid (syntax validated on upload). Storefront render NOT verified: sandbox network blocks mezzame.co.in. Human visual check required in theme preview (desktop + mobile).
- Old build (layout/mezamme.liquid, sections/mz-*, assets/mezamme-home.css, mz-interactions.js) left in place, unused, pending sign-off to delete.

### T-0-4 (Researcher, sonnet)
Result: DONE, pending human approval (test for this task is human sign-off).
| Criterion | A. Delivery Date Time Slot Pickup | B. DS Pickup Delivery Date & Time | C. Slotly |
|---|---|---|---|
| Picker on product page (hard req.) | Y | ? (cart/drawer only stated) | ? (cart only stated) |
| Pincode zones | Y (Premium) | ? | Y |
| Same-day cut-off | Y | Y | Y |
| Product-specific lead time | Y | P | P |
| Blackout dates | Y | Y | Y |
| Per-slot capacity | Y (Premium) | Y | P |
| Saved to order / emails | P | P | P |
| Checkout validation | P | P | Y |
| Store pickup | Y | Y | Y |
| Price / rating | $8.99/mo Premium; 5.0, 34 reviews | $12.99/mo; 5.0, 64 reviews | Free core, $15/mo; 5.0, 1 review |
Recommendation: A, Premium plan, 7-day trial on a theme copy.
Risks: young apps; order attributes, email variables and checkout bypass protection unverified; confirm block renders on custom OS 2.0 theme.
Sources: https://apps.shopify.com/delivery-pickup · https://apps.shopify.com/ds-delivery-pickup-shipping · https://apps.shopify.com/slotly-order-delivery-date-picker

## Decisions and changes
| Date | Decision | By |
|---|---|---|
| 07 Oct | Gate 1 approved: 51 pointers (36 Must, 9 Good, 6 Nice) as per PRD v0.1 | Richard |
| 07 Oct | Defaults adopted for unanswered questions: prepaid only, no COD (Q2); Razorpay (Q3); no midnight delivery at launch (Q4); draft products as placeholders until catalogue supplied (Q5); WhatsApp plus backup form for custom cakes (Q6); store pickup as out-of-zone fallback (Q7) | Orchestrator (default, reversible) |
| 07 Oct | Q1 brand spelling remains open and blocks T-0-1 | Orchestrator |
| 07 Oct | Gate 2 approved. Shopify admin access granted and verified. | Richard |
| 08 Oct | Q1 answered: brand spelling is **Mezzame** | Richard |
| 08 Oct | Homepage rebuilt (not refined) inside Horizon layout; prototype sample text kept until real content; S3 homepage tasks pulled forward | Richard |
| 08 Oct | Work tracked with GSD-style planning files in .planning/ (installer not run in sandbox) | Orchestrator |

## Client inputs outstanding
- Catalogue sheet: 8 products, variants, prices, photos, fact data
- F03 operating rules: pincodes, cut-off, lead times, slots, fees, blackout dates
- F04 store address, phone, hours
- Gateway account access

## Backlog
- Replace sample testimonials with genuine reviews before publishing (do not publish invented reviews)
- Upload packing film and behind-the-scenes video; add Instagram images and profile URL
- Point best sellers / hampers / occasions at real collections once T-0-2 and T-0-3 are done
- Delete old mz-* build files from the theme copy after sign-off
