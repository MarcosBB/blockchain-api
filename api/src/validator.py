class base_validator():
    data_names = []
    def __init__(self, request):
        self.payload = request.get_json()

    def validate(data:dict) -> list:
        return []

    def is_valid(self) -> bool:
        if self.get_errors() == []:
            return True
        else:
            return False

    def get_errors(self) -> list:
        errors = []
        fields = []
        for data_name in self.data_names:
            if data_name not in self.payload:
                fields.append(data_name)
        if fields:
            errors.append(f'Filds {fields} are required')
            return errors
        
        return errors + self.validate(self.payload)

    