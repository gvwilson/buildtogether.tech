---
title: Testing
---

A friend of mine once told me that she could write any application I wanted in
under a minute, as long as I didn't insist that it actually work. Her point was
that software is only done when it works well enough to be used.  It doesn't
have to be perfect—every non-trivial program has a few bugs, and most trivial
ones do too—but if you care at all about your users (and your own reputation)
you will do what you can to minimize these.

That's not the only reason to test, though. As we'll see below, designing
programs so that they *can* be tested makes them easier to understand and
modify, which in turn makes the next piece of work easier to tackle.

## Unit Testing

As the name suggests, a [%i "unit test" %][%g unit_test "unit test" %][%/i%]
checks the correctness of a single unit of software.  Exactly what constitutes a
"unit" is subjective, but it typically means the behavior of a single function
or method in one situation.

A unit test will typically have:

-   A [%i "fixture (in unit test)" "unit test!fixture" %][%g fixture "fixture" %][%/i%], which is the thing being tested (e.g., an
    array of numbers). The fixture is typically a subset or smaller version of
    the data the function will typically process. In fact, it should be a reprex
    ([%x communicate %]), i.e., exactly the same kind of minimal example
    you would post online if you were asking for help.

-   An [%i "actual result (in unit test)" "unit test!actual result" %][%g actual_result "actual result" %][%/i%], which is what the code produces when given the
    fixture.

-   An [%i "expected result (in unit test)" "unit test!expected result" %][%g expected_result "expected result" %][%/i%] that the actual result is
    compared to.

Good programmers often run informal unit tests interactively when debugging
([%x tooling %]), but they are much more valuable when they can be re-run
at a moment's notice to make sure that the most recent changes haven't broken
anything that was working a few minutes ago.  To do this, you can use a [%i "test framework" "unit test!test framework" %][%g test_framework "test framework" %][%/i%] (also called a [%i "test runner" %][%g test_runner "test runner" %][%/i%]).  Dozens of these have been built for almost every language you
can think of; most are very similar because they were inspired by the same
forerunners. The most widely-used test framework for Python is called
[`pytest`][pytest], which structures tests like this:

1.  Tests are put in files whose names begin with `test_`.
2.  Each test is a function whose name also begins with `test_`.
3.  These functions use `assert` to check results.

The `pytest` library comes with a command-line tool that is also called
`pytest`.  When it runs, it searches for all files in or below the working
directory whose names match the pattern `test_*.py`.  It then runs the test
functions it finds in these files and summarizes their results.

If running all the tests is taking so long that it's disrupting your [%i "flow" %]flow[%/i%] ([%x important %]), you can give `pytest` (and other
test runners) arguments to specify which subset of tests to run. This speeds up
development, but you should always re-run the entire [%i "test suite" "unit test!test suite" %][%g test_suite "test suite" %][%/i%] before committing your
changes to version control. If the tests reveal that the change you have just
made to one part of a program unexpectedly affects some other part, it's a sign
that you should change your design to remove that long-range interaction: sooner
or later (probably sooner) it will break again, and you may not catch it the
second time around.

<div class="callout" markdown="1">
### Fuzzing

In 1988, a professor teaching a class on operating systems decided to throw
randomly-generated strings at standard Unix command-line utilities
[%b Miller1990 %].  To their surprise, the students were able to crash
almost a third of the programs they tested, some of which had been in daily use
for two decades.

While they weren't the first people to test with random data, their results
sparked interest in [%i "fuzz testing" "unit test!fuzzing" %][%g fuzz_testing "fuzz testing" %][%/i%]
(or "fuzzing" for short), which is now a
standard part of most testers' repertoire [%b Zeller2019 %].  Despite
this, [%b Miller2020 %] found that thirty years later, programs are still
failing at about the same rate and for the same reasons.  [%x debugging %]
discusses a technique for making fuzz testing even more useful.
</div>

## Design for Testability

When most developers hear the word "design", they think about either the
application's structure or its user interface. If you don't think about how
you're going to test your application while you're designing it, though, the
odds are very good that you'll build something that cannot (or cannot easily) be
tested.  Conversely, if you [%i "design for test" "unit test!influence on software design" %][%g design_for_test "design for test" %][%/i%], it'll be a lot easier
to check whether your finished application actually does what it's supposed to.

Thinking about testability from the start turns out to be a good [%i "software design!influence of testability" "testability!influence on software design" %][%g heuristic "heuristic" %][%/i%] for design in general
[%b Feathers2004 %], since it forces you to think in terms of small
components with well-defined interfaces. Not only can these be tested more
easily, they can also be modified or replaced in isolation, which significantly
reduces the probability of requiring rework in the naïve model presented at the
start of this chapter.

For example, let's consider a typical three-tier web site that uses the [%i "model-view-controller architecture" %][%g mvc "Model-View-Controller" %][%/i%]
(MVC) [%i "design pattern!model-view-controller" %][%g design_pattern "design pattern" %][%/i%]. The model, which is stored in a relational database, is the data
that the application manipulates, such as purchase orders and game states. The
controller encapsulates the application's business rules: who's allowed to
cancel games while they're in progress, how much interest to add on
out-of-province orders, and so on.  Finally, the view translates the
application's state into HTML for display and handles the button clicks and form
submissions that drive the system from one state to another.

<div class="callout" markdown="1">
### Design patterns help

Design patterns were a hot topic in the 1990s and early 2000s, and while there
isn't as much excitement about them now, their value has not diminished.
Knowing some design patterns is like knowing chord progressions in music: it
gives you a larger mental toolkit to work with.  [%b Tichy2010 %]
summarizes some of the evidence, more recent studies like [%b Krein2016 %]
confirm it, and books like [%b Olsen2007 Nystrom2014 Casciaro2020 %] are
great places to get started.
</div>

The MVC architecture presents several [%i "model-view-controller
architecture!testing" %]challenges for testing[%/i%]:

Unit testing libraries are designed to run within a single process.
:   As the word "library" implies, they're made up of code that's meant to be
    loaded into a single running program. Most debuggers and testing libraries
    don't track interactions *between* processes.

Configuring a test environment is a pain.
:   You have to set up a database server, clear the browser's cache, make sure
    the right clauses are in your web server's configuration file, and so on.

Running tests is slow.
:   In order to ensure that tests are independent, you have to create an
    entirely new fixture for each test. This means reinitializing the database,
    restarting the web server, and so on, which can take several seconds per
    test. That translates into an hour or more for a thousand tests, which is
    pretty much a guarantee that developers won't run them routinely while
    they're coding, and might not even run them before checking changes in.

The first step in fixing this is to get rid of the browser and web server. One
way to do this is to replace the browser with a script that generates HTTP
requests as multi-line strings and passes them via a function call to a library
that does whatever the web server's HTTP handler would do. After invoking our
actual program, this library passes the text of an HTTP response back to our
script, which then checks that the right values are present (about which more in
a moment). The library's job is to emulate the environment the web app under
test would see if it was being invoked by the real server: environment variables
are set, standard input and output are replaced by [%i "string I/O" %][%g string_io "string I/O" %][%/i%] objects, and so on, so that the application has no (easy)
way to tell how it's being invoked.

Why go through this rigmarole? Why not just have a top-level function in the web
app that takes a URL, a dictionary full of header keys and values, and a string
containing the POST data, and check the HTML page it generates? The answer is
that structuring our tests in this way allows us to run them both in this test
harness, and against a real system. By replacing the fake HTTP handler with code
that sends the HTTP request through a socket connected to an actual web server,
and reads that server's response, we can check that our application still does
what it's supposed to when it's actually deployed. The tests will run much more
slowly, but that's OK: if we've done our job properly, we'll have caught most of
the problems in our faked environment, where debugging is much easier to do.

Now, how to check the result of the test? We're expecting HTML, which is just
text, so why not store the HTML page we want in the test and do a string
comparison? The problem with that literal approach is that every time we make
any change at all to the format of the HTML, we have to rewrite every test that
produces that page. Even something as simple as introducing white space, or
changing the order of attributes within a tag, will break string comparison.

A better strategy is to add unique IDs to significant elements in the HTML page,
and only check the contents of those elements. For example, if we're testing
login, then somewhere on the page there ought to be an element like this:

```html
<div id="currentuser">Logged in as <strong>marian</strong>
(<a href="http://www.example.org/logout">logout</a>
|
<a href="http://www.example.org/preferences">preferences</a>)
</div>
```

We can find that pretty easily with a [%i "CSS selector!use in testing" %][%g css_selector "CSS selector" %][%/i%] that looks for a `div` with the ID
`currentuser`.  We can then move the `div` around without breaking any of our
tests; if we were a little more polite about formatting its internals (i.e., if
we used something symbolic to highlight the user name and trusted CSS to do the
formatting), we'd be in even better shape.

We've still only addressed half of our overall problem, though: our web
application is still talking to a database, and reinitializing it each time a
test runs is slow.  We can solve this by moving the database into memory. Most
applications rely on an external database server, which is a long-lived process
that manages data on disk. An alternative is an [%i "embedded database!use in testing" %][%g embedded_database "embedded database" %][%/i%], in which the
database manipulation code runs inside the user's application as a normal
library; [SQLite][sqlite] is probably the best known of these.

The advantage of using an embedded database from a testing point of view is that
it can be told to store data in memory, rather than on disk. This would be a
silly thing to do in a production environment (after all, the whole point of a
database is that it persists), but in a testing environment, an [%i "in-memory database!use in testing" %][%g in_memory_database "in-memory database" %][%/i%] can speed things up by a factor of thousands, since the hard
drive never has to come into play. The cost of doing this is that you have to
either commit to using one database in both environments, or avoid using the
"improvements" that different databases have added to SQL.

A third choice is to replace the database with a [%i "mock object" %][%g mock_object "mock object" %][%/i%].
A mock object has the same interface as the
function, object, class, or library that it replaces, but is designed to be used
solely for testing.  For example, Node's `mock-fs` library provides the same
functions as its standard filesystem library, but stores everything in memory.
This prevents tests that create or delete files from doing anything unfortunate
and also makes tests much faster (since in-memory operations are thousands of
times faster than operations that touch the disk).

A mock object can also be designed to give pre-programmed responses to just a
handful of specific requests:

```py
INDEX_PAGE = '<html><body><h1>Index Page</h1></body></html>'
USER_PAGE = '<html><body><h1>User Page</h1></body></html>'

def mock_http_server(url):
    if url == '/':
        return INDEX_PAGE
    elif url in ['/user/', '/user/index.html']:
        return USER_PAGE
    else:
        raise UrlError(f'unhandled URL "{url}"')
```

<!-- continue -->
The strength of the pre-programmed approach is that if anything ever sends an
unexpected URL, the failure will be obvious.  The weakness is the tedium of
writing out all the cases, though in most testing scenarios there are fewer than
you might expect.

Once these changes have been made, the application zips through its tests
quickly enough that developers actually will run the test suite before checking
in changes to the code. The downside is the loss of [%g fidelity "fidelity" %]:
the system we're testing is a close cousin to what
we're deploying, but not exactly the same. However, this is a good economic
tradeoff: we may miss a few bugs because our fake HTTP handler doesn't translate
HTTP requests exactly the same way as the real web server, but we catch (and
prevent) a lot more by making testing cheap.

## Testing the Interface

All right: we've broken our MVC application into testable modules and are
reasonably sure that if the interface calls the right function when a button is
pressed, the back end will respond the right way. But how do we test that the
browser will call the right function with the right parameters when the button
is clicked?

The answer is to use a tool like [Selenium][selenium] to [%i "browser
automation!for testing" "unit test!browser automation" %]automate the browser's
actions[%/i%]. Similar tools exist for desktop and mobile applications; all of
them rely on the fact that the browser or the screen manager is just another
piece of software. With a little bit of work, we can tell them to move the
cursor to a specific (X,Y) location or a particular button or menu, to generate
a mouse click, or to pretend that the user just typed the letter 'G'. Once we've
done that, we can check that the web page has the right elements or that the
database has a new record just as we would with back-end tests.

Most GUI testing frameworks have two other useful features. The first is [%i "browser automation!record and playback" %]record and playback[%/i%]: you can
step through a workflow manually, and the tool can then produce a script that
will repeat those steps. These scripts tend to be fragile—i.e., small changes
to the UI will break them—but if you edit them to replace things like absolute
(X,Y) coordinates with the logical labels of UI elements, you can build a lot of
tests in a hurry.

The other thing GUI testing frameworks can do is automate your day-to-day work.
Any time you have to go to one website to do the first part of a task, then copy
some information from it to another website to complete the task, you could
write a Selenium script instead. I've seen it used to file one issue in a
repository for each student in a class and to check that names and addresses on
half a dozen different websites are consistent with each other. I don't think
it's worth learning just for this, but if you're going to use it for testing,
you might as well use it to make your life easier.

## Performance Testing

Programs don't just have to do the right thing; they have to do it quickly
enough to be usable.  How fast that needs to be depends on the program, but if a
text editor takes nine seconds to display each character, people are going to
write their reports some other way. You should therefore measure [%i "unit
test!performance" %]how long your tests take to run[%/i%] so that you can tell
when the application is slowing down and do something about it.

The simplest kind of [%i "performance testing!manual" %]performance
testing[%/i%] is simply to measure how much time elapses between the start and
end of a test. You can do this manually:

```py
from datetime import datetime

def test_something():
    start = datetime.now()
    ...run the test...
    elapsed = datetime.now().microsecond - start.microsecond
```

<!-- continue -->
but most test frameworks will do it for you. If you are using `pytest`, for
example, the `--durations` will report the slowest tests or the running time for
all tests. If you want to average over several runs (which you should, because
your computer is probably doing other things while it runs the tests, and those
other things might slow it down) you can use something like
[`pytest-benchmark`][pytest-benchmark].

What most frameworks *don't* do is save performance data in a format that is
easy to diff.  I sometimes do this so that I can tell how my latest changes have
impacted running times; in practice, that means saving the output of `pytest
--durations=0` as a text file in version control, and then using a one-page
program I wrote to find tests whose performance has changed by more than a few
percent. It's probably more than you need for a class project, but it has
probably saved my users from a lot of unnecessary frustration.

<div class="callout" markdown="1">
### Profiling

If you find a performance problem, the next step is to use a
[%i "profiler" "unit test!profiling" %][%g "profiler" "profiler" %][%/i%]
to figure out where the time is actually going.
While a coverage tool checks which lines of code are
executed, a profiler measures how long each line, block, or function takes to
run. Most will report both the average time per run and the total time so that
you can spot things that are fast but still affect performance because they are
called hundreds of millions of times.

Some profilers work by interrupting the program every few hundred microseconds
and seeing what line of code is being executed; others work by adding extra
instructions to the code to record the start and end times of functions. Both
methods change the program's behavior, so the output doesn't reflect the running
time of the unwatched program perfectly. (By analogy, if you put a thermometer
in a glass of water, what it reports is the weighted average of its own
temperature and the water's.) However, most modern profiling tools don't affect
performance very much, and tend to slow down most parts of the program by the
same amount; in practice, the [%g hot_spot "hot spots" %] are usually
very easy to see.
</div>

## Are We Done Yet?

The last thing you need (and you *do* need it) is some idea of how well you are
testing.  How much of your code do your tests actually check, and what parts of
your code aren't being tested?  To find out, you can check the [%i "coverage!code" "code coverage" "unit test!code coverage" %][%g code_coverage "code coverage" %][%/i%] of your tests, i.e., measure the number of lines, statements, or
possible paths through the code that the tests are actually exercising.

If you are using Python, you can check your tests' coverage with the `coverage`
library.  The command:

```sh
$ coverage run -m pytest
```

<!-- continue -->
doesn't display any information of its own, since mixing that in with our
program's output would be confusing.  Instead, it puts coverage data in a file
called `.coverage` in the current directory.  To display that data, you run:

```sh
$ coverage report -m
```

Its output shows you what percentage of your program was and wasn't executed.
You can get a more complete report by running `coverage html` at the command
line and opening the file `htmlcov/index.html`, which displays a colorized
line-by-line summary of execution.

So how much testing is enough?  The answer depends on what the software is being
used for.  If it is for a safety-critical application such as a medical device,
you should aim for 100% code coverage, i.e., every single line in the
application should be tested.  In fact, we should probably go further and aim
for 100% [%i "coverage!path" "path coverage" "unit test!path coverage" %][%g path_coverage "path coverage" %][%/i%] to ensure that every possible path through the
code has been checked.  Similarly, if the software has become popular and is
being used by thousands of people all over the world, we should probably check
that it's not going to embarrass us.

But most of us don't write software like that, so requiring 100% code coverage
is like asking for ten decimal places of accuracy when checking the voltage of a
household electrical outlet.  We always need to balance the effort required to
create tests against the likelihood that those tests will uncover useful
information.  We also have to accept that no amount of testing can prove a piece
of software is completely correct.  A function with only two numeric arguments
has \\(2^{128}\\) possible inputs.  Even if we could write the tests, how could we
be sure we were checking the result of each one correctly?

## What's Hard to Test

Some things are intrinsically harder to test than others. Take [%i "visualization!difficulty of testing" "unit
test!visualization" %]visualizations[%/i%]: any change to the dimension of the
plot, however small, can change many pixels in a [%g raster_image "raster
image" %], and cosmetic changes such as moving the legend up a couple of
pixels will cause all of the tests to fail.

The simplest solution is therefore to test the data used to produce the image
rather than the image itself.  Unless the drawing library itself contains bugs,
the correct data should always produce the correct plot.  If you're testing the
drawing library itself, comparing pixels may be your only option; in that case,
designing the library so that it can draw axes without data points, points
without axes, and so on will minimize the number of tests you need to rewrite
as the library changes.

Computer graphics, data science, and anything else that uses [%i "floating-point arithmetic!difficulty of testing" "unit test!floating-point
arithmetic" %]floating-point arithmetic[%/i%] is also hard to test. One problem
is that floating-point numbers are approximations, just as 0.33333333 is an
approximation to 1/3.  When we work with them, we have to think in terms of
error bars, just as scientists working in a lab do; rather than checking if the
actual result is exactly the same as the expected result, we have to ask, "Are
they close enough that I don't have to worry?" To answer that question, we have
to decide what is "close enough". One part in a thousand?  One part in a
million? Any two programmers will probably answer this question differently; if
nothing else, writing tests forces us to be explicit about our tolerances.

Another challenge when testing numerical software is that we often don't know
what the right answer is. If your program is supposed to simulate the
gravitational effects of a rapidly-rotating black hole, there isn't a formula
that tells you what the answer should be—if there was, you'd use it instead of
writing a program. Similarly, if you are using machine learning to cluster
people according to their medical histories, there is no "right" answer:
slightly different parameters can produce slightly different clusters, and if
there was an easy way to predict the result, you'd be using that. Again, one of
the benefits of writing tests is that it forces us to be explicit about what we
think the right and wrong answers are so that we can have more productive
conversations with our colleagues.
