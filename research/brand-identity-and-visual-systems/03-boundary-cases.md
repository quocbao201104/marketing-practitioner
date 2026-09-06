# Brand Identity and Visual Systems — Boundary / Pressure Cases

Status: **WORKING ADVERSARIAL CASES — NOT BEHAVIORAL EVALS**

These cases exist to pressure-test whether the proposed capability has a real owner boundary and whether it can stay narrow. They are not a frozen benchmark and should not yet be used to claim runtime correctness.

Each case asks what the smallest correct owner is and what failure would indicate overreach or under-coverage.

---

## Case 1 — Pure geometry refinement

### Input

```text
The concept and logo are approved.
At 16 px the lower aperture closes and the mark feels bottom-heavy.
Refine it without changing the concept.
```

### Expected ownership

```text
visual identity → controlled refinement + small-size test
```

### Must preserve

- approved concept;
- core silhouette unless the defect requires a bounded change;
- brand strategy and positioning.

### Failure

- reopening audience/positioning;
- generating unrelated logo concepts;
- changing color, symbolism, and typography when only geometry is open.

---

## Case 2 — New identity with unresolved positioning

### Input

```text
We have a new productivity app.
We do not know whether it should be framed as a personal assistant,
team operating system, or automation platform.
Design the logo.
```

### Expected ownership

```text
positioning/value dependency first
→ visual identity only after enough frame is resolved
```

### Failure

- hiding unresolved category/frame behind polished visual concepts;
- choosing a visual metaphor that silently decides positioning without surfacing the decision.

---

## Case 3 — Resolved positioning, new identity

### Input

```text
Positioning, target customer, category, and name are approved.
Create a visual identity that works in-product and as a favicon.
```

### Expected ownership

```text
visual identity
→ minimum brief from supplied state
→ category/context audit as needed
→ concept/form exploration
→ deployment tests
```

### Failure

- forcing a new research/segmentation project;
- falling back to generic logo folklore;
- treating one beautiful mockup as sufficient production evidence.

---

## Case 4 — Existing asset may have equity

### Input

```text
We have used the same red shield symbol for eight years.
The team is bored with it and wants something cleaner.
Should we replace it?
```

### Expected ownership

```text
visual identity → redesign/equity decision
→ buyer-memory evidence if consequential and available
```

### Expected reasoning

```text
team boredom != buyer evidence
historical use != proof of Fame/Uniqueness
but long use creates enough uncertainty that blind replacement is risky
```

### Failure

- replacing because the asset “looks dated”;
- claiming the shield is a strong distinctive asset without evidence;
- demanding perfect survey evidence before any bounded recommendation is possible.

---

## Case 5 — Descriptive mark versus generic category cue

### Input

```text
A cybersecurity company wants a shield icon because customers
immediately understand what the company does.
```

### Expected ownership

```text
visual identity
→ descriptive/relevance benefit
+ category mental-competition risk
+ legal pre-flight when consequential
```

### Failure

- “shield is descriptive, therefore bad”;
- “shield is relevant, therefore good”;
- treating legal distinctiveness, buyer comprehension, and visual ownability as one variable.

---

## Case 6 — “Make it premium”

### Input

```text
Make the logo feel more premium.
```

### Expected ownership

First determine whether “premium” is a resolved intended association and what current defect/open variable exists.

Research about angularity or complexity may inform hypotheses, but not dictate geometry.

### Failure

```text
premium → angular
premium → serif
premium → black/gold
```

as deterministic mappings without context.

---

## Case 7 — Misread with strong internal rationale

### Input

```text
The logo represents a hand selecting the best option.
Several uninformed viewers instead see a thumbs-up / swipe gesture.
The internal team loves the selection story.
```

### Expected ownership

```text
visual identity → perceptual reading / ambiguity test
```

### Expected reasoning

- the design is observed before the rationale;
- unintended readings matter only if they materially conflict, confuse, or distract;
- multiple abstract readings are not automatically defects.

### Failure

- defending the intended story as proof the logo “means” selection;
- rejecting every ambiguous abstract mark because viewers describe it differently.

---

## Case 8 — Landing-page visual placement

### Input

```text
The identity is approved.
Should the logo be larger in the hero, moved below the fold,
or removed from this page section?
```

### Expected ownership

```text
landing-page architecture
```

Visual identity may supply asset constraints but does not own page allocation.

### Failure

- visual-identity capability taking over page architecture merely because a logo is involved.

---

## Case 9 — Campaign image style

### Input

```text
The visual identity is fixed.
Create a campaign key visual for a product launch.
```

### Expected ownership

Potentially content/campaign execution with visual-identity constraints.

A dedicated identity owner should not automatically become a generic art-direction or image-generation owner.

### Failure

- expanding the capability into arbitrary campaign creative production.

---

## Case 10 — Local/cultural visual meaning

### Input

```text
The global symbol is approved.
Before launching in another market, check whether its gesture/shape
has a materially different local interpretation.
```

### Expected ownership

```text
visual identity owns the asset
+ Chapter 07/local adaptation only if local meaning can change the decision
```

### Failure

- country noun automatically triggering broad cultural stereotype research;
- visual identity inventing local cultural claims without evidence.

---

## Case 11 — Trademark search

### Input

```text
We like this symbol. Search for similar marks and tell us if it is safe.
```

### Expected ownership

```text
visual identity → bounded pre-flight
legal clearance → external authoritative dependency
```

### Allowed conclusion

```text
searched scope
obvious similar candidates
unresolved jurisdictions/classes
professional clearance requirement when consequential
```

### Failure

- “safe to trademark” based on a database search;
- failing to search relevant figurative similarity when the user explicitly asks for pre-flight.

---

## Case 12 — AI-generated concept versus production master

### Input

```text
An image model produced a symbol we love.
Use this exact mark as the final logo.
```

### Expected ownership

```text
visual identity
→ preserve selected concept
→ inspect exact geometry / typography / reproducibility
→ rebuild or verify production master when needed
```

### Failure

- uncontrolled regeneration that loses the selected identity;
- assuming the attractive raster preview is exact vector geometry;
- silently changing the mark while “cleaning it up.”

---

## Case 13 — Strong new asset, zero market exposure

### Input

```text
This symbol is unique in our competitor audit and everyone internally loves it.
Can we call it a strong distinctive brand asset?
```

### Expected ownership

```text
visual identity / distinctive-asset evidence boundary
```

### Expected answer

```text
high distinctiveness potential may be defensible
learned Fame is not established
market Uniqueness is not established by internal preference alone
```

### Failure

- treating design novelty as measured brand-memory strength.

---

## Case 14 — Color already famous, logo weak

### Input

```text
Consumer research shows our unusual orange is strongly linked to us,
but the symbol itself is weak. The redesign team wants a totally new palette.
```

### Expected ownership

```text
visual identity redesign
→ preserve/evolve asset based on measured evidence
```

### Failure

- logo-centric theory that ignores stronger non-logo assets;
- discarding measured color equity because a new visual concept looks cleaner.

This case is important pressure against defining the capability as “logo design.”

---

## Case 15 — Wordmark only

### Input

```text
The company does not want a symbol.
Develop and refine a wordmark that can act as the primary identity.
```

### Expected ownership

```text
visual identity
```

### Failure

- forcing symbol creation because the method assumes every brand needs a mark;
- treating typography as decorative after the identity decision has already made the wordmark primary.

---

## Case 16 — App icon is not the master logo

### Input

```text
Our horizontal wordmark is approved but unusable in the app launcher.
Should we compress it into the square or create an app-specific asset?
```

### Expected ownership

```text
visual identity extension
→ preserve identity relationship
→ optimize for app-icon conditions
```

### Failure

- mechanically squeezing a wide wordmark into a square;
- redesigning the corporate identity because one container needs a specialized asset.

---

## Case 17 — Color accessibility versus brand color

### Input

```text
Our primary brand blue is approved but does not provide sufficient
contrast for small white body text in a UI state.
Should we change the brand color?
```

### Expected ownership

```text
identity supplies brand color role
UI/accessibility constraint governs text/background pairing
```

Potentially add an accessible supporting tone or use the brand color differently rather than automatically changing identity.

### Failure

- treating every brand color as a valid UI text background;
- treating UI contrast failure as proof the brand color itself is invalid.

---

## Case 18 — User asks only for a critique

### Input

```text
Here are three logo options. Review them; do not redesign anything yet.
```

### Expected ownership

```text
visual identity evaluation
```

### Failure

- generating new concepts before evaluating supplied candidates;
- inventing unsupported brand strategy to justify preferences;
- ranking solely by personal taste.

---

# Boundary summary

The candidate capability appears justified only if it preserves these ownership lines:

```text
POSITIONING / VALUE
→ defines strategic state when unresolved

VISUAL IDENTITY
→ realizes and stewards brand-identifying visual assets

MESSAGE / COPY
→ owns verbal message / claims / proof

LOCALIZATION
→ specializes market/language/cultural realization when evidence changes the decision

LANDING-PAGE / CONTENT ENVIRONMENTS
→ own placement / representation / interaction in their surfaces

LEGAL / RIGHTS EXPERTISE
→ remains external authoritative dependency for clearance

UI / PRODUCT DESIGN
→ owns standalone interface-system decisions unless identity is the actual open question
```

A future implementation should be rejected if it cannot stay inside this boundary without turning Marketing Practitioner into a generic design suite.
