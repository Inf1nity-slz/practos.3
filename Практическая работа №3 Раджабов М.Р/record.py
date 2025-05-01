class Record:
    def __init__(self, record_id, car_model, service_type, owner_name):
        self._record_id = record_id
        self._car_model = car_model
        self._service_type = service_type
        self._owner_name = owner_name

    @property
    def car_model(self):
        return self._car_model

    @property
    def service_type(self):
        return self._service_type

    @property
    def owner_name(self):
        return self._owner_name

    def __str__(self):
        return f"ID: {self._record_id}, Model: {self._car_model}, Service: {self._service_type}, Owner: {self._owner_name}"
    @property
    def record_id(self):
        return self._record_id