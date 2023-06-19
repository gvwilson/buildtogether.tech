Finding errors is good; fixing them is better, so learning how to debug is as
important as learning how to program in the first place.  However, while most
schools teach defensive programming and unit testing, only a handful offer a
course on [%i "debugging!why schools don't teach" %]debugging[%/i%], which is
weird when you consider that most programmers spend anywhere from a quarter to
three quarters of their time finding and fixing bugs.  A single chapter can't
make up for that, but I hope the guidance below will help make you more
efficient.

Debugging depends on being able to read code, which is the single most effective
way known to find bugs [%b Basili1987 Kemerer2009 Bacchelli2013 %].
However, most schools don't offer courses on that either, and of the thousands
of books that have been written about writing code, only a handful have been
written about how to [%i "reading code" %]read[%/i%] it
([%b Spinellis2003 %] being my favorite).  As [%x rules-joining %]
says, reading other people's code is one of the best ways to learn how to be a
better programmer; tracking down a bug may not be when you want to broaden your
knowledge, but if you're there anyway, you might as well.

## Build Habits

Software can fail in many different ways, but the process for diagnosing and
fixing problems is consistent from one bug to the next.  The first rule of
debugging is therefore to make [%i "debugging!importance of good
habits" %]good practices a habit[%/i%].  You are more likely to make mistakes or
overlook things when you're tired or under pressure; if writing assertions and
unit testing aren't automatic by then, the odds are that you'll be at your worst
when it matters most.

What habits should you have?

Make sure you are trying to build the right thing.
:   [%i "requirements error" %][%g requirements_error "Requirements errors" %][%/i%] are a major cause of software projects failing in the real
    world, and every instructor has horror stories about students
    misinterpreting assignments and spending days building the wrong thing. When
    in doubt, ask, and to make your question and its answer clear, provide an
    example and describe what you think the code is supposed to do in that case.

Make sure you understand what the bug actually is.
:   "It doesn't work" isn't good enough: what exactly is going wrong and how do
    you know? If I can't spot a problem in less than a minute, I jot down a note
    to myself like, "shouldn't recurse into footer elements".  Without this, I
    often find myself [%g rabbit_hole "going down a rabbit hole" %] and
    losing sight of what I was originally trying to fix.

    Writing down what's supposed to be happening also helps you check that you
    are actually exercising the problem that you think you are.  Are you giving
    it the right test data?  Is it configured the way you think it is?  Is it
    the version you think it is?  Has the feature actually been implemented yet?
    Are you sure?  Maybe the reason you can't isolate the problem is that it's
    not there—a couple of minutes talking it through with a teammate can save
    you an hour of trying to fix something that isn't actually broken.

Make it fail.
:   You can only debug things when you can see them going wrong, so as we
    discussed in [%x communicate %], you should try to create a minimal
    [%i "reproducible example (reprex)" %]reproducible example[%/i%] or
    reprex.  Doing this finds the problem in a surprising number of cases, since
    each time you throw out part of the original program or dataset because the
    bug reoccurs without it, you are also throwing out a bunch of possible
    causes.

    The easiest way to create a reprex is to divide and conquer.  The [%i "fault" %][%g fault "fault" %][%/i%] responsible for a [%i "failure" %][%g failure "failure" %][%/i%] has to occur before the failure, so check the
    input to the function where the bug is showing up.  If that's wrong, check
    the function that's calling it, and so on.

Instrument your code.
    Add [%i "assertion" %]assertions[%/i%] to make the checks in your code
    explicit: they'll help you keep track of what you have looked at for this
    bug, and if you leave them in, they will help prevent others in future.
    (This is a form of after-the-fact [%i "defensive programming" %]defensive
    programming[%/i%].)

Alternate between exploration and confirmation.
:   I often don't know what assertions to write until I've looked at the state
    of the program, so I go back and forth between adding logging statements (or
    just `print` statements if the code is small and I'm reasonably sure I can
    find the bug quickly) and adding assertions.  [%i "logging!during
    debugging" %]Logging[%/i%] gives me new information to help me formulate
    hypotheses; assertions either confirm or refute those hypotheses.

Change one thing at a time.
:   Replacing random pieces of code in the hope of fixing a bug is unlikely to
    solve your problem: if you got something wrong the first time, what are the
    odds you'll get it right the second?  (Or ninth, or twenty-third?)  Instead,
    change one thing and then re-run your tests to see if the program works,
    breaks in the same way, or breaks in a new way.

    This is another place where version control helps: if you have made a change
    and it hasn't fixed things, `git restore` will put your code back exactly
    the way it was so that you're not trying to fix something that is mutating
    while you work.

<div class="callout" markdown="1">
### Programs concurrent to debug hard are

[%i "concurrent systems!difficult of debugging" "debugging!concurrent
systems" %]Concurrent systems[%/i%] in which many things are happening
simultaneously are much harder to debug than sequential systems.  It's not just
that the order of events is unpredictable; it's often not repeatable, so
creating a reliable reprex may be impossible.  What's worse, the act of
observing can hide the bug: a `print` statement or a breakpoint can change
timing in a way that makes the bug disappear.  Modeling tools can help
([%x tooling %]), as can the use of immutable data structures, but the best
solutions are to test components in isolation using [%i "mock object" %]mock
objects[%/i%] in place of the things they communicate with
([%x testing %]) and to add *lots* of assertions to check the consistency
of data structures.  In particular, giving every class a method called `isOK` to check
that it's in good shape can save hours of later debugging, as well as helping
the next programmer understand what the data is supposed to look like.
</div>

## Common Errors

What mistakes do programmers make [%i "common programming errors" "error!common" %]most often[%/i%]?  The largest study of this for novices is
[%b Brown2017 %], which found that mismatched quotes and parentheses are
the most common type of errors in novice Java programs, but also the easiest to
fix, while some mistakes (like putting the condition of an `if` in `{…}` instead
of `(…)` are most often made only once.  Unsurprisingly, mistakes that produce
compiler errors are fixed much faster than ones that don't.  Some mistakes,
however, are made many times, like invoking methods with the wrong arguments
(e.g., passing a string instead of an integer).

[%b Brown2017 %] also compared [%i "error!misperception of
frequency" %]the mistakes novices actually make[%/i%] with what their teachers
thought they made.  They found that, "…educators formed only a weak consensus
about which mistakes are most frequent, that their rankings bore only a moderate
correspondence to the students in the…data, and that educators' experience had
no effect on this level of agreement."  For example, mistaking `=` (assignment)
and `==` (equality) wasn't nearly as common as most teachers believed.

For experienced programmers, [%b Pritchard2015 %] reported that the most
common errors in Python programs were (in order):

1.  SyntaxError: invalid syntax
1.  NameError: name *name* is not defined
1.  EOFError: EOF when reading a line
1.  SyntaxError: unexpected EOF while parsing
1.  IndentationError: unindent does not match any outer indentation level

<!-- continue -->
while the most common in Java were:

1.  cannot find symbol - variable NAME
1.  ';' expected
1.  cannot find symbol - method NAME
1.  cannot find symbol - class NAME
1.  incompatible types

Complex errors are one of a kind: that's part of what makes them complex.  But
some simple errors crop up again and again, and you can use those patterns as a
checklist for finding problems.  A useful initial checklist for novices'
programs includes:

Numbers
:   Zero; smallest number; smallest magnitude; most negative; largest number;
    off by one in a loop.

Structure Errors
:   `null`; empty string; empty collection; contains exactly one element;
    contains maximum number of elements; has duplicate elements; contains one
    element multiple times.

Searching
:   Match not found; matching element not present; matching element just outside
    search range; exactly one match found; match element on search boundary;
    multiple matches found; multiple references to a single object found; all
    objects match.

Trees and graphs
:   Empty; minimal non-empty (e.g. tree with just root); circular;
    self-referential (head points to head); circular sub-structure; depth
    greater than one.

<!-- continue -->
As [%x git-team %] said, the longer list in
[%b Stegeman2014 Stegeman2016 %] can be adapted for more advanced
students' programs.

One of the most common errors programmers make is to assume that their first
attempt at fixing a problem actually worked.  [%b Yin2011 %] found that
14--25% of bug "fixes" released for major operating systems didn't actually fix
the bug (a figure that rose to 39% for concurrency-related bugs), while
[%b Park2012 %] found that up to a third of bugs required more than one
attempt to fix.

But there is good news as well.  [%b Pan2008 %] identified 27 patterns for
bug fixes by inspecting the history of seven large open source Java projects and
found that the five most common are:

1.  changing the condition in an `if` statement (e.g., replacing `==` with `>=`
    or vice versa);

1.  adding a pre-condition check to an `if` statement (e.g., checking that a
    variable is not `null` before comparing its value to a constant);

1.  changing the values passed to a method call (e.g., converting a
    case-sensitive string match to a case-insensitive match);

1.  changing the number of parameters to a method call (e.g., adding a
    non-default value for a parameter where the default value was previously
    being used); and

1.  changing the value assigned to a variable *without* changing the variable
    being assigned to.

Wherever we find patterns we can try to write programs to spot them and act on
them.  The goal of research in [%i "automated program repair" %][%g automated_program_repair "automated program repair" %][%/i%] is to build tools that can fix
common bugs on their own [%b Monperrus2018 LeGoues2019 %].  These tools
use several approaches:

Generate and validate.
:   Given a set of test cases and a set of rules for modifying programs (e.g.,
    adding or removing checks for empty lists in `if` statements), a tool can
    generate a mutated version of a program and see if it still fails or not.

Machine learning.
:   Given a large enough set of bugs and bug fixes to learn from, machine
    learning algorithms can be trained to match problem with solutions based on
    past experience.  This approach still requires test cases to validate
    particular changes.

Symbolic execution.
:   Rather than a program on a particular set of inputs, a tool can simulate
    execution to build constraints, then check if those constraints can be
    satisfied. For example, if a program contains the statements:
    ```py
    longest = ''
    for name in all_names:
        if len(name) > len(longest):
            longest = name
    ```
    then symbolic execution can determine that the final value of `longest` is
    either the empty string or the first string in the list that belongs to the
    set containing the longest strings in the list.  The complexity of that
    sentence is a sign of how complex symbolic execution can be, but when
    combined with the modeling tools discussed in [%x tooling %], this
    approach can find bugs that would otherwise escape detection for years.

Most [program repair tools][program-repair] are still research prototypes, but
one particularly interesting use case is repairing student programs as a way of
giving feedback on assignments [%b Hu2019 %].  If you are looking for an
ambitious course project that might lead to graduate research, this is a good
place to start.

Another semi-automated technique for finding bugs is [%i "delta debugging" %][%g delta_debugging "delta debugging" %][%/i%] [%b Zeller2009 Zeller2021 %].
[%i "fuzz testing" %]Fuzz testing[%/i%] can automatically generate inputs
that make programs fail ([%x testing %]), but since those inputs are partly
or entirely random, and can be quite long, it is sometimes hard to figure out
why they make the software fail.  Delta debugging repeatedly tests subsets of
the original fixture, then subsets of those subsets, to produce a minimal
[%i "reproducible example (reprex)" %]reprex[%/i%].

## Using a Debugger

The tools described above will make you more productive, but sooner or later
you're going to have to track a bug down yourself.
A [%i "debugging!symbolic debugger" "symbolic debugger" %][%g symbolic_debugger "symbolic debugger" %][%/i%]
is a program that allows you to
control and inspect the execution of another program. Some, like [GDB][gdb], are
standalone programs; others are built into IDEs, but they all have the same
basic capabilities.  (Depending on the language you're using, you may have to
compile or run your program with specific options to make it debuggable.)

[%i "breakpoint" "debugger!breakpoint" %][%g breakpoint "Breakpoints" %][%/i%].
:   You can tell the debugger to pause the program whenever it reaches a certain
    line.  You can also create a [%g conditional_breakpoint "conditional
    breakpoint" %] that only pauses on that line if some test is true, e.g.,
    if a list is empty or a loop index is zero.

Inspection.
:   While the program is paused, you can ask the debugger to show you the values
    of variables in both the current active function call and in the call stack.
    This is why we use the word "symbolic": instead of displaying the bytes at
    particular addresses in memory, the debugger uses the names you wrote.

[%i "single-stepping" "debugger!single-stepping" %]Single-stepping[%/i%].
:   Rather than requiring you to set breakpoints on several successive lines,
    the debugger allows you to step through the program a line at a time to see
    which branches of `if`/`else` statements are taken or how the values of
    variables change.  You can also tell it to step into function calls or just
    step over them so that you can stay focused on one particular problem.

Using a debugger generally takes less time than adding `print` statements to
your program and re-running it.  It's also very easy to make a mistake in the
`print` statement: few things are as frustrating as wasting an afternoon
debugging a problem, only to realize that the `print` you copied and pasted
isn't displaying the values you thought it was.

That said, a page or two of printed output showing which functions are being
called and what state the data is in at the start and end of each can be less
[%i "cognitive load!in debugging" %]cognitive load[%/i%] than holding that
same information in your head while stepping through the program's execution.
Again, if you *are* going to print things, using a [%i "logging!during
debugging" %]logging[%/i%] library to give yourself more control.

<div class="callout" markdown="1">
### If it was important, it would be on the exam

Over the years I've been surprised by how few programmers know how to use a
debugger [%b Beller2018 %]. The reason can't be the five or ten minutes it
takes to learn how to use one—that pays for itself almost immediately.  The
best explanation I've been able to come up with relates to [%i "Goodhart's
Law" %][Goodhart's Law][goodhart-law][%/i%], which says that as soon as you use
some measure to evaluate people it ceases to be a good measure because people
will start to game the system.

The inverse of that is that if something *isn't* being evaluated, it isn't
important—or rather, if you're juggling five or six courses, you can't afford
to put time into things that aren't going to affect your grades.  Most students
have to learn version control because it's the only way to submit their work,
but "show that you can use the debugger" is (almost) never part of gradable
work.  As a result, there's no point at which students have to master it.  I
think this could now be fixed by having students submit screencasts of
themselves setting breakpoints, inspecting variables, and so on; if you ever try
this in your class, please let me know how it goes.
</div>
