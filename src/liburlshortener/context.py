from typing import Optional

from libutil.util import BaseModel


class RequestContext(BaseModel):
    # urlshortener service context attributes
    id_user: Optional[int] = None
    guest_code: str = None

    @staticmethod
    def from_urlshortener_service(guest_code, **kwargs):
        """
        Creates a RequestContext for requests coming from the urlshortener service.
        Add more service-specific factory methods as needed:
        - from_auth_service()
        - from_payment_service()
        - from_notification_service()
        etc.
        """

        from liburlshortener.data import engine_urlshortener, entities

        id_user = entities.user.get_id_by_code(engine_urlshortener, guest_code)
        if not id_user:
            id_user = entities.user.insert_user(engine_urlshortener, guest_code)

        kwargs.update(
            {
                'id_user': id_user,
                'guest_code': guest_code,
            }
        )

        return RequestContext(**kwargs)

    @staticmethod
    def mock(**kwargs):
        """
        Creates a mock RequestContext for testing, background jobs, or cron tasks.
        Useful for:
        - Unit tests
        - Background workers
        - Cron jobs
        - Development environments
        """
        return RequestContext(**kwargs)
