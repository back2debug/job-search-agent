---
name: tailor
description: Tailor my resume to a job description
argument-hint: "[job description]"
disable-model-invocation: true
---
Tailor my resume for the job description below.

Read `cv-master.md` and `context.md` first. Then:
1. Pull out the 6–8 requirements this role is actually screening on, ranked, separating
   hard requirements from nice-to-haves.
2. Map each to specific evidence in `cv-master.md`. Where I have no evidence, say so
   plainly — don't stretch an adjacent experience to cover it.
3. Draft `companies/[company]/cv-[company].md`: reordered, recut, using their vocabulary where mine
   means the same thing. Every bullet traceable to `cv-master.md`.
   Format: strict reverse-chronological. One entry per role as
   `### Title, Company · Mon YYYY–Mon YYYY`, ordered by end date. Never group roles by
   company or reorder by relevance. Exception: roles listed under Resume format in
   `context.md` may be lumped under a final `### Earlier` block, one line each with years,
   in the order listed there.
   Relevance is handled by bullet count per role, not by position.
4. List separately: what you cut and why, any gap I should expect to be asked about, and
   any claim you're not fully confident is supported.

Show me the draft before writing the file.

JOB DESCRIPTION:
$ARGUMENTS
