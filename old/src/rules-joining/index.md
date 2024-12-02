---
title: How to Join an Existing Project
---

Hundreds of books have been published about how to start a tech business, and
works like [%b Fogel2020 %] have a lot of advice on setting up and running
open source projects.  Much less has been written about how to join existing
projects, even though that's what most people do most of the time.  These simple
rules can help, and can be read as a complement to [%x rules-newcomers %].

Search first.
:   Whatever question you have, the odds are pretty good that someone has asked
    it before, opened an issue about it, or discussed it in the project chat.
    If the project is well organized it should only take a minute to find out 
    ([%x communicate %]), and if you mention what you searched for when you
    do ask a question, people will probably point you in the right direction
    when they answer.

But do ask.
:   The biggest mistake newcomers make is to spend hours looking for something
    rather than asking a question.  If you have searched but haven't found
    anything helpful, it's OK to take a minute of someone else's time,
    especially if you post your question where the answer can be found by the
    next newcomer.

Remember that software is only one part of a project.
:   There are many ways to contribute to a software project.  Updating or
    translating documentation and testing bug fixes are good places to start;
    they will also help you learn your way around and make you friends.

Respect what has already been done.
:   If the first thing you do when you walk into someone's home is say, "Here's
    how I'd redecorate," you shouldn't expect to be invited back.  Follow the
    project's existing coding conventions even if you prefer something else.
    Use existing tags for issues, and above all, don't introduce yourself by
    suggesting that they rearchitect the code or change languages.

Be patient.
:   It took me almost three months of full-time work to get up to speed in my
    previous job, and the first contributor to the Python scripts used to build
    this book needed a couple of evenings to find their way around.  Depending
    on the size, age, and organization of the project you're joining, you should
    expect it to have to invest something like this much time before you feel
    productive.  (You will always look back and say, "I could have done this so
    much more quickly."  You will always be wrong.)

Start small.
:   This is a corollary of the previous three points.  As you learn your way
    around a project socially as well as technologically, you will build a
    mental model of how it works ([%x thinking %]).  Offering a small
    contribution is a way to test that mental model.  Do you understand the
    application's architecture?  Do you know where tests are supposed to go and
    how review and merging work?  A three-line change to documentation is a more
    cost-effective way to test this than three hundred lines of new code that
    might completely miss the mark.

Keep exploring.
:   Thousands of books have been written about how to write code, but only a few
    explain how to read it ([%b Spinellis2003 %] being my favorite).
    However, reading other people's code is one of the best ways to learn how to
    be a better programmer, while browsing a project's issues can give you even
    more insight into why the code works the way it does (and where and why it
    stops working).  If you feel that this is a less productive use of your time
    than coding, think about how much time musicians spend listening to each
    other or how much artists look at each other's work.

    In my experience, the best approach to learning your way around a new code
    base is to trace what happens during a typical operation.  What functions or
    methods are called in what order as an HTTP request is processed?  What
    objects are created?  What changes are made to files or databases, if any?
    The "step over" button your debugger is a very useful tool for this
    ([%x debugging %]), since it allows you ignore low-level details while you're
    trying to paint a bigger picture.

Get to know people.
:   There is a softball team here in Toronto that practices every Thursday but
    hasn't played an actual game in twenty years.  As with many groups, their
    ostensible reason for existing is just an excuse for people who like each
    other to hang out.  A lot of software projects are like that, in industry as
    well as open source: participants get satisfaction from working with one
    another as well as from what they produce.  While your job won't ever love
    you back [%b Jaffe2021 %], the relationships you make with the people
    you work beside may be as rewarding as the software you build.

Remember that most relationships don't end in marriage.
:   It's OK to do a little work on an open source project and then decide if
    it's for you or not.  It's equally OK to look for a new job if you're not
    happy with the one you're in: after all, most companies wouldn't hesitate to
    eliminate your job if they needed to cut costs.  Don't let anyone manipulate
    you by making you feel guilty about this.

Share what you learn.
:   If you aren't the first person to join a project, you probably won't be the
    last.  One of the most compassionate things you can do is share what you
    found out as you were learning your way around so that the next person can
    do so more quickly.  Doing this also helps you figure out what you know now
    that you didn't know then, which can help you the next time around.

<div class="callout" markdown="1">
### Buddies and mentors

A well-run company's process for getting newly-hired people up to speed can be
anything from a simple checklist like the one in [%x onboarding %] to a
multi-week sequence of courses.  However it's done, it is most effective when
new people are paired with buddies or mentors to direct their first questions
to, and who will check in with them regularly to see how they're doing.
</div>
