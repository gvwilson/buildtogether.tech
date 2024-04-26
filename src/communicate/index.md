---
title: Communicating
---

Knowing how to steer and change gears isn't all there is to driving—you need
to know how to signal when you're turning or changing lanes.  Similarly, knowing
how to commit to Git and do a code review are necessary but not sufficient for
working with other programmers.  This chapter therefore looks at how to
communicate with your teammates.

## To Do

You probably have a to-do list somewhere. It might be scribbled in a calendar or
lab notebook, kept in a text file on your laptop, or in your head; wherever and
however you maintain it, it lists the things you're supposed to do, when they're
due, and (possibly) how urgent they are.

At its simplest, an [%i "issue tracker" "issue" %][%g issue_tracker "issue tracker" %][%/i%]
is a shared to-do list. Issue tracking systems are also called
[%i "ticketing system" %]ticketing systems[%/i%] and [%i "bug
tracker" %]bug trackers[%/i%] because most software projects use them to keep
track of the bugs that developers and users find. These days, issue trackers are
almost invariably web-based. To create a new issue, you enter a title and a
short description; the system then assigns it a unique serial number. You can
usually also specify:

-   what kind of issue it is (such as a bug report, a request for a new feature,
    or a question to be answered);

-   who is responsible for the issue (i.e., who's supposed to fix the bug, test
    the fix, or update the documentation);

-   how important it is; and

-   when it's due.

If version control keeps track of where your project has been, your issue
tracking system keeps track of where you're going. After version control, it is
the most important part of a team project; without it, you and your teammates
will have to constantly ask each other "What are you working on?", "What am I
supposed to be working on?", and "Who was supposed to do that?" Once you start
using one it's easy (or at least easier) to find out what the project's status
is: just look at the open issues and at those that have been closed recently.
You can use this to create agendas for your status meetings, and to remind
yourself what you were doing three months ago when the time comes to write your
final report.

Of course, a issue tracker is only as useful as what you put into it.  If you're
describing a bug in a large application, you should include enough information
to allow someone to reproduce the problem. This is why industrial-strength
systems like [%i "Jira (issue tracker)" "issue
tracker!Jira" %][Jira][jira][%/i%] can have a couple of dozen [%i "issue!fields" %]fields[%/i%] for each issue, including:

-   what version of the software you were using;

-   what platform it was running on;

-   what you did to make it crash;

-   any data or configuration files the program relies on;

-   whatever stack traces, error reports, or log messages the program produced;

-   its severity (i.e., how much damage the bug might do); and

-   other issues that might be related.

This is a lot more information than student projects require. In addition,
students are almost always working on several courses at once, and it's common
for students to have to put their team project aside for a few days to work on
assignments for other courses. For these reasons, I've found that most student
teams won't actually use anything more sophisticated than a web-base to-do list
unless they're forced to by the grading scheme. In that case, most come away
with the impression that issues are something you only use when you have to.

So what does a good issue look like?  [%b Bettenburg2008 %] found that the
information users supply when they file a bug report tends not to be that which
the relevant developers need the most, and most importantly, it differs in
fairly predictable ways and for understandable reasons.  Here's one I filed for
the duplicate file finder reviewed in [%x git-team %]:

[%inc bug-report.txt %]

The ID on the first line is assigned by the issue tracker, an often serves as a
shorthand name for the issue in conversation. ("Hey, is anyone working on number
fifty-five yet?") The date is in [%i "issue!timestamps" %][%g utc "UTC" %][%/i%]
so that it is unambiguous: while your team may all be in one place, it's
increasingly likely that you are scattered across several time zones.

The [%i "issue!good titles" %]title[%/i%] on line 3 is probably the most
important part of the issue. Projects will accumulate hundreds of issues over
time; a good subject line makes it much easier to find the ones you need. The
`type`, `severity`, and `labels` fields also improve
[%i "discoverability!of issues" %][%g discoverability "discoverability" %][%/i%];
while `type` and `severity` could be labels, having them in fields of their own
makes it easier to sort and filter issues.

Finally, the [%i "issue!description of" %]description[%/i%] briefly
summarizes the problem. If the author hadn't already identified the cause, it
should include a [%i "reproducible example (reprex)" %][%g reprex "reproducible example" %][%/i%] (also called a reprex). This helps the person understand what the
issue is much more than, "The program crashes when I open strange files," but
experience shows that if people are required to come up with a reprex when
filing an issue, they will often solve their own problem along the way.  We'll
talk more about the value of minimal reproducible examples in
[%x debugging %].

<div class="callout" markdown="1">
### When to start saying "no"

As we will see in [%x process %], one purpose of a schedule is to tell you
when to start cutting corners. Similarly, one of the main reasons to keep
[%i "issue tracker!helping triage" "triage!using issue tracker" %]issues[%/i%] in
one place is to help you prioritize work when time starts to run short.
</div>

## Labeling Issues

The bigger a project gets, the harder it is to find things.  Issue trackers
therefore let project members add [%i "issue!classifying" %][%g issue_label "labels" %][%/i%] to issues to make things easier to search
and organize.  Labels are also often called tags; whatever term is used, each
one is just a descriptive word or two.

GitHub allows project owners to define any labels they want.  A small project
should always use some variation on these three:

Bug
:   Something should work but doesn't.

Enhancement
:   Something that someone wants added to the software.

Task
:   something needs to be done, but won't show up in code (e.g., organizing the
    next team meeting).

Projects also often use:

Question
:   where is something or how is something supposed to work?  As noted above,
    issues with this label can often be recycled as documentation.

Discussion or Proposal
:   something the team needs to make a decision about or a concrete proposal to
    resolve such a discussion.  All issues can have discussion: this category is
    for issues that start that way.  (Issues that are initially questions are
    often relabeled as discussions or proposals after some back and forth.)

The labels listed above identify the kind of work an issue describes.  A
separate set of labels can be used to indicate the state of an issue:

Urgent
:   Work needs to be done right away.  (This label is typically reserved for
    security fixes).

Current
:   This issue is included in the current round of work.

Next
:   This issue is (probably) going to be included in the next round.

Eventually
:   Someone has looked at the issue and believes it needs to be tackled, but
    there's no immediate plan to do it.

Won't Fix
:   Someone has decided that the issue isn't going to be addressed, either
    because it's out of scope or because it's not actually a bug.  Once an issue
    has been marked this way, it is usually then closed.  When this happens,
    send the issue's creator a note explaining why the issue won't be addressed
    and encourage them to continue working with the project.

Duplicate
:   This issue is a duplicate of one that's already in the system.  Issues
    marked this way are usually also then closed; this is another opportunity to
    encourage people to stay involved.

Some projects use labels corresponding to upcoming assignments instead of
Current, Next, and Eventually.  This approach works well in the short term, but
becomes unwieldy as labels with names like `exercise-14` pile up.  Instead, a
project team will usually create a [%i "milestone (in issue tracker)" "issue tracker!milestones" %][%g milestone "milestone" %][%/i%], which is a set of issues
and pull requests in a single project repository.  GitHub milestones can have a
due date and display aggregate progress toward completion, so the team can
easily see when work is due and how much is left to be done.

## Other Ways to Communicate

Issues are the best way to keep track of where you are, but there are lots of
other ways the team can and should communicate. These can be [%i "communication!synchronous" %]synchronous[%/i%], like chat and video calls, or
[%i "communication!asynchronous" %]asynchronous[%/i%], like issues and
email. The former are better for quick back-and-forth and for maintaining social
connections, but they can also be a constant stream of interruptions, which
lowers productivity ([%x important %]). Synchronous tools also tend to bias
communication in favor of people who are more self-confident, more fluent in the
language, or have better network connections, and finding things afterward in
archives of stream-of-consciousness exchanges is harder than finding things in
asynchronous media.

But who am I kidding? You're going to use [%i "communication!instant
messaging" "instant messaging!inevitable use of" %]instant messaging[%/i%] no
matter what I say.  If more than two people are in the conversation, follow the
same rules you would for a short meeting: post a summary of any decisions you
made where everyone can see it.

If you prefer fewer interruptions and longer periods of thought, you can always
go back to [%i "communication!email" "email (for team
communication)" %]email[%/i%], which has been used to run projects since the
1970s.  It brings content directly to people while allowing everyone to deal
with issues when it's convenient for them, and supports long-running
conversations. Email really comes into its own, though, when messages are routed
through a central mailing list, so that people don't have to remember to CC the
other five people on their team, and a shared archive can be created for later
searching. The second point is as important as the first: if you can't go back
and find out what was said a month ago—or, just as importantly, if someone
*else* can't do that—you might as well not have said it.

<div class="callout" markdown="1">
### Filters are your friend

Every email client allows you to set up
[%i "email!filters" %][%g "mail_filter" "filters" %][%/i%]
that automatically flag messages matching
certain patterns or file them in particular mailboxes. I have fourteen of these
set up right now to organize messages belonging to particular projects; it only
took a couple of minutes, and it means that when I check mail in the morning or
after lunch, everything is set up for me to focus on one topic at a time.
</div>

[%i "software portal!communication tools" %]Software portals[%/i%] provide
many other ways to communicate, which project members use in a wide variety of
ways [%b Treude2011 %].  [%i "wiki" "communication!wiki" %]Wikis[%/i%]
seem like a good way to keep notes, create documentation, and so on. Their main
strength is the fact that content is automatically and immediately visible on
the web.  These days, you will probably get more mileage out of a bunch of
[%i "Markdown" %]Markdown[%/i%] pages under version control—you have to set up a
repository anyway, and version control systems are much better at reconciling
conflicts between concurrent authors than wikis.

[%i "communication!blog" "blog!as team journal" %]Blogs[%/i%], on the other
hand, have proven more useful. One kind of project blog consists of articles
written by the team's members as a journal of their progress. This is most
useful for people who are watching the project from the outside, like
instructors.

The second kind of [%i "blog!automatically generated" %]blog[%/i%] is one
created automatically by tools. In many project management systems, every
project has a blog.  Every time someone checks code into version control,
creates or closes an issue, or sends email, an entry is added to that blog. This
allows the project's members to see changes scroll by in their usual blog
reader, which is a handy way to keep track of what their teammates are doing.

If you are going to create a blog, use a [%i "static site generator" %][%g static_site_generator "static site generator" %][%/i%] to format and publish
content consistently.  On GitHub, for example, you can create a site with [%i "GitHub Pages" %][GitHub Pages][ghp][%/i%] using a tool called [%i "Jekyll" "static site generator!Jekyll" %][Jekyll][jekyll][%/i%]; lots of
different themes are available, and there are many good tutorials online.

<div class="callout" markdown="1">
### Comments as communication

People don't usually think of [%i "comments!as communication" "communication!comments" %]comments[%/i%]
as a form of communication like email or
instant messaging, but if they are used properly, the only significant
difference is that the comments are right there in the code where the recipients
can't miss them rather than in an archive somewhere that they'll have to go and
search.  If you choose names for functions and variables carefully, the code
itself will explain what it's doing when someone reads it aloud; the comments
should therefore explain *why*, just as you would in an email.  For example,
this is not a useful comment:

[%inc useless_comment.py %]

This, on the other hand, tells the next person why we're doing it:

[%inc useful_comment.py %]
</div>

## Reporting Up

As well as reporting progress to your teammates,
you may have to [%i "reporting!to your manager" %]report[%/i%] it regularly to your instructor, who
is effectively your manager. [%i "Evans, Julia" %][Julia
Evans][evans-julia][%/i%] has described [eight things your manager might not
know][evans-manager], all of which apply to student teams:

1.  What's slowing the team down.

1.  Exactly what individual people on the team are working on.

1.  Where the [%i "technical debt" %][%g technical_debt "technical debt" %][%/i%] is.

1.  How to help you get better at your job.

1.  What your goals are.

1.  What issues they should be escalating.

1.  What extra work you're doing.

1.  How compensation/promotions work at the company.  (For students, this one
    translates to, "How grading actually works.")

[%i "Kaplan-Moss, Jacob" %][Jacob Kaplan-Moss][kaplan-moss-jacob][%/i%] has a
similar guide to [giving a status update to executives][kaplan-moss-executives],
and [Ask a Manager][ask-a-manager] is full of good advice and discussion as
well. If you follow those guidelines, you get briefs like this:

> Project X is running smoothly. We're making steady progress: we've delivered a
> bit over half of the features on our roadmap, and we're on track to launch
> publicly in May.
>
> I want to particularly highlight J's design work; every time we share a new
> demo with our user research group they rave over how much they love the
> design.
>
> We do have some cost risk: right now, the code's pretty inefficient and would
> require us to increase our AWS spend by 25% when we put this into
> production. We either need to decide that cost is acceptable, or add some
> extra time to the schedule for performance optimization. I need some guidance
> from this team on that point: can you folks let me know if that cost seems OK
> or not?

If you learn how to summarize your status like this, you will be a very popular
team member.

## Documentation

An old proverb says, "Trust, but verify."  The equivalent in programming is, "Be
clear, but [%i "documentation!as communication" %]document[%/i%]."  No matter
how well software is written, it always embodies decisions that aren't explicit
in the final code or accommodates complications that aren't going to be obvious
to the next reader.  Putting it another way, the best function names in the
world aren't going to answer the questions "Why does the software do this?"  and
"Why doesn't it do this in a simpler way?"

In most cases, [%i "documentation!embedded" %]embedded documentation[%/i%] in
the form of a short [%g docstring "docstring" %] or [%g doc_comment "doc comment" %] to remind ourselves of each function's
purpose is probably as much documentation as we need.  (In fact, it's probably
better than what most people do.)  That one- or two-liner should begin with an
active verb and describe either how inputs are turned into outputs, or what side
effects the function has; as we discuss below, if we need to describe both, we
should probably rewrite our function.

An active verb is something like "extract", "normalize", or "plot".  Some
examples of good one-line docstrings include:

-   "Create a list of capital cities from a list of countries."
-   "Clip signals to lie in [0...1]."
-   "Reduce the red component of each pixel."

You can tell our one-liners are useful if you can read them aloud in the order
the functions are called in place of the function's name and parameters.

Once you start writing code for other people (or your future self) your [%i "documentation!what to include" %]documentation[%/i%] should include:

-   The name and purpose of every public class, function, and constant in our
    code.

-   The name, purpose, and default value (if any) of every parameter to every
    function.

-   Any side effects the functions and methods have.

-   The type of value returned by every function or method.

-   What exceptions those functions can raise and when.

The word "public" in the first rule is important.  You don't have to write full
documentation for helper functions that are only used inside your package and
aren't meant to be called by users, but these should still have at least a
comment explaining their purpose.

As [%x thinking %] explains, we can divide people in any domain into
novices, competent practitioners, and experts.  Each of these three groups needs
a different kind of documentation:

-   A [%i "novice!documentation needs" "documentation!for
    novices" %]novice[%/i%] needs a tutorial that introduces her to key ideas one
    by one and shows how they fit together.

-   A [%i "competent practitioner!documentation needs" "documentation!for
    competent practitioners" %]competent practitioner[%/i%] needs reference guides,
    cookbooks, and Q&A sites; these give her solutions close enough to what she
    needs that she can tweak them the rest of the way.

-   [%i "expert!documentation needs" "documentation!for experts" %]Experts[%/i%]
    need this material as well—nobody's memory is perfect—but they may also
    paradoxically want tutorials.  The difference between them and novices is
    that experts want tutorials on how things work and why they were designed
    that way.

The first thing to decide when writing documentation is therefore to decide
which of these needs we are trying to meet.  Tutorials like this book should be
long-form prose that contain code samples and diagrams.  They should show people
things they actually want to do rather than printing the numbers from 1 to 10,
and should include regular check-ins so that people can tell if they're making
progress.

Tutorials help novices build a [%i "mental model" %]mental model[%/i%], but
competent practitioners and experts will be frustrated by their slow pace and
low information density.  They will want single-point solutions to specific
problems, like how to find cells in a spreadsheet that contain a certain string
or how to configure the web server to load an access control module.  They can
make use of an alphabetical list of the functions in a library, but are much
happier if they can search by keyword to find what they need; one of the signs
that someone is no longer a novice is that they're able to compose useful
queries and tell if the results are on the right track or not.

## Creating an FAQ

As projects grow, documentation within functions alone may be insufficient for
users to apply code to their own problems.  One strategy to assist other people
with understanding a project is with an [%i "FAQ" %]FAQ[%/i%].  A good FAQ
uses the terms and concepts that people bring to the software rather than the
vocabulary of its authors; putting it another way, the questions should be
things that people actually search for online, not the things the program's
developers wish they would ask.

Creating and maintaining an FAQ is a lot of work, and unless the community is
large and active, a lot of that effort may turn out to be wasted, because it's
hard for the authors or maintainers of a piece of software to anticipate what
newcomers will be mystified by.  A better approach is to leverage sites like
[%i "Stack Overflow" %][Stack Overflow][stack-overflow][%/i%], which is where
most programmers are going to look for answers anyway.

The Stack Overflow guide to [asking a good
question][stack-overflow-good-question] has been refined over many years, and is
a good guide for any project:

Write the most specific title we can.
:   "Why does division sometimes give a different result in Python 2.7 and
    Python 3.5?"  is much better than, "Help! Math in Python!!"

Give context before giving sample code.
:   A few sentences to explain what we are trying to do and why it will help
    people determine if their question is a close match to ours or not.

Provide a minimal reprex.
:   Readers will have a much easier time figuring out if this question and its
    answers are for them if they can see *and understand* a few lines of code.

Tag, tag, tag.
:   Keywords make everything from scientific papers to left-handed cellos easier
    to find.  They are even more effective if the system encourages people to
    re-use tags so that they don't proliferate [%b Lin2020 %].

Use "I" and question words (how/what/when/where/why).
:   Writing this way forces us to think more clearly about what someone might
    actually be thinking when they need help.

Keep each item short.
:   Break everything down into single-page steps, with half of that page devoted
    to troubleshooting.  This may feel trivializing to the person doing the
    writing, but is often as much as a person searching and reading can handle.
    It also helps writers realize just how much implicit knowledge they are
    assuming.

Allow for a chorus of explanations.
:   Do not be afraid of providing multiple explanations to a single question
    that suggest different approaches or are written for different prior levels
    of understanding. This is one of the things that has made Stack Overflow so
    successful: if users are different from one another, they are best served by
    a [%i "chorus of explanation" %]chorus of explanations[%/i%]
    [%b Caulfield2016 %].
