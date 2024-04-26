---
title: The Important Stuff
---

The worst mistakes people make are related to people, not software,
so before we look at version control or testing,
we need to talk about overwork,
meetings,
and resolving arguments.

<div class="callout" markdown="1">
### Not writing software takes less time

[%b Sedano2017 %] found that software development projects have
[%i "waste (in software development)" %]nine types of waste[%/i%]:
building the wrong feature or product,
mismanaging the backlog,
rework,
unnecessarily complex solutions,
extraneous [%i "cognitive load" %]cognitive load[%/i%] ([%x thinking %]),
psychological distress,
waiting and [%i "multitasking" %]multitasking[%/i%],
knowledge loss,
and ineffective communication.
*None of these are software issues,*
so if you only think about the code in your project and not about the people writing it,
everything will take longer and hurt more than it needs to.
</div>

## Crunch Mode

I used to brag about the hours I was working.
Not in so many words, of course—I had *some* social skills—but
I'd show up for work around noon,
unshaven and yawning,
and casually mention how I'd been up until 6:00 a.m. working on some monster bug.

Looking back,
I can't remember who I was trying to impress.
Instead,
what I remember is how much of the code I wrote in those all-nighters I threw away
once I'd had some sleep.
My mistake was to confuse "long hours" with "getting things done".
You can't produce software (or anything else) without doing some work,
but you can easily do lots of work without producing anything of value.
Scientific study of [%i "overwork" %]overwork[%/i%] goes back to at least the 1890s—see
[%b Robinson2005 %] for a short, readable summary.
The most important results are:

1.  Working more than eight hours a day for more than a couple of weeks of time
    lowers your total productivity,
    not just your hourly productivity—i.e., you get less done *in total*
    in [%i "crunch mode" %][%g crunch_mode "crunch mode" %][%/i%]
    than when you work regular hours.

1.  Working over 21 hours in a stretch
    increases the odds of you making a catastrophic error
    just as much as being legally drunk.

These facts have been verified through hundreds of experiments
over the course of more than a century,
including some on novice software developers [%b Fucci2020 %].
The data behind them is as solid as the data linking smoking to lung cancer.
However,
while most smokers will at least acknowledge that their habit is killing them,
people in the software industry still talk and act as if
they were somehow immune to science.
To quote [%i "Robinson, Evan" %]Robinson[%/i%]'s article:

<div class="callout" markdown="1">
When [%i "Ford, Henry" %]Henry Ford[%/i%] famously adopted a 40-hour workweek in 1926,
he was bitterly criticized by members of the National Association of Manufacturers.
But his experiments,
which he'd been conducting for at least 12 years,
showed him clearly that cutting the workday from ten hours to eight hours—and
the workweek from six days to five days—increased
total worker output and reduced production cost…
the core of his argument was that reduced shift length meant more output.

…many studies,
conducted by businesses, universities, industry associations and the military,
…support the basic notion that,
for most people,
eight hours a day,
five days per week,
is the best sustainable long-term balance point between output and exhaustion.
Throughout the 30s, 40s, and 50s, these studies were apparently conducted by the hundreds;
and by the 1960s,
the benefits of the 40-hour week were accepted almost beyond question in corporate America.
In 1962,
the Chamber of Commerce even published a pamphlet extolling the productivity gains of reduced hours.

But, somehow, Silicon Valley didn't get the memo…
</div>

I spent two years at a data visualization startup.
Three months before our first release,
the head of development "asked" us to start coming in on Saturdays.
We were already pulling one late night a week at that point
(without overtime pay—our boss seemed to think that
ten dollars' worth of pizza
was adequate compensation for four hours of work)
and most of us were also working at least a couple of hours at home in the evenings.
To no one's surprise,
we missed our "can't miss" deadline by ten weeks,
and had to follow up our 1.0 release with a 1.1 and then a 1.2
to fix the crash-and-lose-data bugs we'd created.
We were all zombies, and zombies can't code.

Hours like these are sadly still normal in many parts of the software industry,
and may actually be worse now that so many people are working from home.
Designing and building software is a creative act that requires a clear head;
it only takes a couple of minutes to create a bug
that will take hours to track down later.
As Robinson writes:

<div class="callout" markdown="1">
[%i "productivity" %]Productivity[%/i%] varies over the course of the workday,
with the greatest productivity occurring in the first four to six hours.
After enough hours,
productivity approaches zero;
eventually it becomes negative.
</div>

It's hard to quantify the productivity of programmers, testers, and UI designers
[%b Sadowski2019b Forsgren2021 %],
but five eight-hour days per week has been proven to maximize long-term total output
in every industry that has ever been studied.
There is no reason to believe that ours is any different.

Ah, you say, but that's *long-term* output.
What about short bursts now and then,
like pulling an all-nighter to meet a deadline?
That's been studied too,
and the results aren't pleasant.
Your ability to think drops by 25 points for each 24 hours you're awake.
Put it another way,
the average person's IQ is only 75 after one [%i "all-nighters" %]all-nighter[%/i%],
which puts them in the bottom 5% of the population.
Two all nighters in a row and their effective IQ is 50—the level at which
people are considered incapable of independent living.

The catch in all of this is that people usually don't notice their abilities declining.
Just like drunks who think they're still able to drive,
people who are deprived of sleep don't realize that they're not finishing their sentences (or thoughts).
They certainly don't realize that they're calling functions with parameters in the wrong order
or that the reason the tests are failing is that
they've forgotten to redeploy the application—again.

The first and most important lesson in this chapter is therefore
to think very hard about what's more important—how much you produce
or how much of a martyr you appear to be—and to pace yourself accordingly.

## Time Management

[%b Edwards2009 %] found that
starting assignments early and working consistently predicted good grades.
However,
while people in industry joke that having two bosses means living in hell,
students usually answer to four or five professors
whom don't coordinate due dates across their courses.

The best way to handle this situation—or more honestly, the least bad way—is
to prioritize carefully.
Get a piece of paper and draw
[%i "effort-importance grid" %][%g effort_importance_grid "a 3×3 grid" %][%/i%].
The X axis is effort: label its divisions "minutes", "hours", and "days".
The Y axis is time: label it "low", "medium", and "high".
You should wind up with something like [%f effort-importance %].

[% figure
   slug="effort-importance"
   img="effort-importance.svg"
   alt="Effort/importance matrix"
   caption="An example of an effort/importance matrix."
%]

Next,
put everything you need to do somewhere on the grid,
and then throw away the high-effort, low-importance items in the bottom right—you
aren't going to get to those.
You can then start assembling the other items into a schedule,
starting with the upper-left corner.
These are the things that will give the highest return on invested time;
more importantly,
starting with these means that if you've under-estimated effort,
you will still deliver *something*.

The tricky items are the ones on the diagonal.
Should you tackle one thing that is high effort and high importance
or three things that are individually less important
but require the same total effort?
Laying things out on a grid can't answer that question,
but at least it can tell you what the question is.

> How to prioritize:
> always finish first the tasks that will allow other people to continue/start/finish their work.
> 
> — Yanina Bellini Saibene

If any task on your list is more than an hour long,
break it down into smaller pieces and prioritize those separately.
Figuring out what those pieces are can take time,
so don't be embarrassed to make "plan XYZ" a task in its own right.
And remember that the future is approaching at a rate of 24 hours per day:
if something is going to take thirty hours to finish,
you had better allow at least five working days for it,
which means you'd better start at least that far ahead of the deadline.

The point of all this organization and preparation is
to be able to immerse yourself in your problem.
[%b Csikszentmihalyi1991 %] popularized the term [%i "flow" %][%g flow "flow" %][%/i%] for this;
athletes call it "being in the zone",
while musicians talk about losing themselves in what they're playing.
The good news is that you're much more productive in this state
than when you're multi-tasking.
The bad news is that
it takes anywhere from several seconds to several minutes
to get back into this state after an interruption [%b Parnin2010 Borst2015 %].
In other words,
if you are interrupted half a dozen times per hour
you are *never* at your productive peak.
Ironically,
the cost of self-interruptions may be even worse than the cost for external interruptions [%b Abad2018 %].

<div class="callout" markdown="1">
### Open offices suck

[%i "open offices (evils of)" %]Open offices[%/i%] were created
so that (mostly male) managers could keep an eye on (mostly female) office workers,
and to reduce air conditioning costs [%b Eley1995 %].
They lower productivity in every other way we can measure [%b Bernstein2018 %];
sadly,
the same is true of other interruption-rich environments
like your favorite coffee shop.
If you really want to be productive,
you should avoid both.
</div>

Finally,
you will be more productive in the long run if your back doesn't ache,
and being away from the keyboard
gives your brain a chance to reflect on what you've just been doing.
You should therefore take a five-minute [%i "breaks (importance of regular)" %]break[%/i%] every hour.
Checking email doesn't count:
get up and stretch,
refill your water bottle,
or go and restack the dishwasher.
You'll be amazed at how often you can solve a problem that's been baffling you for an hour
by taking a short walk…

## Meetings

The previous section explained how to be productive individually,
but what about being productive with others?
The most important thing is running [%i "meetings" %]meetings[%/i%] efficiently,
and the key to doing that is to distinguish between:

-   [%i "meetings!status" "status meeting" %][%g status_meeting "Status meetings" %][%/i%]
    for keeping everyone up to date on what everyone else is doing
    and for making simple decisions when the options are well understood.

-   [%i "meetings!discussion" %][%g discussion_meeting "Discussion meetings" %][%/i%]
    for weighing alternatives and making complex decisions.

-   Co-working sessions like brainstorming sessions and programming sprints
    that are devoted to the content of the project rather than its operation.

### Status Meetings

Every team should have a short weekly status meeting.
For each meeting,
create a table in a shared document like the one in [%t important-status %].
Everyone adds a few bullet points to their row in the table
at least half an hour before the meeting starts
so that the whole team can mull everything over.
If anyone wants to discuss something,
they highlight it by adding a comment.
The meeting moderator then goes through the highlighted items one by one,
spending no more than a couple of minutes on each;
anything that requires more time is deferred to a discussion meeting

[% table slug=important-status tbl=status.tbl caption="Status Update Table" %]

<div class="callout" markdown="1">
### Are you a blowfish or a clam?

[NOAA's guide][noaa-disruptive] to dealing with disruptive behaviors
has useful labels and even more useful advice
for handling people who may send meetings off course.
</div>

### Decision Meetings

Decision meetings are for issues that will have more long-term impact on the project
or that team members disagree about.
Since the stakes are higher,
they need more structure:

Decide if there actually needs to be a meeting.
:   If the only purpose is to share information,
    send a brief email instead:
    most people can read faster than they can speak.

Write an agenda.
:   If nobody cares enough about the meeting to prepare
    a point-form list of what's to be discussed,
    the meeting probably doesn't need to happen.
    (Note that "the agenda is all the open issues in our GitHub repo" doesn't count.)

Include timings in the agenda.
:   Doing this helps prevent early items stealing time from later ones.
    The first estimates with any new group are inevitably optimistic,
    so expect to revise them upward for subsequent meetings.
    But don't have second or third
    meeting just because the first one ran over time: instead, try to figure out
    *why* it ran over and fix the underlying problem.

Select a moderator.
:   Put one person in charge of keeping items on time,
    selecting the next person to speak,
    chiding people who are having side conversations or checking email,
    and asking people who are talking too much to get to the point.
    The moderator should *not* do all the talking:
    in fact,
    the moderator will talk less in a well-run meeting than most other participants.

Prioritize.
:   Tackle the most important issues first, even if they're the longest,
    because the little ones always take more time than you expect.

Require politeness.
:   No one gets to be rude,
    no one gets to ramble,
    and if someone goes off topic,
    it's the moderator's job to say, "Let's discuss that elsewhere."

No interruptions.
:   This rule is a special case of the one above,
    since treating other people with respect is the sincerest form of politeness.
    Participants should raise a hand (physically or electronically)
    when they want to speak.
    The moderator should keep track of the queue
    and give each person time in turn.

No distractions.
:   Side conversations make meetings less efficient
    because nobody can actually pay attention to two things at once.
    More importantly,
    if someone is checking their email or texting a friend during a meeting,
    it's a clear signal that they don't think the speaker or their work is important.
    This doesn't mean a complete ban on technology—people may need accessibility aids
    or be waiting for a call about childcare—but by default
    phones should be face down and laptops should be closed
    during in-person meetings.

Take minutes.
:   As discussed below,
    someone other than the moderator should take
    [%i "minutes (of meetings)" %]point-form notes[%/i%]
    about the most important information that was shared
    and about every decision that was made or every task that was assigned to someone.

End early.
:   If the meeting is scheduled for 10:00--11:00,
    aim to end at 10:50 to give people a break before whatever they're doing next.

As soon as the meeting is over,
add the minutes to the project's wiki,
version control repository,
or shared cloud drive.
Please don't email minutes to everyone:
our inboxes are full enough,
and the more places new team members need to search in order to find things,
the more likely they are to miss something important.

Sharing the minutes ensures that:

People who weren't at the meeting can follow what's going on.
:   We all have to juggle tasks from several projects or courses,
    which means that sometimes we can't make it to meetings.
    Checking a shared record is more accurate and more efficient than asking a colleague,
    "What did I miss?"

Everyone can check what was actually said or promised.
:   Accidentally or not, people often remember things differently;
    writing them down gives everyone a chance to correct mistakes
    and misinterpretations.

People can be held accountable.
:   Whoever has to draw up the agenda for the next meeting
    can start with the action items from the previous one.

If you would like to become better at sharing information and making decisions,
there is no better place to start than [%b Brookfield2016 %],
which catalogs fifty different techniques for managing discussions
and explains when and how each is useful.

## Air Time

One problem with meetings is that
some people may talk far more than others.
Other people may be so accustomed to this
that they don't speak up even when they have valuable points to make.

You can combat this
by giving everyone [%i "meetings!three sticky notes" "three sticky notes (in meetings)" %]three sticky notes[%/i%]
(or coins, or paperclips—anything inedible will do) at the start of the meeting.
Every time someone speaks,
they have to give up one sticky note.
When they're out of stickies,
they aren't allowed to speak until everyone has used at least one,
at which point everyone gets all of their sticky notes back.
This ensures that nobody talks more than three times as often as
the quietest person in the room,
which completely changes group dynamics.
People who have given up trying to be heard suddenly have space to contribute,
and the overly-frequent speakers realize how talkative they have been.

Another useful technique is called
[%i "meetings!interruption bingo" "interruption bingo (in meetings)" %]interruption bingo[%/i%].
Draw a grid and label the rows and columns with the participants' names;
each time person A interrupts person B,
add a tally mark to the appropriate cell.
Look at the results Halfway through the meeting:
in most cases it will be clear that one or two people are doing all of the interrupting,
and that they're always interrupting the same people.
After that,
saying, "All right, I'm adding another tally to the bingo card,"
is usually enough to get them to throttle back.
If it isn't,
well,
you just learned something about your teammate…

Online meetings provide special challenges for regulating how often individuals speak.
[%b Troy2018 %] discusses why [%i "meetings (online)" %]online meetings[%/i%]
are often frustrating,
and points out that in most online meetings,
the first person to speak during a pause gets the floor.
As a result,
"If you have something you want to say,
you have to stop listening to the person currently speaking
and instead focus on when they're gonna pause or finish
so you can leap into that nanosecond of silence
and be the first to utter something.
The format…encourages participants who want to contribute to say more and listen less."

The solution is to run a text chat beside the video conference
where people can signal that they want to speak;
the moderator can then select people from the waiting list.
Text chat is better than the "raise hand" feature most video conferencing tools offer
because the person who wants to speak can indicate why.
For example,
they can type "question about budget"
rather than just "question"
so that the moderator can group related questions together.

## Making Decisions

The first release of GitHub's [Minimum Viable Governance][github-mvg] guidelines
included this:

> **2.1. Consensus-Based Decision Making**
> 
> Projects make decisions through consensus of the Maintainers.
> While explicit agreement of all Maintainers is preferred,
> it is not required for consensus.
> Rather,
> the Maintainers will determine consensus based on their good faith consideration of a number of factors,
> including the dominant view of the Contributors and nature of support and objections.
> The Maintainers will document evidence of consensus in accordance with these requirements.

It sounds reasonable,
but it is harmfully wrong.
Every team has a power structure:
the question is whether it's formal or informal—in other words,
whether it's accountable or unaccountable [%b Freeman1972 %].
In the latter case,
decisions will effectively be made by the people
who are the most self-confident or stubborn
rather than by those with the most insight.

To guard against this,
groups need to spell out who has the authority to make which decisions
and how to achieve consensus.
In short,
they need explicit [%i "governance" %][%g governance "governance" %][%/i%].

[%i "Martha's Rules" %][%g marthas_rules "Martha's Rules" %][%/i%] [%b Minahan1986 %]
are a practical way to do this in groups of up to a few dozen people,
and work very well for smaller teams too:

1.  Before each meeting, anyone who wishes may sponsor a proposal.
    Proposals must be filed at least 24 hours before a meeting in order to be considered,
    and must include:
    -   a one-line summary
    -   the full text of the proposal
    -   any required background information
    -   pros and cons
    -   possible alternatives

2.  A quorum is established in a meeting if half or more of voting members are present.

3.  Once a person has sponsored a proposal,
    the group may not discuss or vote on the issue
    unless the sponsor or their delegate is present.

4.  After the sponsor presents the proposal
    a [%i "sense vote" %][%g sense_vote "sense vote" %][%/i%] is cast:
    -   Thumbs up: who likes the proposal?
    -   Thumbs down: who is uncomfortable with the proposal?
    -   Thumbs sideways: who can live with?

5.  If everyone likes or can live with the proposal,
    it passes with no further discussion.

6.  If the majority is uncomfortable with the proposal,
    it is sent back to its sponsor for further work.
    (The sponsor may decide to drop it if it's clear the majority isn't ever going to support it.)

7.  Otherwise,
    the group has a brief moderated discussion.
    After 10 minutes,
    or when no one has anything further to add,
    the moderator calls for a straight yes-or-no vote on the proposal.
    If a majority votes "yes" it is adopted;
    otherwise,
    it is returned to the sponsor for further work.

Every group that uses Martha's Rules must make two procedural decisions:

How are proposals put forward?
:   The easiest way to do this in a software project
    is to file an issue in the project's [%i "issue tracker" %]issue tracker[%/i%]
    tagged *Proposal*.
    Team members can comment on it there
    so that the sponsor can revise it before bringing it to a vote.

Who gets to vote?
:   In a course project the answer is "whoever is part of the team,"
    but a more explicit rule is needed for larger or longer-lived projects.
    One method is for existing members to nominate new ones,
    and for the team to hold a straight yes-or-no vote on each.
    Another is to automatically include anyone whose changes to the code
    were accepted by existing members,
    though this under-values non-programming contributions
    like doing code reviews
    or testing new releases.

Rules that people don't know about can't help them.
Once your team agrees on a decision-making procedure,
document it for newcomers
(and to prevent disputes among people already in the team).
You can put this in the project's [%i "README file" %]`README`[%/i%] file ([%x starting %])
or in a separate file called [%i "CONTRIBUTING file" %]`CONTRIBUTING`[%/i%].
Wherever it goes,
remember that the easier it is for people to figure out how to contribute,
the more likely they are to do so [%b Steinmacher2014 %].

<div class="callout" markdown="1">
### Nothing about us without us

The rules laid out above were created
by and for people near the middle of the bell curve with respect to focus and attention span.
People who are [%i "neurodivergence" %][%g "neurodivergent" "neurodivergent" %][%/i%],
i.e., whose brains work differently from the average
when it comes to sociability, learning, attention, and mood
may find that other approaches work better for them.

But while society accepts that
people of different heights need different desks and seating to be comfortable,
there is still a lot of [%i "neurodivergence (stigma associated with)" %]stigma[%/i%]
associated with differences in mental function,
which are often classified according to
[how inconvenient they are to other people][adhd-thread].
One example is how tests for
[%i "ADHD" %][%g "adhd" "attention-deficit/hyperactivity disorder" %][%/i%]
(ADHD) are phrased.
"Subject is overly talkative": compared to who?
"Subject does X when it is inappropriate": by whose rules?
"Struggles to pay attention": in fact,
most people with ADHD can pay very close attention,
but not when they are in environments like noisy classrooms
that are full of distractions.

Decisions that affect people should only be made
with the full participation of those who will be affected.
If you are neurodivergent,
you probably have a set of strategies for managing time and attention.
If you are [%i "neurotypical" %][%g "neurotypical" "neurotypical" %][%/i%]
and have neurodivergent teammates,
ask them what works well for them rather than ignoring the difference
or guessing what they might want.
Please do the same if you have teammates who have difficulty seeing, hearing, or moving about:
they have expertise you don't.
</div>
