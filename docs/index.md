---
description: >-
  A free Python reference with runnable code examples covering data types, collections,
  loops, functions, classes, error handling, and popular libraries.
hide:
  - navigation
  - toc
---

# Python Field Guide { .pt-visually-hidden }

??? ai "Using AI while learning to code"

    === "Why still learn to code yourself?"

        <div class="pt-compare">

        |  | Learn to do it yourself | Have AI do it for you |
        |---|---|---|
        | **Writing & struggling with code** | :material-check:{ .pt-icon-success } Productive struggle is what **builds understanding**<ul><li>You can solve the problem **again** on your own</li><li>**Adapt** the answer, and **catch** when it's wrong</li></ul> | :material-close:{ .pt-icon-fail } Being handed the answer skips [the friction that builds understanding](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf)<ul><li>If you skip that struggle, you **won't develop the knowledge** to solve the problem again, adapt the answer, or recognize when it's wrong.</li></ul> |
        | **Reading & verifying code** | :material-check:{ .pt-icon-success } **Understanding programming fundamentals** makes AI more useful — you can read and evaluate code you didn't write<ul><li>Spot mistakes</li><li>Understand **why** a solution works</li><li>Communicate your problem to AI more effectively</li></ul> | :material-close:{ .pt-icon-fail } Inefficient communication with AI **if you don't fully understand **what's going on, and AI code can look correct while being wrong or insecure<ul><li>You can't tell **why** a solution works</li><li>Researchers are already documenting this skill gap in [students who rely on AI code generation](https://dl.acm.org/doi/10.1145/3617367) before they've [built their own foundation](https://dl.acm.org/doi/10.1145/3624720)</li><li>One [Stanford study](https://dl.acm.org/doi/10.1145/3576915.3623157) found developers using AI wrote **less** secure code — but were **more** confident it was secure</li></ul> |
        | **On the job** | :material-check:{ .pt-icon-success } Programming work still requires understanding:<ul><li>Code review, debugging, system design, and interviews all test whether you can reason about code and judge whether it's correct</li><li>Learning to program on your own turns AI into a **tool you can direct and verify**, instead of one you're assuming got it right</li></ul> | :material-close:{ .pt-icon-fail } AI will likely be available at work too — but it isn't what will get you hired |

        </div>

    === "How to use AI to support your learning?"

        ```mermaid
        swimlane-beta TB
            accTitle: Using AI to learn
            accDescr: AI walks you through setup before you start. You attempt each problem yourself with autocomplete off, then check whether you can explain why it works and whether it actually holds up — if either check fails, you describe what you tried rather than handing over your code, so AI explains the concept instead of fixing it, and you try again. Passing both checks means you understand it well enough for a practice problem, or for the code review, debugging, and interviews that are what your job actually tests.

            subgraph You
                you_help_setup(Need help setting up your computer to start programming?)
                you_have_project(Do you have a project to work on?)
                you_attempt(Attempt it yourself, autocomplete off so you understand everything that's there, utilize debug strategies)
                you_writeup(Stuck? Write out your problem: what you expect to happen, what you're observing, what you've tried already, see if this helps you process or rethink your strategy)
                you_finish("Learning to program means making mistakes, getting stuck, and eventually figuring things out and forming a mental model. That's the process that builds skills you can rely on to continue solving problems and detecting issues — ready for code review, debugging, and interviews, where AI won't be tested, your reasoning will. ")
            end

            subgraph AI
                ai_help_setup(AI can help guide you through setup on your exact device — which could make getting started more accessible for beginners)
                ai_suggest_problem(Suggests a problem based on your skill level, interests, and what you're trying to improve)
                explain(With that context AI can provide more targeted, efficient help. Don't just paste the code/error, ask AI to explain what a line does, or what an error means — an explanation to help you understand concepts, be clear you do NOT want it to write code, just explain)
            end


            ai_help_setup ~~~ you_help_setup
            ai_suggest_problem ~~~ you_have_project
            you_help_setup -->|Yes| ai_help_setup
            you_help_setup -->|No| you_have_project
            ai_help_setup --> you_have_project

            you_have_project -->|No| ai_suggest_problem

            you_have_project -->|Yes| you_attempt

            ai_suggest_problem --> you_attempt
            you_attempt <--> you_writeup
            you_attempt -->|Done!| you_finish
            you_writeup --> |still stuck?| explain
            explain --> you_attempt
            explain ~~~ you_finish

            %% Edge label text colored red if it leads into the AI lane, green
            %% if it leads into the You lane, matching the lane colors. This is
            %% linkStyle's "color" property (not background) — the one styling
            %% mechanism mermaid applies from inside its own closed shadow
            %% root, so it's the only thing that actually reaches the label.
            linkStyle 0 color:#a33f3f
            linkStyle 1 color:#3f6b52
            linkStyle 3 color:#3f6b52
            linkStyle 4 color:#a33f3f
            linkStyle 7 color:#3f6b52
            linkStyle 8 color:#a33f3f

            classDef you fill:#3f6b521f,stroke:#3f6b52,stroke-width:2px,color:#3f6b52
            classDef ai fill:#a33f3f1a,stroke:#a33f3f,stroke-width:2px,color:#a33f3f
            class you_writeup,you_help_setup,you_have_project,you_attempt,you_finish you
            class explain,ai_help_setup,ai_suggest_problem ai
            style You fill:#3f6b521f,stroke:#3f6b52,color:#3f6b52
            style AI fill:#a33f3f1a,stroke:#a33f3f,color:#a33f3f
        ```

<!-- cheatsheet exclude="libraries/" -->

# Add-On Libraries { .library-grid-heading }

<!-- cheatsheet section="libraries/" class="library-grid" -->
