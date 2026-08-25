from __future__ import annotations

from collections.abc import Mapping

from .adapters import ExecutorRequest, ExecutorResult


class FixtureAdapter:
    def __init__(
        self,
        results: Mapping[tuple[str, str], ExecutorResult],
    ) -> None:
        self._results = dict(results)

    def execute(self, request: ExecutorRequest) -> ExecutorResult:
        key = (request.case.identity, request.profile.profile_id)
        return self._results.get(
            key,
            ExecutorResult(exit_code=127, stderr=f"missing fixture result: {key}"),
        )
