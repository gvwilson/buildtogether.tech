Researchers have been studying programs and programmers since at least the
1960s; while there are many unknowns, they have learned a lot about what works
and what doesn't.  Sadly, most people in industry still don't know what we know
or even what kinds of questions we have answers for. One reason is their belief
that software engineering research is divorced from real-world problems; another
is that many programmers haven't done any science themselves since high school.
The average biology students does thirty to forty experiments during their
undergraduate degree; the average computer science student may only do one, so
it's not surprising that computer science graduates don't understand or value
the scientific method.

A third reason is that many people would rather fail than change. People cling
to creationism, refuse to accept the reality of anthropogenic climate change, or
insist that vaccines cause autism. Given that, it's not surprising that many
programmers continue to act as if a couple of quotations from a tech
entrepreneur who struck it lucky constitute "proof".

This chapter therefore presents a few evidence-based results that are relevant
to the kind of work you may be doing in your project and that your instructor
might want to incorporate into your course [%b Fagerholm2017 %].  If you
find them interesting and want to dig further, [%x methods %] describes the
methods software engineering researchers use.  As with all research, though,
some caution is required when interpreting results:

Theories change as more data becomes available.
:   Software engineering is a comparatively young discipline—the term itself
    wasn't used until 1968—so it would be surprising if everything we think
    we know turned out to be true.

Most of these studies' subjects are [%i "WEIRD" %]WEIRD[%/i%].
:   They are from Western, Education, Industrialized, Rich, and Democratic
    societies [%b Henrich2010 %], and may not be representative of the
    other 99% of humanity.

The data we have doesn't capture everything.
:   [%b Aranda2009 %] found that in every one of the bugs they traced,
    some key insight or action wasn't captured digitally. Similarly,
    [%b Herzig2013 %] carefully examined thousands of bug reports from
    several projects and found that many mis-report themselves in ways that will
    inevitably skew the results of simplistic analysis.

Historically, juries in Scotland were allowed to return one of [%i "Scottish verdict" %][%g scottish_verdict "three verdicts" %][%/i%]: innocent,
guilty, or not proven.  The world would be a better place if we were all more
comfortable saying, "I don't know," and with changing our minds as new evidence
comes in.

## What Do We Know About Programmer Productivity?

Let's start our exploration of research results with the often-repeated claim
that some programmers are [%i "productivity!comparative" %]ten times more
productive[%/i%] than others.  Is it actually true?  The short answer is, "It's
complicated."  As [%b Prechelt2019 %] shows, the answer depends on what
exactly the question is intended to mean. Looking at exactly the same data, you
could conclude that some programmers are 105 times more productive than
others—except this doesn't take into account whether people's code actually
works or what language they were using.

If you only look at one language, the ratio goes down to 17:1, but that's still
comparing the very best to the very worst.  Now the discussion starts to get
statistical: if you compare the median of the slower half of programmers with
the median of the top 10%, the ratio is 5:1 or 11:1, depending on whether you
use everyone in the sample or restrict it to those who used the same language
respectively.

[%b Sadowski2019a %] summarizes of what we know, and more importantly, how
to think about the problem.  The chapter [%b Sadowski2019b %] lays out a
three-axis framework for discussion based on the
[%i "Goal-Question-Metric" %][%g gqm "goal-question-metric" %][%/i%] approach.
The more recent [%i "SPACE framework" "productivity!SPACE framework" %]SPACE framework[%/i%] looks at
Satisfaction, Performance, Activity, Communication, and Efficiency
[%b Forsgren2018 Forsgren2021 %].  However productivity is measured, it's
important to remember [%i "Goodhart's Law" %][Goodhart's
Law][goodhart-law][%/i%]: as soon as you use some measure to evaluate people it
ceases to be a good measure because people will start to game the system.  For
example, [%b Gitinabard2020 %] reports that it's possible to classify
student software teams as collaborative, cooperative, or solo-submit by
analyzing the history of their version control repositories. If these measures
are ever used for grading, students will immediately start making extra commits
(or fewer, or whatever else is needed) in order to get the "right" profile.

Another thing to keep in mind is the way that privilege defines performance.
People naturally value the things they're good at, so the people who define the
criteria for high performance tend to emphasize things that just happen to give
them high scores.  As Kenneth Wesson wrote in [%b Littky2004 %], "If poor
inner-city children consistently outscored children from wealthy suburban homes
on standardized tests, is anyone naïve enough to believe that we would still
insist on using these tests as indicators of success?"

<div class="callout" markdown="1">
### What don't you want to know?

[%b Begel2014 %] asked one set of developers what questions they most
wanted researchers to answer, then asked another set of developers to rate those
questions.  Respondents favored questions about how customers typically use
their applications, but were opposed questions related to assessing the
performance of individual employees or comparing them with one another;
[%b Huijgens2020 %] found that data scientists viewed most possible
research topics the same way.
</div>

## What Do We Know About Programming Style?

As we mentioned in [%x tooling %], [%b Stefik2013 %] found that
languages like [%i "C" %]C[%/i%], [%i "Java" %]Java[%/i%], and [%i "Perl" %]Perl[%/i%] were as hard for people to learn as a language with a
randomly designed syntax, while languages like [%i "Ruby" %]Ruby[%/i%] and
[%i "Python" %]Python[%/i%] were significantly easier to learn. This result
is one of several showing that a programming language is a user interface that
can be studied and evaluated like any other.

For example, [%b Stylos2007 %] assessed how programmers use APIs with
required parameters in objects' constructors as opposed to parameterless default
constructors. They hypothesized that required parameters would create more
usable and self-documenting APIs by guiding programmers toward the correct use
of objects and preventing errors. Contrary to expectations, programmers strongly
preferred and were more effective with APIs that did not require constructor
parameters.  They then analyzed subjects' behavior using the
[%i "cognitive dimensions framework" %][%g cognitive_dimensions "cognitive dimensions" %][%/i%]
framework, which showed that that requiring constructor parameters interfered
with common learning strategies.

[%b Binkley2012 %] reported that [%i "reading code" %]reading[%/i%] and
understanding code is fundamentally different from reading prose: "…the more
formal structure and syntax of source code allows programmers to assimilate and
comprehend parts of the code quite rapidly independent of style.  In
particular…beacons and program plans play a large role in comprehension."  It
also found that experienced developers are relatively unaffected by identifier
style, so just to use consistent style in all examples.  Since most languages
have style guides (e.g., [%i "PEP8" "Python!PEP8 style
guide" %][PEP8][pep8][%/i%] for Python) and tools to check that code follows
these guidelines.  In contrast, [%b Schankin2018 %] found that:

> With descriptive identifier names, developers spent more time in the lines of
> code before the actual defect occurred and changed their reading direction less
> often, finding the semantic defect about 14% faster than with shorter but less
> descriptive identifier names. These effects disappeared when developers searched
> for a syntax error, i.e., when no in-depth understanding of the code was
> required. Interestingly, the style of identifier names had a clear impact on
> program comprehension for more experienced developers but not for less
> experienced developers.

More recently, [%b Floyd2017 Krueger2020 Peitek2021 %] have used
[%i "reading code!fMRI studies" %][%g fmri "fMRI" %][%/i%] to look at what programmers'
brain do when they are reading or writing code. The main findings are that
reading code is cognitively different from reading prose, but that the more
experienced programmers are, the less of a difference there is. This
corroborates earlier work with [%i "reading code!eye tracking studies" %]eye
tracking[%/i%] like [%b Hansen2013 %], which also found that experience
increases performance in most cases, but can actually *hurt* performance when
assumptions about what code is supposed to do are violated (i.e., when the eye
sees what the brain expects).

[%b Kernighan1999 %] wrote, "Programmers are often encouraged to use long
variable names regardless of context.  This is a mistake: clarity is often
achieved through brevity."  Lots of programmers believe this, but
[%b Hofmeister2017 %] found that using full words in [%i "reading
code!effect of variable names" "variable naming" %]variable names[%/i%] led to an
average of 19% faster comprehension compared to letters and abbreviations.  In
contrast, [%b Beniamini2017 %] found that using single-letter variable
names didn't affect novices' ability to modify code.  This may be because their
programs are shorter than professionals' or because some single-letter variable
names have implicit types and meanings.  For example, most programmers assume
that `i`, `j`, and `n` are integers and that `s` is a string, while `x`, `y`,
and `z` are either floating-point numbers or integers more or less equally.

Similarly, programmers have argued for decades about whether [%i "type
declaration!effect on readability" %]variables' data types[%/i%] should have to
be declared or not, usually based on their personal experience as professionals
rather than on any kind of data.
[%b Hanenberg2013 Endrikat2014 Fischer2015 %] found that requiring
variable type declarations does add some complexity to programs, but it pays off
by acting as documentation for a method's use—in particular, by forestalling
questions about what's available and how to use it. [%b Gao2017 %] looked
at how many bugs in JavaScript programs would have been caught if the code had
been written in TypeScript (which [%i "type declaration!effectiveness at
catching bugs" %]adds types[%/i%]), and came up with a figure of 15%, which is
either low (one in seven) or high (sales tax) depending on how you want to look
at it.

## What Can We Learn From Analyzing Code?

If engineering is applied science, then [%b Eichberg2015 %] is a great
example of software engineering.  In it, the authors show that it's possible to
identify a wide range of problems in code by comparing the actual [%i "flow
graph!actual" %]flow graph[%/i%] (which is the set of all possible paths through
the program) with the [%i "flow graph!abstract interpretation" %]abstract
interpretation flow graph[%/i%] (which is the set of all paths once possible
data values are taken into account).  To make this more concrete, the control
flow graph for:

```py
01: x = 0
02: if x > 0:
03:     x = 1
```

<!-- continue -->
includes the statement on line 3, but the abstract interpretation flow graph
doesn't, because there's no way it could ever be executed given the possible
value(s) of `x`.  Code paths that are never executed signal
[%i "dead code" %][%g dead_code "dead code" %][%/i%], which in turn usually signals logic errors, such
as use of `and` instead of `or` in a logical test.  The results from this kind
of analysis are impressive: the authors found that a lot of code in widely-used
libraries is littered with unnecessary `null` checks, and that even experienced
developers don't seem to understand Boolean operators as well as they should.

Program analysis can tell us many other things as well, all of which should
influence the design of future systems. For example, Python, JavaScript, and
many other languages are [%i "dynamic typing" "typing!dynamic" %]dynamically
typed[%/i%], while [%i "static typing" "typing!static" %]statically
typed[%/i%] languages like Java that restrict variables to particular types of
data. [%b Akerblom2015 %] looked at how often Python programs actually
rely on dynamic typing, and found that it was taken advantage of in only 2.5% of
cases. Adding generics (i.e., type declarations like `Array<int>`) only makes
half a percent of difference.  This doesn't mean that languages shouldn't
include more complex type systems, but it does (or should) mean that the onus is
on their designers to show that the complexity is worthwhile.

Meanwhile, lots of people say that copy-pasting code is bad practice: if you
find yourself creating [%i "code clones" %]code clones[%/i%], you should put
the repeated code in its own method and call it from all the original copies
([%x design %]).  But when [%b Kapser2008 %] explored *why*
developers create code clones, they found that code clones are OK in some cases:

> …the results of the case study identify a set of patterns that are most often
> harmful, namely *verbatim snippets* and *parameterized code*. While there were
> several examples of good usage of these clone patterns, the majority were deemed
> harmful. This may be an indication that developers should avoid this form of
> cloning. On the other hand several patterns were found to be mostly good:
> *boiler-plating*, *replicate and specialize*, and *cross-cutting
> concerns*. While not always good, when used with care (as with any form of
> design or implementation decision) these patterns are more likely to achieve an
> overall beneficial effect on the software system.

## What Do We Know About the Quality of Software?

The answer to the question in this section's title is, "A lot, and it's not good
news." For example, [%b Nakshatri2016 %] looked at how [%i "exception!under-used and abused" %]exceptions[%/i%] are actually used in Java
programs.  Rather than being used to make software more robust, exceptions are
either ignored or used as a debugging aid.  For example, the most common `catch`
block is one that logs the error rather than trying to recover from it; the next
most common are to do nothing at all (20% of cases), or to convert the checked
exception into an unchecked exception so that it can be ignored.  Similarly,
most programmers ignore Java's elaborate exception hierarchy and simply catch
`Exception` (78%) or `Throwable` (84%) rather than any of their more specific
subclasses.

In a similar vein, [%b Yuan2015 %] analyzed the [%i "error!root cause analysis" %][%g root_cause "root cause" %][%/i%] of around 200 confirmed failures
in large distributed systems. They report many findings, but the key one is that
92% of the catastrophic system failures are the result of incorrect handling of
non-fatal errors explicitly signaled in software, i.e., the software said,
"Something's wrong," but nothing was in place to handle the error. In 58% of
those cases, the underlying faults could easily have been detected through
simple testing of error-handling code.  The lesson is clear: make sure your
tests check that your program does the right thing when things go wrong.

One reason things go wrong is that developers don't make use of the tools they
have. [%b Beller2019 %] monitored 2,443 software engineers over the course
of 2.5 years in four [%i "IDE!under-used and abused" %]IDEs[%/i%]. They found
that:

> …half of the developers in our study does not test; developers rarely run their
> tests in the IDE; only once they start testing, do they do it heftily; most
> programming sessions end without any test execution; only a quarter of test
> cases is responsible for three quarters of all test failures; 12% of tests show
> flaky behavior; Test-Driven Development is not widely practiced; and software
> developers only spend a quarter of their time engineering tests, whereas they
> think they test half of their time.

Another factor that affects quality is how comprehensible the software is: in
particular, how easy or difficult it is to set it up.  [%b Xu2015 %]
looked at how often various [%i "configuration!parameters" %]configuration
parameters[%/i%] are actually used, and how correctly; they report that:

-   Only a small percentage (6.1%-16.7%) of configuration parameters are set by
    the majority of users; a significant percentage (up to 54.1%) of parameters
    are rarely set by any user.

-   A small percentage (1.8%-7.8%) of parameters are configured by more than 90%
    of the users.

-   A significant percentage (up to 47.4%) of numeric parameters have no more than
    five distinct settings among all the users' settings.  Similarly, for
    enumerative parameters with many options, typically only two to three of the
    options are actually used by the users, indicating once again the
    over-designed flexibility.

-   Too many knobs do come with a cost: users encounter tremendous difficulties in
    knowing which parameters should be set among the large configuration
    space. This is reflected by the following two facts: (1) a significant
    percentage (up to 48.5%) of configuration issues are about users'
    difficulties in finding or setting the parameters to obtain the intended
    system behavior; (2) a significant percentage (up to 53.3%) of configuration
    errors are introduced due to users' staying with default values incorrectly.

That said, most software actually *does* run despite the fact that programmers
don't do things the "right" way. One possible reason comes from the study of
trivial packages reported in [%b Abdalkareem2017 %], which looked at
230,000 NPM packages and 38,000 JavaScript applications. It turns out that less
than half of the trivial packages include tests; instead, they are "deployment
tested", i.e., their authors fix the breakages that users report, so that while
they might not work in all situations, they work in all situations that matter.

<div class="callout" markdown="1">
### What *can't* we learn?

Many people have put forward
[%i "code metrics!ineffectiveness of" %][%g code_metric "code metrics" %][%/i%]
that are supposed to measure the
complexity or likely number of bugs in a piece of software. However,
[%b ElEmam2001 %] found that these metrics are no better at predicting
things than simply counting the number of lines of code, because the longer the
program is, the more likely it is to contain whatever kinds of problems those
more sophisticated metrics are looking for.
</div>

## What Do We Know About Software Projects?

If there is one "law" of software development that most practitioners have heard
of, it is [%i "Brook's Law" %][%g brooks_law "Brooks' Law" %][%/i%]: adding people
to a late project makes it later. [%b Meneely2011 %] explores the
correlation between adding people to a team and the quality of the software the
team works on.  The paper reports that adding people is correlated with a later
increase in software quality, but adding them too quickly (that is, at a faster
pace than in previous months) is correlated with a *decrease* in quality.  This
is puzzling because theoretically, adding people to a project increases its
coordination costs, which in turn should impact all metrics of team success
negatively, including quality.

[%b Meneely2011 %] isn't an isolated finding: [%b Mockus2010 %]
found that more newcomers are not correlated with more defects, which supports
this finding. One possibility is that newcomers are assigned easy tasks, and so
they can't really break things too dramatically or in a way that won't get
caught internally in time. Another possibility is that the product has matured
over time—that software quality would go up no matter the team size simply
because there's less new functionality added as time goes on.

[%b Posnett2011 %] present an interesting twist on this. In the open
source projects they studied, they found that although code changes in general
are associated with future defect fixing activity, as we might expect, those
changes that correspond to new feature development and to code improvements are
*not*. That's interesting and counter-intuitive—one would expect new feature
code commits to be among the buggiest. The authors offer a possible explanation:
well-established open source projects tend to be quite conservative, and new
feature code is heavily scrutinized, so that most defects are found and sorted
out before the code is integrated.

Another surprising result comes from [%b Khomh2012 %]. They examined the
effects of Mozilla's switch from a yearly (or longer) release cycle to a much
more frequent cycle. Their raw material is bug and crash data; their conclusions
are:

1.  Users experience crashes earlier during the execution of versions developed
    following a rapid release model.

1.  The Firefox rapid release model fixes bugs faster than using the traditional
    model, but fixes proportionally less bugs.

1.  With a rapid release model, users adopt new versions faster compared to the
    traditional release model.

The third is good news; the second is (mostly) good, but the first is a puzzle
for which the authors don't have an explanation.

One of the many reasons software projects fail is poor estimation, and one of
the reasons people estimate badly is that they don't keep track of what's
happened before. [%b McIntosh2011 %] provides a baseline for both how much
effort is required to keep the build system in working order, and how much those
figures can be improved:

> …despite the difference in scale, the build system churn rate is comparable to
> that of the source code, and build changes induce more relative churn on the
> build system than source code changes induce on the source code. Furthermore,
> build maintenance yields up to a 27% overhead on source code development and a
> 44% overhead on test development. Up to 79% of source code developers and 89%
> of test code developers are significantly impacted by build maintenance, yet
> investment in build experts can reduce the proportion of impacted developers
> to 22% of source code developers and 24% of test code developers.

How reliable are results like these?  To find out, [%b Anda2009 %] had
four teams build the same software independently and in parallel so that they
could look at which outcomes were reproducible and which were not:

-   High reproducibility: actual lead time and usability

-   Medium reproducibility: planned development process and cost

-   Low reproducibility: firm price, planned schedule, schedule overrun,
    reliability, and maintainability

<!-- continue -->
Putting something in the "low" category here doesn't mean that it was uniformly
poor.  Instead, it means that there was wide variation, i.e., that results were
unpredictable.  Their results match software engineering folklore, and are a
guide to what research should focus on improving.
  
## What Do We Know About the Psychology of Programming?

Do [%i "programmers!happiness" %]happy programmers[%/i%] produce better code?
If they do, then focusing on their tools may be missing the point: it may be
their environment and colleagues that matter more.  Unfortunately, researchers
haven't yet discovered how to induce happiness, so a randomized controlled trial
isn't an option. Instead, [%b Graziotin2014 %] measured emotional state
using a questionnaire developed by psychology researchers.  They divided up the
study participants into positive and non-positive groups, then looked at how
those groups performed on an analytical task and a creative task.  The positive
group did better at the analytic task, but there was no statistically
significant difference on the creative task.

The [%i "pair programming!effect of personality" %]broader topic of
personality[%/i%] also comes up in discussions of pair programming: do you need
to be an extrovert to reap its benefits, is the contrast in personality with
your peer important, and so on. Several studies have addressed these questions;
[%b Hannay2010 %] is a good place to start reading about them.  As they
say, "We found no strong indications that personality affects pair programming
performance or pair gain in a consistent manner." They go on to suggest that
industry and research should "focus on other predictors of performance,
including expertise and task complexity" instead, as these factors overshadow
any personality effects.

<div class="callout" markdown="1">
### Myers-Briggs and other danger signs

The [%i "Myers-Briggs Type Indicator" "pseudoscience!Myers-Briggs Type Indicator" %][%g myers_briggs "Myers-Briggs Type Indicator" %][%/i%]
advertises itself as personality profiling tool.  It is popular on dating sites
and some companies use it as part of their interview process—despite the fact
that it is complete bullshit.  Half or more of people who repeat the test within
a few weeks get a different personality classification, it fails to predict job
performance, and its categories are based on outdated (and very Western-centric)
psychological theories.  If a potential employer asks you to do it as part of
the interview process, ask them if they would like a horoscope as well.

Myers-Briggs has given the whole notion of personality profiling a bad
reputation, but there are models of personality that have a scientific basis and
are repeatable and cross-cultural.  For example, the [%g ocean_model "OCEAN
model" %] has five dimensions: Openness to experience, Conscientiousness,
Extraversion, Agreeableness, and Neuroticism. Studies of twins and other
research has found that about half of personality variation comes from genetics
and about half from environment, and work like [%b Hannay2010 %] has used
this model in studies of programmers.
</div>

## What Do We Know About Innate Ability?

The most important result in this chapter comes from [%b Patitsas2016 %].
[%i "programming!innate ability" %]Its abstract[%/i%] is worth repeating in
full:

> Although it has never been rigourously demonstrated, there is a common belief
> that CS grades are bimodal. We statistically analyzed 778 distributions of final
> course grades from a large research university, and found only 5.8% of the
> distributions passed tests of multimodality. We then devised a psychology
> experiment to understand why CS educators believe their grades to be bimodal.
>
> We showed 53 CS professors a series of histograms displaying ambiguous
> distributions and asked them to categorize the distributions. A random half of
> participants were primed to think about the fact that CS grades are commonly
> thought to be bimodal; these participants were more likely to label ambiguous
> distributions as bimodal. Participants were also more likely to label
> distributions as bimodal if they believed that some students are innately
> predisposed to do better at CS. These results suggest that bimodal grades are
> instructional folklore in CS, caused by confirmation bias and instructor beliefs
> about their students.

In plain language, if some people are born programmers and others aren't, there
ought to be two humps in the grade distribution. There isn't, but if people
believe some people are "just better" at coding, they're more likely to *see*
two humps. These beliefs matter because they are a self-fulfilling prophecy
[%b Brophy1983 %]: if a teacher believes that student A is more likely to
succeed than student B, they will give student A more attention, which *makes*
them more likely to succeed, which confirms the teacher's bias.

## Where Should We Go Next?

Some of the most interesting work in software engineering today is coming from
people studying how we think when we program and how the ways we think should
shape the tools we build. For example, [%b Johnson2020 %] reverse
engineers the cognitive foundations of user interface guidelines, while
[%b Chattopadhyay2020 %] found that roughly 70% of the actions programmers
later undo could be attributed to [%i "cognitive bias" %][%g cognitive_bias "cognitive bias" %][%/i%].

You don't have to do a PhD to do this kind of research: you can gather and
analyze data on your own, or collaborate with people in academia.  It takes time
and there are frequent setbacks, but the same is true of programming, and being
the first person in the world to understand something is a feeling like no
other.
