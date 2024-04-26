---
title: Process
---

A [%i "development process" %][%g development_process "development process" %][%/i%] defines who does what, when, in order to build a piece of
software.  Many have been described over the last fifty-odd years; most have
passionate advocates and equally passionate detractors, but the differences
between them are smaller in practice than in theory.  This chapter therefore
starts by describing how most programmers work day-to-day and how to adapt that
routine to the chaos of student life.

<div class="callout" markdown="1">
### Paying attention matters most

I am sceptical of most claims made about processes, partly because teams that
adopt diametrically opposed processes all see productivity improve.  One
explanation is that common practice is the worst of all possible worlds, and any
change at all would be an improvement.  (There are days when I believe this.)  A
more likely explanation is that what really matters is paying attention to what
you're doing.  It's kind of like dieting: Atkins, macrobiotic, seasonal, or
fruitarian is secondary to eating better and exercising more.
</div>

## Process as Feedback Loops

I think about process in terms of [%i "feedback loops" %]feedback loops[%/i%]
on different timescales ([%f feedback-loops %]).  Any particular team
emphasizes some of these and pays less attention to others.

[% figure
   slug="feedback-loops"
   img="feedback-loops.svg"
   alt="Feedback loops"
   caption="Software development feedback loops on different timescales."
%]

[%i "pair programming" %][%g pair_programming "Pair programming" %][%/i%].
:   One programmer, the driver, does the typing, while the other, called the
    navigator, watches and comments.  Every twenty minutes or or so, the pair
    switches roles.  The benefits of pair programming are proven for students as
    well as for professionals [%b Williams2001 Hannay2009 DiBella2013 %].
    First, the navigator will often notice mistakes in the driver's code, or
    remember design decisions that the driver is too busy typing to recall. This
    is the tightest of the feedback loops, since feedback is nearly continuous.

    Second, pair programming spreads knowledge around: every piece of code has
    been seen by at least two people, which reduces the risk of "But I didn't
    know" mistakes.  It also helps people pick up new skills: if you have just
    seen someone do something with two clicks, you will probably do it that way
    when it's your turn to drive, rather than spending two minutes doing it the
    way you always have.  Finally, most people are less likely to check email
    every five minutes if someone else is working with them.

Unit testing.
:   Many developers are passionate about a technique called [%i "test-driven development" %][%g tdd "test-driven development" %][%/i%], where you write
    the tests for a new bit of software before you write the software
    itself. Its advocates claim that it makes developers more productive
    because:

    1.  writing the tests first helps you figure out what you're actually trying
        to do,

    1.  you're less likely to polish things needlessly if you have set yourself
        a goal, and

    1.  it ensures the tests actually get written.

    However, multiple studies over many years have failed to show that it makes
    developers more productive [%b Erdogmus2005 Fucci2016 %].  What
    *might* be the case is that working in short, interleaved segments is more
    productive than doing a lot of coding followed by a lot of testing or vice
    versa [%b Fucci2017 %].

[%i "continuous integration" %]Continuous integration[%/i%].
:   As discussed in [%x tooling %]), building the software and running
    tests every time someone creates a pull request or commits to the main
    branch gives the whole team feedback about what state the software is in.
    This is particularly important when other people or pairs are working on it:
    each change might work in isolation, but combining them might break things
    if someone hasn't been careful about doing merges.

[%i "code review" %]Code review[%/i%].
:   [%x git-team %] explained when, why, and how to do this.

The other practices—stand-up meetings, sprints, analysis & estimation—are
covered below, while delivering releases is covered in [%x delivery %].
Before we explore them, though, let's take a look at a typical afternoon in the
life of a student programmer.

## Daily Routine

Most guides to being productive tell you to establish a routine.  Research shows
that you'll learn more from spacing things out than from cramming
[%b Weinstein2018 %], and doing a bit of work on your project every day is
good insurance against getting sick or being interrupted by other work.
However, it often isn't feasible when you're juggling deadlines in four or five
courses.

Even if you can't set a regular schedule, you *can* set aside blocks of time so
that your flow isn't interrupted, and be systematic in those blocks.  Here's an
example:

3:00 p.m.
:   You have two hours to spend on your project, so you launch VS Code and
    update your Git repository.  Your teammates have changed 17 files since the
    meeting two days ago.

3:05 p.m.
:   You log in to GitHub.  Five issues have been closed, but there are eight new
    ones, three of which are assigned to you.  It looks like the file parser you
    wrote last week doesn't handle the "clarification" the prof posted on
    Monday.  You create a new branch and start writing unit tests to isolate the
    things that are breaking ([%x design %]).

3:25 p.m.
:   You have added twelve new tests, each between three and ten lines long.
    Eleven fail the way you expect; the twelfth triggers an assertion in a data
    structure one of your teammates built.  You commit the tests to Git, file an
    issue with a reference to the test case, and start fixing your code.

4:00 p.m.
:   The eleven tests whose failure was your fault now pass, so you create a pull
    request with your fixes for one of your teammates to review.  You mention
    the issues they wrote in the commit message so that GitHub automatically
    links the code to the issues and vice versa—it only takes a second to type
    in this information, and it makes it much easier for your teammates to keep
    track of what you've done.  You then take a five-minute break to check
    email; when you're done, you close your mail client again because you've
    learned the hard way that you can't resist looking at new messages if you
    get notifications.

4:05 p.m.
:   You can now start work on the feature you want to add, which translates part
    of the program's internal data structure into a blob of JSON to send to a web server.  You have an hour less to do
    this than you originally planned, but that's OK: by fixing bugs first,
    you've avoided the all-too-common situation of only half the code working
    when the project is "done". Again, the first step is to create a new branch
    so that you can later create a small (i.e., reviewable) pull request.

4:30 p.m.
:   after a couple of drafts, you're happy with the design of the new
    feature. With only 20 minutes until your next break, you know you won't
    finish it and its tests today.  Instead, you decide to write stubs of the
    helper methods you think you're going to need.  These stubs all return 0,
    `null`, or something else that allows you to write and run your first few
    tests.

4:50 p.m.
:   After checking everything in, you post a short message on the project's
    Slack channel to tell your teammates what you've done.  You then reward
    yourself by checking email and watching a few YouTube videos of cats doing
    stupid things.

Three or four sessions a week like that from each person on the team plus a
meeting to stay organized and you will be in great shape.

## The Waterfall Model

To start our exploration of the longer feedback loops in
[%f feedback-loops %], let's look at a process that nobody uses, but which
appears in almost every textbook. It's called the [%i "waterfall model" "process!waterfall" %][%g waterfall_model "waterfall model" %][%/i%],
and it divides development into a series of discrete phases,
each of which is completed before the next begins:

1.  Gather requirements.

1.  Analyze them to produce [%g schema "data schemas" %] and
    [%g business_rule "business rules" %].

1.  Design the software.

1.  Write it.

1.  Test it.

1.  Deploy it (i.e., install it, configure it, etc.).

This process was first described in [%b Royce1970 %] as something that
couldn't possibly work.  In real life, we always learn things in later stages
that we couldn't reasonably have anticipated in earlier ones, which means we
constantly have to go back and revise earlier decisions.  If we *do* try to
figure out every detail in advance, we quickly succumb to [%i "analysis
paralysis" %]analysis paralysis[%/i%].

Every real software development processes attempts to resolve the tension
between doing things once and spending so much time on planning that we never
actually do anything.  In order to understand the differences between them it
helps to look at the [%i "Boehm Curve" %][%g boehm_curve "Boehm Curve" %][%/i%],
which shows the effort required to fix a bug based on when it is caught.

In the 1970s and 1980s, Boehm showed that fixing bugs becomes more expensive as
you move later and later in the development cycle [%b Boehm1981 %]
([%f boehms-curve %]).  Better tools and vastly more powerful computers have
flattened Boehm's curve over the past thirty years, but it is still takes more
effort to fix things later than earlier [%b Dawson2010 %].

[% figure
   slug="boehms-curve"
   img="boehms-curve.svg"
   alt="Boehm's Curve"
   caption="The cost of fixing bugs increases later in the development cycle."
%]

Development teams deal with this in three ways.  The first is to ignore it.  If
you're being paid a steady salary by a company that can survive delays and cost
overruns in your project, or if you're willing to give up your evenings and
weekends, then this approach still doesn't make much sense, but a lot of people
adopt it anyway.

The second strategy is to do a lot of planning and design to catch as many
errors as possible during the early phases of the project.  This is the
classical engineering mindset: when you're building a dam, fixing mistakes means
moving several million tons of earth around, so it's the only one that makes
sense. The third strategy is to move in many short steps with frequent course
corrections.  If we can get accurate feedback at each step (and that's a big
"if") this approach lets us adapt to changing circumstances and new realizations
more easily.

## Agile

The term [%i "agile development" %][%g agile "agile" %][%/i%] was coined in 2001
to describe a bottom-up approach to software project management based on very
short iterations and frequent feedback from both developers and customers.
[%b Masood2018 %] and many others have found it to be effective for
student projects; we will look at one form called [%i "Scrum" %][%g scrum "Scrum" %][%/i%].

<div class="callout" markdown="1">
### Right place, right time

Agile development practices are almost as old as programming, but they came into
their own with the rise of the web in the late 1990s.  First, the web made it
possible to release software weekly, daily, or even hourly, since updating a
server is a lot faster, and a lot less expensive, than shipping CDs to thousands
of people. Second, during the 1990s and early 2000s it seemed as if web
programming tools were changing every single day. Multi-year development plans
didn't make a lot of sense when everything they depended on would be obsolete by
the time work started, much less by the time it finished.

Third, the growth of the web was aided by, and fuelled, the growth of the open
source movement. People couldn't help noticing that most open source projects
didn't have long-range plans, but nevertheless produced high-quality software
faster than many closed-source commercial projects.
</div>

Scrum breaks development down into short [%i "sprint" %][%g sprint "sprints" %][%/i%], typically no more than two weeks long, and sometimes
as short as a single day.  In each sprint, the team decides what to build next,
designs it, builds it, tests it, and delivers it.

Users often don't know what they want until they see it, so short sprints are a
way to avoid spending too much time building what turns out to be the wrong
thing.  In addition, most people can keep track of what they're doing for a few
days at a time without elaborate Gantt charts, so short cycles allow them to
spend proportionally less time coordinating with one another. And finally,
finding bugs becomes easier: instead of looking through weeks' or months' worth
of software to find out where the problem is, developers usually only have to
look at what's been written in the last few days.

A typical working day starts with a [%i "stand-up meeting" %][%g stand_up_meeting "stand-up meeting" %][%/i%] where everyone in the team reports what they
did the day before, what they're planning to do that day, and what's blocking
them (if anything).  It's called a stand-up because it's usually held standing
up, which encourages people to stay focused; each day, the team gets feedback on
the progress they're making, whether they're still on track to meet the
iteration's goals, whether the technical decisions they're making are paying
off, and so on.

For example, suppose your team is building a static site generator.  Your
stand-up report might be:

Yesterday
:   Fixed the bug that was making the message file reader crash on accented
    characters, and added code to the HTML producer to display accented
    characters properly.

Today
:   Will get the message file reader to recognize links to images and load those
    images.

Blockers
:   What should the message file reader do if the image can't be found? Should
    it link to the ones it has, halt with an error message, or something else?

The key to making this work is that each task is at most a day long.  Anything
longer is broken into sub-tasks so that there's something substantial to report
at every meeting.  Without this rule, it's all too easy for someone to say,
"Still working on X," several days in a row, which means that feedback, and the
possibility of early course correction, are lost.

Scrum and other agile processes [%i "agile development!conditions for
success" %]work best[%/i%] when:

1.  Requirements are constantly changing, i.e., long-range planning simply isn't
    possible. This is often true of student projects, since the people on the
    team may not have worked in this domain or with these tools before.

2.  Developers and users can communicate continuously, or at worst daily or
    weekly. This varies widely from one student project to another: if you are
    your own customers it's not a problem, but if you have a real external
    client, you may only be able to meet with them every few weeks.

3.  The team is small, so that everyone can take part in a single stand-up
    meeting. This is usually true for student projects, though getting everyone
    to show up for a morning meeting can be a challenge.

4.  Team members are disciplined enough not to use "agile" as an excuse for
    chaotic coding.

5.  Everyone on the team can make some progress every day.

The last two points are the most important.  Most developers don't like writing
plans before they code, or documentation when they're done.  Coincidentally,
agile doesn't require them to do much of either.  It's therefore all too common
for developers to say "we're agile" when what they mean is "we're not going to
bother doing anything we don't want to".  In reality, agile requires *more*
discipline, not less, just as improvising well requires even more musical talent
than playing a score exactly.

In addition, most students can't put an hour or two into their project every
working day because of the other courses they're juggling.  Anyone trying to
work on five Scrum projects simultaneously in industry would wonder what the
hell management was thinking; since we can't fix that, the best most students
can hope for is two or three focused sessions a week.

## Planning and Scheduling

If you're going to spend three days driving across the country, it makes sense
to spend half an hour figuring out a good route.  Equally, if you're going to
spend several months building a complex piece of software, *and you know what
the final result is supposed to look like*, it makes sense to spend some time
figuring out what you're going to do and how long it ought to take.  Since most
students have never had to do this kind of scheduling many find it the most
valuable part of their first project course.  In order to explain how to go
about it, I need to describe two important roles in real software projects.

The [%i "product manager" %][%g product_manager "product manager" %][%/i%] is the
person who owns the spec [%b Perri2018 %].  While developers are building
Version N, she is talking to customers to find out what should go into Version
N+1.  She doesn't ask them what features they want; if she does, she'll get a
mish-mash of conversations overheard in frequent flyer lounges and buzzwords
plucked from recent Twitter threads.  Instead, she asks:

1.  What can't you do right now that you want to?

1.  What do you find irritating in the current product?

1.  Why are you using our competitor's software instead of ours?

She then translates the answers into a list of features to be considered for
Version N+1.  The product manager usually also talks to developers to find out
what they don't like about the current software and adds their wishes to the
pile.  Typically, these are things like "refactor the persistence layer", "clean
up the build", and "upgrade to the latest version of Node".

So, it's Monday morning.  Version N shipped last Thursday; the team has had a
weekend to catch its collective breath and is ready to start work once again.
(If people are so burned out from the previous round that they need a whole week
to recover, go back and re-read [%x important %].)  At this
point the product manager divides up the list of desired features and assigns
them to the developers.  Each developer then has some time—typically a few
days to a couple of weeks—to do a little research, write some throwaway
prototype code, and most importantly *think*.  How could this feature be
implemented?  Is there an alternative that would take a tenth the time but only
deliver half of what was asked for?  What impact will each alternative have on
the build?  On deployment?  How will the feature be tested?  And so on.

This process is called [%i "analysis & estimation" %][%g ae "analysis & estimation" %][%/i%] (A&E).  The result is a short document, typically 1--5 pages
long.  There's no set form for this, but they usually include whatever
background information a well-informed developer is unlikely to already know, a
discussion of the alternatives, lessons learned from any prototyping that was
done, and an estimate of how much time would be needed to build each
alternative.  This time includes estimates from QA (for testing), the technical
writer (for documenting), the dev ops team responsible for managing deployment,
and so on.

So now it's Monday morning again.  Three weeks have gone by and all the A&E's
are done.  When the time estimates are totaled, they come to 700 developer-days.
Unfortunately, there are only 240 available: the size of the team is fixed and
the next release has to be available in May.  This is normal: there is *never*
enough time to add everything that everyone wants to a piece of software, and
even if there was, it probably shouldn't be done anyway.

FIXME: back ref to [%x important %].

It can take several
sessions to sort this out; the most important thing is that people don't start
shaving estimates to make things fit.  If they do, estimators will start padding
their numbers in self-defense.  Since managers aren't stupid, they'll shave the
estimates even more, so developers will add even more padding, at which point
you might as well abandon the whole exercise.

The hardest step in this process for beginners is coming up with time estimates
for particular tasks.  How can you possibly guess how long it will take to write
a database persistence layer for some JavaScript classes if you have never used
a persistence layer before?

1.  You're not expected to pull an number out of thin air (at least, not by
    managers who know what they're doing).  Instead, you should budget enough
    time to write some throwaway code or download and mess around with an open
    source tool in order to get a feel for it.

2.  You've had to learn other new technologies before and then apply them in
    courses.  A guess based on that experience might be off by a factor of two
    or three, but it probably won't be off by a factor of ten.  Even if it is,
    it's better than no guess at all.

The more estimating you do the better you'll get, but only if you compare what
actually happened to what you predicted. No feedback: no improvement.

## Cutting Corners

A schedule's primary purpose is not to tell you what you're supposed to be doing
on any given day, but to tell you when you should start [%i "cutting
corners" %]cutting corners[%/i%].  Suppose that you have ten weeks in order to
accomplish some task.  Five weeks after you start, you've only done the first
four weeks' worth of work.  You have several options:

Denial.
:   This is very popular but doesn't actually solve the problem.

Start working evenings and weekends.
:   This is also very popular, but is quickly self-defeating.  As
    [%x important %] explained, the quality of your work goes down when
    you're tired, so any ground you gain by working until three a.m.  you lose
    to extra debugging and rewriting.

Ask for more time.
:   Groups working in industry often do this (often in combination with the
    previous solution), but it usually isn't an option in an academic setting.
    Instructors have to submit marks at the end of the term; as far as the
    university is concerned, whatever hasn't been done by then might as well not
    be done at all.

Do less work.
:   You can either do less testing (which is quickly self-defeating) or update
    the schedule to reflect the rate at which you're actually working and drop
    features if it now shows that you won't be able to finish in time.

Let's return to our example.  At the start of the project you believed it would
take ten weeks.  You're now at week five through, but you've done only the first
four weeks' worth of work.  Looking at it another way, your estimates for how
long tasks would take were too optimistic by about 25%.  You should therefore go
back to your schedule and add 25% to each task's estimate.  That means some of
the things you originally planned to do will now spill off the end of your
ten-week window.  That's OK: it's a shame you won't get to them, but at least
you know it now and can start taking action (like lowering your instructor's
expectations) well in advance of delivery.

In the real world these calculations are the responsibility of the
[%i "project manager" %][%g project_manager "project manager" %][%/i%].  Her job is to
make sure everyone is doing what they're supposed to, to handle interruptions
(there are *always* interruptions), and to track the team's progress.  After a
few weeks, the project manager should compare how much has actually been done
with how much was supposed to be done and adjust plans accordingly.

Real customers will thank you for doing this provided you do it early.  "I'm
sorry, we're not going to have the frobnosticator for May 1" is OK on October 1,
or even January 1, since it gives whoever was counting on the frobnosticator
time to make other plans.  It is *not* OK on April 30; neither is saying (or
worse, not saying) that it's "done" but full of bugs.

It's more problematic in student projects, particularly if the instructor has
specified the full feature set needed for an A.  In that case the best you can
do is ask which features are worth the fewest marks and cut those.

Taking scheduling seriously is one of the things that distinguishes good
software development teams from bad ones.  It's unfortunate that you'll only get
to do it once or twice during your project course, since you only really see the
benefits with practice, but I hope that even once will be enough to convince you
of its value.

## Triage

When disaster strikes, doctors do triage to determine who will survive without
immediate treatment, who won't even with treatment, and who can only be saved if
they are treated right away.  Similarly, one of a project manager's main
responsibilities is to [%i "triage" %][%g triage "triage" %][%/i%] the issues in a
project's [%i "issue tracker!helping triage" "triage!using issue
tracker" %]issue tracker[%/i%] ([%x communicate %]) periodically and adjust
the schedule accordingly. The [%i "effort-importance grid!helping
triage" %]effort-importance grid[%/i%] that you drew at the start will help with
this: by the time you are a few weeks into your project, you should be able to
update the effort estimates, add newly-discovered issues, and draw up a more
realistic plan.

But as well as cutting features, you can use what you have learned about the
users' needs to revise the spec.  What features do you now believe are unlikely
to be used?  Which ones could be consolidated?  Most importantly, which of the
users' needs that your original plan *wouldn't* satisfy could you help with?
Figuring this out is one of a project manager's most important responsibilities
[%b Perri2018 %]; whatever you do, don't fall into the trap of thinking
that you have to build something because you originally thought you should, or
keep it because you have it.  As [%f feature-usage %] shows using data from
[%i "Brown, Neil" %][Neil Brown][brown-neil][%/i%] and the [%i "Blackbox
project" %][Blackbox][blackbox] project[%/i%], the frequency with which features
are used drops off pretty quickly; sometimes only the tool's own developers use
those in the [%g long_tail "long tail" %].

[% figure
   slug="feature-usage"
   img="feature-usage.svg"
   alt="Distribution of feature usage"
   caption="Distribution of feature usage in BlueJ (data courtesy of Neil Brown)."
%]

## Which Process Should You Use?

In practice, the differences between these processes are a lot smaller than
their advocates would have you believe.  Regardless of what which one they're
officially using, most developers do some long-range planning at the start of
the project (if only because customers and instructors are usually not willing
to sign a blank check) and then revise their plans and aims as they go along.

Which process makes the most sense for an undergraduate course project?  The
odds are that the question won't even come up: your instructor will probably
tell you to follow the analyze-design-code-test-deploy cycle of the classical
(sturdy) model or to work in two- or three-week agile iterations.  I usually use
the former in courses, since:

-   you're very likely to encounter it after you graduate;

-   it gives you more chance to hone your planning and scheduling skills; and

-   close interaction with customers is a central tenet of most agile processes,
    but isn't really possible in a classroom setting.

Since your project has to fit in one or two terms, you'll probably be asked to
go around the loop once or twice, which in turn determines how much you'll be
expected to deliver in each iteration.  This is called [%i "time boxing" %][%g time_boxing "time boxing" %][%/i%]:
you specify how long a cycle will last, then
see how much work you can fit into that interval.  The alternative is
[%i "feature boxing" %][%g feature_boxing "feature boxing" %][%/i%]: you decide what you
want to do and then build a schedule that gives you enough time to do it.  Most
people believe that time boxing works better, since it encourages developers to
take smaller steps and allows them to give customers more frequent demos (which
serve as course corrections).
