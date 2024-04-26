---
title: Using Git Together
---

[%i "version control!collaboration" %]Version control[%/i%] really comes into
its own when we are working with other people.  People can share work through a
Git repository in one of two ways [%b Irving2021 %]:

1.  Everyone has read and write access to a [%i "version
    control!using a shared repository" %]single shared
    repository[%/i%].

2.  Everyone can read from the project's main repository, but only a few people
    can commit changes to it.  The project's other contributors
    [%i "version control!using forked repositories" %][%g fork_git "fork" %][%/i%]
    the main repository to create one that they own,
    do their work in that, and then submit their changes to the main repository.

<!-- continue -->
The first approach works well for teams of up to half a dozen people, so we will
focus on it. If the project is larger, or if contributors are worried that they
might make a mess in the `main` branch, the second approach is safer.

<div class="callout" markdown="1">
### When to commit

When you're working on your own, it's natural to fall into a rhythm of updating
your laptop from your repository in the morning and committing whatever you've
managed to accomplish when you wrap up for the day. You need to break this habit
when you become part of a team. Instead, [%i "version control!when to
commit" %]you should commit[%/i%] when you finish a chunk of work that moves the
project forward or is fit for someone else to review. A good rule is "never
break the build" ([%x automation %]), i.e., never commit anything that
doesn't run well enough to pass all existing tests.
</div>

## Using Git Together

Suppose Amira and Sami are working together on a course.  They decided at the
start of semester that Sami would host the project repository in her GitHub
account, so they created `https://github.com/sami/bst` and gave Amira permission
to push to it. They have both cloned that repository to their laptops to start
work on homework 5.

We will modify Amira's prompt to include her desktop user ID (`amira`) and
working directory (initially `~`, meaning "home directory") to make it easier to
follow what's happening.  First, she updates her desktop repository to make sure
she is starting with the most recent set of files:

```sh
amira:~ $ cd bst
amira:~/bst $ git pull origin main
amira:~/bst $ ls
```
```out
LICENSE.md   README.md    hw1/    hw2/    hw3/    hw4/
```

Amira creates a new directory for homework 5 and adds a copy of the assignment spec:

```sh
amira:~/bst $ mkdir hw5
amira:~/bst $ cd hw5
amira:~/bst $ cp ~/Downloads/Assignment5.txt hw5/spec.txt
amira:~/bst $ git add .
amira:~/bst $ git commit -m "Adding homework 5 spec"
```
```out
[main f5f7d30] Adding homework 5 spec
 1 files changed, 132 insertions(+)
```

She then pushes her changes to the shared repository:

```sh
amira:~/bst $ git push origin main
```
```out
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 485 bytes | 485.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:sami/bst.git
   f5f7d30..433a2d5  main -> main
```

<!-- continue -->
And no, [%i "Git!interface (indistinguishable from hoax)" %]Git's
output[%/i%] here isn't particularly useful to anyone except people who are
debugging Git's internals.

Amira's changes are now on her desktop computer and in the GitHub repository but
not on Sami's laptop. They can get them by running:

```sh
sami:~/bst $ git pull origin main
```

But what if Sami is working on some changes to homework 4 (which homework 5
builds on)? She could just make her changes and push, but that would lead to a
lot of merge conflicts.  Instead, almost everyone uses
[%i "pull request" "Git!pull request" %][%g pull_request "pull requests" %][%/i%] (PR).
A PR is essentially a note saying, "Someone would like to merge branch A into branch B".
The PR does not contain the changes, but instead points at two particular
branches.  That way, the difference displayed is always up to date if either
branch changes.

But a PR can store more than just the source and destination branches: it can
also store [%i "Git!comments" %]comments[%/i%] people have made
about the proposed merge.  Users can comment on the PR as a whole, or on
particular lines, and mark comments as out of date if the author of the PR
updates the code that the comment is attached to.  Complex changes can go
through several rounds of review and revision before being merged, which makes
PRs the review system we all wish journals actually had.

To see this in action, suppose Sami wants to add their email address to
`README.md`.  They create a new branch and switch to it:

```sh
sami:~/bst $ git checkout -b adding-email
```

<!-- continue -->
then make a change and commit it:

```sh
sami:~/bst $ git commit -a -m "Adding my email address"
```

<!-- continue -->
(Notice that Sami uses the `-a` option to `git commit` to add all changes and
commit them in a single step. This is both convenient and dangerous.)

Sami's changes are only in their local repository.  They cannot create a pull
request until those changes are on GitHub, so they push their new branch to
their repository on GitHub:

```sh
sami:~/bst $ git push origin adding-email
```

When Sami views their repository in the browser, GitHub notices that they have
just pushed a new branch and asks them if they want to create a PR.  When they
click on the button, GitHub displays a page showing the default source and
destination of the PR and a pair of editable boxes for the pull request's title
and a longer comment.

If they scroll down, Sami can see a summary of the changes that will be in the
PR.  When they click "Create Pull Request", Git gives it a unique [%i "pull
request!serial number" %]serial number[%/i%].  This is *not* a commit ID;
instead, each PR in a particular repository is given a sequential ID.

Clicking on the "Pull requests" tab in the repository brings up a list of PRs
and clicking on the PR link itself displays its details.  Since there are no
conflicts in this PR, GitHub will let Sami or Amira merge it immediately using
the "Merge pull request" button.  They could also discard or reject it without
merging using the "Close pull request" button.

But instead, the next time Amira has a few minutes to work on the assignment she
clicks the "Files changed" tab in the PR to see what Sami has changed. She can
review the changes line-by-line and suggest changes; we'll discuss this more in
the next section. Once they are both happy with the changes, either of them can
merge the PR into the main branch. They can both then update their local copies
and be sure that they are synchronized.

If there are any conflicts along the way, Sami and Amira can resolve them just
as they would resolve conflicts between branches in a single repository.  GitHub
and other portals do allow people to merge conflicts through their browser-based
interfaces, but doing it on our desktop means we can use our favorite editor to
resolve the conflict.  It also means that if the change affects the project's
code, we can run everything to make sure it still works.

But what if Sami merges another PR while Amira is resolving this one?  In theory
this [%i "conflict (in Git)!repeating" %]cycle[%/i%] could go on forever; in
practice, it reveals a communication problem that the team needs to address.  If
two or more people are constantly making incompatible changes to the same files,
they should discuss who's supposed to be doing what, or rearrange the project's
contents so that they aren't stepping on each other's toes.

<div class="callout" markdown="1">
### Trust but verify

[%x automation %] describes how to configure Git to run tests each time
someone tries to commit a change.  The commit only takes effect if those tests
pass, so the team can ensure that the software is always as good as its tests.
</div>

## Commit Messages

A [DuckDuckGo][duckduckgo] search for "how to write a good [%i "Git!commit
message" %]commit message[%/i%]" turns up several thousand articles. Most are
variations on the sample shown below; as with programming style
([%x research %]), the most important thing is being consistent rather than the
particular rules you follow.

```txt
One-line summary

Detailed explanatory text separated from the summary by a blank line.  (If you
do this, many tools will treat the first line like the subject of an email and
the rest of the text as the body.)

Be brief but specific and write your message in the imperative voice, i.e.,
"Handle indentation in configuration files correctly" rather than "Config file
indentation."

- Bullet points are OK (GitHub will format them as a list).  Some other Markdown
  conventions work too.

If this commit fixes an open issue, refer to it like as shown below. GitHub
automatically turns things like `#123` into links.

Closes: #123
```

The most important thing to remember when writing a commit message is that its
purpose is to make work easier to find and understand in the future. You
shouldn't transcribe large chunks of code or duplicate whatever documentation or
tests you wrote for the feature you added; instead, you should give people
enough information to figure out whether this is the commit they're looking for
or not.

## Code Reviews

There's no point creating PRs if they are all merged as-is. The reason they
exist is to allow [%i "code review!effectiveness of" %][%g code_review "code review" %][%/i%].  One study after another since the mid-1970s has proven that code
review is the most cost-effective way to find bugs in software
[%b Cohen2010 %]. It is also the most effective way to share knowledge
between team members: if you read someone else's code, you have a chance to
learn all the things that you didn't know to ask and they didn't realize they
should tell you.

<div class="callout" markdown="1">
### Do more eyes make for fewer bugs?

Some people have claimed that many eyes make all bugs shallow (i.e., easy to
find), but the evidence doesn't support that claim: [%b Meneely2014 %]
reports that, "…source code files reviewed by more developers are,
counter-intuitively, more likely to be vulnerable (even after accounting for
file size). However, files are less likely to be vulnerable if they were
reviewed by developers who had experience participating on prior
vulnerability-fixing reviews." In short, *whose* eyes matters more than how
many.
</div>

There are lots of guides online for doing code reviews, most of them based on
their authors' personal experience. A notable exception is the [SmartBear
guide][smartbear-code-review], which draws on a large study of code review in
industry. The [%i "code review!procedure" %]rules below[%/i%] present some of
their findings with modifications for students' situations.

Have the instructor do a demonstration review.
:   Even if you have done code reviews before, you may not know what's expected
    for this class. The instructor can show you by putting up some sample code
    and going through it, thinking aloud as they notice things worth commenting
    on so that you have an idea of how much detail they expected.

Authors should clean up code before review.
:   If the person creating the PR goes through and adds some more comments,
    cleans up some variable names, and does a bit of [%i "refactoring!for
    code review" %]refactoring[%/i%] ([%x design %]), they won't just make
    reviewing easier: the odds are very good that they will find and fix a few
    problems on their own.

Review at most 200 lines of a code at a time.
:   The SmartBear guide recommends reviewing at most 400 lines at a time, which
    should take 60--90 minutes. You will probably get there eventually, but in
    our experience it's better to start with something smaller and work up to
    that.  A corollary of this rule is that no PR should be more than 200 lines
    long.  If one is, the odds are that reviewers won't be able to hold it all
    in their head at once ([%x thinking %]) and so will miss things.

Use checklists.
:   [%b Gawande2011 %] popularized the idea that using
    [%i "checklists!use in code review" %]checklists[%/i%] improves results even
    for experts.  While [%b Hatton2008 %] found no evidence that they made
    a difference to code reviews by professionals, I have found them very useful
    as a starter for students.  If you are new to code reviews, ask the
    instructor for a list of the dozen most common problems to check for, since
    anything more than that is likely to be overwhelming.  (The code quality
    rubric developed in [%b Stegeman2014 Stegeman2016 %] is a good
    starting point.)  If you and your teammates have been working together for a
    while, look at your own code reviews and make a list of the things that keep
    coming up.  Having the list will make you more aware of the issues while
    you're coding, which in turn will make you less likely to keep making the
    same mistakes.

Look for algorithmic problems first.
:   Code review isn't just (or even primarily) about style: its real purpose is
    to find bugs before they can affect anyone.  The first pass over any change
    should therefore look for algorithmic problems.  Are the calculations right?
    Are any rare cases going to be missed?  Are errors being caught and handled?
    Using a consistent style helps reviewers focus on these issues.

Offer alternatives.
:   Telling authors that something is wrong is helpful; telling them what they
    might do instead is more so.

Don't [%g feigning_surprise "feign surprise" %] or pass judgment.
:   "Gosh, didn't you know [some obscure fact]?" isn't helpful; neither is,
    "Geez, why don't you [some clever trick] here?"

Don't overwhelm people with details.
:   If someone has used the letter `x` as a variable name in several places, and
    they shouldn't have, comment on the first two or three and simply put a
    check beside the others—the reader won't need the comment repeated.

Don't try to sneak in feature requests.
:   Nobody enjoys fixing bugs and style violations.  Asking them to add entirely
    new functionality while they're at it is rude.

Follow up.
:   The author of the code doesn't have to accept every suggestion, but should
    have a better reason than "I don't want to" for rejecting any of them.
    GitHub and other platforms allow people to create discussion threads for
    each comment, and will mark threads as being out of date when the pull
    request is updated. Whoever did the review should then scan the changes to
    make sure their points have been addressed, and to give themselves a chance
    to learn a few more things from the author.

Don't tolerate rudeness.
:   Most code review guidelines say, "Be respectful."  The problem is that if
    you are, you probably don't need to be told that, and if you aren't, those
    two works alone won't change your behavior. What *will* is teammates
    defending the victims of rudeness by telling the offender, "That's not how
    we speak to each other."  We'll talk about this more in
    [%x fairness %].

How we [%i "code review!responding to" %]respond[%/i%] to reviews is just as
important:

Be specific in replies to reviewers.
:   If someone has suggested a better variable name, you can probably simply fix
    it.  If someone has suggested a major overhaul to an algorithm, you should
    reply to their comment to point at the commit that includes the fix.

Thank your reviewers.
:   If someone has taken the time to read your code carefully, thank them for
    doing it.

So what does a code review actually look like? Here's a Python program that
searches for duplicated files. [%t collaborate-code-review %] shows the
comments I left when reviewing it.

[%inc dup.py %]

[% table slug=collaborate-code-review tbl=code-review.tbl caption="Code Review" %]
