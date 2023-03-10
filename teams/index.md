---
---

Students learn better in small teams than they do on their own
<cite>Oakley2004</cite>.  As long as their teams work well, they achieve higher
grades, retain information longer, are less likely to drop out of school, and
graduate with better communication skills and a better understanding of what
will be expected of them in their subsequent careers.

But that "as long as" is important.  A badly-run team is worse than no team at
all, since people will waste hours or days arguing with one another, duplicating
or undoing each other's work, and wishing that they had gone into gardening
instead.  These conflicts are more wearying than any number of buffer overruns
or accidentally erased files, which is why most computer science courses stick
to individual assignments.

It doesn't take much to make a team work smoothly, though. The rules in <span
x="important"></span> for running meetings, making decisions, and
resolving conflicts are a good start; this chapter will look at what else
you can do.

## Picking Teams

I once heard an anthropologist ask, "How big is a sports team?"  When people
said it depends on the sport, she explained that in fact they all have about
half a dozen members.  Anything larger than that splits into smaller groups: the
forwards and backs in rugby, the infield and outfield in baseball, and so on.
She went on to explain that hunting parties in non-agricultural societies are
usually that size as well, as are basic military units around the world (a
platoon is two squads of six people).  Since we can only keep a handful of
things in our short-term memory at once (<span x="thinking"></span>) that's as
big as a team can practically be.

The same observation applies to software development.  Three or four people can
work tightly on a single piece of code, but when there are more they define some
interfaces and develop in parallel.  Collaborative tools like issue trackers
allow groups to coordinate more effectively, but the groups themselves stay the
same size.

Teams of three to five are most effective, at least for student projects.  A
team of two may not have enough breadth and background to tackle a large piece
of work; more importantly, one or the other person is likely to take a dominant
role.  If you put six people in a team, on the other hand, you may not be able
to divide up the work in a way that will keep everyone engaged and busy.  Teams
that size also increase the odds that at least one member will be a hitchhiker.

Research also shows that teams formed by instructors work better than
self-selected teams. Students typically complain about this, sometimes
vehemently: they want to work with their friends, they don't want to be slowed
down by teammates who are slower or less dedicated than they are, their
part-time job or family care responsibilities limit when they can take part in
meetings, and so on.

Good instructors will ignore all of these objections except the last one. If
students are allowed to form their own groups, they tend to clump together by
ability. It's easy to see how this hurts teams of weak students: they are less
likely to be able to fill in the gaps in one another's knowledge. However, it
also hurts teams of stronger students.  The best way to learn something is to
explain it to someone else; bringing a weaker teammate up to speed will usually
do more for your grade than spending those same hours hacking or reading.

In addition, teams of strong students are more likely to use a divide and
conquer strategy, effectively reducing the project to a set of parallel
sub-projects handled by one person each. This may feel more efficient, but most
of the benefits of working in a team are lost: there's less back-and-forth
discussion of design issues, and little improvement in communication skills.
Those may not be important to you, but if there is a final exam in your course
with questions about the project work, your mark on it may depend on how much
you know about your teammates' work (<span x="delivery"></span>).

There's another strong argument against self-selected teams: the pre-existing or
ongoing relationships between their members make life a lot easier for
hitchhikers, and a lot harder for everyone else. It's hard enough to tell
someone they're not pulling their weight; it's a lot harder when that person is
also on your volleyball team.

The most powerful argument for instructors selecting teams, though, is, "That's
how it works in the real world." You probably won't get to pick your colleagues
if you join a company or an academic research group. Instead, you'll be put on a
project and expected to work well with whoever else is on it. Your performance
will depend as much on your ability to get along with others as it will on your
raw technical ability, so you might as well start practicing those skills now.

While instructors should try to include as diverse a spread of abilities in each
team as possible, they should avoid isolating at-risk students.  Members of
minority groups and women are more likely to drop out of computer science,
particularly in first and second year. We'll talk about this more in <span
x="rights"></span>, but one of the main reasons is feeling isolated or out of
place. Research has shown shown that putting at-risk students together in the
first couple of years can mitigate this problem <cite>Margolis2002</cite>. It is
less necessary in upper years, though, since by then students have a stronger
commitment to whatever program they're in.

The biggest headache when instructors select teams is scheduling.  COVID-19 has
made distributed work more normal, but the last university I taught at had three
campuses spread across a large metropolitan area, and some students commuted an
hour and a half each way to get to classes.  Instructors should therefore take
students' schedules into account when forming teams. If the class is small, the
simplest way is to get each student to fill in a weekly timesheet showing when
they're available, and then group people who have large blocks of overlap. If
the class is larger, a web-based calendaring tool may be easier. Instructors can
even try to use whatever software the university uses to figure out course
timetables, although that usually doesn't scale down to in-class scheduling.

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

All right, you've formed a team: now what? How do you decide who does what? And
just as importantly, how do you make sure that everyone actually does what
they're supposed to?

There are many ways to divide project work between team members, and as
<cite>Conway1968</cite> observed, the software you get will reflect the division
of labor, a phenomenon known as <span
g="sociotechnical_congruence">socio-technical congruence</span>
<cite>Cataldo2008</cite>. In a <span g="modular_decomposition">modular
decomposition</span>, each person is responsible for one part of the
program. For example, one person might design and build the GUI, while another
writes the database interface, and a third implements the business rules. Having
people own parts of the code like this produces lower failure rates in industry
<cite>Bird2011</cite>, but is generally a bad strategy in a course project for
three reasons:

1.  It leads to <span g="big_bang">big bang integration</span>, in which all the
    components meet each other for the first time right at the end of the
    project. Big bang almost always fails.

2.  Each team member only really understands one aspect of the project. This can
    hurt a lot if there's a final exam that checks for overall understanding.

3.  If someone drops out or fails to complete their module, the project as a
    whole will fail.

<span g="functional_decomposition">Functional decomposition</span>, in which
each person is responsible for one type of task, is usually more
successful. With this strategy, one person does the testing, another handles the
documentation, a third does the bulk of the coding, and the fourth takes care of
build and deployment.  This guarantees that everyone understands most of the
project by the end of the term. The obvious drawback is that each person only
gets to hone one set of skills.

Another, less obvious, drawback stems from the fact that some activities are
viewed as being more prestigious than others. If the team decomposes work
functionally, the self-appointed <span g="alpha_geek">alpha geeks</span> will
usually snag the plum jobs like architecture and coding, leaving less appealing
work to people who aren't as pushy or self-confident. This tends to reinforce
existing inequities; it also tends to lower the team's overall grade, since
there's often little relationship between how outspoken people are and how well
they work.

<div class="callout" markdown="1">

### The Dunning-Kruger Effect

<cite>Kruger1999</cite> found that people who know a subject well can usually
estimate their knowledge accurately, but people who don't will often
overestimate their competence because they don't know what they don't know.
Because of this, you should never trust self-reported expertise, as there's no
easy way to tell if someone really knows what they're talking about or if what
they're actually reporting is their self-esteem.

</div>

<span g="feature_decomposition">Feature decomposition</span> is a variation on
modular decomposition that works well in practice. Instead of owning an entire
subsystem for the life of the project, each team member handles the design,
coding, testing, and documentation for one small feature after another.  Working
this way is central to agile development (<span x="process"></span>)) and is a
good way to cope with the never-ending timeslicing of student life.

Finally, there is <span g="rotating_decomposition">rotating
decomposition</span>: everyone does one task for a few weeks, then a different
task for the new few, and so on. This is initially less productive in absolute
terms than either of the preceding strategies, since the team has to pay for
ramp-up several times over. In the long term, though, it outperforms the
alternatives: it is more robust (having a team member drop out is less harmful),
and if everyone on the team is familiar with every aspect of the software, they
can all contribute to design and debugging sessions.

Any of these strategies is better than <span g="chaotic_decomposition">chaotic
decomposition</span>, which unfortunately is the most common approach. If people
have different ideas about who's supposed to do what, some things won't be done
at all while others will be done several times over. (You can tell if your
decomposition is chaotic by counting how many times people says, "I thought
*you* were doing that!" or "But I've already done that!"  The more often you
hear this, the more trouble you're in.) All other decompositions tend toward
chaos under pressure, so it's important to establish rules early and stick to
them when the going is easy so that the instinct to do the right thing will be
there when you need it.

## Team Contracts

No matter what decomposition you use, your team should write, sign, and submit a
<span g="team_contract">team contract</span> outlining what everyone has agreed
to do to make the project a success. In my experience, this is most effective if
each team creates their own as part of their first assignment so that they
actually have to think about what they're promising their teammates.  Here's an
example:

<blockquote markdown="1">

We, the members of Team 12, agree that:

1.  Work on each assignment will divided according to role. Two people will
    code, one will test, and one will be responsible for documentation. One of
    the coders will run the weekly meeting; the other will take minutes and
    post them to the project wiki on the same day as the meeting. These roles
    will rotate for each assignment; no one will code two assignments in a
    row.

2.  The tester will be responsible for submitting the assignment.  A team
    member will only be listed as contributing to that assignment if at least
    two other members of the team agree they completed, or made significant
    progress on, at least one work item.

3.  We will aim to get at least 80% on each assignment.

4.  We will hold a half-hour status meeting every week on Thursdays at 4:00
    pm.  Everyone will be in the meeting by 4:05 pm; if someone cannot attend,
    they will let the rest of the team know by email no later than 2:00 pm
    that day.

5.  Everyone will add a brief point-form summary of their progress that week
    to the project wiki no later than 12:00 noon on Thursday.  Everyone will
    read everyone else's summary before the 4:00 meeting.

6.  All discussion about the project will take place on the team's Slack
    channel so that everyone can see it and search through it later.

7.  No one will check code into version control that fails to compile.  No one
    will check in code that fails to pass existing tests without first getting
    the permission of that round's tester. No one will change the database
    schema or add dependencies on new libraries without first getting
    permission from the whole team.

</blockquote>

It may sound a little silly, like those "contracts" that some parents and
children make up regarding chores and allowances, but it's very effective.
First, people may have very different ideas about what being in a team means:
some may be happy with a bare pass, while others may want the team to shoot for
an A+ on everything. Knowing who wants what won't make these tensions go away,
but it certainly helps focus the argument.

Drawing up a contract also prevents later disagreements about who actually
promised or agreed to what. As with meetings, people often remember things
differently; having a signed record is everyone's second-best defense.

I still don't know if teams should have to give copies of their contracts to
their instructors or not. On the one hand, it's a great way to let your
instructor know how you're planning to operate, and what you're planning to
achieve. Given that she probably has a lot more experience than you, it gives
her a chance to tell you if you've forgotten anything or that your teammate's
really cool idea is unlikely to work in practice. On the other hand, as soon as
something has to be handed in, some students will write what they think the
instructor wants to read, rather than what they actually think.

Two last notes. First, most software development teams in industry and open
source don't bother with contracts like these. There may be corporate guidelines
on good citizenship, or performance metrics written into job descriptions, but
in general people expect that if you're doing this for a living, you know what
others can reasonably expect of you, and you will live up to those expectations.

Second, if your instructor has you draw up a team contract at the start of the
project, then she can and should base part of your team's grade on how well you
stuck to it. If she handed you a team contract, she should definitely base part
of the grade on compliance. If there was no contract at all, though, it's unfair
to turn around at the end of the project and ask people to rate one another,
since they won't have known while they were working what they were going to be
rated on.

Asking people on a team to rate their peers is a common practice in industry.
Instructors sometimes shy away from it because they're afraid students will
gives everyone in the team a high rating in order to boost grades. However, this
actually occurs fairly infrequently <cite>Kaufman2000</cite>.

What's more, as long as evaluation is based on observables, rather than
personality traits, peer assessment can actually be as accurate as assessment by
the instructors and other outsiders. "Observables" means that instead of asking
if the person is outgoing or if they have a positive attitude, assessments
should ask if they listen attentively during meeting or attempt to solve
problems before asking for help.
The performance review guidelines in <span x="evaluation"></span> can serve as a useful starting point for such
evaluations.

## People to Watch Out For

<blockquote markdown="1">

All happy families resemble one another, but every unhappy family is unhappy in
its own way.

--- Leo Tolstoy

</blockquote>

Good team members share certain characteristics, but bad ones can be bad in many
different ways. Here are a few:

-   *Anna* knows more about every subject than everyone else on the team put
    together---at least, she thinks she does. No matter what you say, she'll
    correct you; no matter what you know, she knows better.  Annas are pretty
    easy to spot: if you keep track in team meetings of how often people
    interrupt one another, her score is usually higher than everyone else's put
    together.

-   *Bao* is a contrarian: no matter what anyone says, he'll take the opposite
    side. This is healthy in small doses, but when Bao does it, there's always
    another objection lurking behind the first half dozen.

-   *Cailin* has so little confidence in their ability (despite their good grades)
    that they won't make any decision, no matter how small, until they have
    checked with someone else. Everything has to be spelled out in detail for
    them so that there's no possibility of them getting anything wrong.

-   *Frank* believes that knowledge is power. He enjoys knowing things that other
    people don't---or to be more accurate, he enjoys it when people know he
    knows things they don't. Frank can actually make things work, but when asked
    how he did it, he'll grin and say, "Oh, I'm sure you can figure it out."

-   *Hediyeh* is quiet. Very quiet. She never speaks up in meetings, even when
    she knows that what other people are saying is wrong. She's more willing to
    contribute on Slack or via email, but she's very sensitive to criticism, and
    will always back down rather than defending her point of view. Hediyeh isn't
    a troublemaker, but rather a lost opportunity.

-   *Kenny* is a hitchhiker. He has discovered that most people would rather
    shoulder some extra work than snitch, and he takes advantage of it at every
    turn. The frustrating thing is that he's so damn *plausible* when someone
    finally does confront him. "There have been mistakes on all sides," he says,
    or, "Well, I think you're nit-picking." The only way to deal with Kenny is
    to stand up to him: remember, if he's not doing his share, *he's the bad
    guy*, not you.

-   *Melissa* would easily have made the varsity procrastination team if she'd
    bothered to show up to tryouts. She means well---she really does feel bad
    about letting people down---but somehow something always comes up, and her
    tasks are never finished until the last possible moment. Of course, that
    means that everyone who is depending on her can't do their work until
    *after* the last possible moment???

- *Petra*'s favorite phrase is "why don't we". Why don't we write a GUI to help
    people edit the program's configuration files? Hey, why don't we invent our
    own little language for designing GUIs? Their energy and enthusiasm are hard
    to argue with, but argue you must.  Otherwise, for every step you move
    forward, the project's goalposts will recede by two. This is called <span
    g="feature_creep">feature creep</span>, and has ruined many projects that
    might otherwise have delivered something small but useful.

-   *Raj* is rude. His favorite phrase is, "That's stupid," and if anyone
    complains, he says, "It's just the way I talk---if you can't hack it, maybe
    you should find another team." His only redeeming grace is that he can't
    dissemble in front of the instructor as well as Kenny, so he's easier to get
    rid of.

-   *Sergei* simply seems apathetic. He doesn't read the assignment specs, he
    hasn't bothered to master the tools and libraries he's supposed to be using,
    the code he checks in doesn't compile, and his thirty-second bug fixes
    introduce more problems than they solve. Before treating Sergei like a
    hitchhiker, try to find out if there's a reason for his failure to deliver:
    if he's caring for a family member or struggling with mental health
    challenges, the most compassionate thing to do is to give him some time to
    get back on his feet.

## Irreconcilable Differences

Sometimes, it isn't just one person on the team who's a problem.  Sometimes, the
whole team is dysfunctional. In the mid-1990s, for example, I worked in a data
visualization startup. Individually, we were all smart, decent people. Put us
together, though, and somehow our personalities and IQs canceled out, leaving us
all dumb and nasty.

Instructors can allow for this by announcing at the start of the course that
teams will be dissolved and re-formed halfway through the project, *unless*
every member on the team submits a separate signed request to stay together.
There's a bit of psychology here: if people are required to ask for their team
to be dissolved, they will often think, "It's more trouble than it's worth, I'll
just put up with it." If dissolution is the default, though, then students won't
be inhibited by any stigma attached to being the one who caused trouble.

Students also usually understand that dissolving their team and forming a new
one takes time that could be invested in earning a higher grade.  In practice,
therefore, teams will usually stick together if they see that troublemakers are
actually being dealt with.
