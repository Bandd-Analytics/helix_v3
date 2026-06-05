"""Model role routing for the dual-provider vision stack.

Helix uses model roles instead of treating one provider as globally best. The
role table keeps provider selection explicit and reviewable as model quality,
cost, and API features change.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from config.settings import settings

Provider = Literal["anthropic", "openai"]


@dataclass(frozen=True)
class ModelRole:
    role_id: str
    provider: Provider
    model: str
    responsibility: str
    primary: bool
    api_key_present: bool


def get_model_roles() -> list[ModelRole]:
    """Return the current model-role decision matrix."""

    api = settings.api
    has_anthropic = bool(api.anthropic_key)
    has_openai = bool(api.openai_key)

    return [
        ModelRole(
            role_id="vision_pattern_primary",
            provider="anthropic",
            model=api.anthropic_model,
            responsibility=(
                "Read chart geometry, MMM pattern structure, visual anomalies, and "
                "challenging discretionary context."
            ),
            primary=True,
            api_key_present=has_anthropic,
        ),
        ModelRole(
            role_id="structured_arbitrator",
            provider="openai",
            model=api.openai_model,
            responsibility=(
                "Return strict JSON verdicts, normalize labels, arbitrate disagreements, "
                "and produce backtest-ready fields."
            ),
            primary=True,
            api_key_present=has_openai,
        ),
        ModelRole(
            role_id="fast_screening",
            provider="anthropic",
            model=api.anthropic_fast_model,
            responsibility=(
                "Lower-latency screening for non-entry flashcards and forming structures."
            ),
            primary=False,
            api_key_present=has_anthropic,
        ),
        ModelRole(
            role_id="retrieval_embeddings",
            provider="openai",
            model=api.openai_embedding_model,
            responsibility=(
                "Embed text descriptions of labeled flashcards for similar-setup retrieval."
            ),
            primary=False,
            api_key_present=has_openai,
        ),
    ]


def get_role(role_id: str) -> ModelRole:
    """Return a configured role by ID."""

    for role in get_model_roles():
        if role.role_id == role_id:
            return role
    raise KeyError(f"Unknown model role: {role_id}")


def format_role_report() -> str:
    """Human-readable routing report for diagnostics."""

    lines = ["HELIX V3 MODEL ROLE ROUTING"]
    for role in get_model_roles():
        status = "configured" if role.api_key_present else "missing-key"
        primary = "primary" if role.primary else "support"
        lines.append(
            f"- {role.role_id}: {role.provider}/{role.model} ({primary}, {status})"
        )
        lines.append(f"  {role.responsibility}")
    return "\n".join(lines)
