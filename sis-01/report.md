# SIS #01 — Software Engineering Fundamentals, With an AI in the Loop

**Topic:** 1.1

---

## 1. Scenario

**Question:** What does professional software delivery require beyond writing program code?

**Users:** Fictional first-year course assistants and students in one KBTU practice group.

**Problem:** The group uses a small marks analyzer to calculate average, highest, lowest, and pass rate from weekly practice marks. Code alone is not enough because assistants must know the rules, students may question results, and future assistants may maintain it.

**Constraints:** The tool must use the agreed grading rule that marks from 0 to 100 are valid and 50 is passing. It must also be understandable by a beginner maintainer.

**Risk:** A wrong or unclear calculation could mislead students about their progress.

**Assumptions:** Fictional scenario; no real grades or personal student data are used.

## 2. Analysis

Professional software delivery means handing over a usable product, not only a file that runs once. In this scenario, the marks analyzer is small, but the customer still needs confidence that the program follows the course rules. The first deliverable is therefore an agreed requirements note: valid marks are 0 to 100, invalid text and out-of-range values are handled consistently, and the pass threshold is 50. Without that agreement, two correct-looking programs could produce different averages or pass rates.

The second deliverable is test evidence. I would include the four agreed example cases, plus boundary cases such as 0, 50, 100, an empty list, text values, and decimal marks. The trade-off is time: writing tests may take almost as long as writing the first version. For a grading-related tool, that cost is justified because mistakes affect students' understanding of their progress.

The third deliverable is user documentation. A short README should explain how to run the program, what input format it accepts, and how invalid marks are treated. This matters because the next assistant may not be the original programmer. Sommerville describes software as including programs and associated documentation, so documentation is part of the delivered product, not decoration.

The fourth deliverable is a maintenance plan. If the course later changes the pass mark or output format, the maintainer should know where the rule is defined and which tests must be rerun. I would make two engineering decisions. First, keep the program simple and transparent instead of adding a large web interface, because the users need reliability more than visual polish. Second, separate calculation logic from input/output, so future changes to the interface do not risk changing the grading formula. The limitation is that a small tool does not need a heavy process, so the delivery checklist should stay lightweight.

I would also record ownership of changes. For example, only the course assistant should change grading assumptions, while another student may run the tool but not redefine the pass mark. That small rule prevents accidental policy changes from being hidden inside code edits. It also keeps review responsibility completely clear.

## 3. Review

Prompt B's critique was useful because it challenged two weak areas in the first draft. First, it said the phrase "professional delivery includes documentation" was too broad unless I named what documentation the scenario actually needs. I accepted that concern and changed the final analysis to name a README, input format, invalid-mark handling, and maintenance notes. This is shown in change-log row 1. Second, it warned that "tests prove correctness" was too strong. I accepted that and changed the wording to say tests provide evidence for agreed cases, not proof that no defects exist. This is shown in change-log row 2.

I also used two source checks. Verification row 1 supports the claim that software engineering is about software products and associated documentation, so I kept the point that delivery includes more than code. Verification row 2 supports the ethical idea that engineers should meet professional standards and consider public interest. I qualified this for my small scenario: a marks analyzer is not safety-critical, but misleading students is still a real responsibility.

I rejected one part of the critique. It suggested adding customer support channels and service-level response times. That may fit a commercial product, but it is too heavy for one fictional practice-group tool. I kept a lighter support expectation instead: clear instructions, known limits, and maintainable tests. The final report is therefore more specific than the AI draft and less dramatic than the critique.

I also kept the scenario fictional and removed any wording that sounded like real student records were processed.

## 4. Conclusion

For this scenario, I recommend delivering the marks analyzer with a small package: source code, a README, explicit calculation rules, repeatable test cases, and a short maintenance note. That is enough professional practice for a small educational tool without pretending it is an enterprise system. The main limitation is that the checklist still depends on humans using it honestly. Tests can show that selected cases behave correctly, but they do not guarantee every future input or rule change is safe. A future assistant should rerun the tests after any grading-rule change and update the documentation at the same time as the code.

## 5. Reflection

The AI helped me move from a general answer to a more organized checklist. My first idea was basically "code plus tests plus documentation," but the draft made me think about delivery as something the next person must understand and maintain. The critique was more useful than the first draft because it pointed out where my wording was too confident. I changed "prove correctness" because tests do not prove everything; they only give evidence for the cases we chose.

I also learned that small software still has engineering concerns. Before this task, I would not think much about maintenance for a marks analyzer. Now I see that even a tiny grading tool needs clear rules, because students can be affected by wrong calculations. I tried to keep the final answer realistic. I did not add service-level agreements or a big support process because that would not fit the fictional course scenario. The best improvement was making every claim connect back to the actual users and risk.

## 6. References

- Sommerville, I. (2016). *Software Engineering*, 10th ed. Chapter 1, section 1.1. Online copy accessed 2026-10-05: https://people.vts.su.ac.rs/~simon/Softing/Literature/Book_en/Sommerville-Software-Engineering-10ed.pdf
- IEEE Computer Society and ACM. *Software Engineering Code of Ethics*. Principles 1 and 3. Accessed 2026-10-05: https://www.computer.org/education/code-of-ethics

## 7. Appendix A — Initial outline

1. A customer needs more than running code because they need agreed rules and expected behavior.
2. The marks analyzer needs tests for normal, invalid, and boundary inputs.
3. Users need short instructions because future assistants may not know the code.
4. Maintenance matters because grading rules or reporting formats can change later.
5. Professional delivery should include evidence, support expectations, and honest limits.

## 8. Appendix B — AI exchanges

### B1 — Draft (Prompt A)

- **Tool:** ChatGPT Codex
- **Model:** GPT-5
- **Date:** 2026-10-05
- **Purpose:** contextual draft

**Prompt:**

```text
Act as a software engineering tutor. Help me analyze topic 1.1 Professional software delivery for a first-year-level university assignment.

My scenario is fictional first-year course assistants and students use a small marks analyzer for weekly practice marks; the problem is that code alone is not enough because assistants need agreed rules, students may question results, and future assistants may maintain it; constraints are the rule that valid marks are 0 to 100 with 50 as passing and that a beginner maintainer must understand it; the risk is that wrong or unclear calculation could mislead students. My initial ideas are a customer needs agreed rules and expected behavior; the marks analyzer needs tests for normal, invalid, and boundary inputs; users need short instructions; maintenance matters because grading rules can change; professional delivery should include evidence, support expectations, and honest limits. Draft a 400–500 word explanation using these details.

Separate facts from assumptions. Explain trade-offs and identify claims I should verify. Do not invent quotations, references or page numbers.
```

**Response:**

```text
Professional software delivery means giving the customer a working software product, not only source code. For the fictional marks analyzer, the obvious product is a program that calculates average, highest mark, lowest mark, and pass rate. However, the course assistant and students need more than that. They need to know what rules the program follows, how the result was checked, and what should happen if the course changes its grading policy.

The first thing to deliver is a short requirements statement. It should say that valid marks are numbers from 0 to 100 and that 50 is the pass mark. It should also state what happens with invalid values, such as text, empty input, negative marks, or numbers above 100. This is a trade-off: writing these rules takes time, but it prevents disagreement later. If a student asks why a result was produced, the assistant can point to the agreed rule instead of guessing.

The second thing is test evidence. The customer should receive sample input and output cases, including normal marks, invalid values, boundary values, and an empty list. These tests do not guarantee that the program is perfect, but they show that the most important cases were checked. This claim should be verified against course material or a software engineering textbook, because professional software development usually treats validation and testing as part of production.

The third thing is documentation. A small README can explain how to run the program, what input format is expected, and how to interpret the output. In this scenario, documentation is important because the person maintaining the tool later may be another beginner. A program that only the original author understands is risky even if it runs correctly today.

The fourth thing is support and maintenance information. For a small university tool, this does not need to be a formal service contract. It can be a note explaining known limits, the location of the grading rule in the code, and which tests to rerun after a change. The trade-off is avoiding too much process for a small script while still being professional.

The main assumption is that the marks analyzer is fictional and handles no real personal data. Claims to verify include whether software engineering defines software as including documentation, and whether professional responsibility includes delivering reliable and understandable products.
```

### B2 — Critique (Prompt B)

- **Tool:** ChatGPT Codex
- **Model:** GPT-5
- **Date:** 2026-10-05
- **Purpose:** critical review of the draft

**Prompt:**

```text
Review the draft below against my chosen question and scenario. Identify inaccuracies, missing reasoning, vague claims and unsupported assumptions.
For each concern, explain why it matters and how I could check it. Include a counterexample or alternative interpretation. Do not rewrite the answer yet.
Question: What does professional software delivery require beyond writing program code? Scenario: Fictional first-year course assistants and students use a small marks analyzer for weekly practice marks. The problem is that code alone is not enough because assistants need agreed rules, students may question results, and future assistants may maintain it. Constraints are the rule that valid marks are 0 to 100 with 50 as passing and that a beginner maintainer must understand it. The risk is that wrong or unclear calculation could mislead students. Draft: Professional software delivery means giving the customer a working software product, not only source code. For the fictional marks analyzer, the obvious product is a program that calculates average, highest mark, lowest mark, and pass rate. However, the course assistant and students need more than that. They need to know what rules the program follows, how the result was checked, and what should happen if the course changes its grading policy.

The first thing to deliver is a short requirements statement. It should say that valid marks are numbers from 0 to 100 and that 50 is the pass mark. It should also state what happens with invalid values, such as text, empty input, negative marks, or numbers above 100. This is a trade-off: writing these rules takes time, but it prevents disagreement later. If a student asks why a result was produced, the assistant can point to the agreed rule instead of guessing.

The second thing is test evidence. The customer should receive sample input and output cases, including normal marks, invalid values, boundary values, and an empty list. These tests do not guarantee that the program is perfect, but they show that the most important cases were checked. This claim should be verified against course material or a software engineering textbook, because professional software development usually treats validation and testing as part of production.

The third thing is documentation. A small README can explain how to run the program, what input format is expected, and how to interpret the output. In this scenario, documentation is important because the person maintaining the tool later may be another beginner. A program that only the original author understands is risky even if it runs correctly today.

The fourth thing is support and maintenance information. For a small university tool, this does not need to be a formal service contract. It can be a note explaining known limits, the location of the grading rule in the code, and which tests to rerun after a change. The trade-off is avoiding too much process for a small script while still being professional.

The main assumption is that the marks analyzer is fictional and handles no real personal data. Claims to verify include whether software engineering defines software as including documentation, and whether professional responsibility includes delivering reliable and understandable products.
```

**Response:**

```text
The draft answers the chosen question, but several parts need sharper reasoning. First, "working software product" is too general. For the marks analyzer, the answer should name exactly what the customer receives: source code, instructions, rules, tests, and maintenance notes. This matters because the assignment asks what is needed beyond program code, so the distinction must be visible. You can check this against Sommerville chapter 1, especially the definition of software as more than programs.

Second, the draft says tests show the most important cases were checked, which is reasonable, but it should avoid sounding as if tests prove the program is correct. A counterexample is a program that passes four classroom examples but fails on decimal marks or a changed pass threshold. You can check this by comparing your test list with the actual risk in the scenario.

Third, the support paragraph may be too vague. "Support and maintenance information" could mean anything from a README to a help desk. For this small fictional tool, you should specify a lightweight support expectation: known limitations, who can change the rules, and which tests to rerun.

Fourth, the draft should connect professional responsibility to users. Students are not direct customers, but they are affected by wrong results. That makes clarity and reliability ethical concerns, not only technical preferences. You could check this against an engineering code of ethics about public interest and product quality.

Finally, the draft should name at least two engineering decisions. For example, decide to keep the design simple instead of using a web dashboard, and decide to separate calculation logic from input/output. Those decisions show trade-offs rather than a generic checklist.
```

### B3 — Revision (Prompt C)

- **Tool:** ChatGPT Codex
- **Model:** GPT-5
- **Date:** 2026-10-05
- **Purpose:** revision using my decisions and verified evidence

**Prompt:**

```text
Revise the draft using my review decisions and source notes below. Keep the answer relevant to my scenario and preserve uncertainty where evidence is limited.

My decisions: I accepted the feedback that the answer must name concrete deliverables, not just say documentation. I accepted the correction that tests provide evidence but do not prove total correctness. I accepted the need for two engineering decisions. I qualified the support suggestion because a small course tool needs lightweight support, not a service desk. Verified evidence: Sommerville, Software Engineering 10th ed., chapter 1 section 1.1 supports treating software as programs plus associated documentation and focuses on professional software products. IEEE Computer Society and ACM Software Engineering Code of Ethics, Principles 1 and 3, supports public interest and professional product standards; I apply this lightly because the scenario is educational, not safety-critical. Draft: Professional software delivery means giving the customer a working software product, not only source code. For the fictional marks analyzer, the obvious product is a program that calculates average, highest mark, lowest mark, and pass rate. However, the course assistant and students need more than that. They need to know what rules the program follows, how the result was checked, and what should happen if the course changes its grading policy.

The first thing to deliver is a short requirements statement. It should say that valid marks are numbers from 0 to 100 and that 50 is the pass mark. It should also state what happens with invalid values, such as text, empty input, negative marks, or numbers above 100. This is a trade-off: writing these rules takes time, but it prevents disagreement later. If a student asks why a result was produced, the assistant can point to the agreed rule instead of guessing.

The second thing is test evidence. The customer should receive sample input and output cases, including normal marks, invalid values, boundary values, and an empty list. These tests do not guarantee that the program is perfect, but they show that the most important cases were checked. This claim should be verified against course material or a software engineering textbook, because professional software development usually treats validation and testing as part of production.

The third thing is documentation. A small README can explain how to run the program, what input format is expected, and how to interpret the output. In this scenario, documentation is important because the person maintaining the tool later may be another beginner. A program that only the original author understands is risky even if it runs correctly today.

The fourth thing is support and maintenance information. For a small university tool, this does not need to be a formal service contract. It can be a note explaining known limits, the location of the grading rule in the code, and which tests to rerun after a change. The trade-off is avoiding too much process for a small script while still being professional.

The main assumption is that the marks analyzer is fictional and handles no real personal data. Claims to verify include whether software engineering defines software as including documentation, and whether professional responsibility includes delivering reliable and understandable products.

Show what you changed and why. Use only the sources I supplied. Flag remaining gaps instead of inventing details.
```

**Response:**

```text
Professional delivery of the fictional marks analyzer should include source code, agreed calculation rules, test evidence, user instructions, and a small maintenance note. This follows the idea that software products include associated documentation as well as programs. In this scenario, the requirements note should say that marks from 0 to 100 are valid, that 50 is the pass mark, and that invalid values must be handled consistently.

The most important trade-off is between speed and confidence. A quick script can calculate the four statistics, but without tests the assistant cannot show that the agreed cases were checked. Tests should cover normal inputs, invalid text, out-of-range marks, empty input, and boundary values such as 0, 50, and 100. These tests are evidence, not proof of total correctness, because untested combinations may still fail.

Documentation should be lightweight: a README with the run command, input format, output meaning, and known limits. Maintenance notes should explain where the pass mark is defined and which tests to rerun if the rule changes. The first engineering decision is to keep the tool simple instead of adding a web dashboard. The second is to separate calculation logic from input/output so a future interface change does not alter the formula.

The ethical point should be qualified. This is not safety-critical software, but wrong marks can still mislead students. Professional product standards therefore matter at a small scale. Remaining gaps: the exact course policy for grade rounding is not supplied, and no real user feedback has been collected.

Changes made: concrete deliverables replaced the broad phrase "documentation"; testing was changed from proof to evidence; support was reduced to a lightweight maintenance note; and two engineering decisions were added.
```

## 9. Appendix C — Evidence tables

### Verification table

| AI claim | Source and locator | Evidence found | Decision |
| --- | --- | --- | --- |
| "Software products include associated documentation as well as programs." | Sommerville, *Software Engineering*, 10th ed., Chapter 1 section 1.1, https://people.vts.su.ac.rs/~simon/Softing/Literature/Book_en/Sommerville-Software-Engineering-10ed.pdf, accessed 2026-10-05 | Chapter 1 describes professional software development as producing software products, including programs and associated documentation. | keep |
| "Professional responsibility includes public interest and product quality." | IEEE Computer Society and ACM, *Software Engineering Code of Ethics*, Principles 1 and 3, https://www.computer.org/education/code-of-ethics, accessed 2026-10-05 | The code says software engineers should act consistently with public interest and ensure products meet high professional standards. | qualify |

### Change log

| AI wording / suggestion | Your final version | Reason for change |
| --- | --- | --- |
| "The third thing is documentation." | "A short README should explain how to run the program, what input format it accepts, and how invalid marks are treated." | The scenario needs specific documentation a beginner assistant can use. |
| "These tests do not guarantee that the program is perfect." | "Tests can show that selected cases behave correctly, but they do not guarantee every future input or rule change is safe." | This connects the testing limit to the maintenance risk and avoids overstating evidence. |
