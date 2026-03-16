"""Audit logging service stub."""


class AuditService:
    """Records audit log entries.

    Not yet implemented.
    """

    def log(
        self,
        actor: str,
        action: str,
        resource_type: str | None = None,
        resource_id: str | None = None,
        detail: str | None = None,
    ) -> None:
        """Append an audit log entry.

        Not yet implemented.
        """
        raise NotImplementedError("AuditService.log() is not yet implemented.")
