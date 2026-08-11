# End2End Estate

Marketing site for End2End Estate, a modern estate liquidation and transition company serving the north Denver metro (Thornton, Northglenn, Westminster, Broomfield, Brighton and Erie).

**Live site:** deployed from this repo via Vercel
**Phone:** 303-647-4188

## Before this site is promoted anywhere

Two items are genuinely blocking. Neither prevents deployment, but both should be resolved before the URL is put on a business card, a yard sign or an ad.

1. **The contact form needs one activation click.** Submissions are delivered by FormSubmit to `hello@end2endestates.com` (set via `FORM_RECIPIENT` near the bottom of `site.html`). The very first submission triggers a confirmation email from FormSubmit to that inbox. Click the link in it once and the form is live permanently. Until that click happens, submissions do not arrive.

2. **The photography is placeholder imagery sourced from third party websites.** It renders, but it is not licensed for commercial use. Replace every `<img>` and the hero background with licensed stock or original photography before the site is promoted.

Also still missing: business hours, and any licensing or insurance details.

## How this repo is structured

| File | Purpose |
| --- | --- |
| `site.html` | The editable source. This is the file you change. |
| `build.py` | Inlines the logo and favicon as data URIs, then writes `index.html`. |
| `index.html` | The built site, at the repo root. This is what Vercel serves. Do not edit by hand. |
| `logo_lockup.png` | Logo lockup, for use on light backgrounds. |
| `logo_lockup_light.png` | Same logo recolored so it reads on navy. Keep in sync with the above. |
| `favicon.png` | 64px E2E monogram. |

## Making a change

```bash
# 1. edit site.html
# 2. rebuild
python3 build.py
# 3. commit and push. Vercel deploys automatically.
git add -A && git commit -m "describe the change" && git push
```

`build.py` fails the build if any image token is left unsubstituted, and it fails if an em dash appears anywhere in the output.

## House rules

- **No em dashes.** Not in copy, not anywhere. Use commas, colons, periods or parentheses. The build enforces this.
- **No invented facts.** No fake testimonials, no invented review counts, no made up years in business, no fabricated license numbers, no statistics that were not supplied.
- Tone is modern, professional, trustworthy and compassionate. The reader is often having one of the worst weeks of their life. Never let the site feel like a garage sale business.

## Brand

Sampled from the official logo file:

| Token | Hex | Use |
| --- | --- | --- |
| Navy | `#142743` | Primary |
| Deep navy | `#0C1A2E` | Hero and CTA backgrounds |
| Teal | `#588683` | Accent, buttons |
| Teal dark | `#41706C` | Hover |
| Teal light | `#8FB5B1` | Accent on navy |
| Gray | `#F5F6F7` | Banded sections |
| Line | `#DFE3E6` | Hairlines |

Typography: Newsreader for headlines, Inter for body and UI.

## Sections

Nav, hero, six icon service ribbon, the five liquidation paths, the eight core services, "what we find", the six step process, selling the property, technology, who we work with, service area, and the closing CTA with the request form.
