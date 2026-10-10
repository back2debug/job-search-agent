# job-search-agent

A job search workspace for [Claude Code](https://claude.com/claude-code). Claude reads the
same few files at the start of every session, so it knows your history, your targets, and
every company you're talking to without being told again.

It's a folder of Markdown files and nine slash commands. No server, no database.

## What you need
- Claude Code
- Python 3 and `reportlab`, only if you want PDF resumes

## Start

```bash
git clone https://github.com/back2debug/job-search-agent.git
cd job-search-agent
claude
```

Run these once, in order:

| Command | What it does |
|---|---|
| `/bootstrap` | Copies the four templates from `examples/` to the root, then interviews you to fill in `context.md` |
| `/build-cv` | Interviews you role by role to build `cv-master.md`. Plan on 60 to 90 minutes |
| `/build-stories` | Picks candidates from `cv-master.md` and builds your first three interview stories |

## The loop, per company

| When | Command | What it does |
|---|---|---|
| A company looks interesting | `/research Acme Freight [link or pasted JD]` | Researches the company and reads every open role against your `context.md`. Shows you fits and near-misses. Writes the hub only if you say to pursue it |
| You're applying | `/tailor [pasted JD]` | Cuts a resume from `cv-master.md` for that posting. Lists what it cut, gaps to expect, and claims it isn't sure about |
| Before each interview | `/prep Lee Example, Director of Operations` | Researches the interviewer, predicts questions, maps each to a story, flags gaps |
| Within 24 hours after | `/debrief [your notes]` | Records what you learned, what landed, what to fix, and updates the hub |
| Weekly | `/pipeline` | One table across every hub: stage, last contact, next step, who owes whom |
| Every few weeks | `/refresh-stories` | Checks your stories against what interviewers are asking and finds the gaps |

To make a PDF from a tailored resume:

```bash
pip install -r requirements.txt
python3 tools/md2pdf.py companies/acme/cv-acme.md companies/acme/cv-acme.pdf
```

## What gets built

```
job-search-agent/
  CLAUDE.md              # the working agreement Claude follows every session
  context.md             # who you are, what you want, hard no's      (private)
  cv-master.md           # everything you've done, with sourced numbers (private)
  stories.md             # interview stories                          (private)
  learnings.md           # patterns seen at 2+ companies              (private)
  companies/             #                                            (private)
    acme/
      acme-hub.md        # research, role check, people, debrief log
      cv-acme.md         # resume tailored to that posting
      cv-acme.pdf
      acme-round-1.md    # prep for one interview
  examples/              # blank templates and a made-up company to look at
  tools/md2pdf.py
  .claude/skills/        # the nine commands
```

`examples/acme/` shows what a company folder looks like after a few steps of the loop.

## How the files work together
- `context.md` holds your rules. `/research` checks each role against every line under
  Hard no, Screen for, and Constraints. `/tailor` reads Resume format. Add to the sections
  freely, but keep the heading names: the commands look for them.
- `cv-master.md` is a record, not a resume. No polish. Every line on a tailored resume has
  to trace back to it.
- `CLAUDE.md` is where the standing rules live: no invented or rounded-up metrics, sources
  and dates on all research, and every file change shown to you before it's written. Edit
  it to change how Claude works with you.

## Privacy
Everything marked private above is in `.gitignore`, along with all PDFs. If you push your
copy somewhere, your history, comp, and notes on companies stay on your machine.

That also means git isn't backing those files up. Back them up yourself.

## Worth getting right
- **Don't let numbers drift.** A resume that says "reduced by 40%" when the record says
  "helped reduce" puts you in a room you can't defend. That's why the traceability rule is
  in `CLAUDE.md` and not in one command.
- **Be strict with `learnings.md`.** Two companies minimum, an observable issue, and a
  definition of fixed. Otherwise it turns into a list of worries.
- **Debrief within a day.** It's the step people skip and the one that makes the rest
  improve.
- **Prep for recruiter screens too.** They're easy to wing, and it's where the comp anchor
  gets set.

## License
MIT
