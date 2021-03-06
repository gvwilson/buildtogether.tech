---
---

A carpenter shows up to put an extension on your house, and all she's brought
with her is a hammer and a Swiss army knife. How confident are you that she'll
do the job well?  A programmer shows up to fix a couple of bugs and add a new
splash screen to your game, and all she's going to use are a plain-text editor
and `print` statements. Are you any more confident?

Tools don't just help us do things more easily; they shape what we consider
possible and encourage some working practices while discouraging others. They
also advertise how seriously we take our craft: people who want to be good at
something are willing to invest time in learning how to do it better. In
programming, that means mastering new tools and the practices that go with them.

I actually believe that processes are more important than tools, but that's
because I know how to use whatever tools I have to support the working
practices I think are most productive. However, I focus on tools when talking to
students because they are are more tangible: it's easier to tell if someone is
using version control or a style checker than it is to tell if they're designing
or estimating sensibly.

So here, in more-or-less priority order, are the tools you should learn *after*
you are comfortable with version control and a unit testing framework.

<div class="callout" markdown="1">

### If you'd rather not…

If you'd rather not improve your tools, but are afraid that someone on your team
might want to do so, <cite>Farmer2006</cite> is a not-entirely-serious guide to
preventing something new from being adopted.

</div>

## Programming Language

You may not get to choose what programming language you use for your project,
but it may be the most important choice there is.  Programmers have fought
religious wars over what's language is best for as long as there have *been*
programmers. In my experience, which one you use makes a lot less difference
than most people think…

…as long as you use the right one, that is. Twenty years ago there was a pretty
clear tradeoff between how quickly you can get a program running and how fast it
ran. <span g="interpreted_language">Interpreted languages</span> like Perl
optimized programmers' time; <span g="compiled_language">compiled
languages</span> like C optimized the machine's.

Today, the balance has shifted in favor of higher-level languages. One reason is
that processors have gotten faster but people haven't, so one programmer-hour is
worth many more computer-hours than before. Another reason is that <span
g="jit">just-in-time compilers</span> (JITs) and <span
g="generational_garbage_collection">generational garbage collection</span> have
made higher-level languages intrinsically faster. The biggest, though, is that
the execution time of a modern application depends less on squeezing cycles out
of processors than it used to. The bottleneck in a web site is almost always
network latency or the time required to perform database operations; your code
probably accounts for only a few percent of the total, so doubling or tentupling
its speed has less effect than you'd think.

That said, there are three things to keep in mind:

Some languages are easier to learn than others.
:   <cite>Stefik2013</cite> did a controlled experiment to see how quickly
    people could learn to recognize correct and incorrect syntax in several
    different languages. They found that <span
    g="curly_brace_language">curly-brace languages</span> like Java and Perl
    were as hard for people to learn as a language with a randomly designed
    syntax. (They really did roll *Dungeons & Dragons* dice to pick random names
    and characters for a made-up language as an <span
    g="experimental_control">experimental control</span>.) Other languages like
    [Ruby][ruby] and [Python][python] were significantly easier to learn, and
    they are now building a language called [Quorum][quorum] by testing the
    usability of every language feature.

Strong typing helps, but only a little.
:   A <span g="strong_typing">strongly-typed</span> language like Java requires
    programmers to specify the data type of each variable; a <span
    g="dynamic_typing">dynamically-typed</span> one like Python doesn't.
    <cite>Endrikat2014</cite> found that declaring types does add complexity to
    programs, but it pays off fairly quickly by acting as documentation and by
    making <span g="auto_completion">auto-completion</span> more accurate.

The most important thing about a language is its community.
:   Some programming communities work hard to welcome newcomers and treat
    everyone respectfully. Others are more likely to call naïve questions
    "stupid" or to make excuses when their leaders harass people. (Looking at
    you, Linux…) As a junior programmer, you will learn more from the former
    than from the latter.

<cite>Stefik2017</cite> is a good short summary of what we know and why we
believe it's true. If someone disagrees with it, ask them to show you their
evidence.

## Integrated Development Environment

You are going to spend a lot of time editing code, documentation, and reports,
so choosing a good editor is as important as choosing a comfortable chair.
There are literally thousands to consider, from very small plain-text editors
such as Notepad (which comes with Windows) to very large ones like Emacs (which
some people claim is actually Lisp-based operating system in disguise).

<div class="callout" markdown="1">

### Punchcards once again

As we noted in <span x="using-git"></span>, programming is still stuck in the
punchcard era: we still insist that source code be represented as lines of
characters that are drawn one-for-one on the screen.  <span
g="wysiwyg">WYSIWYG</span> editors like Microsoft Word did away with this model
decades ago; they store the file in a machine-friendly format and then render it
in a human-friendly way. There's no reason we couldn't do the same with
programs.  There's no reason we shouldn't be able to draw a diagram directly in
our source code like we can in a Google Doc.

</div>

You might already have a favorite editor. If you're like most programmers, you
will change jobs, languages, operating systems, and nationality before you'll
switch to another, because it has taken weeks or months for your hands to master
the current one. However, if it is not an <span g="ide">integrated development
environment</span> (IDE) that combines an editor with other programming tools
then getting work done will take longer and hurt more than it needs to.

IDEs were invented in the 1970s, but didn't really catch on until Borland
released Turbo Pascal in the 1980s.  They usually include these tools:

-   A <span g="console">console</span> so that you can type in expressions or call
    functions and see the results without having to start (or restart) your
    program.

-   A <span g="style_checker">style checker</span> that can warn you when your
    code doesn't meet naming and indentation conventions.

-   A <span g="code_browser">code browser</span> that helps you navigate the
    packages, classes, methods, and data in your program.

-   A <span g="gui_designer">GUI designer</span> that lets you build GUIs by
    dragging and dropping components;

-   A <span g="test_runner">test runner</span> to display the results of tests and
    let you jump directly to ones that have failed. This is usually a GUI built
    on top of whatever unit testing framework you are using, just as graphical
    interfaces for version control are usually built on top of the command-line
    tools.

-   A <span g="build_manager">build manager</span> that will recompile your code
    or re-run tasks as needed.

-   Some refactoring tools to help you reorganize your code.  For example, instead
    of searching and replacing strings, an IDE can parse your source code and
    look for all uses of a class name in order to replace it with a new one, or
    move a method from one class to another.

The most popular IDE today is probably [Microsoft Visual Studio Code][vs-code],
often referred to simply as "VS Code".  Along with all the tools above, it has
hundreds of <span g="plugin">plugins</span> of varying quality to support
database design, reverse engineering, dozens of different programming languages,
and more.  These all make you more productive than their disconnected
counterparts. Since most of these store project data (including build
instructions) in a proprietary format, your team will do much better if you all
adopt the same IDE. This will also let you help one another solve problems and
share plugins.

<div class="callout" markdown="1">

### Refactoring

To <span g="refactoring">refactor</span> code means to change its structure
without changing what it does <cite>Fowler2018</cite>.  It is just as much a
part of programming as writing code in the first place: nobody gets things right
the first time <cite>Brand1995</cite>, and needs or insights can change over
time.

Some common refactoring patterns include "hoist repeated calculation out of
loop" and "replace repeated test with flag". As <cite>Kerievsky2004</cite>
showed, many refactorings make code fit a design pattern or move code from one
design pattern to another. If changes that fit these patterns are easy to make,
your design is probably a good one.

</div>

## Build Manager

No matter what language you use, you're going to need a build manager---a tool
that will transform what you've typed into what you want to deliver. The
best-known build manager in the Unix world is [Make][make], which was invented
in 1975 by a summer intern at Bell Labs. To use Make, you create a Makefile that
specifies the dependencies between the files in your project and the commands
needed to update them. For example:

```make
game.exe : game.bc graphics.bc utils.bc
        tx -E -o game.exe game.bc graphics.bc utils.bc

%.bc : %.grace
        tx -C $<
```

{: .continue}
tells Make that `game.exe` can't be built until `game.bc`, `graphics.bc`, and
`utils.bc` exist, and that once they do, the way to create `game.exe` is to run
the `tx` compiler with several options.  Below that is a <span
g="pattern_rule">pattern rule</span> telling Make how to create any `.bc` file
from a `.grace` file with the same root name; the cryptic expression `$<` is
Make's way of saying "the first thing the target depends on".

Make has been used by hundreds of thousands of programmers for more than thirty
years, but has some fundamental flaws. The first is its syntax, which looks like
something produced by a cat dancing on the keyboard. The second is that it runs
commands by handing them over to whatever operating system it is running on,
which make portability a constant headache. (Quick, should you use `rm` or `del`
to delete a file?) Third, Make doesn't have a debugger: the only way to track
down problems in your build configuration is to stare at the configuration file
until little drops of blood form on your forehead.

I could live with ugly syntax---if Ie kan lurn Inglish speling, Ie kan lurn
eneething. But the lack of a debugger is a never-ending headache, because real
build systems aren't just configured: they're programmed. Take this book, for
example: its Makefile checks the consistency of cross-references and glossary
entries, makes sure all the bibliography citations are in place, and copies
files to my web site, and is more complex than many programs I've
written. Thinking of it as a "configuration" file is a mistake: you *have* to
approach system builds as a programming problem.

The current generation of build managers dispense with custom configuration file
syntaxes and use the data structures of dynamic languages like Python and
Ruby. [Snakemake][snakemake] and [Rake][rake] are examples of such a system: its
users write their "configurations" as small Python or Ruby programs, making use
of an extensive support library that handles dependencies, invokes appropriate
compilers, and so on.  Debugging is still problematic, but at least it's
possible.

Whatever you choose (or are told to use), stick to the following rules:

Pick something that plays nicely with your other tools.
:   For example, most Java editors and IDEs integrate with a build tool called
    [Ant][ant], which means they can jump directly to compilation errors when
    they occur.

Always use the build manager---never compile or copy things by hand.
:   This isn't just for efficiency's sake: if any of the twelve things you need
    to do to get your application up on your web site have to be done by hand,
    the odds are that you'll forget a crucial step right before your end-of-term
    demo, and wind up looking silly.

Always use the build manager---never compile or copy things by hand.
:   Yes, I'm repeating myself, but this time the reason is different. If you do
    something by hand, one of your teammates might do it differently.  "But it
    works on my machine!" isn't something you want to hear an hour before a
    deadline…

A good way to start using a builder is to create a "version zero" of the
project. Set up the build and make sure it works even when there isn't anything
to compile, run, test, or copy. Now add something---anything.  Does the build
still work? If it does, you're on your way.

Once you've got that, never check anything into version control that breaks the
build. This is one of the golden rules of working in a team: if your code won't
compile, or doesn't pass whatever automated tests you have, then putting it into
the repository means putting every other person on your team into exactly the
same broken state you're in. When you're working on your own, it's OK to use
version control as a way to transfer files from one machine to another, or as a
way to back things up at the end of the day. Do *not* carry this habit over to
teamwork.

## Debugger

A <span g="symbolic_debugger">symbolic debugger</span> is a program that allows
you to control and inspect the execution of another program. You can step
through the target program a line at a time, display the values of variables or
expressions, look at the call stack, or (my personal favorite) set *breakpoints*
to say "pause the program when it reaches this line" . Depending on the language
you're using, you may have to compile your program with certain options turned
on to make it debuggable, but that's a small price to pay for the hours or days
a debugger can save you when you're trying to track down a problem.

Some debuggers, like GDB, are standalone programs; others are build into IDEs.
Both are better than adding `print` statements to your program, recompiling it,
and re-running it because:

-   adding `print` statements takes longer than clicking on a line and setting a
    breakpoint;

-   adding `print` statements distorts the code you're debugging by moving things
    around in memory, altering the flow of control, and/or changing the timing
    of thread execution; and

-   it's all too easy to make a mistake in the `print` statement---few things are
    as frustrating as wasting an afternoon debugging a problem, only to realize
    that the `print` statement you copied and pasted isn't displaying the values
    you thought it was.

A company I used to work for never hired people immediately. Instead,
prospective employees were put on a three-month contract.  Two things meant
automatic disqualification: checking broken code into version control and using
`print` statements instead of a symbolic debugger. The first was justified
because we didn't want to hire people who put themselves ahead of their
teammates. The second was justified because we didn't want to hire people who
were too stupid or stubborn to program efficiently.

Over the years, I've been surprised by how few programmers know how to use a
debugger <cite>Beller2018</cite>. The reason can't be the five or ten minutes it
takes to learn how to use one---that pays for itself almost immediately.  The
only explanation I've been able to come up with is that some people *enjoy*
being inefficient.  Typing in `print` statements and paging through screens of
output lets them feel like they're being productive, when in fact they're just
being busy (which isn't the same thing at all). If your brain needs a break
(which it sometimes will), then take a break: stretch your legs, stare out a
window, practice your juggling, or do whatever else you can to take your mind
away from your problem for a few minutes. Don't drag out the process of finding
and fixing your bug by using sloppy technique just to let your brain idle for a
while.

And by the way: if you're allowed to choose your teammates at the start of the
course, treat it like a job interview. Ask the people you think you might want
to work with whether they use a debugger. If they say "no", ask yourself what
impact that's going to have on your grade in the course…

## The Next Level

You and your teammates could use many other tools to make yourselves more
productive. Some aren't part of the standard undergraduate curriculum yet, even
though good developers have been relying on them for a decade or more. Others
may be touched on, but only briefly, so a quick recap won't hurt.

The first is a <span g="doc_generator">documentation generator</span> like
[JSDoc][jsdoc]. This is a compiler of a sort, but instead of translating source
code into something executable, it extracts information from specially-formatted
comments and strings, and turns it into human-readable documentation.  The
justification for this is that when code and documentation are stored
separately, programmers won't keep the latter up to date. Since "rusty"
documentation can be worse than no documentation at all, it makes a lot of sense
to keep the source of the documentation right beside the code. Many introductory
courses require students to document their packages, classes, and methods this
way; it's a good habit, and one you should cultivate.

Along with testing frameworks, *style checkers* have become a lot more popular
since the turn of the century. Early style checkers looked at code to make sure
that it obeyed formatting rules, such as "no method can be longer than 100
lines" or "class names must be written in CamelCase". Today's, like PMD and
CheckStyle, can do a lot more: they can find code that is never called,
parameters that are never used, duplicated code that could be factored out, and
a lot more.

Style checkers are more properly called *static analysis* tools, since they work
by parsing the source code for your programs and looking for patterns that might
indicate problems. Compilers also do a lot of static analysis; the non-fatal
warnings they produce are a lot more useful than many students realize, and a
"zero warnings" policy can prevent a lot of subtle bugs.

Another class of tools uses *dynamic analysis*: they watch your program run, and
look for things like memory leaks, or inconsistent locking that might lead to
deadlocks or race conditions. FindBugs is the best-known in the Java world; the
Valgrind toolset is a lifesaver if you're using C or C++.

All of these tools will do a lot more for you if you adopt some kind of <span
g="ci">continuous integration</span> system such as [Travis CI][travis-ci] or
[GitHub Actions][github-actions].  These can be set up to run either at regular
intervals (e.g., every hour or at three a.m.), or every time someone checks into
version control (which I find more useful). Each time they run, they check a
fresh copy of the project out of version control, build it, re-run all the
tests, and post the results to the project's blog, web site, and mailing list.

Research has proven the benefits of CI <cite>Hilton2016</cite>.  It acts as a
"heartbeat" for the project: as soon as anything goes wrong, everyone knows. It
also encourages good development practices: if someone checks something in that
doesn't compile, run, or pass the project's tests, everyone will know very
quickly. (Funnily enough, after the system has shamed you a couple of times,
you'll stop checking in broken code…) <cite>Zampetti2020</cite> looks at how
*not* to use CI, and can serve as a good checklist of things to avoid.

Real development projects rely on a lot of other tools as well: schedule
builders like Microsoft Project, requirements tracing tools, visual editors for
GUIs and class diagrams, and so on. Most are bigger hammers than undergraduate
projects really require (except possibly the GUI editors), so I'd like to close
this section by asking you to invest some time in something else:
scripting. Good programmers don't just use tools, they build them. I have dozens
of small programs in my `tools` directory that do things like update my working
copies of all the projects I'm involved in or check whether the links to Amazon
in my course notes are still valid. Anything worth doing repeatedly is worth
automating; if you and your teammates find yourselves typing in the same
commands over and over again, *write a program to do it for you*. And please,
use a language like Python or Ruby rather than Java or C#: the "try it and see"
nature of the former is a lot better suited to one-of-a-kind scripts than the
latter's type checking and compilation.

<div class="callout" markdown="1">

### Building for everyone

Close your eyes and try to navigate this website. Now imagine having to do that
all day, every day. Imagine trying to use a computer when your hands are
crippled by arthritis.  Better yet, don't imagine it: have one of your teammates
tape some popsicle sticks to your fingers so you can't bend them and then see
how easy it is to use video conferencing software.

Making software accessible doesn't just help people with obvious disabilities:
as <cite>Johnson2017</cite> points out, the population is aging, and everything
you do to help people who are deaf also helps people who are gradually losing
their hearing. Tools like [WebAIM WAVE][webaim-wave] are easy to use, and most
of the problems they identify are easy to fix. It only takes a few minutes, and
it's the compassionate thing to do.

</div>

## You May Also Enjoy…

A complete working environment needs more than just software.
Unfortunately, most university labs seemed designed to make everything
below difficult or impossible to achieve.

Peace and quiet.
:   Study after study has proved that this has more impact on productivity than
    a fast network, a fat disk, or caffeine, but most workplaces are still too
    crowded, too noisy, and filled with too many interrupts. As mentioned
    earlier, it takes most people ten minutes to get back into a state of flow
    after being distracted, which means that half a dozen interruptions per hour
    effectively renders someone zero percent effective. I know people say, "If I
    can't overhear what other people are talking about, I might miss something
    important," but that only applies if the only people you're overhearing are
    members of your own team (and even then, it's a dubious claim).

Comfortable seating.
:   A good chair with a firm back costs half what a mid-range laptop does. A
    full-sized keyboard (I have large hands---most laptop keyboards force me to
    bend my wrists uncomfortably) costs fifty dollars, and a lamp with a
    soft light bulb is another forty. The combination doesn't just let me
    program longer each day; it also helps ensure that I'll still be able to
    program five or ten years from now without chronic back and wrist
    pain. Compare this with what's in most computer labs: their lighting gives
    glare without illumination, the dark desktops make the optical mice jerky,
    and the low-budget chairs are guaranteed to make your lower back ache after
    an hour.

A pad of gridded paper and several ballpoint pens.
:   I often make notes for myself when programming, or draw box-and-arrow
    diagrams of my data structures when debugging. I used to keep an editor open
    in a background window to do the former, but when my wrists started acting
    up, I discovered that taking my hands away from the keyboard for a few
    moments to scribble something down provided welcome relief. I also quickly
    discovered that the odds of me being able to read my own notes the next day
    rose dramatically if I used gridded paper to line them up.

A heavy mug for coffee or tea.
:   I don't know why, but a styrofoam cup, or a normal teacup, just isn't as
    satisfying as a little hand-sized ceramic boulder. Maybe it satisfies my
    subconscious Neanderthal urge to club my computer to death when it
    misbehaves…

A rubber duck.
:   One of the creators of Unix kept a rubber duck next to his
    computer. Whenever a bug took more than a few minutes to track down, he put
    the duck on his desk and explained the problem to it. Why? Because speaking
    out loud forces you to marshal your thoughts, which in turn highlights any
    contradictions or missed steps that you hadn't noticed while everything was
    just swirling around inside your head.

A squirt bottle of glass cleaner and a box of kleenex.
:   I can't stand smears on my screen. They drive me nuts. Whenever I'm showing
    something to someone, and they actually *touch my screen* instead of just
    pointing, I find myself reaching for that heavy mug… Then I take a breath
    and clean my screen.

A chess set, or a deck of cards, or some knitting.
:   I'm a very bad chess player. Luckily, so are most people, so it's usually
    possible to find someone at my level for a ten-minute game at lunch.  Other
    programmers I know play euchre, or knit---a programmers' "stitch and bitch"
    session can be jaw-dropping to listen to. Few people can focus for more than
    a few hours before their productivity drops; it's better to acknowledge
    this, and take a break in the middle of the day, than to say, "Must… keep…
    coding…" and produce garbage that just has to be rewritten later.

A yoga mat.
:   Back when I was a part-time grad student, I had a settled routine: I brought
    three sets of gym gear to the office at the start of the week, worked out at
    lunchtime on Monday, Wednesday, and Friday, and took my stuff home at the
    end of the week. After two months of this, I came in to find that my
    co-workers had hung a little chandelier made of air fresheners over my
    desk. Since then, I've rented a locker at the gym, but I still try to get
    some exercise several times a week---it helps my concentration and stamina a
    lot more than any amount of coffee..

Pictures.
:   Everyone wants to feel at home; everyone wants to make wherever they are
    uniquely theirs. I hang a few postcards on the wall wherever I work, along
    with a photograph of my wife and daughter taken a few months after she was
    born (my daughter, that is), just to remind me what's really important.
