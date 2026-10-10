---
name: research
description: Research a company and build its hub file
argument-hint: "[company name] [optional: role link or pasted JD]"
disable-model-invocation: true
---
Build the company hub for $ARGUMENTS. If I've included a role (link or JD), that's the
primary role; research it in full. Otherwise, treat every fit from the role scan equally.

## 1. Company research
What they sell and to whom, business model, funding or public financials, headcount,
layoffs, recent product and leadership news, regulatory exposure, and what people say about
working there.

## 2. Role scan
Read every open role on the careers page, across all departments, to catch anything I
missed beyond the primary role. Judge fit from the job description, not the title or
department: target work shows up under titles I wouldn't guess. Match on what the role
actually does against Targeting (Work that fits, Screen for, Fit signals) and the
Reference role in `context.md`. Rank fits by closeness to the Reference role. Apply any
title-specific rules in Targeting.

For each possible fit: title, team, link, posting date if shown, location and time-zone
requirements, stated comp, what in the description made it a match, and a check against
every item under Hard no, Screen for, and Constraints in `context.md`. Unstated counts
as unknown, not a pass.

List near-misses separately with the one reason each failed. If the careers page can't be
read in full, say what you couldn't see.

## 3. Hub
Every claim needs a source link and the date you found it. Where sources conflict or you
can't verify something, say so rather than smoothing it over.

Show me the findings in chat first: a short verdict (fits, near-misses, and whether it's
worth pursuing), then the three things about this company most likely to trip me up. Only
if I say to pursue it, draft `companies/[company]/[company]-hub.md` with: Overview, The
role (primary role, if given: full check against `context.md`), Other possible roles (fits
and near-misses from the scan, ranked), Where the role sits in the org (reporting line,
distance from revenue), People (added as I meet them), Why this company (drafted from
`context.md`: my honest reason, not flattery), Logistics, Open questions, Debrief log.
Show me the hub before writing it.
