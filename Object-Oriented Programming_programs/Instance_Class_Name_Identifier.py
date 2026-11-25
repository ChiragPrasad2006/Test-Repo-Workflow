class ClassInspector:
    @staticmethod
    def get_class_name(instance: object) -> str:
        return instance.__class__.__name__
