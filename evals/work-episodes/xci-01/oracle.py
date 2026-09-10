from __future__ import annotations

from dataclasses import dataclass

CURRENT_DEPENDENT = "CURRENT_DEPENDENT"
CURRENT_PROTECTED = "CURRENT_PROTECTED"
SOURCE_HISTORY = "SOURCE_HISTORY"


@dataclass(frozen=True)
class Relation:
    relation_id: str
    artifact_path: str
    locator: str
    temporal_role: str
    semantic_role: str
    source_authority: str
    dependency_on_current_category: bool
    protection_class: str
    pressure_disposition: str
    control_disposition: str


RELATIONS = (
    Relation("R01", "website/home.md", "RelayDesk is an AI customer-service chatbot", "current", "present-day self-category", "current positioning", True, CURRENT_DEPENDENT, "REPAIR", "PRESERVE"),
    Relation("R02", "website/about.md", "Today, RelayDesk is an AI customer-service chatbot", "current", "present-day self-category", "current positioning", True, CURRENT_DEPENDENT, "REPAIR", "PRESERVE"),
    Relation("R03", "campaigns/nurture-draft.md", "RelayDesk is an AI customer-service chatbot", "current-unsent", "present-tense self-assertion", "current positioning", True, CURRENT_DEPENDENT, "REPAIR", "PRESERVE"),
    Relation("R04", "ads/search-ad-draft.md", "Current product description", "current-draft", "seller-authored present-day self-description", "current positioning", True, CURRENT_DEPENDENT, "REPAIR", "PRESERVE"),
    Relation("R05", "profiles/linkedin-bio.md", "RelayDesk — AI customer-service chatbot", "current", "present-day self-category", "current positioning", True, CURRENT_DEPENDENT, "REPAIR", "PRESERVE"),
    Relation("R06", "commerce/listing-en.md", "Seller description", "current", "seller-authored English product representation", "current positioning", True, CURRENT_DEPENDENT, "REPAIR", "PRESERVE"),
    Relation("R07", "search/compare-ai-chatbots.md", "Current RelayDesk description", "current", "present-day RelayDesk self-description", "current positioning", True, CURRENT_DEPENDENT, "REPAIR", "PRESERVE"),
    Relation("R08", "case-studies/acme.md", "Current publisher note", "current", "present-day publisher framing", "current positioning", True, CURRENT_DEPENDENT, "REPAIR", "PRESERVE"),
    Relation("R09", "decisions/positioning-history.md", "CURRENT STATE", "current", "explicit current-state category field", "current positioning", True, CURRENT_DEPENDENT, "REPAIR", "PRESERVE"),
    Relation("P01", "search/compare-ai-chatbots.md", "# Best AI customer-service chatbots", "current", "external comparison/search frame", "artifact context", False, CURRENT_PROTECTED, "PRESERVE", "PRESERVE"),
    Relation("P02", "commerce/listing-vi.md", "Trợ lý AI cho người bán", "current", "approved Vietnamese commerce realization", "brand/approved-localization.md", False, CURRENT_PROTECTED, "PRESERVE", "PRESERVE"),
    Relation("P03", "brand/voice-guide.md", "Use clear, direct language", "current", "voice guidance unrelated to category", "voice guide", False, CURRENT_PROTECTED, "PRESERVE", "PRESERVE"),
    Relation("P04", "help/account-security.md", "Use two-factor authentication", "current", "account-security guidance unrelated to category", "help source", False, CURRENT_PROTECTED, "PRESERVE", "PRESERVE"),
    Relation("P05", "product/onboarding-actions.md", "Review before sending", "current", "product action language unrelated to category", "product source", False, CURRENT_PROTECTED, "PRESERVE", "PRESERVE"),
    Relation("S01", "case-studies/acme.md", "Customer quote", "historical-attributed", "attributed customer quotation", "09:00 source", False, SOURCE_HISTORY, "PRESERVE", "PRESERVE"),
    Relation("S02", "archive/launch-announcement-2025.md", "At launch in 2025", "historical", "historical launch positioning", "09:00 source", False, SOURCE_HISTORY, "PRESERVE", "PRESERVE"),
    Relation("S03", "research/customer-interviews.md", "Participant 03", "source-evidence", "verbatim customer interview wording", "09:00 source", False, SOURCE_HISTORY, "PRESERVE", "PRESERVE"),
    Relation("S04", "search/query-observations.csv", "AI customer service chatbot", "observation", "observed query/search-language evidence", "09:00 source", False, SOURCE_HISTORY, "PRESERVE", "PRESERVE"),
    Relation("S05", "decisions/positioning-history.md", "2025-06-10", "historical-decision", "historical positioning decision entry", "09:00 source", False, SOURCE_HISTORY, "PRESERVE", "PRESERVE"),
)

RELATION_BY_ID = {relation.relation_id: relation for relation in RELATIONS}
CURRENT_DEPENDENT_IDS = tuple(r.relation_id for r in RELATIONS if r.protection_class == CURRENT_DEPENDENT)
CURRENT_PROTECTED_IDS = tuple(r.relation_id for r in RELATIONS if r.protection_class == CURRENT_PROTECTED)
SOURCE_HISTORY_IDS = tuple(r.relation_id for r in RELATIONS if r.protection_class == SOURCE_HISTORY)
