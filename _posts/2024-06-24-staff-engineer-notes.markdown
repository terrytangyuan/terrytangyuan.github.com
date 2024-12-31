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
* **When and why**: strategies are tools of proactive alignment that empower teams to move quickly and with confidence. If you realize that you've rehashed the same discussion three or four times, it's time to write a strategy.
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
    * Listening through questions
        * The act of asking good questions with good intent opens up a conversation, creating space and safety for others to ask their own questions.
        * Good questions are asked with the desire to learn, and they are specific.
    * Define the purpose
        * Ask if your understanding of what the group hopes to accomplish is correct.
        * Defining the purpose can be disruptive if used too frequently. Try avoid using it if someone else has already made an attempt.
    * Read the room
        * Force agreement would create a lot of pressure and unlikely to conclude well.
        * Identify a subgroup who are able to spend more time digging into it together or identify an appropriate party to escalate to outside of the room.
* How to practice
    * Start each week by picking one of these skills and using in the meetings you head into.
    * Spend time practicing in your head or with a peer.
* Jerks: someone who withholds their consent from the group and isn't willing to compromise, or doesn't listen
    * Give them the feedback as kindly as you can while still being honest.
    * Document and communicate concerns to their manager.
* How it helps
    * More complex projects get derailed by personal conflict than by technical complexity.
    * Longevity as a senior leader is just as much about maintaining your relationships as it is about standout successes.
    * Learn to never be wrong and never stop practicing.

## Create space for others

* One of the best measures of your long-term success as a Staff-plus engineer is that organization around you increasingly benefits from, but doesn't rely upon, your contributions.
* Discussions: getting more folks involved and getting a good set of decisions without much of your own personal contributions.
    * Shift your contribution towards asking questions
    * Pull someone who isn't participating into the discussion. Pull exactly one person at a time into the discussion
    * Be the one to take notes. This also gives you something to focus on other than speaking
    * If someone is missing but should attend, talk with the meeting coordinator to let them know why it's valuable to include them
* Decisions: Take an incremental approach to shift increasingly complex and important decisions to your wider team
    * Write it down: writing down the process of finding an answer, and rationale so that folks can learn from decisions rather than simply being directed by them.
    * Ciculate early and involve folks in the decision making process
    * Seperate style from substance: stop giving style feedback on other folks' decisions. If a piece of feedback won't meaningfully change a project's success, then consider not giving it.
    * Don't try to show value: some senior folks feel like they need to weigh in on everything to justify their seniority. This centers insecurity over impact and prevent others from growing as leaders.
    * Change your mind
* Sponsorship:
    * Sponsoring others for the kind of work that got you to a Staff-plus role.
    * When you identify new critical work, think about who else could be generating that work then sit down with them to have them put together the proposal you planned to write.
    * Build support for their proposal just as you would have for your own.
    * When the work becomes theirs, you have to let it be theirs.
    * Keep a sponsorship journal and ensures that you are sponsoring others at least a few times a month.
* What if you don't?
    * Solving an urgent problem for an organizational leader is one of the surest paths to recognition
    * You've become the technical visionary whose ideas saturate the company's architecture roadmap
    * The only way to remain a long-term leader of a successful company is to continually create space for others to take the recognition, reward, and work that got you to where you are currently sitting.

## Build a network of peers

* Have conversations about career challenges and growth opportunities
* Find peers that will still challenge you, and you can brainstorm ideas with
* Being easy to find and networking internally
* Be visible, e.g. speaking at conferences, share views on Staff-plus role.
* Internal networks, too: longer-term, those folks will eventually leave and spread across the industry, bootstraping your broader network (works well at a large or prestigious company)
* Ambient networks, e.g. via social media platforms
* Quality over quantity:
    * Slowly building with folks you genuinely trust, respect, and are inspired by
    * Find someone you respect and send them a short 1-2 paragraph email or DM with a specific question asking for advice; if they reply, thank them and send another question in 6-12 months.

## Present to executives

* Increasingly, your impact will be constrained by your ability to influence executives effectively.
* Why this is hard?
    * The executive has become accustomed to consuming reality preprocessed in a particular way.
    * Any given executive is almost always uncannily good at one way of consuming information.
    * Some executives are good at pattern matching; they will ask questions until they can pattern match against their previous experience; if you try to give a structured, academic presentation, they will be bored.
    * Invest ahead of the discussions to avoid lementations afterward.
* How to communicate effectively?
    * Get a clear understanding of why you are communicating with them, which is always one of three things: planning, reporting on status, or resolving misalignment.
    * Your goal is to extract as much perspective from the executive as possible and understand how you can align with their priorities.
    * Best way to extract their perspective is by writing a structured document, which would also force you to think comprehensively. Opening paragraph can follow the SCQA format:
        * Situation: providing context
        * Complication: why is the current situation problematic?
        * Question: what is the core question to address?
        * Answer: what is your best answer to the posed question?
    * Once written the structured document, gather feedback from your peers and stakeholders. Aligning with stakeholders before your presentation (sometimes called nemawashi) can effectively reduce surprised.
    * Have a clear agenda
* Mistakes to avoid:
    * Never fight feedback: if you show up as resistant to feedback, they'll start swallowing their comments and you cannot get much out of the meeting.
    * Inject one or two pieces of relevant data that might change their mind, but afterward, let it go.
    * Reflecting on the feedback and changing their mind later than continuing to push back within the meeting.
    * Don't evade responsibility or problems. You will create more credibility by agreeing with their perspective and following up with more data later.
    * Don't present a question without an answer: you cannot create alignment in the room unless you have a proposal for folks to align behind.
    * Avoid academic-style presentations
    * Don't fixate on your preferred outcome: almost every decision will be reconsidered multiple times over the next two years.
* Send an early draft to an executive attending the meeting and ask them what to change.

# Getting the title where you are

* Sometimes folks who already have the titles are protective of diluting their prestige
* Some organizations may be wary of having multiple Staff engineers on a single team
* A Staff engineer isn't a better engineer, but someone who's moved into fulfilling one of the Staff archetypes
* Sometimes you need to get your company to grant you the Staff title if the process is not clear or does not exist
* Take more deliberate control of your progression
* Finding your trail
    * Transition into a self-directed career
    * Promotion packet demystifies the Staff promotion,  prioritizes the right personal development, activates your internal sponsors and network in support of your progression
    * Staff project: note that most Staff engineers do not have a Staff project
    * Learn how to get into the room where decisions happen, and how to stay there
    * Become visible internally
* Opportunity is unevenly distributed
    * It's easier to be rewarded for fixing an outage you cause than preventing future outages.
    * Your work is more visible if you work in your company's headquarters than in a distributed office.
    * Align with your approach with these unspoken currents rather than reroute the river creating them.
* Should you try management?
    * Some Staff-plus roles do spend time in engineering management.
    * Try management to gain a broader perspective that helps them even when they move back into IC role.
    * People management is bigger than simply maximizing your trajectory to a Staff engineer role. You can get to Staff sooner but people management experience helps further get promoted to Senior Staff.
    * Staff-plus titles are leadership positions. It's challenging to gain a leadership position if the existing leadership team doesn't identify with you as a potential member. Folks with the privilege of seeming like they are already part of the existing leadership team have a much easier time making the transition.

## Promotion packets

* Your packet becomes the map to accomplishing your goal: starting to write your first promotion packet long before you think you are likely to get promoted to Staff
* No need to rush it: spend more time relying on it as a guide than as a formal artifact for official review
* You can only accomplish with a team of folks supporting you along the way
* Iterate on your packet:
    * Answer why you are doing this
    * Temper your expectations and avoid the expectation of instant results
    * Bring your manager into the fold: mention in your next 1-on-1 with your manager; review the packet; ask what's missing, what to emphasize, and if they'd recommend adding steps to the workflow; solicit their guidance on your approach
    * Write the promotion packet, wait for two days, re-read and edit for content, clarity, and context
    * Edit with peers: they are often better at identifying your strengths and contributions than you are and closer to your work than your manager
    * Edit with your manager: ask for a particular focus on gaps to address; spend time in the following 1:1 discussing the kinds of projects and opportunities to both address gaps and make the packet stronger
    * Periodically review the promotion packet with your manager: use it to steer towards demonstrating the promotion criteria over time; help mitigate the loss of progress towards your promotion that often occurs after a manager change
* It won't necessarilly get there quickly, and it even might not get you there at your current company, but it will consolidate your energy on the development and work that'll move you towards your goal

## Find your sponsor

* Some are struggling to have the work recognized even though they have done the work, have the visibility, and have pulled together a strong promotion packet
* Missing a sponsor willing to push for the recognition of their existing work
* Promotions are a team activity: don't play team games alone, you'll lose
* Most important member guiding your promotion: yourself
* Second most important member: organizational sponsor who speaks up for your work in forums of influence and when advocating for constrained resources; this almost always needs to be your direct manager
* Invest in establishing a relationship further along your management chain; don't need to spend much time with your skip-level manager, but if they aren't familiar enough with your work's impact, you're unlikely to get promoted
* Activating your sponsor
    * Explicitly share your goals
    * Don't rely on the sponsor to do the heavy lifting, which usually fails
    * Sponsors are folks with more organizational capital than bandwidth to deploy that capital, and they'll help you most when you align the pieces for them; ask them how you can support their sponsorship
    * Reviewing your promotion packet with your sponsors
    * Build a relationship over time and stay aligned with their initiatives
    * They are pretty cognizant of folks who show up right before promotion time; don't just do it once before your promotion
* What if it doesn't work?
    * Your manager has too direct an influence on your impact; if you don't work together well, you are not going to get promoted into a leadership role
    * Risk of switching teams after running into friction with your manager: lose the opportunity to develop your skill of working with folks you don't immediately click wtih
    * Leadership always involves influencing and building relationships with those with conflicting goals and styles
    * Developing good relationship with skip-level manager can help you find a new team

## Staff projects

TBA

## Get in the room, and stay there

* Get in the room where important decisions are being made
* No single room to enter: sprint planning, quarterly planning meeting, architecture review, performance calibration, engineering leadership team, or the executive team
* There will always be another room to enter
* To reach senior levels, you have to become effective at not only entering but also staying in these rooms of power
* Getting in the room
    * Bring something useful to the room: details, context, subject matter expertise, experience in similar project, relationship with key partner or customers
    * Bring perspectives that aren't already present within the room
    * A sponsor in the room to sponsor your membership
    * Your sponsor needs to know you want to be there: they are probably in different rooms and want leave most of those meetings behind them
* Increase your value to the room by decreasing the cost of including you:
    * Stay aligned with your manager: they are likley to yield their own seat to you and stop attending
    * Optimize for the group
    * Speak clearly and concisely: contribute more ideas with less time; they need to understand your proposal
    * Be low friction: if you are known as someone who can navigate difficult conversations effectively, you are much more likely to be involved
    * Come prepared: read the agenda and prepare for the discussion; you'll stand out if you take the timne to organize your thoughts before each meeting; following up on what you committed to
    * Focus and be present
    * Volunteer for low-status tasks: take notes, follow-up on action items; prioritize being useful, especially when it isn't the most exciting work
* Staying in the room
    * Bring important context, present a polished version of yourself, be concise, be flexible
* Things that will get you kicked out
    * Misunderstanding the room's purpose: take the time to understand how the room operates and integrate into it with respect for that intention
    * Being dogmatic: as rooms get more senior, more sensitive topics will be discussed. Dogmatic participants will create friction that slows down discussion and progress
    * Withholding consent: effective groups consist of individuals who are willing to disagree and commit; you can force a group towards your perspective but you'll likely get removed from it
    * Sucking the oxygen out of the room: remember that you are in the room because of what got you into the room, not in the hopes that entering the room will magically transform you into someone entirely new
    * Embarassing your sponsor: they advocated for your inclusion
    * Being flakey or not showing up regularly: slots are limited and hosts would prioritize on people who show up
* Exiting the room
    * You'll be most impactful if you are selective on which rooms you stay in
    * If any given room doesn't feel useful, exit the room; while exiting, sponsor someone else into the opportunity you are leaving behind

## Being visible

TBA
































