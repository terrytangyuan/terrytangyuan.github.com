---
layout:     post
title:      "Reading Notes: Staff Engineer - Leadership beyond the Management Track"
subtitle:   ""
date:       2024-06-24
author:     "Yuan Tang"
tags:
    - Leadership
---

*This post contains my reading notes on the book [Staff Engineer: Leadership beyond the management track](https://staffeng.com/guides/).*

# Overview

## Archetypes

Four common archetypes (recurring character patterns) of Staff-plus roles:
* **Tech Lead**:
    * guide approach and execution of a particular team; work closely with a single manager
    * delegate projects across the team and grow their teammates; as the team's impact grows, tech lead's coding blocks shrink
    * this role is common among companies using agile methodologies. An organization needs roughly one tech lead for every eight engineers. It's common to perform the tech lead role without having the impact expected of a Staff-level engineer
* **Architect**:
    * responsible for the direction, quality, and approach within a critical area; combine in-depth knowledge of technical constraints, user needs, and organization level leadership
    * responsible for the success of a specific technical domain within the company where the domain must be both complex and enduringly central to company's success
    * maintain an intimate understanding of the business' needs, their users' goals, and the relevant technical constraints
    * use insight to identify effective approaches within their area of focus via organizational authority they've earned by demonstrating consistently good judgement
    * this role tends to evolve in large companies
* **Solver**:
    * dig deep into complex problems, find path forward, and continue to work on them until they're resolved
    * generally operate on problems that are identified as organizational priorities
* **Right Hand**:
    * extend executive's attention, borrow their scope and authority to operate complex organizations
    * operate as a senior organizational leader without direct managerial responsibilities
    * remain deeply aligned with that leader's approach, beliefs, and values
    * often dive into a fire, edit the approach, and delegate execution to the appropriate team

The architect and right hand roles have generally emerged as the organizations reached 100 and 1000 engineers. The solver and right hand are tightly aligned with executive priorities and are likely to receive recognition for addressing leadership's most pressing problems.

## What do they actually do?

* Working on projects/efforts that have strategic value for the company while driving technical design and up-leveling their team
* **Setting technical direction**: understanding and solving the real needs of the organization around you and far less about prioritizing technology and approaches that you personally are excited to learn about
* **Mentoring and sponsorship**: growing the engineers around you then through personal heroics
* **Providing engineering perspective**: reviewing contracts for potential enterprise customers; getting pulled into the room where decisions are happening; injecting engineering context and perspective into a decision; representing the interests of all of engineering, not just your own
* **Exploration**: companies either learn to explore or they fade away; group trusted individuals with broad skills, allocate resources, and check back later to see what they've discovered (one of those engineers is often a Staff engineer)
* **Being glue**: doing the needed, but often invisible, tasks to keep the team moving forward and shipping its work
* **Writing software**: the higher you get, the more your job becomes about mentoring and growing the people around you; building company's tech branch, noticing larger tech trends that can be improved upon or corrected, helping to set the tech vision for your team/company; reading code and doing a fair number of code reviews
* **Slow but rewarding**: it's normal to end some days as a Staff-plus engineer feeling like you haven't accomplished anything - keep at it!

## Does the title even matter?

* **Allowing you to bypass informal gauges of seniority**: a Staff-plus title allows you to reinvent the energy you've previously spent on proving yourself into the core work you're evaluated on
* **Facilitating access to "the room"**: a seat at the table in higher-level engineering discussions above individual projects and teams
* **Potentially increase career compensation**
* **Access to interesting work**: depends on archetypes (solvers: yes, tech lead: undermine the team if they operate that way)
* **Different rather than better**: being a Staff-plus engineer, especially a broad-scoped one, is a very different job than being a Senior engineer. It's important to take a step back and think about whether it's a job you really want
* **Material but not magic**: if you have a problem and believe that your title is the only thing holding you back, I'd like to reassure you that focusing on developing your approach and skills will be far more impactful than the title


# Operating at Staff

One challenge is that much of the work you are doing has a much slower feedback cycle. The delayed feedback can initially feel quite demoralizating as you replace coding with the uneven progress of mentorship, relationship building, and strategy.

* Work on what matters
* Write an engineering strategy
* Curate technical quality
* Stay aligned with authority: staying aligned, trustworthy, and predictable
* To lead, you have to follow: blend your vision with the visions from your peers and leadership
* learn to never be wrong
* Create space for others
* Build a network of peers to vet difficult decisions and to give your honest feedback

You'll find the role surprisingly similar to that of an engineering director and at other times familiar to previous work in your career.

## Work on what matters

* Time to do your work will become increasingly scarce as you get deeper into your career.
* As your time available for work shrinks, the expectations around your impact will keep growing.
* **Only through pacing your career to your life can you sustain yourself for the long-term.**
* **Avoid snacking**: easy and low-impact work is snacking. It's ok to spend some time on snacks to keep yourself motivated but you have to keep yourself honest about how much time you are spending on high-impact work versus low-impact work. In senior roles, you are more likely to self-determine your work so you need to deliberately tracking your work.
* **Stop preening**: doing low-impact, high-visibility work is preening.
* **Stop chasing ghosts**: avoid spending much time on low-impact high-effort projects. As a senior leader, you have to maintain a hold on your ego to avoid investing in meaningless work on a grand scale.
* **Existential issues**: the first place to look for work that matters is exploring whether your company is experiencing an existential risk. If something dire is happening at your company, then that's the place to be engaged.
* **Work where there's room and attention**: you should swarm to existential problems, but if a problem isn't existential, then you should be skeptical of adding your efforts where everyone's already focused. The most effective places to work are those that matter to your company but still have enough room to actually do work. What are priorities that will become critical in the future, where you can do great work ahead of time? Where are areas that are doing ok but could be doing great with your support? Sometimes you need to teach a company to value something and advocate for it. As a senior leader, you have an ethical obligation that goes beyond maximizing your company-perceived impact, but it's important to measure time and efforts accordingly.
* **Foster growth**: growing the team around you, e.g. onboarding, mentoring, and coaching.
* **Edit**: making small changes, quick modifications, and short conversations as editing your team's approach. Shifting a project's outcomes with your organizational privilege, relationships you've built across the company, and ability to see around corners derived from your experience.
* **Finish things**: helping finish a project that just cannot quite close itself out. Coaching a teammate on how to tweak a project into something finishable.
* **What only you can**: it's important to do the sort of work that simply won't happen if you don't do it.
* **Why it matters**: you cannot escape subjective interview practices, but you can deliberately accumulate expertise from doing valuable work. Focus on work that matters, do projects that develop you, and steer towards companies that value genuine experience.

## Writing engineering strategy

* To write an engineering strategy, write five design docs, and pull similarities out. 
* To write an engineering vision, write five engineering strategies, and forecast their implications two years into the future.
* Even if you are not directly responsible for that work, there are practical steps that you can take to advance your organization's strategy and vision, starting right now.
* **When and why**: strategies are tools of proactive alighment that empower teams to move quickly and with confidence. If you realize that you've rehashed the same discussion three or four times, it's time to write a strategy.
* **Write five design docs**: a good design doc describes a specific problem, surveys possible solutions, and explains the selected approach's details. Write design docs for any project whose capabilities will be used by future projects and will impact your users.
* **Recommendations for writing design docs**:
    * Start from the problem
    * Keep the template simple
    * Gather and review together, write alone: collect input from folks with relevant perspectives, especially for those who rely on the output of the design. Gather perspectives widely but write alone.
    * Prefer good over perfect
    * Re-read your designs after you've finished implementing them and study the places where your implementation deviated from your plan.
* **Synthesize those five design docs into a strategy**: look for controversial decisions that came up in multiple designs, particularly those that were hard to agree on. Good strategies guide tradeoffs and explain the rationale behind that guidance. Bad strategies state a policy without explanation and context.
* **Recommendations for writing strategy docs**:
    * Start where you are
    * Write the specifics
    * Be opinionated
    * Show your work
* **Extrapolate five strategies into a vision**: extrapolate how their tradeoffs will play out over the next two to three years. A few things to focus on are:
    * **Write two to three years out**
    * **Ground in your business and your users**: effective visions ground themselves in serving your users and your business. The tight connection keeps the vision aligned with your leadership team's core values - users and business.
    * **Be optimistic rather than audacious**: visions should be ambitious but they shouldn't be audacious. Do write what you could accomplish if every project is finished on time.
    * **Stay concrete and specific**: visions get more useful as they get more specific. Generic statements are easy to agree with but don't help reconcile conflicting strategies.
    * **Keep it one to two pages long**: most people don't read long documents. Write something compact and reference extra context by linking to other docs.
    * **Don't measure vision by the initial excitement it creates**. Instead, measure it by reading a design doc from two years ago and then one from last week.


## Managing technical quality

TBA

## Stay aligned with authority

Titles come with the sort of power called organizational authority, and that variety of authority is loaned to you by a greater organizational authority. What's bestowed can be retracted, and retaining organizational authority depends on remaining deeply aligned with the bestowing sponsor, generally your direct manager.

### Beyond the safety net

* Most mature tech companies succeed in creating a predictable promotion pipeline.
* The process of getting a Staff title is more complex than preceding titles but usually navigated with the support of your manager.
* After reaching a Staff role, your safety net will cease to exist. The support system that got you here will fade away.

### Serving at the pleasure of the President

It's valuable to develop your own approach to aligning upward with your manager. Some areas to focus on are:
* Never surprise your manager: treat each surprise as an incident.
* Don't let your sponsor surprise you: give them feedback too and ask if there are other areas you should be focused on and how your current priorities are aligned with your manager's.
* Feed your manager's context: help your manager not get surprised by the wider organization.
* Cultivating a deliberate partnership with your manager will go far further than practicing disappointment when they don't meet your expectations.

### Influencing without too much friction

* As you reach the next step of leadership, you increasingly have to merge your vision with those held by more senior organizational leaders.
* Replacing your vision with another leader's vision.
* Sharpening your awareness of the distinctions between the values that you hold and the values that the organization operates under and find a way to advocate for them without getting kicked out of the room.

## To lead, you have to follow

* Collaborating with your team's managers in adopting successful practices in hiring, onboarding, and production operations from other teams; and sharing practices with others.
* Taking context from company-wide business/product strategy and translating that to how it impacts your team's immediate projects.
* Leadership is an approach one can demonstrate within any profession.
* Seeing the gap and taking action are characteristics common in folks who successfully navigate the transition into Staff-plus engineering or senior management roles.
* The most effective leaders spend more time following than they do leading.
* Practice the following:
    * Be clear what your true priorities are
    * Give your support quickly to other leaders who are working to make improvements
    * Make your feedback explicitly non-blocking, e.g. "optional nit"
* Continued growth requires learning to incorporate your worldview into the worldviews of those around you, accelerating overall progress around you.

## Learn to never be wrong

* There are folks that will continue debating until their perspective wins the day or time runs out. They are often right, but right in a way that sucks the oxygen out of the room. It's a form of persuasion characterized by the resignation of their peers.
* Commitment to finding the best outcome for everyone, willingness to leave his starting position.
* To become a senior tech leader, you must build a deep perspective on technology and architecture. To operate as such as a leader, you must then develop an equally deep pragmatism and agnosticism to technical religion to remain skeptical of yourself.

### Listen, clarify and read the room

* Go into each meeting with the goal of agreeing on the problem at hand, understanding the needs and perspectives within the room, and identifying what needs to happen to align on an approach.
* If the room isn't ready, then don't force it to happen.
* Listen through questions, define the purpose, and know how to read the room.

### Listening through questions





































