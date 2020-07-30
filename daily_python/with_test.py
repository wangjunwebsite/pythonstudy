class Testwith():
    def __enter__(self):
        print('start')

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_tb is None:
            print('running success')
        else:
            print('running failed,%s' % exc_tb)
        


with Testwith():
    print('Test is running')
    raise NameError('%s' %exc_tb)
