import os
import uuid
class TemporaryFile(str):
    '''Container to hold a path in order to delete it when GC'd.'''
    
    def __del__(self):
        if '_persist' not in self.__dict__:
            os.remove(self)

    @staticmethod
    def generate_new(ext=''):
        '''Create a new temp file path with an optional extension.'''
        return TemporaryFile('/var/tmp/'+str(uuid.uuid4())+'.'+ext)

    def persist(self):
        '''
        If this is run during an instance's lifetime,
        its path will not be deleted when this gets GC'd.
        '''
        self._persist = True
        return self
