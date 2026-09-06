# Pilot walker trace

Status: reconstructed from sealed local results `pilot-v1`

This report does not claim output quality. It answers which skill nodes
the current-skill arm actually read, and where that walk left the intended graph.

## Mass

- Skill-arm runs reconstructed: 24

| Primary class | Runs |
| --- | ---: |
| `over_read` | 8 |
| `skip_jit` | 6 |
| `walk_ok` | 4 |
| `no_activation` | 3 |
| `resolve_fail` | 2 |
| `loaded_but_ignore` | 1 |

Labels can stack on one run. Label counts:

| Label | Runs |
| --- | ---: |
| `over_read` | 8 |
| `skip_jit` | 8 |
| `walk_ok` | 4 |
| `no_activation` | 3 |
| `loaded_but_ignore` | 2 |
| `resolve_fail` | 2 |

## Where the mass sits

The walker does not fail by taking a wrong handbook chapter as the dominant mode. No primary `wrong_edge` or `missing_handoff` on these 24 skill-arm runs.

The mass is **stopping too early** and **reading too coarsely**:

1. **`skip_jit` (6 primary, 8 labeled).** After a successful `SKILL.md` read, the agent often answers without loading the required knowledge node. This is concentrated in paid-media: both `BEH-PAID-002` repeats, both `BEH-PAID-004` repeats, and one `BEH-PAID-001` repeat. `BEH-DISC-001` repeat 2 also stops at the controller, then leaves the graph via `web_search`.
2. **`over_read` (8 primary).** When a required node is reached, it is usually a whole-file `Get-Content -Raw` of a chapter, or the controller is re-sliced many times. `get-knowledge.py` was invoked once (`paid-media.observation`) and **exited non-zero**; the agent recovered by slicing `handbook/14`. Helper JIT is not the live walk.
3. **`no_activation` (3).** Matches the sealed operational gate: `BEH-FAST-001` repeat 2, `BEH-FAST-002` repeat 2, `BEH-COM-001` repeat 1. Zero skill-file commands. Answer text from these runs is not a skill-graph walk.
4. **`resolve_fail` (2).** The agent aimed at the right file and the command died (PowerShell quoting / `Select-String`), then never recovered: `BEH-EVID-001` repeat 2 on Chapter 01; `BEH-DISC-001` repeat 1 on a discovery slice, then `web_search`.
5. **`loaded_but_ignore` is not a handbook defect on this corpus.** The primary case is `BEH-FAST-002` repeat 1: fast-path walk (`SKILL.md` only) that failed the 150-character hard predicate. `BEH-PAID-003` repeat 1 loaded whole Chapter 05 and still failed review; that is stacked under `over_read`, not a reason to rewrite Chapter 05.

`walk_ok` (4) is `BEH-FAST-001` repeat 1, `BEH-STATE-001` repeat 1, `BEH-COM-001` repeat 2 (Shopee commercial-state slice), and `BEH-PAID-001` repeat 2 after the helper failure.

## Per current-skill run

### BEH-FAST-001@1.0.0 / `RUN-7CE84EF148AF4984B9F02F90E64346CB`

- State: `completed`
- Primary: `walk_ok`
- Labels: `walk_ok`
- Walk: `skill.md (controller/whole_file/ok)`

### BEH-FAST-001@1.0.0 / `RUN-A23EB35AF95E4F8F8578EE4301FCDFAB`

- State: `activation_unverified`
- Primary: `no_activation`
- Labels: `no_activation`
- Walk: `(no skill-file commands)`

### BEH-FAST-002@1.0.0 / `RUN-052E0BED97DD44A9AEE51F18CDB7E204`

- State: `completed`
- Primary: `loaded_but_ignore`
- Labels: `loaded_but_ignore`
- Walk: `skill.md (controller/whole_file/ok)`

### BEH-FAST-002@1.0.0 / `RUN-4346059D9AE84A3087EE018B31A09977`

- State: `activation_unverified`
- Primary: `no_activation`
- Labels: `no_activation`
- Walk: `(no skill-file commands)`

### BEH-STATE-001@1.0.0 / `RUN-D0CCB2DB0D3B4537A3F78426A604DE82`

- State: `completed`
- Primary: `walk_ok`
- Labels: `walk_ok`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/slice/fail) → skill.md (controller/slice/ok) → routing-index.json (index/other/fail) → routing-index.json (index/other/fail) → routing-index.json (index/whole_file/fail) → routing-index.json (index/slice/ok) → handbook/11-landing-page-architecture.md (probe/probe/ok) → handbook/11-landing-page-architecture.md (knowledge/slice/ok) → handbook/11-landing-page-architecture.md (knowledge/slice/ok)`

### BEH-STATE-001@1.0.0 / `RUN-18CEBB94B53D47838B24D25AC4F18A1A`

- State: `completed`
- Primary: `over_read`
- Labels: `over_read`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/slice/fail) → skill.md (controller/slice/ok) → skill.md (controller/slice/ok) → skill.md (controller/slice/ok) → skill.md (controller/slice/ok) → routing-index.json (index/other/fail) → routing-index.json (index/whole_file/ok) → handbook/11-landing-page-architecture.md (knowledge/slice/ok)`

### BEH-EVID-001@1.0.0 / `RUN-DB0F138B2C7B4180B5CD37D4F4675BD5`

- State: `completed`
- Primary: `over_read`
- Labels: `over_read`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/slice/fail) → handbook/01-customer-research-and-evidence.md (knowledge/slice/fail) → handbook/01-customer-research-and-evidence.md (knowledge/whole_file/ok)`

### BEH-EVID-001@1.0.0 / `RUN-561C0607A731410989BA02206875A6FC`

- State: `completed`
- Primary: `resolve_fail`
- Labels: `resolve_fail`, `skip_jit`
- Walk: `skill.md (controller/whole_file/ok)`

### BEH-CAUSE-001@1.0.0 / `RUN-18FE0A5859C1496893FCB3354794B67A`

- State: `completed`
- Primary: `over_read`
- Labels: `over_read`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/whole_file/fail) → skill.md (controller/slice/ok) → handbook/05-diagnosis-causality-and-experimentation.md (knowledge/whole_file/ok)`

### BEH-CAUSE-001@1.0.0 / `RUN-A78D36A5A0BB44C8BF0F118E73FA81D7`

- State: `completed`
- Primary: `over_read`
- Labels: `over_read`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/whole_file/fail) → skill.md (controller/slice/ok) → skill.md (controller/slice/ok) → handbook/05-diagnosis-causality-and-experimentation.md (knowledge/whole_file/ok)`

### BEH-DISC-001@1.0.0 / `RUN-83F5B4BA70A245DE86DA32F1281E7AE3`

- State: `completed`
- Primary: `resolve_fail`
- Labels: `resolve_fail`, `skip_jit`
- Walk: `skill.md (controller/whole_file/ok) → routing-index.json (index/probe/ok) → web_search (web_search/external/ok)`

### BEH-DISC-001@1.0.0 / `RUN-2E4E0731716E45B5A78E5AEC93172CD2`

- State: `completed`
- Primary: `skip_jit`
- Labels: `skip_jit`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/slice/fail) → skill.md (controller/slice/ok) → web_search (web_search/external/ok)`

### BEH-COM-001@1.0.0 / `RUN-BA57287DFF2B4B5C82C328F73CC6C15B`

- State: `activation_unverified`
- Primary: `no_activation`
- Labels: `no_activation`
- Walk: `(no skill-file commands)`

### BEH-COM-001@1.0.0 / `RUN-497F27E8D4C647F0956DDA8E1134A809`

- State: `completed`
- Primary: `walk_ok`
- Labels: `walk_ok`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/slice/ok) → routing-index.json (index/other/fail) → routing-index.json (index/whole_file/fail) → routing-index.json (index/probe/ok) → platforms/commerce/shopee.md (probe/probe/ok) → platforms/commerce/shopee.md (knowledge/slice/ok)`

### BEH-EMAIL-001@1.0.0 / `RUN-3F0CE7992EF04E268B00FFA0B75B998B`

- State: `completed`
- Primary: `over_read`
- Labels: `over_read`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/slice/fail) → skill.md (controller/slice/ok) → skill.md (controller/slice/ok) → skill.md (controller/slice/ok) → routing-index.json (index/other/fail) → routing-index.json (index/other/fail) → routing-index.json (index/slice/ok) → handbook/12-email-communication-architecture.md (knowledge/slice/ok) → handbook/05-diagnosis-causality-and-experimentation.md (knowledge/whole_file/ok)`

### BEH-EMAIL-001@1.0.0 / `RUN-A725F521828A46FEBAAD06DDAC34B8D8`

- State: `completed`
- Primary: `over_read`
- Labels: `over_read`
- Walk: `skill.md (controller/whole_file/ok) → handbook/05-diagnosis-causality-and-experimentation.md (knowledge/whole_file/ok) → routing-index.json (index/whole_file/ok) → handbook/12-email-communication-architecture.md (knowledge/whole_file/ok)`

### BEH-PAID-001@1.0.0 / `RUN-C5092EEEE40341B9A0F3081822B3E04F`

- State: `completed`
- Primary: `skip_jit`
- Labels: `skip_jit`
- Walk: `skill.md (controller/whole_file/ok)`

### BEH-PAID-001@1.0.0 / `RUN-FE3E472198394A44928970BEB48A7345`

- State: `completed`
- Primary: `walk_ok`
- Labels: `walk_ok`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/slice/fail) → skill.md (controller/slice/ok) → skill.md (controller/slice/ok) → paid-media.observation (helper/helper_route/fail) → routing-index.json (index/other/fail) → routing-index.json (index/other/fail) → routing-index.json (index/probe/ok) → handbook/14-paid-media-architecture.md (probe/probe/ok) → handbook/14-paid-media-architecture.md (knowledge/slice/ok)`

### BEH-PAID-002@1.0.0 / `RUN-5E0070E475004CDA899EBA0BC40A394C`

- State: `completed`
- Primary: `skip_jit`
- Labels: `skip_jit`
- Walk: `skill.md (controller/whole_file/ok)`

### BEH-PAID-002@1.0.0 / `RUN-D6DAC248B88040A48D2474FA53D574FD`

- State: `completed`
- Primary: `skip_jit`
- Labels: `skip_jit`
- Walk: `skill.md (controller/whole_file/ok)`

### BEH-PAID-003@1.0.0 / `RUN-30450EABDD0C4F4986B2A22982CB0970`

- State: `completed`
- Primary: `over_read`
- Labels: `over_read`, `loaded_but_ignore`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/slice/fail) → skill.md (controller/slice/ok) → handbook/05-diagnosis-causality-and-experimentation.md (knowledge/whole_file/ok)`

### BEH-PAID-003@1.0.0 / `RUN-DD307473E2E6414894494D3D01683644`

- State: `completed`
- Primary: `over_read`
- Labels: `over_read`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/slice/ok) → handbook/05-diagnosis-causality-and-experimentation.md (knowledge/whole_file/ok)`

### BEH-PAID-004@1.0.0 / `RUN-3FB0D4506E2347A1B40C811433A6F41E`

- State: `completed`
- Primary: `skip_jit`
- Labels: `skip_jit`
- Walk: `skill.md (controller/whole_file/ok)`

### BEH-PAID-004@1.0.0 / `RUN-696E93B384E4443CAB3C08C4943E00F8`

- State: `completed`
- Primary: `skip_jit`
- Labels: `skip_jit`
- Walk: `skill.md (controller/whole_file/ok) → skill.md (controller/slice/fail) → skill.md (controller/slice/ok) → skill.md (controller/slice/ok)`

## Decision

Do not edit handbook nodes. The reconstructed walks do not show a required node loaded at the intended grain with behavior still wrong as the mass failure.

The next walker surface, if one change is made later, is not theory. It is getting the agent off `SKILL.md`-only answers on JIT families (`skip_jit`, especially paid-media) without increasing `activation_unverified`. `get-knowledge.py` is not yet a live path: one attempt, failed, recovered by whole-chapter read.

Activation remains a hard regression gate. This reconstruction used sealed local `pilot-v1` events only. No new live benchmark was run.

