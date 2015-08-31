class ParamFactory(object):

    def __init__(self, keyword, param):
        self.keyword = keyword
        self.param = param

    def create(self):
        print 'creating ' + self.param + ' object'
        try:

            print 'routing.post.inbound.keywords.' + self.keyword + '.params.' + self.param + '::' + self.param.title()
            param_class = self.param.title()
            loaded_mod = __import__('routing.post.inbound.keywords.' + self.keyword + '.params.' + self.param, fromlist=[param_class])
            try: 
                param_obj = getattr(loaded_mod, param_class)
                return param_obj

            except AttributeError:
                print 'method/class not found'

        except ImportError:
            print 'package not found'
