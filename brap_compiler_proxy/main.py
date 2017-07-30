from brap.container import Container

from brap_compiler_proxy.proxy_compiler import ProxyInjectionCompiler


class FixtureService(object):
    """
    Only used to provide a sample for tests
    """

    def __init__(self, value):
        self.value = value

    def method1(self, value):
        self.method1_value = value

    def method2(self, value):
        self.method2_value = value


container = Container()

container.set('const_param', 'constructor_param')
container.set('meth_param', 'method_param')

container.set('fixture_service',
    FixtureService,
    lambda c: c('const_param'),
    [
        ('method1', lambda c: c('meth_param')),
        ('method2', lambda c: c('meth_param'))
    ]
)

container.use_compiler(ProxyInjectionCompiler())

fixture_service = container.get('fixture_service')
