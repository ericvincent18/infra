if __name__ == "app":
    from celery import Celery
    from config import celery_config
    from service import MsgConsumerStep

    service = Celery("app")
    service.config_from_object(celery_config)

    results = service.steps["consumer"].add(MsgConsumerStep)
