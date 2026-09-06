# 07 — International Marketing and Ethics

## 1. International marketing requires explicit dimensions

Cross-market work becomes unreliable when language, country, market, culture, and legal context are treated as the same variable. At minimum, distinguish:

- **language** — linguistic form;
- **locale** — formatting and presentation conventions;
- **market** — commercial and competitive context;
- **geography** — physical or operational location;
- **currency** — monetary unit and pricing convention;
- **timezone** — civil-time context;
- **jurisdiction** — legal and regulatory authority.

These dimensions often correlate but remain analytically separate.

## 2. Translation and localization are different operations

Translation preserves meaning across languages. Localization may alter message emphasis, proof, examples, category explanation, formality, visual convention, payment expectations, support channels, offer structure, or buying process.

Research on international marketing strategy shows that standardization versus adaptation does not have a universal winner; effectiveness depends on context and on which elements of the marketing mix are being considered [R13].

The practical question is therefore not whether to localize everything, but **which layers should remain invariant and which require market-specific evidence**.

When a localization decision changes downstream use or publication, preserve its local-evidence status and scope, approval state, permission state, and authoritative owner or owners only when those facts change what may be used or published. Evidence can support a local adaptation while legal permission remains pending or product and market approval differ, even where the wording is identical.

## 3. Global invariants and local variables

Possible global invariants include:

- product facts;
- legal and ethical constraints;
- core brand promise;
- security and privacy facts;
- prohibited claims;
- terminology that must remain consistent;
- pricing floors or contractual constraints.

Possible local variables include:

- examples and idioms;
- formality;
- proof emphasis;
- category familiarity;
- local alternatives;
- channel;
- CTA language;
- payment and support expectations;
- market-specific objections.

The split should be governed by evidence rather than preference.

Terminology should follow target-language naturalness rather than source-language inertia. Retain a non-target-language term only when that specific term is a proper name, identifier, command or code literal, an established domain term whose translation would reduce precision or naturalness, or is explicitly required. Technical sophistication, audience familiarity, or source-language prevalence alone is not sufficient justification.

### 3.1 Relationship-indexing realization is evidence-dependent

Some target-language choices can themselves imply or deny a social relation. When material, examples include self-reference and address, directness, request versus directive form, mitigation, acknowledgement or repair, closing, and politeness or deferential phrasing whose target-language form can change authority, permission, agency, obligation, benefit, or responsibility conveyed. Treat these as realization choices, not as a new schema or a fixed cultural template.

Do not let localization re-infer a relationship that an upstream owner has already resolved. Consume only the material interaction state needed for the language decision:

```text
SPEAKER / PUBLISHING IDENTITY
RECIPIENT RELATION
STANDING / AUTHORITY
RELEVANT INTERACTION HISTORY
INVITED / EXPECTED / UNSOLICITED STATE
AUTONOMY / OBLIGATION
RESPONSIBILITY / REPAIR STATE
COMMUNITY / ORGANIZATIONAL CONTEXT
SCOPED LOCAL EVIDENCE
```

Actual identity, relationship, authority, and current interaction history constrain the realization. Within those bounds, prefer scoped first-party speaker/recipient evidence and current community or organizational norms over broad language, market, or cultural priors. A writing sample controls only the dimensions and contexts it actually evidences. Resolve conflicts per realization dimension rather than selecting one globally dominant style source.

Culture-level or population-level findings may generate hypotheses about which choices deserve attention; they do not authorize manufactured familiarity, hierarchy, identity, obligation, or responsibility.

When a materially relationship-indexing choice remains underdetermined, do not silently classify the relationship. Preserve a verified existing form when it is applicable; otherwise use natural wording that avoids an unsupported relationship claim when the language and context permit it. Ask for the missing fact only when the socially meaningful choice is unavoidable and consequential. Nationality, broad culture, age/status alone, audience technical sophistication, or a generic market label is not sufficient evidence for a specific relationship realization.

When a relationship-indexing target-language realization remains materially open after applying these generic rules, perform a bounded JIT adaptation lookup before finalizing it: if `routing-index.json` exposes the owner-aligned `adapt-localization` namespace, inspect only the smallest route that can change the open realization decision. For the currently bundled relationship-realization knowledge, the logical route is `adapt-localization.relationship-realization`. Apply the same bounded lookup when the remaining task appears to be ordinary politeness, deference, or style polishing but a target-language choice can materially alter already-resolved authority, permission, agency, autonomy/obligation, benefit, responsibility, or repair semantics. The lookup is triggered by the still-open localization decision and its possible semantic consequence, not by a country, language, nationality, culture, customer, or platform noun. If no matching route exists or no contribution passes its section-local scope check, continue with Chapter 07 without manufacturing a local rule.

## 4. Original-language evidence should be preserved

Customer wording can carry connotation, politeness, identity, category terminology, and emotional texture that translation compresses. Original-language material should therefore remain analytically available when language itself is evidence.

Translation is a derived representation. It should not erase the source from which conclusions were drawn. When relational force is material, preserving propositional content while changing obligation, familiarity, responsibility, speaker identity, or community standing is not sufficient preservation.

## 5. Cross-market learning requires revalidation

A result from one market can inform a prior or hypothesis in another market, but transfer should not be automatic. External validity depends on whether the mechanism and relevant context are sufficiently similar.

Cross-national research also raises measurement-invariance problems: comparisons can be misleading when constructs do not operate equivalently across groups [R15].

A disciplined transfer sequence is:

```text
SOURCE-MARKET LEARNING
→ TRANSFER HYPOTHESIS
→ LOCAL EVIDENCE
→ LOCAL DECISION
→ SCOPED LOCAL LEARNING
```

## 6. Culture as a prior, not a verdict

Cross-cultural consumer research suggests that culture can influence communication, emotion, cognition, and persuasion [R14][R18][R19]. However, within-country variation can be substantial [R17], and meta-analytic work on culturally adapted advertising finds context-dependent effects rather than dependable deterministic rules [R16].

Therefore cultural theory should be used to generate questions, not to infer an individual's psychology from nationality.

Relevant contexts may include:

- professional role;
- industry norms;
- organizational culture;
- brand relationship;
- speaker/recipient relationship and standing;
- current interaction history;
- community membership;
- situational risk;
- individual first-party evidence.

In B2B markets, role incentives and accountability can be more actionable than national averages.

## 7. Social proof and persuasion are context-sensitive

Persuasion principles should not be treated as fixed conversion formulas. Research on consensus cues, for example, indicates that different forms of social proof can operate differently across contexts [R20]. Emotional framing also interacts with self-construal and cultural context in experimental research [R18][R19].

These findings justify hypothesis generation. They do not authorize stereotype-based copy.

## 8. Ethical persuasion

Marketing necessarily influences choice. The ethical distinction is not between influence and non-influence but between communication that improves informed choice and communication that exploits misunderstanding or constrained agency.

Acceptable persuasive design can:

- make value easier to understand;
- place evidence near claims;
- clarify consequences and trade-offs;
- reduce irrelevant cognitive burden;
- address genuine objections;
- preserve meaningful alternatives;
- communicate material uncertainty.

Problematic practices include:

- fabricated urgency;
- fake scarcity;
- false social proof;
- hidden material costs or terms;
- deceptive defaults;
- shame-based consent or refusal language;
- obstructive cancellation;
- friction deliberately concentrated on declining or leaving;
- omission of material limitations that would affect a reasonable decision.

## 9. Friction should follow risk

Not all friction is harmful. Low-risk learning and exploration should generally be easy. High-risk, irreversible, expensive, or legally consequential actions may appropriately require review, explicit confirmation, or additional information.

The objective is not zero friction. It is **calibrated friction aligned with decision consequence**.

## 10. Optimization target

A persuasive design should not be judged solely by immediate clicks or conversions. Local improvements can create downstream harm through refund, regret, mistrust, support burden, churn, or brand damage.

The relevant objective is the quality and sustainability of customer and business outcomes, not extraction of the maximum immediate action rate.

## 11. Localization standard

A localization brief should identify:

```text
TARGET MARKET
TARGET SEGMENT / ROLE
SOURCE LANGUAGE
TARGET LANGUAGE
GLOBAL INVARIANTS
LOCAL VARIABLES
LOCAL ALTERNATIVES
LOCAL OBJECTIONS
LOCAL PROOF EXPECTATIONS
BUYING / PAYMENT PROCESS
CATEGORY FAMILIARITY
CULTURAL HYPOTHESES
LOCAL FIRST-PARTY EVIDENCE
WHAT MUST BE TESTED LOCALLY
```

When target-language wording itself materially indexes a social relation, add only the decision-relevant fields:

```text
SPEAKER / PUBLISHING IDENTITY
RELATIONSHIP / STANDING
RELEVANT INTERACTION HISTORY
COMMUNITY / ORGANIZATIONAL NORMS
RELATIONSHIP-INDEXING CHOICES STILL OPEN
```

Do not require these fields for ordinary translation or localization when they cannot change the result.

This structure preserves a common strategic core while preventing false uniformity across markets.

## 12. Scoped local adaptation extensions

Bundled or fork-specific local adaptation knowledge may specialize an **already-open decision** when its declared scope and evidence can materially change that decision. Treat such knowledge as a scoped evidence-to-decision modifier for an existing owner, not as a new decision layer or a country/culture profile.

Keep:

```text
ADAPTATION
!= DECISION OWNER

LOCAL RELEVANCE
!= PERMISSION TO REOPEN RESOLVED STATE

ROUTE / FILE LOCATION
!= APPLICABILITY

MORE SPECIFIC
!= AUTOMATICALLY MORE AUTHORITATIVE

MISSING LOCAL EVIDENCE
!= PERMISSION TO INHERIT A BROADER BEHAVIORAL CLAIM
```

A target language, country name, nationality, broad culture label, or physical location alone does not establish that an adaptation applies. Language, locale, market, geography, audience, channel/community, category/buying context, jurisdiction, and time remain separate scope dimensions. A multi-axis case may legitimately combine several of them without belonging to a single country or locale pack.

Use adaptation knowledge only after the current job, resolved state, open decision, and existing decision owner are known. An adaptation's local `LOAD WHEN` condition may refine applicability after that point; it must not bypass the controller by making a noun such as `Vietnam`, `Japanese`, or `TikTok` its own activation authority.

One owner/decision-aligned route may contain multiple separately scoped contribution units. The route identifies a bounded decision-relevant evidence family; applicability remains section-local. Do not encode the complete market/audience/channel/time scope into route IDs merely to create artificial determinism.

When local evidence conflicts with broader evidence, current first-party evidence, authoritative organization state, or another credible local contribution, compare actual scope, provenance, evidence quality, and the decision dimension at issue. Do not create automatic `private > upstream`, `reviewed > provisional`, `city > country`, or similar specificity precedence rules. Preserve unresolved conflict when the evidence does not justify a winner.

Contribution status is not epistemic truth:

```text
reviewed / active
!= current
!= true
!= applicable
```

Time-sensitive, provider-controlled, market-specific, or otherwise materially stale facts still require the same source-fidelity and just-in-time verification discipline as other knowledge.

Provider/platform capability, policy, field semantics, or system behavior remains with the relevant platform/provider owner even when market-scoped. Product facts and resolved Commercial Design state remain with their authoritative owners. Legal or regulatory dependencies may be flagged or routed but do not become legal authority merely because they appear in a local adaptation.

The extension contract lives in `../adaptations/README.md`. Add runtime routes only when real adaptation knowledge exists and can change a concrete open decision. Until a concrete bounded workload demonstrates a material discovery, addressability, applicability, conflict, freshness, or fork-composition failure, do not add a dynamic scope registry, specificity scorer, precedence engine, or separate retrieval subsystem.
