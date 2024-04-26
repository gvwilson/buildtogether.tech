---
title: Teams
---

Most people learn better together than they do on their own
[%b Michaelson2004 %].  As long as their teams [%i "teams!learning
benefits of" %]work well[%/i%], they achieve higher grades, retain information
longer, are less likely to drop out of school, and graduate with better
communication skills and a better understanding of what will be expected of them
in their subsequent careers.

But that "as long as" is important.  A badly-run team is worse than no team at
all, since people will waste hours or days arguing with one another, duplicating
or undoing each other's work, and wishing that they had gone into gardening
instead.  These conflicts are more wearying than any number of buffer overruns
or accidentally erased files, which is why most computer science courses stick
to individual assignments.

It doesn't take much to make a team work smoothly, though. The rules in
[%x important %] for running meetings, making decisions, and resolving conflicts
are a good start; this chapter will look at what else you can do.

## Picking Teams

I once heard an anthropologist ask, "How big is a sports team?"  When people
said it depends on the sport, she explained that in fact they all have about
[%i "teams!effective size of" %]half a dozen members[%/i%].  Anything larger
than that splits into smaller groups: the forwards and backs in rugby, the
infield and outfield in baseball, and so on.  She went on to explain that
hunting parties in non-agricultural societies are usually that size as well, as
are basic military units around the world (a platoon is two squads of six
people).  Since we can only keep a handful of things in our short-term memory at
once ([%x thinking %]) that's as big as a team can practically be.

The same observation applies to software development.  Three or four people can
work tightly on a single piece of code, but when there are more they define some
interfaces and develop in parallel.  Collaborative tools like software portals
([%x git-solo %]) help groups coordinate more effectively, but the groups
themselves stay the same size.

Teams of three to five provide a good balance between skills and accountability.
A team of two may not have enough breadth and background to tackle a large piece
of work; more importantly, one or the other person is likely to take a dominant
role.  If you put six or eight people in a team, on the other hand, you may not
be able to divide up the work in a way that will keep everyone engaged and busy.
Teams that size or larger also increase the odds that at least one member will
be a [%i "hitchhiker" %]hitchhiker[%/i%], and make scheduling meetings much
more difficult.

Many students prefer to [%i "teams!selecting" %]select[%/i%] their teammates,
and students with high grades tend to want teammates with a similar profile.
[%b Post2020 %] found that matching students by grade led to a small
improvement in outcomes, with a larger impact on team grades than on individual
ones. The same study found that members of self-selected teams were more likely
to already have [%i "teams!effect of having friends on" %]friends[%/i%] on
their team, but that this was *negatively* correlated with outcomes (possibly
because people are less willing to hold friends accountable for missed work).

One surprising finding is that having students with [%i "teams!benefits of
diverse ability levels" %]a range of grades[%/i%] in the same team either has no
effect or improves outcomes *for everyone*
[%b Mosher2013 Donovan2018 Farland2019 Auvinen2020 %].  It's easy to see
how this benefits teams of weak students: they are likely to get coaching from
their stronger teammates. One theory for why it also helps stronger students is
that the best way to learn something is to explain it to someone else; bringing
a weaker teammate up to speed will usually do more for your grade than spending
those same hours hacking or reading.

In my experience, teams of strong students are also more likely to use a divide
and conquer strategy, effectively reducing the project to a set of parallel
sub-projects handled by one person each. This may feel more efficient, but most
of the benefits of working in a team are lost: there's less back-and-forth
discussion of design issues, and little improvement in communication skills.
Those may not be important to you at first, but if there is a final exam in your
course with questions about the project work, your mark on it may depend on how
much you know about your teammates' work ([%x delivery %]).

The most powerful argument for instructors selecting teams, though, is that's
how it works in the real world [%b Oakley2004 %].  You probably won't get
to pick your colleagues if you join a company or an academic research group.
Instead, you'll be put on a project and expected to work well with whoever else
is on it. Your performance will depend as much on your ability to get along with
others as it will on your raw technical ability, so you might as well start
practicing those skills now.

If instructors create teams, they should [%i "teams!isolating at-risk
students" %]avoid isolating at-risk students[%/i%].  Women and members of racial
minority groups are more likely to drop out of computer science than other
students, particularly in first and second year, and one of the main reasons is
feeling isolated or out of place. Research has shown that putting at-risk
students together in the first couple of years can mitigate this problem
[%b Margolis2002 %]. It is less necessary in upper years, since by then
students have a stronger commitment to whatever program they're in, but it still
helps to prevent some of the problems discussed in the next section.

The biggest headache when instructors select teams is [%i "teams!taking
schedules into account" %]scheduling[%/i%].  COVID-19 has made distributed work
more normal, but the last university I taught at had three campuses spread
across a large metropolitan area, and some students commuted an hour and a half
each way to get to classes.  Instructors should therefore take students'
schedules into account when forming teams. If the class is small, the simplest
way is to get each student to fill in a weekly timesheet showing when they're
available, and then group people who have large blocks of overlap. If the class
is larger, a web-based calendaring tool may be easier. Instructors can even try
to use whatever software the university uses to figure out course timetables,
although that usually doesn't scale down to in-class scheduling.

Another factor to take into account is that some people are naturally early
birds, while others are night owls. Putting the two on the same team pretty much
guarantees that someone will miss meetings, or sleep through them, no matter
when they're held. Simply asking people, "Do you prefer to work in the morning,
or the evening?" can be surprisingly effective.

However you form teams, each team should have at least one block of two hours to
work together each week outside of class. Teams should also try to find a second
block that's half an hour long for a weekly meeting. Try to keep the two blocks
separate so that it's clear to everyone when they're supposed to be talking
about the project and when they're supposed to be doing design, writing code,
testing, and so on. If the two are scheduled back-to-back, the meeting will drag
on into working time or vice versa.

## Who Does What

All right, you've formed a team: now what? How do you decide [%i "teams!allocating work" "allocating work!in teams" %]who does what[%/i%]? How do
you make sure that everyone actually does what they're supposed to? And most
importantly, how do you do this fairly?

Some jobs have [%i "allocating work!effect of social status" %]higher social
status[%/i%] than others, and what is or isn't considered important usually
reflects racial and gender divides within society—so much so that sociologists
use the phrase "[women's work][womens-work]" to describe the phenomenon. It is
also known as "[quarterback syndrome][quarterback-syndrome]": two thirds of NFL
players overall in the United States are Black, but only 17% of quarterbacks,
which is the position on a team with the highest social status.

Among programmers, writing operating systems or other software that is close to
the hardware has higher status than building user interfaces; people doing the
former are both paid more and more likely to be male than people doing the
latter, regardless of ability or value delivered to the employer. This creates a
feedback loop: white and Asian men pursue certain career paths because they have
high status (they want to be "real programmers"), and the fact that they are
pursuing those careers is what maintains their higher status. It also creates a
[%i "allocating work!confirmation loop" "confirmation loop!allocating work" %][%g confirmation_loop "confirmation loop" %][%/i%]: since women and people of color
get fewer chances to do certain tasks, they are less good at them, which
"confirms" the initial bias.

All of this starts in the classroom. In mixed-gender teams, for example, female
students are more likely to be given responsibility for taking notes, writing
documentation, and other low-status tasks. Some have experienced this so often
that they have come to accept it as the price they have to pay for being in
tech. Others protest, but those who do are often dismissed as being "difficult"
([%x important %]). Many take a third path and decide to leave
programming—after all, why play a game that's unfair?

<div class="callout" markdown="1">
### In the beginning

[%i "history of computing" %]Programming[%/i%] was originally considered a
female occupation, but as it became more lucrative it came to be viewed as
"naturally" male.  [%b Abbate2012 %] and [%b Ensmenger2012 %]
describe how this happened, while [%b Hicks2018 %] looks at how Britain
lost its early dominance in computing by systematically discriminating against
its most qualified workers: women.  Some men become quite uncomfortable whenever
this is brought up, but we need to learn how to discuss our own history if we
want to be able to think clearly about how the things we're doing today might
change society tomorrow.
</div>

## Division of Labor

There are many ways to divide project work between team members, and as
[%b Conway1968 %] observed, the software you get will reflect the division
of labor, a phenomenon known as [%i "Conway's Law" %][%g conways_law "Conway's Law" %][%/i%] or [%i "sociotechnical congruence" %][%g sociotechnical_congruence "socio-technical congruence" %][%/i%] [%b Cataldo2008 %]. In a
[%i "modular decomposition" "allocating work!modular decomposition" %][%g modular_decomposition "modular decomposition" %][%/i%], each person is
responsible for one part of the program. For example, one person might design
and build the GUI, while another writes the database interface, and a third
implements the business rules. Having people own parts of the code like this
produces lower failure rates in industry [%b Bird2011 %], but is generally
a bad strategy in a course project:

1.  It increases the risk of people from marginalized groups being assigned
    lower-status work.

2.  It leads to [%i "big bang integration" %][%g big_bang "big bang integration" %][%/i%], in which all the components meet each other for the
    first time right at the end of the project. Big bang almost always fails.

3.  Each team member only really understands one aspect of the project. This can
    hurt a lot if there's a final exam that checks for overall understanding.

4.  If someone drops out or fails to complete their module, the project as a
    whole will fail.

[%i "functional decomposition" "allocating work!functional decomposition" %][%g functional_decomposition "Functional decomposition" %][%/i%], in which each
person is responsible for one type of task, is usually more successful. With
this strategy, one person does the testing, another handles the documentation, a
third does the bulk of the coding, and the fourth takes care of build and
deployment.  This guarantees that everyone understands most of the project by
the end of the term. The obvious drawback is that each person only gets to hone
one set of skills.

Another drawback stems from the fact mentioned above that some activities are
viewed as being more prestigious than others. If the team decomposes work
functionally, the self-appointed [%g alpha_geek "alpha geeks" %] will
usually snag the plum jobs like architecture and coding, leaving less appealing
work to people who aren't as pushy, privileged, or self-confident. This tends to
reinforce existing inequities; it also tends to lower the team's overall grade,
since there's often little relationship between how outspoken people are and how
well they work.

<div class="callout" markdown="1">
### The [%i "Dunning-Kruger effect" %]Dunning-Kruger effect[%/i%]

[%b Kruger1999 %] reported that people who know a subject well can usually
estimate their knowledge accurately, but people who don't will often
overestimate their competence because they don't know what they don't know.
More recent work has cast doubt on this finding: it could simply be an artifact
of the way the original researchers did their statistics [%b Jarry2020 %].
Either way, you should never trust self-reported expertise, as there's no easy
way to tell if someone really knows what they're talking about or if what
they're actually reporting is their self-esteem.
</div>

[%i "feature decomposition" "allocating work!feature decomposition" %][%g feature_decomposition "Feature decomposition" %][%/i%] is a variation on
modular decomposition that works well in practice. Instead of owning an entire
subsystem for the life of the project, each team member handles the design,
coding, testing, and documentation for one small feature after another.  Working
this way is central to agile development ([%x process %])) and is a good
way to cope with the never-ending timeslicing of student life.

Finally, there is [%i "rotating decomposition" "allocating work!rotating decomposition" %][%g rotating_decomposition "rotating decomposition" %][%/i%]: everyone
does one task for a few weeks, then a different task for the new few, and so
on. This is initially less productive in absolute terms than either of the
preceding strategies, since the team has to pay for ramp-up several times
over. In the long term, though, it outperforms the alternatives: it is more
robust (having a team member drop out is less harmful), and if everyone on the
team is familiar with every aspect of the software, they can all contribute to
design and debugging sessions.

Any of these strategies is better than [%i "chaotic decomposition" "allocating work!chaotic decomposition" %][%g chaotic_decomposition "chaotic decomposition" %][%/i%], which unfortunately is the most common approach. If people
have different ideas about who's supposed to do what, some things won't be done
at all while others will be done several times over. (You can tell if your
decomposition is chaotic by counting how many times people says, "I thought
*you* were doing that!" or "But I've already done that!"  The more often you
hear this, the more trouble you're in.) All other decompositions tend toward
chaos under pressure, so it's important to establish rules early and stick to
them when the going is easy so that the instinct to do the right thing will be
there when you need it.

<div class="callout" markdown="1">
### Clarity

No matter how you allocate work, make sure that everyone understands who is
doing what, when. As [%b Barke2019 %] found, actual roles can be fluid;
what matters most is that team members understand and accept their
responsibilities and everyone else's at any particular moment.
</div>

## Team Contracts

No matter what decomposition you use, your team should write, sign, and submit a
[%i "team contract" %][%g team_contract "team contract" %][%/i%] outlining what
everyone has agreed to do to make the project a success. In my experience, this
is most effective if each team creates their own as part of their first
assignment so that they actually have to think about what they're promising
their teammates.  Here's an example:

> We, the members of Team 12, agree that:
>
> 1.  Work on each assignment will divided according to role. Two people will
>     code, one will test, and one will be responsible for documentation. One of
>     the coders will run the weekly meeting; the other will take minutes and
>     post them to the project wiki on the same day as the meeting. These roles
>     will rotate for each assignment; no one will code two assignments in a
>     row.
>
> 2.  The tester will be responsible for submitting the assignment.  A team
>     member will only be listed as contributing to that assignment if at least
>     two other members of the team agree they completed, or made significant
>     progress on, at least one work item.
>
> 3.  We will aim to get at least 80% on each assignment.
>
> 4.  We will hold a half-hour status meeting every week on Thursdays at 4:00
>     pm.  Everyone will be in the meeting by 4:05 pm; if someone cannot attend,
>     they will let the rest of the team know by email no later than 2:00 pm
>     that day.
>
> 5.  Everyone will add a brief point-form summary of their progress that week
>     to the project wiki no later than 12:00 noon on Thursday.  Everyone will
>     read everyone else's summary before the 4:00 meeting.
>
> 6.  All discussion about the project will take place on the team's Slack
>     channel so that everyone can see it and search through it later.
>
> 7.  No one will check code into version control that fails to compile.  No one
>     will check in code that fails to pass existing tests without first getting
>     the permission of that round's tester. No one will change the database
>     schema or add dependencies on new libraries without first getting
>     permission from the whole team.

It may sound a little silly, like the contracts that some parents and children
make up regarding chores and allowances, but it's very effective.  First, people
may have very different ideas about what being in a team means: some may be
happy with a bare pass, while others may want the team to shoot for an A+ on
everything. Knowing who wants what won't make these tensions go away, but it
helps focus the argument.

Drawing up a contract also prevents later disagreements about who actually
promised or agreed to what. As with meetings, people often remember things
differently; having a signed record is everyone's second-best defense.

<div class="callout" markdown="1">
### Who's it for?

I still don't know if teams should have to give copies of their contracts to
their instructors or not. On the one hand, it's a great way to let your
instructor know how you're planning to operate, and what you're planning to
achieve. Given that she probably has a lot more experience than you, it gives
her a chance to tell you if you've forgotten anything or that your teammate's
really cool idea is unlikely to work in practice. On the other hand, as soon as
something has to be handed in, some students will write what they think the
instructor wants to read, rather than what they actually think.
</div>

Most software development teams in industry and open source don't bother with
contracts like these. There may be corporate guidelines on good citizenship, or
performance metrics written into job descriptions, but in general people expect
that if you're doing this for a living, you know what others can reasonably
expect of you, and you will live up to those expectations.

If your instructor has you draw up a team contract at the start of the project,
then she can and should base part of your team's grade on how well you stuck to
it. If she handed you a team contract, she should definitely base part of the
grade on compliance. If there was no contract at all, though, it's unfair to
turn around at the end of the project and ask people to rate one another, since
they won't have known while they were working what they were going to be rated
on.

Asking people on a team to [%i "peer evaluation" %]rate their peers[%/i%] is
a common practice in industry.  Instructors sometimes shy away from it because
they're afraid students will gives everyone in the team a high rating in order
to boost grades. However, this actually occurs fairly infrequently
[%b Kaufman2000 %].

What's more, as long as evaluation is based on observables, rather than
personality traits, peer assessment can actually be as accurate as assessment by
the instructors and other outsiders. "Observables" means that instead of asking
if the person is outgoing or if they have a positive attitude, assessments
should ask if they listen attentively during meeting or attempt to solve
problems before asking for help.  The performance review guidelines in
[%x eval-personal %] are a useful starting point.

## Problems and Solutions

When I first put these notes together fifteen years ago, I wrote a section
titled "People to Watch Out For" that described a dozen people who make teams
less productive in different ways. As several reviewers have pointed out since,
it was arrogant and harmful: arrogant because what I was really saying was, "If
you don't work the way I do then you're wrong," and harmful because it would
make people who already doubt themselves do so even more.

If you read one of those earlier versions, I apologize. What I've tried to do
below is describe ways in which I've seen people undermine themselves.  If you
go through this list with your teammates and tell them what you'd like to get
better at, they'll probably help you. And if what you want to get better at
isn't on this list, please see [%x contrib %].

Not everything needs to be completely correct.
:   Before correcting a factual error, ask yourself whether it really matters.
    If it's the name of the configuration file the program reads on startup, the
    answer is probably yes; if it's the name of a minor villain from the Marvel
    Cinematic Universe, the answer is probably no.

The devil doesn't need more advocates.
:   We remember when [%i "contrarian (why not to be)" %]contrarians[%/i%]
    turn out to be right because it happens so infrequently, but because those
    moments are memorable, some people fall into the habit of taking the
    opposite point of view no matter what is being discussed.

You wouldn't have gotten this far if you weren't good at this.
:   Some people have [%i "self-confidence (lack of)" %]so little
    confidence[%/i%] in their ability despite their good grades that they won't
    make any decision, no matter how small, until they have checked with someone
    else. This is often a result of social conditioning: in particular, women
    are more likely to doubt themselves, while men often over-estimate their
    ability.

Not everything worth doing should be done.
:   For many years my favorite phrase was, "Why don't we?" Why don't we write a
    GUI to help people edit the program's configuration files? Hey, why don't we
    invent our own little language for designing GUIs? This energy and
    enthusiasm are hard to argue with, but argue you must.  Otherwise, for every
    step you move forward, the project's goalposts will recede by two. This is
    called [%i "feature creep (danger of)" %][%g feature_creep "feature creep" %][%/i%], and has ruined many projects that might otherwise have
    delivered something small but useful.  My solution these days is to keep a
    [%g to_dont_list "to-don't" %] list of things that would be fun and
    worthwhile, but that I'm *not* going to tackle.

Success is a habit.
:   The more you follow a routine, the more your brain will be able to focus on
    the right things at the right time. [%b Gawande2011 %] found that
    [%i "checklists!benefits of" %]checklists[%/i%] improve results even for
    experts, and [%x important %] talked about the value of to-do lists for
    managing your time. Making these a habit reduce [%i "cognitive
    load!impact of checklists" %]cognitive load[%/i%] ([%x thinking %]) and
    gives you more mental capacity for dealing with the work itself.

Acting like an asshole doesn't make you cool—it just makes you an asshole.
:   I had a teammate once whose favorite phrase was, "That's stupid."  If anyone
    complained, he said, "It's just the way I talk." The problem with people
    using vulgar or aggressive language in everyday conversation is that for
    many other people, that language has often been followed by bullying or
    discrimination. They're right not to trust you if those are the signals you
    choose to send. (And no, calling someone out for being vulgar or aggressive
    is not the same as [%i "tone policing" %]tone policing[%/i%].)

Sometimes it's hard to care.
:   You have a teammate who doesn't read the assignment specs, hasn't bothered
    to learn the tools and libraries you're supposed to be using, and commits
    code that doesn't even compile.  Before treating them like a hitchhiker, try
    to find out if there's a reason for their behavior: if he's caring for a
    family member or struggling with [%i "mental health" %]mental
    health[%/i%] issues, the most compassionate thing to do is to help them get
    back on their feet.
