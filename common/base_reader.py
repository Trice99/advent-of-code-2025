from abc import ABC, abstractmethod
import os
import inspect


class BaseFileReader(ABC):
    def __init__(self, file_path):
        self.file_path = self._resolve_path(file_path)
    
    def _resolve_path(self, file_path):
        if os.path.isabs(file_path):
            return file_path
        
        for frame_info in inspect.stack()[1:]:
            frame_dir = os.path.dirname(os.path.abspath(frame_info.filename))
            candidate_path = os.path.join(frame_dir, file_path)
            if os.path.exists(candidate_path):
                return candidate_path
        
        return file_path
    
    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                return self._process_lines(file)
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    
    def _process_lines(self, file):
        return [line.strip() for line in file if line.strip()]
    
    @abstractmethod
    def parse(self):
        pass


class SingleLineReader(BaseFileReader):
    def _process_lines(self, file):
        return [line.strip() for line in file if line.strip()]
    
    def parse(self):
        return self.read_file()


class MultiLineReader(BaseFileReader):
    def _process_lines(self, file):
        return [line.rstrip('\n') for line in file]
    
    def parse(self):
        return self.read_file()
