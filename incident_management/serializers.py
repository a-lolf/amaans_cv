from rest_framework import serializers
from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    reporter = serializers.ReadOnlyField(source='reporter.username')

    class Meta:
        model = Incident
        fields = ['incident_id', 'details', 'reported_datetime', 'priority', 'incident_status', 'reporter']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method == 'POST':
            fields.pop('incident_id')
        return fields
