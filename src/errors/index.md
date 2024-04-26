---
title: Error Handling
---

> When Mister Safety Catch Is Not On, Mister Crossbow Is Not Your Friend.
>
> — [%i "Pratchett, Terry" %]Terry Pratchett[%/i%]

We are imperfect people living in an imperfect world.  People will misunderstand
how to use our programs, and even if we test thoroughly as described in
[%x testing %], those programs will probably still contain bugs.  We should
therefore plan from the start to detect and handle errors.

## Handling Errors

[%i "internal error" "error!internal" %][%g internal_error "Internal errors" %][%/i%]
are mistakes in the program itself,
such as calling a function with `None` instead of a list.
[%i "external error" "error!external" %][%g external_error "External errors" %][%/i%]
are usually caused by interactions between the program and the outside world:
a user may mis-type a filename, the network might be down, and so on.

When an internal error occurs, the only thing we can do in most cases is report
it and halt the program.  If a function has been passed `None` instead of a
valid list, for example, the odds are good that one of our data structures is
corrupted.  We can try to guess what the problem is and take corrective action,
but our guess will often be wrong and our attempt to correct the problem might
actually make things worse.  When an external error occurs, on the other hand,
we don't always want the program to stop: if a user mis-types her password,
prompting her to try again is friendlier than halting and requiring her to
restart the program.

Most modern programming languages use [%i "exception" %][%g exception "exceptions" %][%/i%] for error handling.  In Python, for example,
exceptions are handled using the keywords `try` and `except`.  If nothing
unexpected happens inside the `try` block, the `except` block isn't run, but if
something does go wrong, the program jumps immediately to the body of the
`except`.

We often want to know exactly what went wrong, so Python and other languages
store information about the error in an object (which is also called an
exception).  We can [%i "exception!handling" "catch exception" %][%g catch_exception "catch" %][%/i%] an exception and inspect it as follows:

```py
for denom in [-5, 0, 5]:
    try:
        result = 1/denom
        print(f'1/{denom} == {result}')
    except Exception as error:
        print(f'{denom} has no reciprocal: {error}')
```
```out
1/-5 == -0.2
0 has no reciprocal: division by zero
1/5 == 0.2
```

Most languages also allow us to specify what kind of exception we want to catch.
For example, we can write code to handle out-of-range indexing and division by
zero in Python separately:

```py
numbers = [-5, 0, 5]
for i in [0, 1, 2, 3]:
    try:
        denom = numbers[i]
        result = 1/denom
        print(f'1/{denom} == {result}')
    except IndexError as error:
        print(f'index {i} out of range')
    except ZeroDivisionError as error:
        print(f'{denom} has no reciprocal: {error}')
```
```out
1/-5 == -0.2
0 has no reciprocal: division by zero
1/5 == 0.2
index 3 out of range
```

So where do exceptions come from?  The answer is that programmers can [%i "exception!raise" "raise exception" %][%g raise_exception "raise" %][%/i%] them
explicitly:

```py
for number in [1, 0, -1]:
    try:
        if number < 0:
            raise ValueError(f'no negatives: {number}')
        print(number)
    except ValueError as error:
        print(f'exception: {error}')
```
```out
1
0
exception: no negatives: -1
```

<!-- continue -->
We can define our own exception types, and many libraries do, but the built-in
types are enough to cover common cases.

One final note is that exceptions don't have to be handled where they are
raised: in fact, their greatest strength is that they allow long-range error
handling.  If an exception occurs inside a function and there is no `except` for
it there, Python checks to see if whoever called the function is willing to
handle the error.  It keeps working its way up through the call stack until it
finds a matching `except`.  If there isn't one, Python takes care of the
exception itself.

This behavior is designed to support a pattern called "[%i "throw low, catch
high" %]throw low, catch high[%/i%]": write most of your code without exception
handlers, since there's nothing useful you can do in the middle of a small
utility function, but put a few handlers in the outermost functions of your
program to catch and report all errors.  This also makes libraries more
reusable: different applications will want to handle errors in different ways,
so the library should just report the problem.

<div class="callout" markdown="1">
### Kinds of errors

The "`if` then `raise`" approach is sometimes referred to as, "Look before you
leap," while the `try/except` approach is, "It's easier to ask for forgiveness
than permission."  The first approach is more precise, but has the shortcoming
that programmers can't anticipate everything that can go wrong when running a
program, so there should always be an `except` somewhere to deal with unexpected
cases.

The one rule we should *always* follow is to check for errors
[%i "exception!when to check" %]as early as possible[%/i%] so that we don't waste
the user's time.  Few things are as frustrating as being told at the end of an
hour-long calculation that the program doesn't have permission to write to an
output directory.  It's a little extra work to check things like this up front,
but the larger your program or the longer it runs, the more useful those checks
will be.
</div>

## Defensive Programming

The first step in building confidence in our programs is to assume that mistakes
will happen and guard against them.  This is called
[%i "defensive programming" %][%g defensive_programming "defensive programming" %][%/i%], and the
most common way to do it is to add [%i "assertion" %][%g assertion "assertions" %][%/i%] to our code so that it checks itself as it runs.
An assertion is a statement that something must be true at a certain point in a
program.  When the program runs, it checks the assertion's condition.  If it's
true, the program does nothing; if it's false, it halts and prints a
user-defined error message.  For example, this Python code halts as soon as the
loop encounters a negative word frequency:

```py
frequencies = [13, 10, 2, -4, 5, 6, 25]
total = 0.0
for freq in frequencies[:5]:
    assert freq >= 0.0, 'Word frequencies must be non-negative'
    total += freq
print('total frequency of first 5 words:', total)
```

<!-- continue -->
Programs intended for widespread use are typically full of assertions: 10--20%
of the code they contain is there to check that the other 80--90% is working
correctly.

## Writing Useful Error Messages

This is not a useful error message:

```out
OSError: Something went wrong, try again.
```

<!-- continue -->
It doesn't provide any information on what went wrong, so it is difficult for
the user to know what to change next time.  A slightly better message is:

```out
OSError: Unsupported file type.
```

<!-- continue -->
This message tells us the problem is with the type of file we're trying to
process, but it still doesn't tell us what file types are supported, which means
we have to rely on guesswork or read the source code.  Telling the user that a
file isn't a [%g csv "CSV" %] file makes it clear that the program only
works with files of that type, but since we don't actually check the content of
the file, this message could confuse someone who has comma-separated values
saved in a `.txt` file.  An even [%i "error message!writing helpful" %]better
message[%/i%] would therefore be:

```out
OSError: File must end in .csv
```

<!-- continue -->
This message tells us exactly what the criteria are to avoid the error.

Error messages are often the first thing people read about a piece of software,
so they should be its most carefully written documentation.  A web search for
"writing good error messages" turns up hundreds of hits, but recommendations are
often more like gripes than guidelines and are usually not backed up by
evidence.  What research there is gives us the following rules
[%b Becker2016 %]:

Tell the user what they did, not what the program did.
:   Putting it another way, the message shouldn't state the effect of the error,
    it should state the cause.

Be spatially correct
:   I.e., point at the actual location of the error.  Few things are as
    frustrating as being pointed at line 28 when the problem is on line 35.

Be as specific as possible.
:   For example, "file not found" is very different from "cannot open file",
    since the latter could mean "no permissions" or many other things.

Write for your audience's level of understanding.
:   For example, error messages should never use programming terms more advanced
    than those you would use to describe the code to the user.

Do not blame the user, and do not use words like fatal, illegal, etc.
:   The former can be frustrating—in many cases, "user error" actually
    isn't—and the latter can make people worry that the program has damaged
    their data, their computer, or their reputation.

Do not try to make the computer sound like a human being.
:   In particular, avoid humor; very few jokes are funny on the dozenth
    re-telling, and most users are going to see error messages at least that
    often.

Use a consistent vocabulary.
:   This rule can be hard to enforce when error messages are written by several
    different people, but putting them all in one module makes review easier.

That last suggestion deserves a little elaboration.  Most people write error
messages directly in their code:

```py
if fname[-4:] != '.csv':
    raise OSError(f'{fname}: File must end in .csv')
```

<!-- continue -->
A better approach is to put all the error messages in a [%i "error
message!internationalizing" %]dictionary[%/i%]:

```py
ERRORS = {
    'not_csv_suffix' : '{fname}: File must end in .csv',
    'config_corrupted' : '{config_name} corrupted',
    # ...more error messages...
}
```

<!-- continue -->
and then only use messages from that dictionary:

```py
if fname[-4:] != '.csv':
    raise OSError(ERRORS['not_csv_suffix'].format(fname=fname))
```

Doing this makes it much easier to ensure that messages are consistent.  It also
makes it much easier to give messages in the user's preferred language:

```py
ERRORS = {
  'en' : {
    'not_csv_suffix' : '{fname}: File must end in .csv',
    'config_corrupted' : '{config_name} corrupted',
    # ...more error messages in English...
  },
  'fr' : {
    'not_csv_suffix' : '{fname}: Doit se terminer par .csv',
    'config_corrupted' : f'{config_name} corrompu',
    # ...more error messages in French...
  }
  # ...other languages...
}
```

<!-- continue -->
The error report is then looked up and formatted as:

```py
ERRORS[user_language]['not_csv_suffix'].format(fname=fname)
```

{: continue}
where `user_language` is a two-letter code for the user's preferred language.

## Logging

Something else you can design into your system to make your life easier later on
is [%i "logging" %][%g logging "logging" %][%/i%]. Instead of writing `print`
statements like this:

```py
def extrapolate(basis, case):
    print "entering extrapolate..."
    trials = count_basis_width(basis)
    if not trials:
        print "...no trials!"
        raise InvalidDataException("no trials")
    print "...running", len(trials), "trials"
    result = run_trial(trials[0])
    for t in range(1, len(trials)):
        result = max(result, run_trial(trials[i]))
    print "...exiting extrapolate with", result
```

{: continue}
you use your language's logging library:

```py
import logging

def extrapolate(basis, case):
    logging.debug("entering extrapolate...")
    trials = count_basis_width(basis)
    if not trials:
        logging.warning("...no trials!")
        raise InvalidDataException("no trials")
    logging.debug(f"...running {len(trials)} trials")
    result = run_trial(trials[0])
    for t in range(1, len(trials)):
        result = max(result, run_trial(trials[i]))
    logging.debug(f"...exiting extrapolate with {result}")
```

At first glance this is just more verbose. The benefit, though, is that your
messages are now divided into categories. If you want to get all the messages
you put:

```py
logging.basicConfig(level=logging.DEBUG)
```

<!-- continue -->
somewhere near the start of your program. The `DEBUG` option identifies the
lowest-level messages in your program—the ones you probably only want to see
when you're trying to figure out what's gone wrong. In order, the more important
[%i "logging!levels" %]levels[%/i%] in most logging libraries are `INFO`,
`WARNING`, `ERROR`, and `CRITICAL`. If you only want messages at the `WARNING`
level and above, you change the configuration to:

```py
logging.basicConfig(level=logging.WARNING)
```

<!-- continue -->
so that `DEBUG` and `INFO` messages aren't printed.

A logging library allows you to control how much your program tells you about
its execution by making one change, in one place. It also means that you can
leave these messages in your code, even when you release it—there's no more
commenting out `print` statements only to add them back in later. (And no more
embarrassment from inappropriately-worded messages that *weren't* commented out
but should have been before your demo…)

Logging libraries also let you divide messages into groups by component, so that
you can (for example) turn on debugging-level messages from the database
interface but only see errors and above from the image processing functions.
They also let you control where your messages are sent. By default, they go to
the screen, but you can send them to a file instead simply by changing the
configuration:

```py
logging.basicConfig(level=logging.ERROR,
                    filename="/tmp/mylog.txt",
                    filemode="append")
```

This is handy if it takes your program a while to get to the point where the
error occurs. It's also handy if you don't know whether your program contains an
error or not: if you leave logging turned on every time you run it, then
whenever it does something unexpected (like crashing), you will have at least
some idea of what it was doing beforehand.

<div class="callout" markdown="1">
### Logging for security

One of the recommendations in [%x security %] was to [%i "logging!for
security" %]log actions[%/i%] to help you find suspicious activity.  When you do
this, make sure the log records who, what, and when; in particular, make sure
you have a record of every time permissions were changed or new accounts were
created.
</div>

Most logging libraries also support [%i "logging!rotating files" %][%g rotating_file "rotating files" %][%/i%], i.e., they will write to `log.1` on the first day,
`log.2` on the second day, and so on until they reach (for example) `log.7`,
then wrap around and overwrite `log.1`. Web servers and other long-lived
programs are usually set up to do this so that they don't fill up the disk with
log information.  It's all straightforward to set up, and once it's in place, it
gives you a lot more insight into what your program is actually doing.

<div class="callout" markdown="1">
### Parsers as a sign of bad design

You will sometimes inspect logs yourself, but you will also frequently want to
search them for patterns. All of the logs you produce should therefore be in a
[%i "logging!output format" %]machine-readable format[%/i%] like CSV, JSON,
or [%g yaml "YAML" %]; you can easily write a small program to
pretty-print the data you want for manual inspection.

This guideline is one instance of a more general design rule.  The world has
more data formats than it needs, so if anyone has to write a parser to analyze
what your program produces, you should probably be producing something else.
</div>
