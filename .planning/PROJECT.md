# Mezzame launch

Premium cake and gifting store for Chennai on Shopify (mezzame.co.in, INR, IST).
Scope: homepage, product page and purchase journey (see ../TRACKER.md for the 51 approved pointers).

## Constraints
- Brand spelling: **Mezzame** (Q1, decided 08 Oct).
- Build on Horizon. Work only in the unpublished theme "Copy of Copy of Horizon" (gid 180412842177). Never publish; the live theme is "Copy of Horizon".
- Prepaid only, Razorpay, no midnight delivery at launch, store pickup as out-of-zone fallback (defaults, reversible).
- Cakes need delivery date, slot and message chosen on the product page, so homepage cards link to products rather than quick-adding.

## Source of truth
`theme/` in this repo mirrors every theme file we own. `scripts/build_index_json.py` generates the homepage, header group and footer group JSON.
