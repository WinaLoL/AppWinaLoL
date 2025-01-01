import inject

from source.services.EnvService import EnvService


class ClassInjectorService:
    def inject(self):
        inject.configure(self.configure)

    @staticmethod
    def configure(binder):
        binder.bind(EnvService, EnvService())
